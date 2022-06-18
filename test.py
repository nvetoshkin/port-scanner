import aiohttp.test_utils as aio_ut
import aiohttp
from aiohttp.test_utils import AioHTTPTestCase, TestClient,\
     TestServer, loop_context
from aiohttp import web
from main import create_app
import sys

app = create_app()
test = AioHTTPTestCase()
loop = aio_ut.setup_test_loop()
client = TestClient(TestServer(app), loop=loop)
loop.run_until_complete(client.start_server())
try:
    v = sys.argv[1] #ключ -в для подробного вывода информации
    if v != '-v':
        v = None
except:
    v = None

async def test_index():
    resp = await client.get("/")
    text = await resp.text()
    try:
        test.assertIn("<h1>Сканер портов</h1>", text)
        print('index... ok')
    except Exception as e:
        print(str(e))

async def test_scan(ip, begin_port, end_port, v=None):
    resp = await client.get(f"/scan/{ip}/{begin_port}/{end_port}")
    text = await resp.text()
    count = 0
    for i in range(begin_port, end_port+1):
        try:
            test.assertIn(f"\"port\": \"{i}\"", text)
            if v == '-v':
                print(f'IP {ip} port {i}... ok')
        except Exception as e:
            count = count + 1
            if v == '-v':
                print(str(e))
    if v == None:
        print(f"got {count} error in {ip} port scanning")
            
        
    
loop.run_until_complete(test_index())
loop.run_until_complete(test_scan('ya.ru', 79, 81, v))
loop.run_until_complete(test_scan('google.com', 79, 81, v))
loop.run_until_complete(test_scan('localhost', 22, 22, v))
loop.run_until_complete(client.close())
del test
loop.close()


