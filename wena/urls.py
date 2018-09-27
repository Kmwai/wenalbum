from django.urls import path
from . import views


app_name = 'wena'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('<str:location_slug>/', views.photo_list, name='photo_list_by_location'),
    path('<int:id>/<str:slug>/', views.photo_detail, name='photo_detail'),

]
