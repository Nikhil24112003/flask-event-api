import json
from models import Event

FILE_PATH = 'events.json'

def load_events():
    try:
        with open(FILE_PATH, 'r') as f:
            return [Event.from_dict(e) for e in json.load(f)]
    except FileNotFoundError:
        return []

def save_events(events):
    with open(FILE_PATH, 'w') as f:
        json.dump([e.to_dict() for e in events], f, indent=4)
