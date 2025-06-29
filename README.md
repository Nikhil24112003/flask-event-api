# flask-event-api (Flask Backend)

This is a simple Python Flask application that allows users to **Create**, **Read**, **Update**, and **Delete** (CRUD) events.

Each event includes:
- Title
- Description
- Start Time
- End Time

All events are stored in a JSON file (`events.json`) for **data persistence**.

---

## Features

1) Create new events  
2) View all scheduled events (sorted by start time)  
3) Update existing events  
4) Delete events  
5) File-based persistence using JSON  
6) Tested via Postman (collection included)

---

##  Tech Stack

- Python 3.x
- Flask
- JSON
- Postman (for API testing)

---

## How TO Run 
pip install -r requirements.txt
python app.py
App will start at: http://127.0.0.1:5000/

## API Endpoints :
 # Create Event  
  Method: POST
  URL: /events
  Body (JSON):

  # View Events
  Method: GET
  URL: /events

  # Update Event
  Method: PUT
  URL: /events/<event_id> - Enter Event Id
  Body (JSON):

  # Delete Event
  Method: DELETE
  URL: /events/<event_id> -Enter Event Id

## Postman Collection
Nikhil_Event_Manager(Flask REST API).postman_collection.json


 



