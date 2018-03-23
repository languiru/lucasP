from django.conf.urls import url
from . import views
from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<carro_id>[0-9]+)/$', views.detail)


]
