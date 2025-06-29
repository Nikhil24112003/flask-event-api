from datetime import datetime
import uuid

class Event:
    def __init__(self, title, description, start_time, end_time, event_id=None):
        self.id = event_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @staticmethod
    def from_dict(data):
        return Event(
            title=data["title"],
            description=data["description"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            event_id=data["id"]
        )
