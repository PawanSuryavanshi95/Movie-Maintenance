# Generated by Django 3.0.2 on 2022-02-20 14:59

from django.db import migrations


def addRow(apps, schema_editor):
    
    Movie = apps.get_model('api', 'Movie')
    bourne = Movie.objects.get(name="Bourne Identity")

    Actor = apps.get_model('api', 'Actor')
    matt = Actor.objects.get(name="Matt Damon")

    Linking = apps.get_model('api', 'Linking')
    newLink = Linking(movie_id=bourne.id, actor_id=matt.id)
    newLink.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220220_2020'),
    ]

    operations = [
        migrations.RunPython(addRow),
    ]
