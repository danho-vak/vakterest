from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')  # related_name 으로user object에서 article.writer를 접근 할 때 설정함
    title = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)
