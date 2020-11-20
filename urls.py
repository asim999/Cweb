from django.conf.urls import url
from django.views.static import serve

from rpwebapp import views
from rpwebsite.settings import STATIC_DIR

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_DIR}, name='static'),
]
