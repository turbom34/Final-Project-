# Import required libraries
import requests

def get_game_scores():
    url = "https://www.balldontlie.io/api/v1/games"
    response = requests.get(url)
    data = response.json()
    scores = []
    for game in data['data']:
        scores.append({
            'home_team': game['home_team']['full_name'],
            'home_score': game['home_team_score'],
            'away_team': game['visitor_team']['full_name'],
            'away_score': game['visitor_team_score']
        })
    return scores
    
   

