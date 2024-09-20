from django.db import models

from artist.models import Artist

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    released_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.artist}"

# Create your models here.
