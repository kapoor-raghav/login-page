from django import forms
from .models import EventApplication, EventImage, EventVideo
    
# ✅ Custom widget that allows multiple files
class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = EventApplication
        fields = [
            'username', 'user_type', 'ministry_name', 'department','state','district',
            'event_name', 'event_state', 'event_district', 'event_venue',
            'event_start_date', 'event_end_date', 'event_time',
            'no_of_participants', 'event_description', 'youtube_links'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User name'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'ministry_name': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'event_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'event_district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter District'}),
            'event_venue': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter event venue'}),
            'event_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'no_of_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter event description'}),
            'youtube_links': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Paste YouTube links (one per line)'}),
        }


# ✅ Image upload form using MultiFileInput
class EventImageForm(forms.ModelForm):
    image = forms.ImageField(widget=MultiFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = EventImage
        fields = ['image']


# ✅ Video upload form using MultiFileInput
class EventVideoForm(forms.ModelForm):
    video = forms.FileField(widget=MultiFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = EventVideo
        fields = ['video']
