from aiohttp import web
import json
import aiohttp_jinja2
import socket as soc
import threading as thr
import syslog #подключение к 514 порту rsyslog

#хэндл или индекс
async def handle(request):
    #открываем шаблон стартовой страницы
    try:
        f = open("index.html", "r")
    except:
        syslog.syslog("index.html is absent")
    #возвращаем его
    return web.Response(text=f.read(), content_type='text/html')

#пробуем подключаться к порту
def connect(ip, number_port, is_open):
    #АФ_ИНЕТ - сокет вида айпи:порт, СОК_СТРИМ - ТСП
    TCPsoc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    TCPsoc.settimeout(0.5)
    #Пробуем подключиться к сокету
    try:
        TCPsoc.connect((ip, number_port))
        is_open[number_port] = 'open'
    except:
        is_open[number_port] = 'close'
        syslog.syslog("сокет недоступен")
        
#основная функция сканирования
async def scan(request):
    try:
        #получаем урл строку из ГЕТ метода и парсим
        string = request.path
        string = string.split('scan/')[1]
        ip = string.split('/')[0]
        begin_port = int(string.split('/')[1])
        end_port = int(string.split('/')[2])

        threads = []
        is_open = {}
        result = []

        # Создаём потоки
        for i in range(begin_port, end_port+1):
            t = thr.Thread(target=connect, args=(ip, i, is_open))
            threads.append(t)


        # Запускаем
        for i in range(end_port - begin_port+1):
            threads[i].start()

        # Пока выполняется поток останавливаем главный поток
        for i in range(end_port - begin_port+1):
            threads[i].join()
                
        # Выводим результат в джсон
        for i in range(begin_port, end_port+1):
            if is_open[i] == 'open':
                result.append({'port':str(i), 'state':is_open[i]})
                syslog.syslog(syslog.LOG_INFO, str(result[i-begin_port]))
            else:
                result.append({'port':str(i), 'state':is_open[i]})
                syslog.syslog(syslog.LOG_INFO, str(result[i-begin_port]))
        
        return web.Response(text=json.dumps(result, indent=1),\
                                            status=200)
    except Exception as e:
        syslog.syslog(str(e))
        return web.Response(text=str(e), status=500)
