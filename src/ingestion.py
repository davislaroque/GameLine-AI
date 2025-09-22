# src/ingestion.py
import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ODDS_API_KEY")

BASE_URL = "https://api.the-odds-api.com/v4/sports"

def fetch_player_props(sport="basketball_nba", markets="player_points", regions="us", odds_format="decimal"):
    """
    Fetch NBA player prop odds from The Odds API.
    sport: "basketball_nba"
    markets: e.g., "player_points", "player_rebounds", "player_assists"
    regions: "us", "us2", "eu", etc.
    odds_format: "decimal" or "american"
    """
    url = f"{BASE_URL}/{sport}/odds"
    params = {
        "apiKey": API_KEY,
        "markets": markets,
        "regions": regions,
        "oddsFormat": odds_format
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

def props_to_dataframe(props_json, markets="player_points"):
    """
    Convert Odds API JSON to a flat pandas DataFrame with canonical fields.
    """
    records = []
    timestamp = datetime.utcnow().isoformat()
    
    for game in props_json:
        game_id = game["id"]
        home_team = game["home_team"]
        away_team = game["away_team"]
        commence_time = game["commence_time"]

        for bookmaker in game["bookmakers"]:
            book = bookmaker["title"]
            last_update = bookmaker["last_update"]

            for market in bookmaker["markets"]:
                if market["key"] != markets:
                    continue
                for outcome in market["outcomes"]:
                    records.append({
                        "timestamp": timestamp,
                        "game_id": game_id,
                        "commence_time": commence_time,
                        "home_team": home_team,
                        "away_team": away_team,
                        "bookmaker": book,
                        "last_update": last_update,
                        "player_name": outcome.get("description"),
                        "market": market["key"],
                        "line": outcome.get("point"),
                        "price": outcome.get("price")
                    })
    return pd.DataFrame(records)

def save_snapshot(df, markets="player_points"):
    """
    Save DataFrame snapshot into data/ folder with timestamp in filename.
    """
    os.makedirs("data", exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = f"data/odds_{markets}_{ts}.csv"
    df.to_csv(path, index=False)
    print(f"Saved snapshot → {path}")
    return path

def update_canonical_table(df, canonical_path="data/odds_canonical.csv"):
    """
    Append new odds snapshot into a canonical line-change table.
    """
    if os.path.exists(canonical_path):
        existing = pd.read_csv(canonical_path)
        combined = pd.concat([existing, df], ignore_index=True)
    else:
        combined = df
    combined.to_csv(canonical_path, index=False)
    print(f"Canonical table updated → {canonical_path}")

if __name__ == "__main__":
    props_json = fetch_player_props(markets="player_points")
    df = props_to_dataframe(props_json, markets="player_points")
    save_snapshot(df, markets="player_points")
    update_canonical_table(df)
