from django.conf.urls import url, include
from .views import register, login, login_required, logout

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^login_required/$', login_required, name='login_required'),
    url(r'^logout/$', logout, name='logout'),

    ]