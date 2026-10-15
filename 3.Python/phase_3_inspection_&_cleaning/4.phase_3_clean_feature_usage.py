import pandas as pd

# --------------------------------------------------
# STEP 3.4 - CLEAN FEATURE USAGE DATASET
# --------------------------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_path = PROJECT_ROOT / "1.data" / "1.raw" / "ravenstack_feature_usage.csv"
#raw_path = "1.data/1.raw/ravenstack_feature_usage.csv"
cleaned_path = "1.data/2.cleaned/ravenstack_feature_usage_cleaned.csv"

# Load raw data
feature_usage = pd.read_csv(raw_path)

print("RAW FEATURE USAGE DATA")
print("-" * 50)
print("Shape:", feature_usage.shape)

print("\nMissing values:")
print(feature_usage.isna().sum())

# --------------------------------------------------
# Convert usage_date to datetime
# --------------------------------------------------

feature_usage["usage_date"] = pd.to_datetime(
    feature_usage["usage_date"],
    errors="coerce"
)

# --------------------------------------------------
# Validate date conversion
# --------------------------------------------------

print("\nAFTER DATE CONVERSION")
print("-" * 50)

print("usage_date data type:")
print(feature_usage["usage_date"].dtype)

print("\nMissing usage dates:")
print(feature_usage["usage_date"].isna().sum())

# --------------------------------------------------
# Check repeated usage IDs
# --------------------------------------------------

duplicate_usage_ids = (
    feature_usage["usage_id"]
    .duplicated(keep=False)
    .sum()
)

unique_repeated_usage_ids = (
    feature_usage.loc[
        feature_usage["usage_id"].duplicated(keep=False),
        "usage_id"
    ].nunique()
)

print("\nUSAGE ID VALIDATION")
print("-" * 50)

print("Rows belonging to repeated usage IDs:")
print(duplicate_usage_ids)

print("Number of repeated usage_id values:")
print(unique_repeated_usage_ids)

# --------------------------------------------------
# Check numeric ranges
# --------------------------------------------------

print("\nNUMERIC RANGE VALIDATION")
print("-" * 50)

print("Minimum usage_count:")
print(feature_usage["usage_count"].min())

print("Minimum usage_duration_secs:")
print(feature_usage["usage_duration_secs"].min())

print("Minimum error_count:")
print(feature_usage["error_count"].min())

# --------------------------------------------------
# Save cleaned data
# --------------------------------------------------

feature_usage.to_csv(cleaned_path, index=False)

print("\nCLEANED FEATURE USAGE DATA SAVED")
print("-" * 50)
print("Output:", cleaned_path)
print("Final shape:", feature_usage.shape)