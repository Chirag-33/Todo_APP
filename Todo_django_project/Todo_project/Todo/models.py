from django.db import models

# Create your models here.
class  task(models.Model):
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title