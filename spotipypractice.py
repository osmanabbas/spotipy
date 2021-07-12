import requests
import spotipy

CLIENT_ID = '964c90ea741a46d298455b803c7d7608'
CLIENT_SECRET = '660c5a0815414b448b93549be135e829'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
  'grant_type': 'client_credentials',
  'client_id': CLIENT_ID,
  'client_secret': CLIENT_SECRET,
})

print(auth_response.status_code)
#auth_response_data = auth_response.json()

auth_response_data = auth_response.json()
auth_response_data

access_token = auth_response_data['access_token']
headers = {
  'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '5TCBWmEBrin7etRa4Lswr1'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers = headers)
r = r.json()
r
