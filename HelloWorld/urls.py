from django.conf.urls import url
 
from . import views
# import django.views.static
# from django.conf.urls import url,include
# from django.contrib import admin
# from django.conf.urls.static import static
# from django.conf import settings

# url(r'^imgs/(?P<path>.*)',django.views.static.serve,{'document_root':'E:\人机交互\HelloWorld\imgs'}),
# urlpatterns = [
#     url(r'^$', views.hello),
# ]
from django.urls import path

urlpatterns = [
    path('', views.home),
    url(r'^test/$', views.test),
    # url(r'^static/(?P<path>.*)$', static.serve,
    #     {'document_root': settings.STATIC_ROOT}, name='static')  # 解决静态文件加载失败问题
]