# Generated by Django 3.1.1 on 2020-10-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=255)),
                ('movie_genre', models.CharField(max_length=255)),
                ('movie_year', models.DateField()),
                ('image', models.ImageField(upload_to='movie')),
            ],
        ),
    ]
