from django.db import models
from django.contrib.auth.models import User

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.title


class GalleryFolder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    folder = models.ForeignKey(GalleryFolder, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    image = models.ImageField(upload_to="gallery/%Y/%m/%d/")  # optional: organize by date
    caption = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.caption


class DailyVerse(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='verses/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Verse {self.id}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='meetings/')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name