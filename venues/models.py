from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timedelta

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
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_people = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.check_availability():
            raise ValidationError("The venue is not available for the selected date and time.")
        super(Booking, self).save(*args, **kwargs)

    def check_availability(self):
        # Check if there is any booking that overlaps with the desired time slot for the same venue
        overlapping_bookings = Booking.objects.filter(
            venue=self.venue,
            date=self.date
        ).exclude(
            id=self.id  # exclude the current booking from the check in case of update
        ).filter(
            models.Q(end_time__gt=self.start_time) & models.Q(start_time__lt=self.end_time)
        )
        return not overlapping_bookings.exists()


class Review(models.Model):
    venue = models.ForeignKey(Venue, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
