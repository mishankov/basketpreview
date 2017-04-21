from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    short_body = models.TextField()
    date = models.DateTimeField()
    cover_link = models.ImageField(default = 0)
    image_link = models.ImageField(default = 0)

    def __str__(self):
        return self.title
