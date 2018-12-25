from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField
from mdeditor.fields import MDTextField


class Post(models.Model):
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = MDTextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# class ExampleModel(models.Model):
#     name = models.CharField(max_length=10)
#     content = MDTextField()


# Create your models here.
