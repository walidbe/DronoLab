from django.db import models
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    source = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    download_speed = models.CharField(max_length=10)
    altitude = models.CharField(max_length=10)
    pression = models.CharField(max_length=10)

    def publish(self):
        self.published_date = timezone.now()
        self.save()