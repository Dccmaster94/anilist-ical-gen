import requests
from ics import Calendar, Event
from datetime import datetime

user_name = 'dccmaster'  # replace with the username you want to lookup
access_token = 'YOUR_ACCESS_TOKEN'  # replace with your AniList API Access Token

# GraphQL query to get the list of anime a user is currently watching or planning to watch
query = '''
query ($userName: String) {
  MediaListCollection(userName: $userName, type: ANIME) {
    lists {
      entries {
        media {
          title {
            english
          }
          nextAiringEpisode {
            airingAt
            episode
          }
        }
        status
      }
    }
  }
}
'''

variables = {
    'userName': user_name
}

headers = {
    ##'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

response = requests.post('https://graphql.anilist.co',
                         json={'query': query, 'variables': variables},
                         headers=headers)

data = response.json()
calendar = Calendar()

# Iterate over the retrieved shows
for media_list in data['data']['MediaListCollection']['lists']:
    for entry in media_list['entries']:
        if entry['status'] in ['CURRENT', 'PLANNING']:
            media = entry['media']
            title = media['title']['english']
            next_episode = media.get('nextAiringEpisode')
            if next_episode:
                event = Event()
                event.name = f"{title} - Episode {next_episode['episode']}"
                event.begin = datetime.utcfromtimestamp(
                    next_episode['airingAt'])
                calendar.events.add(event)

# Write the calendar to file
with open('anime_schedule.ics', 'w') as my_file:
    my_file.writelines(calendar)

print("iCal file has been written to anime_schedule.ics")