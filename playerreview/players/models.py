from django.db import models

class Players(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=200)
    number_of_reviews = models.IntegerField(default=0)
class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

