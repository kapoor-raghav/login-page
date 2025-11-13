import json
from .Registration.models import State, District, Ministry

# Load States
with open('state.json', encoding='utf-8') as f:
    data = json.load(f)
for st in data["stateList"]:
    State.objects.get_or_create(name=st["name"])

# Load Ministries
with open('ministry.json', encoding='utf-8') as f:
    data = json.load(f)
for m in data:
    Ministry.objects.get_or_create(name=m["ministry_name"], website=m["official_website_url"])

# Load Districts
with open('district.json', encoding='utf-8') as f:
    data = json.load(f)
for d in data["districtList"]:
    try:
        state = State.objects.get(name=d["state_name"])
        District.objects.get_or_create(name=d["name"], state=state)
    except:
        pass
