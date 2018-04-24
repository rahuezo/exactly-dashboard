from django.conf.urls import url, include
from . import views


app_name = 'exactly_dashboard_home'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),

]