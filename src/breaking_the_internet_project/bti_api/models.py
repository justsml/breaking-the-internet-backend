from django.db import models
from django.utils import timezone
default=timezone.now
# Create your models here.

class Images(models.Model):
    """Stores urls of snapshots taken and the time they were created."""

    image_url = models.URLField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)

    def image_store(self, url):
        self.created_on = timezone.now()
        self.image_url = url
        self.save()

        # return self.image_url
