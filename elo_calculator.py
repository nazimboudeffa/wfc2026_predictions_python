import pandas as pd
from typing import Dict, List, Tuple

ELO_INITIAL = 1500
K_FACTOR = 32 # K-factor: sensitivity of the rating change

def calculate_elo(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Dict]:
    """
    Calculates the updated ELO ratings for all teams based on historical match data in the DataFrame.
    The calculation is sequential and cumulative to properly model ranking changes.
    Returns the modified DataFrame and a dictionary of final team ratings.
    """
    # 1. Collect unique teams and initialize ratings
    unique_teams = set(df['Home'].dropna().tolist() + df['Away'].dropna().tolist())
    elo_ratings: Dict[str, float] = {team: ELO_INITIAL for team in unique_teams}

    processed_df = df.copy()

    # 2. Process matches sequentially to update ratings
    for index, row in processed_df.iterrows():
        home_team = row['Home']
        away_team = row['Away']
        score_home = row['HomeGoals']
        score_away = row['AwayGoals']

        if not home_team or not away_team:
            continue

        # Get current ratings (use initial if somehow missing)
        rating_A = elo_ratings.get(home_team, ELO_INITIAL)
        rating_B = elo_ratings.get(away_team, ELO_INITIAL)

        # --- Core Logic: Estimate Expected Goals ($\mu$) based on rating difference ---
        # The expectation (lambda) is modeled as a base rate + adjustment proportional to the rating difference.
        EXPECTATION_SCALE = 900.0 
        expected_home_score = max(0.5, 1 + (rating_A - rating_B) / EXPECTATION_SCALE)
        expected_away_score = max(0.5, 1 + (rating_B - rating_A) / EXPECTATION_SCALE)

        # --- Update Ratings: Delta est la différence entre l'ATTENTION et l'EXPECTATION ---
        
        # Le delta pour le taux de buts est réduit par un coefficient (e.g., / 5) pour des changements plus stables
        delta_home = score_home - expected_home_score
        delta_away = score_away - expected_away_score
            
        # Update ratings: Rating change is proportional to the performance differential
        elo_ratings[home_team] += K_FACTOR * delta_home / 5.0
        elo_ratings[away_team] -= K_FACTOR * delta_home / (K_FACTOR * 2) # Compensation for home advantage/loss

    return processed_df, elo_ratings