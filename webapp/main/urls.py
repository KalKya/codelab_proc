from django.urls import path
from .views import (
    list_view, 
    client #work exercise, Insert code here
)

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),
    path('join-now',client, name='hangout'),#new url route

]