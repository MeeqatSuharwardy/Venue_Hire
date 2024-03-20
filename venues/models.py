from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Venue(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to='venues/featured_images/')
    gallery_images = models.ImageField(upload_to='venues/gallery_images/')
    features = models.TextField()
    Number_of_guests = models.TextField()
    description = models.TextField()
    address = models.TextField()
    postcode = models.CharField(max_length=10)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

class Review(models.Model):
    venue = models.ForeignKey(Venue, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
