from django.conf.urls import url

from lookup import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
