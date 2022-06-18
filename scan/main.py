from aiohttp import web
import syslog

def setup_routes(application):
   try:
      from urls import setup_urls
      setup_urls(application)
   except:
      syslog.syslog("something wrong with urls.py file")

def setup_app(application):
   setup_routes(application)

def create_app():
   app = web.Application()
   setup_app(app)
   return app

if __name__ == "__main__":
   app = create_app()
   try:
      web.run_app(app, host="0.0.0.0", port=80)
   except:
      syslog.syslog("web app run error")
