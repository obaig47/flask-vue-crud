import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

import data
EVENTS = sorted(data.EVENTS, key=lambda k: k['date'], reverse=False)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_event(event_id):
    for event in EVENTS:
        if event['id'] == event_id:
            EVENTS.remove(event)
            return True
    return False


@app.route('/events', methods=['GET', 'POST'])
def all_events():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        EVENTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'image': post_data.get('image'),
            'date': post_data.get('date'),
            'time': post_data.get('time'),
        })
        response_object['message'] = 'Event added!'
    else:
        response_object['events'] = EVENTS
    return jsonify(response_object)


@app.route('/events/<event_id>', methods=['PUT', 'DELETE'])
def single_event(event_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_event(event_id)
        EVENTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'image': post_data.get('image'),
            'date': post_data.get('date'),
            'time': post_data.get('time'),
        })
        response_object['message'] = 'Event updated!'
    if request.method == 'DELETE':
        remove_event(event_id)
        response_object['message'] = 'Event removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
