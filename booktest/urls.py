from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^editor/$', views.editor),
    url(r'^show/', views.show),
]
