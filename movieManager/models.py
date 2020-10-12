from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    movie_genre = models.CharField(max_length=255)
    movie_year = models.DateField()
    image = models.ImageField(upload_to='movieManager')

    def __str__(self):
        return '{} {} {}'.format(self.movie_title, self.movie_genre, self.movie_year)
