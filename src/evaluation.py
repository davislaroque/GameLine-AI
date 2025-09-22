"""
evaluation.py
-------------
Functions for evaluating model predictions against market lines.
"""

import numpy as np
import pandas as pd

def backtest(predictions, market_lines, threshold=0.55):
    """
    Simulate bets based on model vs market.
    Returns ROI and bet log.
    """
    bets = []
    bankroll = 1000
    stake = 10

    for pred, line in zip(predictions, market_lines):
        implied_prob = line
        if pred > implied_prob and pred > threshold:
            bankroll += stake
            bets.append("win")
        elif pred < implied_prob and (1 - pred) > threshold:
            bankroll -= stake
            bets.append("loss")
        else:
            bets.append("pass")

    roi = (bankroll - 1000) / 1000
    return {"final_bankroll": bankroll, "ROI": roi, "bets": bets}

def evaluate_accuracy(predictions, outcomes):
    """
    Compare predicted probabilities vs. actual outcomes.
    """
    correct = np.sum((predictions >= 0.5) == outcomes)
    accuracy = correct / len(outcomes)
    return accuracy
