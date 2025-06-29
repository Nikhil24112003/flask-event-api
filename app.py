from flask import Flask, jsonify, request
from models import Event
from storage import load_events, save_events
from datetime import datetime

app = Flask(__name__)
events = load_events()

@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda e: e.start_time)
    return jsonify([e.to_dict() for e in sorted_events]), 200

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    try:
        new_event = Event(
            title=data['title'],
            description=data['description'],
            start_time=data['start_time'],
            end_time=data['end_time']
        )
        events.append(new_event)
        save_events(events)
        return jsonify(new_event.to_dict()), 201
    except KeyError:
        return jsonify({'error': 'Missing fields'}), 400

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    for event in events:
        if event.id == event_id:
            event.title = data.get('title', event.title)
            event.description = data.get('description', event.description)
            event.start_time = data.get('start_time', event.start_time)
            event.end_time = data.get('end_time', event.end_time)
            save_events(events)
            return jsonify(event.to_dict()), 200
    return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [e for e in events if e.id != event_id]
    save_events(events)
    return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
