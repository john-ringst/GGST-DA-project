""" Script to test the API and extract data from it """
import json
import time
import requests

BASE_API_URL = (
    "https://puddle.farm/ggst/api/player/210613092355980527/SL/history"
)

all_matches = []
OFFSET = 0
COUNT = 100

while True:
    params = {
        "count": COUNT,
        "offset": OFFSET,
    }

    response = requests.get(BASE_API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    history = data["history"]

    if len(history) == 0:
        break

    all_matches.extend(history)
    OFFSET += COUNT
    time.sleep(1)

print(f"Total matches extracted: {len(all_matches)}")

with open("data/raw/match_history.json",
          "w",
          encoding="utf-8"
          ) as file:
    json.dump(
        all_matches,
        file,
        ensure_ascii=False,
        indent=4
    )
