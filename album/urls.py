from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.album,name='album'),
    url(r'^search/', views.search, name='search'),
    url(r'^image/(\d+)',views.image,name ='image'),
   
]