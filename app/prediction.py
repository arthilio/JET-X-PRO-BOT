import random

def predict_match(home_team: str, away_team: str):
    # Simulation avec "logique experte"
    score_home = random.choices([0,1,2,3], weights=[10, 25, 40, 25])[0]
    score_away = random.choices([0,1,2,3], weights=[15, 30, 35, 20])[0]
    confidence = round(random.uniform(85, 99), 2)  # Marge d'erreur simulée < 10%
    return {
        "home_team": home_team,
        "away_team": away_team,
        "score": f"{score_home} - {score_away}",
        "confidence": f"{confidence} %"
    }
