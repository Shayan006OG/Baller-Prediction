import json
import os
import pandas as pd
from tqdm import tqdm

RAW_DATA_PATH = "../data/raw"

all_deliveries = []

# Recursively find all JSON files inside subfolders
files = []

for root, dirs, filenames in os.walk(RAW_DATA_PATH):
    for filename in filenames:
        if filename.endswith(".json"):
            files.append(os.path.join(root, filename))

print(f"Total JSON files found: {len(files)}")

# Process all match files
for file_path in tqdm(files):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            match = json.load(f)

        info = match.get("info", {})

        venue = info.get("venue", "Unknown")

        match_date = info.get("dates", ["Unknown"])[0]

        innings = match.get("innings", [])

        for inning in innings:

            team = inning.get("team", "")

            overs = inning.get("overs", [])

            for over_data in overs:

                over_number = over_data.get("over")

                deliveries = over_data.get("deliveries", [])

                for ball in deliveries:

                    batter = ball.get("batter")
                    bowler = ball.get("bowler")
                    non_striker = ball.get("non_striker")

                    runs = ball.get("runs", {})
                    batter_runs = runs.get("batter", 0)
                    extras = runs.get("extras", 0)
                    total_runs = runs.get("total", 0)

                    wicket = 0
                    wicket_type = None

                    if "wickets" in ball:
                        wicket = 1
                        wicket_type = ball["wickets"][0].get("kind")

                    all_deliveries.append({
                        "venue": venue,
                        "match_date": match_date,
                        "batting_team": team,
                        "over": over_number,
                        "batter": batter,
                        "bowler": bowler,
                        "non_striker": non_striker,
                        "batter_runs": batter_runs,
                        "extras": extras,
                        "total_runs": total_runs,
                        "wicket": wicket,
                        "wicket_type": wicket_type
                    })

    except Exception as e:
        print(f"Error processing file: {file_path}")
        print(e)

# Create dataframe
df = pd.DataFrame(all_deliveries)

print(df.head())

# Create processed folder if not exists
os.makedirs("../data/processed", exist_ok=True)

# Save dataset
df.to_csv("../data/processed/all_deliveries.csv", index=False)

print("Dataset saved successfully!")
print(f"Total deliveries processed: {len(df)}")