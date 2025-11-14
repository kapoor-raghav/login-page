# 🎨 Event Creation Template

## 📌 Overview
This template provides the **frontend form** for creating an event in the Vande Mataram application.  
It uses **Bootstrap 5** for styling and integrates with **Django forms** to render dynamic fields.  

The template supports:
- User type selection (`Ministry`, `State`, `College`, etc.)
- Conditional rendering of ministry/department fields
- Conditional rendering of state/district fields
- Event details (name, venue, dates, participants, description)
- Uploading images and videos
- Adding YouTube links
- Terms & conditions 

## ✅ Key Features
- **Dynamic Features
- **Dynamic form rendering** based on `user_type form rendering** based on `user_type`
- **AJAX integration`
- **AJAX integration** with `/api/ministries`, `/api/states`, `/api/districts`
- **Bootstrap** with `/api/ministries`, `/api/states`, `/api/districts`
- **Bootstrap styling** for responsive styling** for responsive layout
- **Error layout
- **Error handling** via Django handling** via Django messages
- **Media uploads** for images and videos
- **Validation ready messages
- **Media uploads** for images and videos
- **Validation ready** (integrates with Django model validators** (integrates with Django model validators)

# 📝 Event Application Models Update

## 📌 Summary
This update introduces **model-level validators** to the `EventApplication` model.  
Validators enforce **data integrity, consistency, and business rules** across all entry points (forms, admin, APIs, scripts).

---

## 🔹 Changes Made

### 1. Field-Level Validators
```python
username = models.CharField(
    max_length=100,
    validators=[MinLengthValidator(3)]  # must be at least 3 characters
)

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

event_name = models.CharField(
    max_length=150,
    validators=[MinLengthValidator(5)]  # event name must be meaningful
)

no_of_participants = models.PositiveIntegerField(
    validators=[MinValueValidator(1)]  # must be at least 1
)

event_description = models.TextField(
    max_length=1000,
    validators=[MinLengthValidator(20)]  # description must be at least 20 chars
)

youtube_links = models.TextField(
    blank=True,
    null=True,
    validators=[validate_youtube_links]  # custom validator for comma-separated URLs
)
```
# 📑 Django Forms for Event Management

## 📌 Overview
This file defines **forms** for the `EventApplication`, `EventImage`, and `EventVideo` models.  
It leverages Django’s `ModelForm` to automatically bind form fields to model attributes, while customizing widgets for better **Bootstrap integration** and **multi-file uploads**.

---
## Data shifting
- data shifted from json to typle
    - Less moving parts: No need to maintain external JSON files, paths, or helper functions.
    - Immutable: Tuples are fixed at runtime, so you avoid accidental edits or malformed JSON breaking your app.
    - No static files dependency: You don’t need to ship JSON files with your app or worry about file paths in production

# 📑 Template Change Log

## 🔹 Added
- Added event state → district linkage with AJAX fetch.
- Added role‑based UI toggling for Ministry vs State.
- Added department field reset when Ministry selected.

## 🔹 Changed
- District dropdown now clears and repopulates dynamically.
- State dropdown listener added inside `user_type === "State"` branch.

## 🔹 Removed
- Static district options (replaced with dynamic fetch).


