from django.contrib import admin
from .models import *


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['genre']


@admin.register(Studios)
class StudiosAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Statuses)
class StatusesAdmin(admin.ModelAdmin):
    list_display = ['status']


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'studio', 'category', 'status']
    list_filter = ['studio', 'category', 'status']


@admin.register(AnimeRatings)
class AnimeRatingsAdmin(admin.ModelAdmin):
    list_display = ['value', 'user', 'anime']


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ['value']
