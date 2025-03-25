from django.db import models
from django.db.models import Count


class DirectorModelManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(directors_count=Count('movie_directors')).order_by('-directors_count', 'full_name')




