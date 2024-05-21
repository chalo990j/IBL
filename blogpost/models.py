from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f" {self.id} {self.title}, {self.content}"
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
