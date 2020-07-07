from django.urls import path
from . import views

urlpatterns = [
    path('newgame/', views.generate_party),
    path('game/<str:uuid>/', views.get_party),
]
