from django import forms
from .models import PG,RoomDetails

class PGform(forms.ModelForm):
    class Meta:
        model=PG
        fields=['pg_name','owner_name','contact','email','full_address','landmark','google_map_link','check_in_time','check_out_time','gate_closing_time',
                'minimum_stay','available_from','pg_type','image','image','description','pg_wifi','pg_food','pg_ac','pg_parking','rent']




