from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/<sort>/', views.ShowAll, name='movie-list'),
    path('actor-list/', views.ShowAllActors, name='actor-list'),
    path('movie-update/', views.updateMovie, name='movie-update'),
]