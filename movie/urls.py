from django.urls import path 
from .import views

app_name = 'movie'

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('movie/<slug:slug>', views.MovieDetailView.as_view(), name='movie_detail'),
	path('contact/', views.ContactPageView.as_view(), name='contact'),

	#News url 
	path('posts/', views.AllPostView.as_view(), name='posts'),
	path('post/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
	path('posts/<slug:category_slug>', views.getCatPost, name='category_posts'),
	path('tags/<slug:tag_slug>', views.getTagPost, name='tag_posts'),

	#Genres and Ctegories
	path('janr/<slug:genre>', views.genreDetail, name='genre_detail'),

	#Search  and other utils
	path('search/', views.search, name='search'),
	
	path('aloqalar/', views.aloqalar, name='aloqalar'),
	path('movies/', views.movies, name='movies'),
]