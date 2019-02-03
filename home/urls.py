from django.conf.urls import url, include
from .views import concept, following

urlpatterns = [
    url(r'^$', concept, name='concept'),
    url(r'^$', following, name='following'),

    ]