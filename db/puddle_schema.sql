CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    own_rating_value INTEGER NOT NULL,
    opponent_name TEXT NOT NULL,
    opponent_character TEXT NOT NULL,
    opponent_character_short TEXT NOT NULL,
    opponent_rating_value INTEGER NOT NULL,
    result_win BOOLEAN NOT NULL,
)