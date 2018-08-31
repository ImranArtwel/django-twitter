from django.conf.urls import url
from . import views

app_name = 'twits'

urlpatterns = [
    url(r'^create/$',views.twit_create, name='create'),
    url(r'^$',views.twitts_index, name='twitts_index'),
    
    
]