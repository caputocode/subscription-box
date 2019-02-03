from django.conf.urls import url, include
from .views import display_boxes, box_detail
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', display_boxes, name='boxes'),
    url(r'^(?P<pk>\d+)/$', box_detail, name='box_detail'),


    ]