from django.db import models
from django.contrib.auth.models import User


class Genres(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Studios(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    established = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Studio'
        verbose_name_plural = 'Studios'


class Categories(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Statuses(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Anime(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default='')
    genres = models.ManyToManyField(
        Genres,
        related_name='animes'
    )
    studio = models.ForeignKey(
        Studios,
        on_delete=models.CASCADE,
        related_name='animes'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='animes'
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.CASCADE,
        related_name='animes'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'


# Model, that keeps possible rating values. (0-10)
class Ratings(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class AnimeRatings(models.Model):
    value = models.ForeignKey(
        Ratings,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    def __str__(self):
        return f'{self.anime}: {self.value}\nby: {self.user.username}'





