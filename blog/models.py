from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()

    date = models.DateField()

    def __str__(self):
        return self.title
