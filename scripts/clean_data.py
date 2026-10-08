""" Clean data, remove some unnecessary columns and save it (as csv?) """
#pylint: disable=line-too-long
import json
import pandas as pd

with open ("data/raw/match_history.json", "r", encoding="utf-8") as file:
    match_history = json.load(file)

df = pd.DataFrame(match_history)
# df.to_csv("data/processed/match_history.csv", index=False, encoding="utf-8")

# columns to drop: floor (deprecated?), opponent platform (useless?), opponent id (useless for sure), opponent is legend (not relevant to me, only top 100 players)
# df = df.drop(columns=["floor", "opponent_platform", "opponent_id", "opponent_is_legend"])
# df.to_csv("data/processed/match_history_cleaned.csv", index=False, encoding="utf-8")
