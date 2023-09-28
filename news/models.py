from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    keyword = models.CharField(max_length=30)
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=80, null=True)
    source_id = models.CharField(max_length=30, null=True)
    source_name = models.CharField(max_length=30, null=True)
    article_url = models.TextField(null=True)
    image_url = models.TextField(null=True)
    description = models.TextField(null=True)
    date_published = models.DateTimeField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs= {'pk': self.pk})