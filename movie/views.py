from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *

from .forms import MovieRatingForm, ContactForm 
import telebot

me = 1971799716
TOKEN = '1958584001:AAEzosysE-gTcF5FuyK82p7ziy1j7DYtiI8'
bot = telebot.TeleBot(TOKEN)

class HomePageView(View):
	# Home Page Movies View
	def get(self,request):
		form = MovieRatingForm(request.GET)
		if form.is_valid():
			form.save()
		else:
			form = MovieRatingForm()
		movie = Movie.objects.all()

		top_viewed = Movie.objects.all().order_by('-views')[:6]
		recent_add = Movie.objects.all().order_by('-id')[:6]
		random_movies = Movie.objects.all().order_by('?')[:6]
		fantastic_movies = Movie.objects.all().order_by('-id')[:6]
		zombie_movies = Movie.objects.all().order_by('-id')[6:]
		all_movies = Movie.objects.all().order_by('-id')
		for x in all_movies:
			print(x.title)
			print(x.title)
			print(x.title)
			print(x.title)
			
		context = {
			'top_viewed':top_viewed,
			'movies':movie,
			'recent_add':recent_add,
			'random_movies':random_movies,
			'form':form,
			'fantastic_movies':fantastic_movies,
			'zombie_movies':zombie_movies,
			'all_movies':all_movies,
		}
		return render(request, 'index.html', context)


class MovieDetailView(DetailView):
	model = Movie
	template_name = 'single.html'
	slug_field = 'slug'

class ContactPageView(View):
	def get(self, request):
		form = ContactForm()
		context = {'form': form}
		return render(request, 'contact.html', context)

	def post(self, request):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'contact.html')
		else:
			form = ContactForm()
			context = {'form': form}
		return render(request, 'contact.html', context)


# Test  views 

class AllPostView(ListView):
	model = Post
	paginated_by = 10
	template_name = 'news.html'
	context_object_name = 'posts'

class PostDetailView(DetailView):
	model = Post
	slug_field = 'slug'
	template_name = 'news-single.html'


def getCatPost(request,category_slug):
	category = PostCategory.objects.get(slug=category_slug)
	posts = category.posts.all
	return render(request, 'cat_post.html', {'posts':posts})

def getTagPost(request,tag_slug):
	tag = Tags.objects.get(slug=tag_slug)
	posts = tag.posts.all()
	return render(request, 'cat_post.html', {'posts':posts})



# Genres And Categories

def genreDetail(request, genre):
	genre = get_object_or_404(Genre, slug=genre)
	movie = Movie.objects.filter(genre=genre)
	context = {
		'movie':movie
	}
	return render(request, 'genres.html', context)


def search(request):
	q = request.GET.get('search', None)
	movies = Movie.objects.filter(title__icontains=q)
	posts = Post.objects.filter(title__icontains=q)
	total_results = len(movies) + len(posts)
	query = request.GET['search']
	context = {
		'movies':movies,
		'posts':posts,
		'total_results':total_results,
		'query':query
	}
	return render(request, 'searchResult.html', context)


def aloqalar(request):
	d = bot.send_message(me,"gfgdfgdfgf")
	print(d)
	if request.method == 'POST':
		first_name = request.POST['name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		Contact.objects.create(first_name=first_name,last_name=last_name,subject=phone,email=email,message=message)
		# messages.add_message(request, messages.SUCCESS, 'Tabriklaymiz aloqa muofaqiyat amalga oshirildi tez orada sizbilan boglanamiz')
		bot.send_message(me,f"Saytdan xabar bor\nIsmi:  {first_name}\n Familiyasi: {last_name}\n Telfon raqami:  {phone}\nEmail:  {email}\n Xabari:  {message}")
	return render(request,'contact.html')

def movies(request):
	return render(request, 'movies.html')

