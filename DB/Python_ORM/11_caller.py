import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from datetime import date
from django.db.models import Q, Count, Avg, F


def populate_db() -> None:

    director1 = Director.objects.create(
        full_name="Christopher Nolan",
        birth_date=date(1970, 7, 30),
        nationality="British",
        years_of_experience=30
    )

    director2 = Director.objects.create(
        full_name="Quentin Tarantino",
        birth_date=date(1963, 3, 27),
        nationality="American",
        years_of_experience=35
    )

    actor1 = Actor.objects.create(
        full_name="Leonardo DiCaprio",
        birth_date=date(1974, 11, 11),
        nationality="American",
        is_awarded=True
    )

    actor2 = Actor.objects.create(
        full_name="Christian Bale",
        birth_date=date(1974, 1, 30),
        nationality="British",
        is_awarded=True
    )

    movie1 = Movie.objects.create(
        title="Inception",
        release_date=date(2010, 7, 16),
        storyline="A skilled thief is given a chance at redemption if he can successfully perform inception.",
        genre=Movie.MovieChoices.ACTION,
        rating=8.8,
        is_classic=True,
        director=director1,
        starring_actor=actor1
    )

    movie2 = Movie.objects.create(
        title="Pulp Fiction",
        release_date=date(1994, 10, 14),
        storyline="The lives of two hitmen, a boxer, and a gangster intertwine in a series of unexpected events.",
        genre=Movie.MovieChoices.DRAMA,
        rating=8.9,
        is_classic=True,
        director=director2,
        starring_actor=actor2
    )

    # Adding actors to movies
    movie1.actors.add(actor1, actor2)
    movie2.actors.add(actor1, actor2)


def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)
    elif search_name is not None:
        query = Q(query_name)
    else:
        query = Q(query_nationality)

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    return "\n".join(
        f"Director: {d.full_name}, "
        f"nationality: {d.nationality}, "
        f"experience: {d.years_of_experience}"
        for d in directors
    )


def get_top_director() -> str:
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""
    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actor = Actor.objects.prefetch_related(
        'starring_movies'
    ).annotate(
        movies_count=Count('starring_movies'),
        average_rating=Avg('starring_movies__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not actor or not actor.movies_count:
        return ""

    movies = ', '.join(m.title for m in actor.starring_movies.all())

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {movies}, "
            f"movies average rating: {actor.average_rating:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        participation_number=Count('actor_movies')
    ).order_by(
        '-participation_number', 'full_name'
    )[:3]

    # If there are no movies and respectively no actors participating, return an empty string ("").
    if not actors or not actors[0].participation_number:  # Първия ако няма, няма смисъл да търсим в другите..
        return ""

    return "\n".join(f"{a.full_name}, participated in {a.participation_number} movies" for a in actors)


def get_top_rated_awarded_movie():
    movie = Movie.objects.select_related('starring_actor').prefetch_related('actors').filter(is_awarded=True).order_by('-rating', 'title').first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    cast = ', '.join(m.full_name for m in movie.actors.order_by('full_name'))

    return (f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. Cast: {cast}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10.0)

    if not movies_to_update:
        return "No ratings increased."

    updated_count = movies_to_update.count()

    movies_to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_count} movies."



