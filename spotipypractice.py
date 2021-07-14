import requests
import spotipy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
def create_track_id(song_link):
  stop=31
  song_link=song_link[stop::]
  return song_link
def make_a_dict(album_name,artists,song,track_number,release_date):
  dict={
    'Song name': song,
    'Album name': album_name,
    'Artist(s)': artists,
    'Track number in album': track_number,
    'Release date': release_date
  }
  return dict
CLIENT_ID='2aa8da1299594be28d5bced0f4008ab3'
CLIENT_SECRET='2a2e4cb0bcb54dc6b5b894d5052162e7'
AUTH_URL='https://accounts.spotify.com/api/token'
response=requests.post(AUTH_URL,{
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})
response_json=response.json()
#print(response_json)
#print(response.status_code)
access_token=response_json['access_token']
headers={'Authorization': 'Bearer {token}'.format(token=access_token)}
BASE_URL='https://api.spotify.com/v1/'
#track_id='1GCcR23J4crjdOfdScSwoZ' #for hello world
#track_id='0TQ1FvC8TJ09iibSfwRP81'
track_id=input("Please paste a spotify song link here: ")
track_id=create_track_id(track_id)
r=requests.get(BASE_URL+'tracks/'+track_id, headers=headers)
r_json=r.json()
album_name=r_json['album']['name']
number_of_artists=len(r_json['artists'])
artists=[]
for i in range(number_of_artists):
  artists.append(r_json['artists'][i]['name'])
song=r_json['name']#returns song name
track_number=r_json['track_number']#returns track number in album
release_date=r_json['album']['release_date']#album release date
dict=make_a_dict(album_name,artists,song,track_number,release_date)
#print(dict)
song_dataframe = pd.DataFrame.from_dict(dict)
engine=create_engine('mysql://root:codio@localhost/spotipy1')
song_dataframe.to_sql('song_details', con=engine, if_exists='replace', index=True) #the table song_details has not been made yet