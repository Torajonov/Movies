from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
	list_display = ['name', 'age', 'country']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['title', 'genre', 'year']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Comment)
admin.site.register(Contact)


#Blog 

@admin.register(PostCategory)
class CategoryPostAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','id','category', 'author']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}