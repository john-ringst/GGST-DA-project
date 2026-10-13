""" Load data into the sqlite database """
import sqlite3
import pandas as pd

COLUMNS = [
    "match_id",
    "timestamp",
    "own_rating_value",
    "opponent_name",
    "opponent_character",
    "opponent_character_short",
    "opponent_rating_value",
    "result_win",
]

df = pd.read_csv("data/processed/match_history_cleaned.csv", encoding="utf-8")
connection = sqlite3.connect("db/puddle_analysis.db")

with open("db/puddle_schema.sql", "r", encoding="utf-8") as file:
    schema = file.read()

try:
    with connection:
        connection.executescript(schema)
        cursor = connection.executemany(
            f"""INSERT INTO matches ({", ".join(COLUMNS)})
            VALUES ({", ".join("?" * len(COLUMNS))})
            ON CONFLICT(match_id) DO NOTHING""",
            df[COLUMNS].itertuples(index=False, name=None)
        )
        inserted = cursor.rowcount
finally:
    connection.close()

print(f"Inserted {inserted} rows into the database.")
