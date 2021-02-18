from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_ajax', views.form_ajax, name='form_ajax'),
    url(r'^message_ajax', views.message_ajax, name='message_ajax'),
]