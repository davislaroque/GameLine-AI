# src/analysis.py

"""
Analysis utilities for sportsbook odds data.
Includes functions to parse markets, find best odds, and detect arbitrage.
"""

from typing import Dict, Any

def parse_market(game: Dict[str, Any], market_key: str) -> Dict[str, Dict[str, Any]]:
    """
    Parse a specific market from a single game.
    Returns nested dict: outcome -> {bookmaker, price}.
    """
    parsed = {}
    for bookmaker in game.get("bookmakers", []):
        for market in bookmaker.get("markets", []):
            if market["key"] == market_key:
                for outcome in market.get("outcomes", []):
                    name = outcome["name"]
                    price = outcome["price"]
                    if name not in parsed or price > parsed[name]["price"]:
                        parsed[name] = {"bookmaker": bookmaker["title"], "price": price}
    return parsed


def find_best_odds(parsed_market: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Return the highest odds per outcome (already handled in parse_market).
    Simply returns parsed_market for clarity.
    """
    return parsed_market


def implied_prob(decimal_odds: float) -> float:
    """Convert decimal odds to implied probability."""
    return 1 / decimal_odds


def detect_arbitrage(best_odds: Dict[str, Dict[str, Any]]):
    """
    Check for arbitrage opportunities in a two-outcome market.
    Returns profit margin (%) if arbitrage exists, else None.
    """
    if len(best_odds) != 2:
        return None  # Only works for two-outcome markets (H2H, spreads, totals)

    probs = [implied_prob(data["price"]) for data in best_odds.values()]
    total_prob = sum(probs)

    if total_prob < 1:
        return round((1 - total_prob) * 100, 2)
    return None
