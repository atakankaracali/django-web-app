# Generated by Django 3.2.12 on 2022-03-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="isPublished",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.TextField(verbose_name="Movie Description"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="image",
            field=models.CharField(max_length=50, verbose_name="Movie Image"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Movie Name"),
        ),
    ]
