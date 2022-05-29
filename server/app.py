import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


EVENTS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Picnic at the Park',
        'image': 'https://static.wikia.nocookie.net/pikmin/images/3/32/P3_Yellow_Pikmin.png',
        'date': '2022-05-11',
        'time': '17:00',
        'attending': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Book Club Meeting',
        'image': 'https://pikmin.wiki.gallery/images/e/ee/Purple_Pikmin_HD.png',
        'date': '2022-05-13',
        'time': '15:30',
        'attending': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Company Retreat',
        'image': 'https://pikmin.wiki.gallery/images/5/55/Blue_Pikmin.png',
        'date': '2022-05-12',
        'time': '17:00',
        'attending': True
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
            'image': post_data.get('image'),
            'date': post_data.get('date'),
            'time': post_data.get('time'),
            'attending': post_data.get('attending')
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
            'attending': post_data.get('attending')
        })
        response_object['message'] = 'Event updated!'
    if request.method == 'DELETE':
        remove_event(event_id)
        response_object['message'] = 'Event removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
