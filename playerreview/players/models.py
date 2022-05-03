from django.db import models

class Players(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=200, null=True)
    number_of_reviews = models.IntegerField(default=0, null=True)
class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Players, on_delete=models.CASCADE, null=True)
    review = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    accepted = models.BooleanField(default=False, null=True)
    image_link = models.CharField(max_length=200, null=True)
    date_of_submit = models.DateTimeField(auto_now_add=True, null=True)

