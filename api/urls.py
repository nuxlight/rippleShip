from django.urls import path
from . import views

urlpatterns = [
    path('newgame/', views.generate_party),
    path('game/<str:uuid>/', views.get_party),
    path('game/ship/<int:pk>/', views.update_ship),
    path('game/position/<int:pk>/', views.update_position),
]
