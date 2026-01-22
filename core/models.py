from django.db import models

# Create your models here.
class PersonDb(models.Model):
    name = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
