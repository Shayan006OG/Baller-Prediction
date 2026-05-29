import pandas as pd
import os

# Load master delivery dataset
df = pd.read_csv("../data/processed/all_deliveries.csv")

print("Dataset Loaded Successfully!")
print(f"Total deliveries: {len(df)}")

# Convert match_date to datetime
df["match_date"] = pd.to_datetime(df["match_date"])

# Filter matches from 2017 onwards
df = df[
    df["match_date"].dt.year >= 2017
]

print(f"Filtered deliveries (2017+): {len(df)}")

# Create matchup statistics
matchups = df.groupby(
    ["batter", "bowler"]
).agg(
    balls_faced=("batter", "count"),
    runs_scored=("batter_runs", "sum"),
    dismissals=("wicket", "sum")
).reset_index()

# Remove very small sample sizes
matchups = matchups[
    matchups["balls_faced"] >= 6
]

# Strike Rate
matchups["strike_rate"] = (
    matchups["runs_scored"] / matchups["balls_faced"]
) * 100

# Batting Average
matchups["batting_average"] = (
    matchups["runs_scored"] /
    matchups["dismissals"].replace(0, 1)
)

# Runs Per Ball
matchups["runs_per_ball"] = (
    matchups["runs_scored"] /
    matchups["balls_faced"]
)

# Vulnerability Score
matchups["vulnerability_score"] = (
    matchups["dismissals"] /
    matchups["balls_faced"]
)

# Sort by highest vulnerability
matchups = matchups.sort_values(
    by="vulnerability_score",
    ascending=False
)

# Create processed folder if needed
os.makedirs("../data/processed", exist_ok=True)

# Save dataset
matchups.to_csv(
    "../data/processed/batter_vs_bowler.csv",
    index=False
)

print("Matchup dataset created successfully!")
print(matchups.head())

print(f"Total matchup records: {len(matchups)}")