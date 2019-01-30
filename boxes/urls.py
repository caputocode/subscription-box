from django.conf.urls import url, include
from .views import display_boxes

urlpatterns = [
    url(r'^boxes/', display_boxes, name='boxes')
    ]