import requests
from bs4 import BeautifulSoup
from flask import Flask, request, url_for
from flask_restful import Resource, Api, reqparse


def get_events(url):
    all_events = []
    source = requests.get(url).content
    soup = BeautifulSoup(source, 'lxml')
    events = soup.find_all('div', {'class':'card'})
    for event in events:
        event_desc = {}
        event_desc['link'] = 'https://meetup.com'+event.find('a')['href']
        event_desc['title'] = event.find('a', {'class':'eventCardHead--title'}).text
        event_desc['datetime'] = event.find('time')['datetime']
        event_desc['datetime_str'] = event.find('time').text
        event_desc['location'] = event.find('address').text
        all_events.append(event_desc)
    return {'all_events':all_events}

parser = reqparse.RequestParser()
parser.add_argument('url', type=str, help='The URL of the event page of the meetup')

class Home(Resource):
    def get(self):
        return {"Usage":"Send a POST request with the event page URL to /get_events"}

class Events(Resource):
    def post(self):
        args = parser.parse_args()
        url = args['url']
        return get_events(url)

app  = Flask(__name__)
api = Api(app)
api.add_resource(Home, '/')
api.add_resource(Events, '/get_events')
