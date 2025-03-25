import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from datetime import date
from django.db.models import Count, Q, F, Avg, Max


def populate_db():
    first_director = Director(
        full_name="James Cameron",
        birth_date=date(1970, 7, 30),
        nationality="British",
        years_of_experience=25
    )

    second_director = Director(
        full_name="Zack Shneider",
        birth_date=date(1963, 3, 27),
        nationality="American",
        years_of_experience=30
    )

    new_directors = [first_director, second_director]
    Director.objects.bulk_create(new_directors)

    first_actor = Actor(
        full_name="Johnny Depp",
        birth_date=date(1974, 11, 11),
        nationality="American",
        is_awarded=True
    )

    second_actor = Actor(
        full_name="Djerard Butler",
        birth_date=date(1974, 1, 30),
        nationality="British",
        is_awarded=True
    )

    third_actor = Actor(
        full_name="Arno9ld Schverzenegger",
        birth_date=date(1963, 12, 18),
        nationality="American",
        is_awarded=True
    )

    new_actors = [first_actor, second_actor, third_actor]
    Actor.objects.bulk_create(new_actors)

    first_movie = Movie(
        title="Inception",
        release_date=date(2010, 7, 16),
        storyline="A skilled thief is given a chance to have his past crimes forgiven if he can implant an idea into someone's subconscious.",
        genre="Action",
        rating=8.8,
        is_classic=True,
        director=first_director,
        starring_actor=first_actor
    )

    second_movie = Movie(
        title="The Dark Knight",
        release_date=date(2008, 7, 18),
        storyline="Batman faces the Joker, a criminal mastermind bent on creating chaos in Gotham.",
        genre="Action",
        rating=9.0,
        is_classic=True,
        director=first_director,
        starring_actor=second_actor
    )

    third_movie = Movie(
        title="Once Upon a Time in Hollywood",
        release_date=date(2019, 7, 26),
        storyline="A fading television actor and his stunt double navigate the changing Hollywood film industry.",
        genre="Comedy",
        rating=7.6,
        is_classic=False,
        director=second_director,
        starring_actor=third_actor
    )

    new_movies = [first_movie, second_movie, third_movie]
    Movie.objects.bulk_create(new_movies)

    first_movie.actors.add(first_actor, third_actor)
    second_movie.actors.add(first_actor, second_actor)
    third_movie.actors.add(first_actor, third_actor)


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    director_name = Q(full_name__icontains=search_name)
    director_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(director_name) & Q(director_nationality)
    elif search_name is not None:
        query = Q(director_name)
    else:
        query = Q(director_nationality)

    directors = Director.objects.filter(query).order_by("full_name")
    if not directors:
        return ""

    return "\n".join(
        f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in directors
    )


def get_top_director():
    tot_director = Director.objects.get_directors_by_movies_count().first()
    if not tot_director:
        return ""

    return f"Top Director: {tot_director.full_name}, movies: {tot_director.directors_count}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        movie_count=Count('movie_starring_actors'),
        average_rating=Avg('movie_starring_actors__rating')
    ).order_by(
        '-movie_count', 'full_name'
    ).first()

    if not top_actor or not top_actor.movie_count:
        return ""

    movies = ', '.join(m.title for m in top_actor.movie_starring_actors.all())

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {movies}, "
            f"movies average rating: {top_actor.average_rating:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        movie_count=Count('movie_actors'),
    ).order_by('-movie_count', 'full_name')[:3]

    if not actors or not actors[0].movie_count:
        return ""

    return '\n'.join(f"{a.full_name}, participated in {a.movie_count} movies" for a in actors)


def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(
            is_awarded=True
    ).order_by('-rating', 'title').first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    participating_actors = ', '.join(a.full_name for a in movie.actors.order_by('full_name'))

    return (f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. Cast: {participating_actors}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(
        is_classic=True,
        rating__lt=10
    )

    if not movies_to_update:
        return "No ratings increased."

    updated_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_count} movies."

