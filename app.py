from flask import Flask, request, jsonify
from utils import load_events, save_events, parse_datetime
import uuid

app = Flask(__name__)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data['description'],
        "start_time": data['start_time'],
        "end_time": data['end_time'],
        "recurrence": data.get('recurrence')  # optional
    }
    events = load_events()
    events.append(event)
    events.sort(key=lambda x: parse_datetime(x['start_time']))
    save_events(events)
    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = load_events()
    events.sort(key=lambda x: parse_datetime(x['start_time']))
    return jsonify(events)

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    events = load_events()
    for event in events:
        if event['id'] == event_id:
            event.update({k: v for k, v in data.items() if k in event})
            save_events(events)
            return jsonify(event)
    return jsonify({"error": "Event not found"}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    new_events = [e for e in events if e['id'] != event_id]
    if len(new_events) == len(events):
        return jsonify({"error": "Event not found"}), 404
    save_events(new_events)
    return jsonify({"message": "Event deleted"})

@app.route('/search', methods=['GET'])
def search_events():
    query = request.args.get('q', '').lower()
    events = load_events()
    matched = [e for e in events if query in e['title'].lower() or query in e['description'].lower()]
    return jsonify(matched)

if __name__ == '__main__':
    app.run(debug=True)