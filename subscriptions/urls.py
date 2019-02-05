from django.conf.urls import url, include
from .views import display_offers

urlpatterns = [
    url(r'^$', display_offers, name='offers'),

    ]