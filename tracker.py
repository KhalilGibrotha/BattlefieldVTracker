import requests

BASE_URL = "https://battlefieldtracker.com/bfv/profile/origin/
BASE_API_URL = "https://api.tracker.gg/api/v1/bfv/"
PROFILE_URL = BASE_API_URL + "profile/origin/"
LAST_GAMES = BASE_API_URL + "gamereports/origin/latest/"
GAME_REPORT = BASE_API_URL + "gamereports/origin/direct/"

resp_profile = requests.get(PROFILE_URL)
if resp_profile.status_code !=200:
    #Something bad happened
    raise ApiError('GET /tasks/ {}'.format(respon_profile.status_code))
for todo_item in resp_profile.json():
    print('{} {}'.format(todo_item{'id'}, todo_item['summary']))
