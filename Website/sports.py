# Import required libraries
from flask import render_template
import requests

# Define the sports function
def sports():
    # Request data from the sports API
    api_url = 'https://api.sportsdata.io/v3/nfl/scores/json/ScoresByWeek/2021/1?key=<your-api-key>'
    response = requests.get(api_url)
    
    # Parse data from response
    games = response.json()
    scores = []
    for game in games:
        home_team = game['HomeTeam']
        home_score = game['HomeScore']
        away_team = game['AwayTeam']
        away_score = game['AwayScore']
        scores.append({'home_team': home_team, 'home_score': home_score, 'away_team': away_team, 'away_score': away_score})
    
    # Render the sports page using Jinja template
    return render_template('sports.html', scores=scores)

