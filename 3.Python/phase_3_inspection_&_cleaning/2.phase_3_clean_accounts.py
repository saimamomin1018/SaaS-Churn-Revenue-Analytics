import pandas as pd

# --------------------------------------------------
# STEP 3.2 - CLEAN ACCOUNTS DATASET
# --------------------------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_path = PROJECT_ROOT / "1.data" / "1.raw" / "ravenstack_accounts.csv"
# File paths
#raw_path = "1.data/1.raw/ravenstack_accounts.csv"
cleaned_path = "1.data/2.cleaned/ravenstack_accounts_cleaned.csv"

# Load raw Accounts data
accounts = pd.read_csv(raw_path)

print("RAW ACCOUNTS DATA")
print("-" * 50)
print("Shape:", accounts.shape)
print("Missing values:")
print(accounts.isna().sum())

# --------------------------------------------------
# Convert signup_date to datetime
# --------------------------------------------------

accounts["signup_date"] = pd.to_datetime(
    accounts["signup_date"],
    errors="coerce"
)

# --------------------------------------------------
# Basic validation after conversion
# --------------------------------------------------

print("\nAFTER DATE CONVERSION")
print("-" * 50)

print("signup_date data type:")
print(accounts["signup_date"].dtype)

print("\nMissing signup dates:")
print(accounts["signup_date"].isna().sum())

# --------------------------------------------------
# Save cleaned Accounts dataset
# --------------------------------------------------

accounts.to_csv(cleaned_path, index=False)

print("\nCLEANED ACCOUNTS DATA SAVED")
print("-" * 50)
print("Output:", cleaned_path)
print("Final shape:", accounts.shape)