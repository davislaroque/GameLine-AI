"""
processing.py
-------------
Functions for cleaning and transforming sportsbook odds data.
"""

import pandas as pd

def american_to_prob(odds):
    """
    Convert American odds to implied probability.
    """
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def clean_odds(raw_data):
    """
    Turn The Odds API JSON response into a tidy DataFrame.
    """
    records = []
    for game in raw_data:
        home_team = game["home_team"]
        away_team = game["away_team"]
        for book in game["bookmakers"]:
            bookmaker = book["title"]
            for market in book["markets"]:
                market_key = market["key"]
                for outcome in market["outcomes"]:
                    records.append({
                        "home_team": home_team,
                        "away_team": away_team,
                        "bookmaker": bookmaker,
                        "market": market_key,
                        "player": outcome.get("name"),
                        "price": outcome.get("price"),
                        "prob": american_to_prob(outcome.get("price"))
                    })
    return pd.DataFrame(records)
