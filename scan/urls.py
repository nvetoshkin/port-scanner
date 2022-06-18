import views
import syslog

def setup_urls(app):
   try:
      app.router.add_get('/', views.handle)
      app.router.add_get(r'/scan/{ip}/{begin_port}/{end_port}', views.scan,\
                         name = 'scan')
   except:
      syslog.syslog("wrong url")
