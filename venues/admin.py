from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from .models import Venue, Booking, Review
# Optional: Extend the UserAdmin to include related models or fields
class UserAdmin(DefaultUserAdmin):
    pass

# Register the extended UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Admin for Venue
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'postcode')
    search_fields = ('name', 'address')

admin.site.register(Venue, VenueAdmin)

# Admin for Booking
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'venue', 'email', 'mobile_number')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Booking, BookingAdmin)

# Admin for Review
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('venue', 'user', 'text', 'created_at')
    search_fields = ('venue__name', 'user__username', 'text')

admin.site.register(Review, ReviewAdmin)
