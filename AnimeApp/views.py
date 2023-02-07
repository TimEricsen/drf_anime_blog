from django.db.models import *
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny, DjangoModelPermissionsOrAnonReadOnly
from .permissions import IsOwnerOrReadOnly, IsNotAuthenticated, IsUser

# All views are created with generics


class GenresList(ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class GenreRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class StudiosList(ListCreateAPIView):
    queryset = Studios.objects.all()
    serializer_class = StudioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class StudioRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Studios.objects.all()
    serializer_class = StudioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class CategoriesList(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class CategoryRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class StatusesList(ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class StatusRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class AnimeList(ListAPIView):
    queryset = Anime.objects.all().annotate(
        rating=Avg('ratings__value__value')
    ).order_by('rating').reverse()
    serializer_class = AnimeSerializer


class AnimeRetrieve(RetrieveAPIView):
    queryset = Anime.objects.all().annotate(
        rating=Avg('ratings__value__value')
    )
    serializer_class = AnimeSerializer


class AnimeAdminList(ListCreateAPIView):
    queryset = Anime.objects.all().annotate(
        rating=Avg('ratings__value__value')
    ).order_by('title')
    serializer_class = AnimeSerializer
    permission_classes = [IsAdminUser]


class AnimeAdminRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all().annotate(
        rating=Avg('ratings__value__value')
    )
    serializer_class = AnimeSerializer
    permission_classes = [IsAdminUser]


class AnimeRatingList(ListCreateAPIView):
    queryset = AnimeRatings.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnimeRatingRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = AnimeRatings.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UseRetrieve(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny, IsNotAuthenticated]



