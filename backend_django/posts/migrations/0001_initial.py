# Generated by Django 3.1 on 2022-08-28 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import genres.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('url_website', models.URLField(blank=True, null=True)),
                ('url_video', models.URLField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image_post', models.ImageField(upload_to=genres.models.get_file_path)),
                ('initial_featured_date', models.DateTimeField(blank=True, null=True)),
                ('end_featured_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(related_name='postsgen', to='genres.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_post', models.ImageField(upload_to=genres.models.get_file_path)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageps', to='posts.post')),
            ],
        ),
    ]
