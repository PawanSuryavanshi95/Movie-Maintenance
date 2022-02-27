from django.contrib import admin

from . models import Actor, Linking, Movie

# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Linking)