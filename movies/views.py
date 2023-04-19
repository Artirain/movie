from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
from .models import Movie


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movies.html', {'movie_list': movies})

# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug) #будем искать фильм по полю url который равен slug
#         return render(request, 'movies/movie_detail.html', {'movie': movie})



#отвечает за отображение записей
class MoviesView(ListView): #наследуемся от класса Django View
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False) #забираем все записи, у которвых fraft=False
    # template_name = 'movies/movies.html'
    
#класс отвечает за url, по которому будет находить нужную запись
class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'url' #по какому полю будем искать нужную запись (url)
    