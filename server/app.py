import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


EVENTS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


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
            'author': post_data.get('author'),
            'date': post_data.get('date'),
            'read': post_data.get('read')
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
            'author': post_data.get('author'),
            'date': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Event updated!'
    if request.method == 'DELETE':
        remove_event(event_id)
        response_object['message'] = 'Event removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
