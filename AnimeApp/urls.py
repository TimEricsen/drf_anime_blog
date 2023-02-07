from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('genres/', GenresList.as_view()),
    path('genre/<pk>/', GenreRetrieve.as_view()),

    path('studios/', StudiosList.as_view()),
    path('studio/<pk>/', StudioRetrieve.as_view()),

    path('categories/', CategoriesList.as_view()),
    path('category/<pk>/', CategoryRetrieve.as_view()),

    path('statuses/', StatusesList.as_view()),
    path('status/<pk>/', StatusRetrieve.as_view()),

    path('animelist/', AnimeList.as_view()),
    path('anime/<pk>/', AnimeRetrieve.as_view()),

    path('ratings/', AnimeRatingList.as_view()),
    path('rating/<pk>', AnimeRatingRetrieve.as_view()),

    path('users/', UsersList.as_view()),
    path('user/<pk>', UseRetrieve.as_view()),
    path('register/', RegisterView.as_view()),

    # Special links for admin users, to add/update/delete objects.
    path('adminanimelist/', AnimeAdminList.as_view()),
    path('adminanime/<pk>/', AnimeAdminRetrieve.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
