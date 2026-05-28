import pandas as pd
import os

# Load master delivery dataset
df = pd.read_csv("../data/processed/all_deliveries.csv")

print("Dataset Loaded Successfully!")
print(f"Total deliveries: {len(df)}")

# Create matchup statistics
matchups = df.groupby(
    ["batter", "bowler"]
).agg(
    balls_faced=("batter", "count"),
    runs_scored=("batter_runs", "sum"),
    dismissals=("wicket", "sum")
).reset_index()

# Strike Rate
matchups["strike_rate"] = (
    matchups["runs_scored"] / matchups["balls_faced"]
) * 100

# Batting Average
matchups["batting_average"] = (
    matchups["runs_scored"] /
    matchups["dismissals"].replace(0, 1)
)

# Economy Against Bowler
matchups["runs_per_ball"] = (
    matchups["runs_scored"] /
    matchups["balls_faced"]
)

# Vulnerability Score
matchups["vulnerability_score"] = (
    matchups["dismissals"] /
    matchups["balls_faced"]
)

# Save dataset
os.makedirs("../data/processed", exist_ok=True)

matchups.to_csv(
    "../data/processed/batter_vs_bowler.csv",
    index=False
)

print("Matchup dataset created successfully!")
print(matchups.head())