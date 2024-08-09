from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/', views.all_musician_list, name='all_musician_list'),
    path('musician/create/', views.create_musician, name='create_musician'),
    path('musician/edit/<int:id>/', views.edit_musician, name='edit_musician'),
    path('musician/delete/<int:id>/', views.delete_musician, name='delete_musician'),
    path('album/create/', views.create_album, name='create_album'),
    path('album/edit/<int:id>/', views.edit_album, name='edit_album'),
    path('album/delete/<int:id>/', views.delete_album, name='delete_album'),
]
