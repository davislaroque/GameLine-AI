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


def flatten_odds_to_df(data, market="h2h"):
    """
    Flatten The Odds API JSON into a clean DataFrame.
    
    Args:
        data (list): JSON response from The Odds API
        market (str): market key (e.g., "h2h", "totals", "spreads", "player_points")
        
    Returns:
        pd.DataFrame: tidy dataframe of odds
    """
    records = []
    
    for game in data:
        game_id = game.get("id")
        sport = game.get("sport_title")
        commence_time = game.get("commence_time")
        home_team = game.get("home_team")
        away_team = game.get("away_team")
        
        for book in game.get("bookmakers", []):
            bookie = book.get("title")
            last_update = book.get("last_update")
            
            for m in book.get("markets", []):
                if m.get("key") != market:
                    continue
                for outcome in m.get("outcomes", []):
                    records.append({
                        "game_id": game_id,
                        "sport": sport,
                        "commence_time": commence_time,
                        "home_team": home_team,
                        "away_team": away_team,
                        "bookmaker": bookie,
                        "last_update": last_update,
                        "market": m.get("key"),
                        "outcome_name": outcome.get("name"),
                        "price": outcome.get("price")
                    })
                    
    return pd.DataFrame(records)



