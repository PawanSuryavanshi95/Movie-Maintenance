from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.CharField(max_length=100, null=False, blank=False)
    release_date = models.DateField()
    like = models.IntegerField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Linking(models.Model):
    movie_id = models.IntegerField()
    actor_id = models.IntegerField()

    def __str__(self):
        return str(self.movie_id) + "_" + str(self.actor_id)