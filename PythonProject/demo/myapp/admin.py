from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email')
