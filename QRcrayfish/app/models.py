from django.db import models


# Пример модели Post, если она должна существовать
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
