from django.contrib import admin
from .models import PG, RoomDetails
# Register your models here.
@admin.register(PG)
class PGAdmin(admin.ModelAdmin):
    list_display = ('pg_name', 'owner_name', 'pg_type', 'available_from')





