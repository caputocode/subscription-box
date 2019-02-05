"""subscription_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from cart import urls as urls_cart
from boxes import urls as urls_boxes
from subscriptions import urls as urls_subscriptions
from blogposts import urls as urls_blogposts
from accounts.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^boxes/', include(urls_boxes)),
    url(r'^offers/', include(urls_subscriptions)),
    url(r'^concept/', include(urls_home)),
    url(r'^cart/', include(urls_cart)),
    url(r'^blog/', include(urls_blogposts)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
