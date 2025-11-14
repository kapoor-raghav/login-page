from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventApplicationForm, EventImageForm, EventVideoForm
from .models import EventImage, EventVideo
from django.http import JsonResponse
import json, os
from django.conf import settings

# Helper function to load JSON file
def load_json_file(filename):
    file_path = os.path.join(settings.BASE_DIR, "Registration", "static", "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# district API
def districts(request):
    data = load_json_file("district.json")
    state_id = request.GET.get("state_id")

    if state_id:
        filtered = [d for d in data["districtList"] if str(d.get("parent_id")) == str(state_id)]
        return JsonResponse({"districtList": filtered}, safe=False)

    return JsonResponse(data, safe=False)


# Ministries API
def ministries(request):
    data = load_json_file("ministry.json")
    return JsonResponse(data, safe=False)

# States API
def states(request):
    data = load_json_file("state.json")
    return JsonResponse(data, safe=False)

# Districts API (optionally filter by state_id)
def districts(request):
    data = load_json_file("district.json")
    state_id = request.GET.get("state_id")

    if state_id:
        # Filter districts belonging to the selected state
        filtered = [d for d in data["districtList"] if str(d.get("parent_id")) == str(state_id)]
        return JsonResponse({"districtList": filtered}, safe=False)

    return JsonResponse(data, safe=False)



def event_application_view(request):
    if request.method == 'POST':
        form = EventApplicationForm(request.POST)
        image_form = EventImageForm(request.POST, request.FILES)
        video_form = EventVideoForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save()

            # Handle multiple image uploads
            for img in request.FILES.getlist('image'):
                EventImage.objects.create(event=event, image=img)

            # Handle multiple video uploads
            for vid in request.FILES.getlist('video'):
                EventVideo.objects.create(event=event, video=vid)

            messages.success(request, "✅ Event Application submitted successfully!")
            return redirect('event_application')

        else:
            messages.error(request, "❌ The form has errors")
    else:
        form = EventApplicationForm()
        image_form = EventImageForm()
        video_form = EventVideoForm()

    return render(request, 'event_form_2.html', {
        'form': form,
        'image_form': image_form,
        'video_form': video_form,
    })
