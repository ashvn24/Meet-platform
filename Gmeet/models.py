from django.db import models

# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    google_meet_link = models.URLField(null=True, blank=True)