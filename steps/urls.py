from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('know/', views.know, name='know'),
    path('connect/', views.connect, name='connect'),
    path('grow/', views.grow, name='grow'),
    path('change/', views.change, name='change'),
    path('person/', views.person, name='person'),
    path('person/progress/<str:person>/<int:id>', views.progress, name='progress'),
    path('know/completed/<str:step>', views.completed, name='completed'),

    
]
