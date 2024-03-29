from django import forms
import re
from django.utils import timezone
from .models import Reservation

#https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_guests', 'table_location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': timezone.localdate().isoformat()}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '10:00', 'max': '22:00'}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'number_of_guests': forms.Select(choices=[(i, i) for i in range(1, 9)]),
            'table_location': forms.Select()
        }
        
    def clean_name(self):
        name = self.cleaned_data.get('name')  
        if name is None:  # Check if name is None
            raise forms.ValidationError("Name cannot be empty.")
        name = name.strip()  
        if not name:  # Check if name is empty after stripping whitespace
            raise forms.ValidationError("Name cannot contain only spaces.")
        if len(name.strip()) < 3:  # Check if the name has less than 3 characters
            raise forms.ValidationError("Name must contain at least 3 letters.")
        if re.match(r'^[a-zA-Z\s]+$', name):  # Check if the name contains only letters and spaces
            return name  
        else:
            raise forms.ValidationError("Name can only contain letters and spaces.")
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['table_location'].choices = Reservation._meta.get_field('table_location').choices
