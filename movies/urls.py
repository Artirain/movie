from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'), #в url будем принимать pk(id) как число
    # path('<int:pk>/', views.MovieDetailView.as_view()),

]