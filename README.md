# 💎Port scanner
## 🙈Stack
- [x] **python 3.10.4**
- [x] **aiohttp 3.8.1**
## 🌁Структура
> scan/
> 
> &emsp; \_\_init\_\_.py
>   
> &emsp; index.html
>     
> &emsp; main.py
>     
> &emsp; requirements.txt
>     
> &emsp; test.py
>   
> &emsp; urls.py
> 
> &emsp; views.py
## ♻️Установка через rpm
**spec-файл прилагается**
```
sudo dnf install scan-1.0-1.0.noarch.rpm
```
Или
```
sudo rpm -ivh scan-1.0-1.0.noarch.rpm
```

Устанавливается в /usr/bin/scan
## 🌇Запуск
Веб приложение запускается через
```
sudo python main.py
```
## 🌙Логи
Логи пишутся в syslog по 514 порту через модуль Python - **syslog**

## 🌆Тесты
```
python test.py
```
Или с подробным выводом:
```
python test.py -v
```
