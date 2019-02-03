from django.conf.urls import url, include
from .views import concept

urlpatterns = [
    url(r'^$', concept, name='concept'),


    ]