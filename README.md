# AniList to iCal

A simple Python script to fetch the currently watching and planning to watch shows from a user's AniList account and convert the airing schedule of the next episodes into an iCal file. The current workflow generates an ICA file for my own personal use, but you can see how it works and fork it for your own usage.

## Features
- Fetches user's AniList watching and planning to watch shows.
- Converts next episode airing dates to iCal format.
- Writes the iCal data to a file.

## Prerequisites
- Python 3.x
- AniList Account
- AniList API Access Token

## Installation
Clone the repository:
```sh
git clone https://github.com/Dccmaster94/anilist-ical-gen.git
cd anilist-ical-gen
```

Install required packages:

```sh
pip install requests ics
```

## Usage
1. Replace `YOUR_ANILIST_USERNAME` with the AniList username you want to look up.
2. Replace `YOUR_ACCESS_TOKEN` with your AniList API Access Token. For the public API this is not required.
3. Run the script:
```sh
python anilist-ical.py
```
4. The iCal file will be written to `anime_schedule.ics`.

## Notes
- Make sure the user's list is public, or the script won't be able to fetch the shows.
- Handle API responses and errors adequately in a production environment.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
