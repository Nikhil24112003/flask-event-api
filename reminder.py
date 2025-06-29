import time
from datetime import datetime, timedelta
from storage import load_events

def show_reminders():
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        upcoming = datetime.now() + timedelta(hours=1)
        for event in load_events():
            if now <= event.start_time <= upcoming.strftime('%Y-%m-%d %H:%M'):
                print(f" Reminder: '{event.title}' at {event.start_time}")
        time.sleep(60)
