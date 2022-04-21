# Generated by Django 4.0.4 on 2022-04-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_reviews_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='number_of_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reviews',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]