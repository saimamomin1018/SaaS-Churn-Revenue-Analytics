import pandas as pd

# --------------------------------------------------
# STEP 3.6 - CLEAN CHURN EVENTS DATASET
# --------------------------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_path = PROJECT_ROOT / "1.data" / "1.raw" / "ravenstack_churn_events.csv"
#raw_path = "1.data/1.raw/ravenstack_churn_events.csv"
cleaned_path = "1.data/2.cleaned/ravenstack_churn_events_cleaned.csv"

# Load raw data
churn_events = pd.read_csv(raw_path)

print("RAW CHURN EVENTS DATA")
print("-" * 50)
print("Shape:", churn_events.shape)

print("\nMissing values:")
print(churn_events.isna().sum())

# --------------------------------------------------
# Convert churn_date to datetime
# --------------------------------------------------

churn_events["churn_date"] = pd.to_datetime(
    churn_events["churn_date"],
    errors="coerce"
)

# --------------------------------------------------
# Validate date conversion
# --------------------------------------------------

print("\nAFTER DATE CONVERSION")
print("-" * 50)

print("churn_date data type:")
print(churn_events["churn_date"].dtype)

print("\nMissing churn dates:")
print(churn_events["churn_date"].isna().sum())

# --------------------------------------------------
# Validate refund amount
# --------------------------------------------------

print("\nREFUND AMOUNT VALIDATION")
print("-" * 50)

print("Minimum refund_amount_usd:")
print(churn_events["refund_amount_usd"].min())

print("Maximum refund_amount_usd:")
print(churn_events["refund_amount_usd"].max())

print("Negative refund amounts:")
print(
    (churn_events["refund_amount_usd"] < 0).sum()
)

# --------------------------------------------------
# Validate churn event IDs
# --------------------------------------------------

print("\nCHURN EVENT ID VALIDATION")
print("-" * 50)

print("Total churn event IDs:")
print(churn_events["churn_event_id"].count())

print("Unique churn event IDs:")
print(churn_events["churn_event_id"].nunique())

# --------------------------------------------------
# Validate account IDs
# --------------------------------------------------

print("\nACCOUNT ID VALIDATION")
print("-" * 50)

print("Unique accounts with churn events:")
print(churn_events["account_id"].nunique())

print("Maximum churn events for one account:")
print(churn_events["account_id"].value_counts().max())

# --------------------------------------------------
# Save cleaned data
# --------------------------------------------------

churn_events.to_csv(cleaned_path, index=False)

print("\nCLEANED CHURN EVENTS DATA SAVED")
print("-" * 50)
print("Output:", cleaned_path)
print("Final shape:", churn_events.shape)