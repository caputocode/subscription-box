from django.conf.urls import url, include
from .views import register, login, login_required

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^login_required/$', login_required(), name='login_required'),

    ]