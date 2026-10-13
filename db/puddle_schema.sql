CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL UNIQUE,
    own_rating_value INTEGER NOT NULL,
    opponent_name TEXT NOT NULL,
    opponent_character TEXT NOT NULL,
    opponent_character_short TEXT NOT NULL,
    opponent_rating_value INTEGER NOT NULL,
    result_win INTEGER NOT NULL CHECK (result_win IN (0, 1)) /* sqlite no boolean type, so we enforce 0/1 for false/true */
);