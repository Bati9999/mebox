from django.conf.urls import patterns, url
from books import views

urlpatterns=patterns('', 
        url(r'^$', views.index, name='index'),
        #url(r'^$', views.detail, name='detail'),
        #url(r'^$', views.cat, name='cat'),
        #url(r'^$', views.tag, name='tag'),
                
)
