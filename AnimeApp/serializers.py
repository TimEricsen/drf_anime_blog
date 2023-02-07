from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class GenresSerializer(ModelSerializer):
    animes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Genres
        fields = ['id', 'genre', 'animes']


class StudioSerializer(ModelSerializer):
    animes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Studios
        fields = ['id', 'name', 'description', 'established', 'animes']


class CategoriesSerializer(ModelSerializer):
    animes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Categories
        fields = ['id', 'category', 'animes']


class StatuSerializer(ModelSerializer):
    animes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Statuses
        fields = ['id', 'status', 'animes']


class AnimeSerializer(ModelSerializer):
    rating = serializers.DecimalField(
        read_only=True,
        decimal_places=2,
        max_digits=3
    )

    genres = serializers.SlugRelatedField(
        many=True,
        queryset=Genres.objects.all(),
        slug_field='genre'
    )

    studio = serializers.SlugRelatedField(
        queryset=Studios.objects.all(),
        slug_field='name'
    )

    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='category'
    )

    status = serializers.SlugRelatedField(
        queryset=Statuses.objects.all(),
        slug_field='status'
    )

    class Meta:
        model = Anime
        fields = ['id', 'title', 'desc', 'genres', 'studio', 'category', 'status', 'rating']


class RatingSerializer(ModelSerializer):
    value = serializers.SlugRelatedField(
        queryset=Ratings.objects.all(),
        slug_field='value'
    )

    user = serializers.ReadOnlyField(
        source='user.username'
    )

    anime = serializers.SlugRelatedField(
        queryset=Anime.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = AnimeRatings
        fields = ['anime', 'value', 'user']

    def create(self, validated_data):
        rating, _ = AnimeRatings.objects.update_or_create(
            user=validated_data.get('user', None),
            anime=validated_data.get('anime', None),
            defaults={
                'value': validated_data.get('value', None)
            }
        )

        return rating


class UserSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'ratings']


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        required=True, write_only=True,
        validators=[validate_password]
    )

    password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
