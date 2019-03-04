from django.db import models


class Meme(models.Model):
    image = models.FileField(upload_to='', blank=True)
    title = models.CharField(max_length=255)
