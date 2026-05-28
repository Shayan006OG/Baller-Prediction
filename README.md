# Bowler Recommendation System 🏏

AI-powered T20 cricket bowler recommendation system using:

* Matchup analysis
* Pitch conditions
* Machine Learning
* Player vulnerability analysis

---

# Project Overview

This project predicts the optimal bowler against a batsman in T20 cricket by analyzing:

* Historical bowler vs batsman matchups
* Pitch conditions
* Match phase
* Bowler type
* Player vulnerability patterns

The system aims to recommend bowlers that maximize dismissal probability.

---

# Features

✅ Ball-by-ball T20 data analysis
✅ Batter vs bowler matchup engine
✅ Vulnerability scoring
✅ Pitch-aware recommendations
✅ Machine Learning based prediction
✅ Tactical bowler ranking system

---

# Tech Stack

* Python
* Pandas
* Scikit-learn
* XGBoost
* Flask / FastAPI
* Cricsheet Dataset

---

# Project Structure

```txt
bowler-recommendation-system/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── scripts/
├── backend/
├── models/
├── notebooks/
├── outputs/
│
├── requirements.txt
└── README.md
```

---

# Dataset Setup

Download datasets from:

https://cricsheet.org/downloads/

Required datasets:

* IPL JSON
* T20I JSON

Extract them inside:

```txt
data/raw/
```

Expected structure:

```txt
data/raw/
    ipl_male_json/
    icc_mens_t20_world_cup_male_json/
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Generate Master Dataset

Run:

```bash
cd scripts
python parse_cricsheet.py
```

This generates:

```txt
data/processed/all_deliveries.csv
```

---

# Current Progress

✅ Data Pipeline Built
✅ Cricsheet Parser Completed
✅ Master Dataset Generated
⬜ Matchup Engine
⬜ Feature Engineering
⬜ ML Model Training
⬜ Recommendation API
⬜ Frontend Dashboard

---

# Future Goals

* Pitch classification
* Bowler type detection
* Dismissal probability prediction
* Explainable AI recommendations
* Real-time tactical engine

---

# Author

Shayan Ghosh

GitHub:
https://github.com/Shayan006OG
