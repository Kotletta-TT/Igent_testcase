from django.db import models

# Create your models here.


class Post(models.Model):
    post_id = models.CharField(max_length=30)
    owner_id = models.CharField(max_length=30)
    text = models.TextField()
