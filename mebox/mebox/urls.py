from django.conf.urls import patterns, include, url
from django.contrib import admin
from mebox import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mebox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #root
    url(r'^$', views.index, name='index'),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),
    
    #books
    url(r'^books/', include('books.urls',namespace="books")),
   
)
