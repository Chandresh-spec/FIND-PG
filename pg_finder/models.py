from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class PG(models.Model):
    pgtye_choices=[
        ('BOYS','Boys'),
        ('GIRLS','Girls'),
        ('COED','co-ed'),
    ]
    pg_name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=100)
    contact = PhoneNumberField("Contact Number", region='IN', null=False, blank=False)
    email=models.EmailField(null=False,blank=False,max_length=254)
    full_address=models.TextField(null=False,blank=False,max_length=250)
    landmark=models.CharField(max_length=150)
    google_map_link=models.URLField(blank=True,null=True)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    gate_closing_time = models.TimeField(blank=True, null=True)
    minimum_stay = models.PositiveIntegerField(help_text="In months")
    available_from = models.DateField()
    pg_type = models.CharField(max_length=10, choices=pgtye_choices)


class
    
    
