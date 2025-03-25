from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from main_app.mixins import IsAwardedMixin, LastUpdatedMixin
from main_app.choices import MovieGenreChoices
from main_app.managers import DirectorModelManager


class BaseData(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
        )
    birth_date = models.DateField(
        default='1900-01-01'
    )
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )


class Director(BaseData):
    years_of_experience = models.SmallIntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0
    )

    objects = DirectorModelManager()


class Actor(BaseData, IsAwardedMixin, LastUpdatedMixin):
    pass


class Movie(IsAwardedMixin, LastUpdatedMixin):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(
        max_length=6,
        choices=MovieGenreChoices,
        default=MovieGenreChoices.OTHER,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ],
        default=0.0
    )
    is_classic = models.BooleanField(
        default=False
    )
    director = models.ForeignKey(
        # Establishes a one-to-many relationship with the Director model,
        # associating each movie with a director
        Director,
        on_delete=models.CASCADE,
        related_name='movie_directors',
    )
    starring_actor = models.ForeignKey(
        # Establishes a one-to-many relationship with the Actor model,
        # associating each movie with a starring actor who is the main character.
        Actor,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='movie_starring_actors',
    )
    actors = models.ManyToManyField(
        # Establishes a many-to-many relationship with the Actor model,
        # allowing multiple actors to participate in a movie and an actor to participate in multiple movies.
        Actor,
        related_name='movie_actors',
    )









