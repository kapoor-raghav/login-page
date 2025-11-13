from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    MinValueValidator,
    URLValidator
)
from django.core.exceptions import ValidationError

def validate_end_date(value):
    """Custom validator to ensure end date is not before start date."""
    # This will be checked in clean() instead, since we need both start and end dates
    return value

def validate_youtube_links(value):
    """Ensure that youtube_links contains valid URLs (comma-separated)."""
    urls = [url.strip() for url in value.split(",") if url.strip()]
    validator = URLValidator()
    for url in urls:
        try:
            validator(url)
        except ValidationError:
            raise ValidationError(f"Invalid URL: {url}")

class EventApplication(models.Model):
    USER_TYPE_CHOICES = [
        ("Ministry", "Ministry"),
        ("State", "State"),
        ("College", "College"),
        ("Institute", "Institute"),
        ("School", "School"),
        ("Other", "Other"),
    ]

    username = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    ministry_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^[A-Za-z ]+$', 'Only letters and spaces allowed')]
    )
    department = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^[A-Za-z ]+$', 'Only letters and spaces allowed')]
    )
    state = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)

    event_name = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )
    event_state = models.CharField(max_length=100)
    event_district = models.CharField(max_length=100)
    event_venue = models.CharField(max_length=300)

    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)

    no_of_participants = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    event_description = models.TextField(
        max_length=1000,
        validators=[MinLengthValidator(20)]
    )
    youtube_links = models.TextField(
        blank=True,
        null=True,
        validators=[validate_youtube_links]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Cross-field validation: ensure end_date >= start_date."""
        if self.event_end_date and self.event_start_date:
            if self.event_end_date < self.event_start_date:
                raise ValidationError({
                    "event_end_date": "End date cannot be before start date."
                })

    def __str__(self):
        return self.event_name


class EventImage(models.Model):
    event = models.ForeignKey(EventApplication, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f"Image for {self.event.event_name}"


class EventVideo(models.Model):
    event = models.ForeignKey(EventApplication, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='event_videos/')

    def __str__(self):
        return f"Video for {self.event.event_name}"
