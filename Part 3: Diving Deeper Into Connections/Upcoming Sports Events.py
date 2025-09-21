from datetime import datetime

import requests


def upcoming_sports(url, headers):
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    if response.status_code == 200 and 'response' in data:
        games = data['response']

        # Iterate through each game and extract details
        for game in games:
            game_id = game['id']
            home_team = game['teams']['home']['name']
            visitor_team = game['teams']['visitors']['name']
            game_time = game['date']['start']
            status = game['status']['long']
            arena_name = game['arena']['name']
            arena_city = game['arena']['city']
            arena_state = game['arena']['state']

            # Format game time (converting from UTC to local time if desired)
            game_datetime = datetime.strptime(game_time, "%Y-%m-%dT%H:%M:%S.000Z")
            formatted_time = game_datetime.strftime("%A, %B %d, %Y at %I:%M %p")

            # Print Game Information
            print(f"Game ID: {game_id}")
            print(f"{home_team} vs. {visitor_team}")
            print(f"Date and Time: {formatted_time}")
            print(f"Arena: {arena_name}, {arena_city}, {arena_state}")
            print(f"Game Status: {status}")
            print("-" * 40)

    else:
        print(f"Error: {response.status_code} - Could not fetch the games.")


# Code for NBA
sport = "nba"
date = input("And for what day? Answer in this format: yyyy-mm-dd. ")

url = f"https://v2.{sport}.api-sports.io/games?date={date}"
headers = {
    'x-rapidapi-key': 'd734db294c41267fd4d4575315f6c353',
    'x-rapidapi-host': 'v2.nba.api-sports.io'
}

upcoming_sports(url, headers)
