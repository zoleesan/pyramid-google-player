from pyramid.view import view_config
from gmusicapi import Mobileclient
from datetime import timedelta
from google_player.config import *
from google_player.helper import *
import pprint
import os.path
import json

pp = pprint.PrettyPrinter(indent=2)


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):

    sync = request.params.get('sync', None)
    api = Mobileclient()

    api.login(GOOGLE_EMAIL,
              GOOGLE_MUSIC_PASS,
              Mobileclient.FROM_MAC_ADDRESS)

    if os.path.isfile('songs.json') and not sync:
        f = open('songs.json', 'r')
        songs = f.read()
        songs = json.loads(songs)
    else:
        print('dadadad')
        songs = api.get_all_songs()
        songs = list(reversed(resort_by_added(songs)))

        f = open('songs.json', 'w')
        f.write(json.dumps(songs, indent=4, separators=(',', ': ')))
        f.close()

    result = []
    back = timedelta(days=10)
    now = datetime.now()

    for track in songs:
        d = get_datetime(track['creationTimestamp'])
        if (now - d) < back:
            result.append({'name': track['title'],
                           'url': api.get_stream_url(track['id'],
                                                     GOOGLE_DEVICE_ID),
                           'date': d.strftime("%a %d-%m-%Y %H:%M")})

    return {'song_list': result, 'name': "Song list", 'req_host': request.host}
