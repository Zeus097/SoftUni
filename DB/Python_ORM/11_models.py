from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import IsAwardedMixin, IsUpdatedMixin


class Base(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )

    class Meta:
        abstract = True


class Director(Base):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    objects = DirectorManager()


class Actor(Base, IsAwardedMixin, IsUpdatedMixin):
    pass


class Movie(IsAwardedMixin, IsUpdatedMixin):
    class MovieChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5)
        ]
    )
    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True
    )
    genre = models.CharField(
        max_length=6,
        choices=MovieChoices,
        default=MovieChoices.OTHER
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ],
        default=0.0
    )
    is_classic = models.BooleanField(default=False)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='director_movies'  # Through Director, we use it with this name
    )
    starring_actor = models.ForeignKey(
        Actor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='starring_movies'  # Through Actor, we use it with this name
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='actor_movies'  # Through Actor, we use it with this name
    )











