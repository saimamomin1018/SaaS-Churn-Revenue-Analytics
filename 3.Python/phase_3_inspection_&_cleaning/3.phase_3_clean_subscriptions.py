import pandas as pd

# --------------------------------------------------
# STEP 3.3 - CLEAN SUBSCRIPTIONS DATASET
# --------------------------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_path = PROJECT_ROOT / "1.data" / "1.raw" / "ravenstack_subscriptions.csv"
#raw_path = "1.data/1.raw/ravenstack_subscriptions.csv"
cleaned_path = "1.data/2.cleaned/ravenstack_subscriptions_cleaned.csv"

# Load raw data
subscriptions = pd.read_csv(raw_path)

print("RAW SUBSCRIPTIONS DATA")
print("-" * 50)
print("Shape:", subscriptions.shape)

print("\nMissing values:")
print(subscriptions.isna().sum())

# --------------------------------------------------
# Convert date columns
# --------------------------------------------------

subscriptions["start_date"] = pd.to_datetime(
    subscriptions["start_date"],
    errors="coerce"
)

subscriptions["end_date"] = pd.to_datetime(
    subscriptions["end_date"],
    errors="coerce"
)

# --------------------------------------------------
# Validate date conversion
# --------------------------------------------------

print("\nAFTER DATE CONVERSION")
print("-" * 50)

print("start_date data type:")
print(subscriptions["start_date"].dtype)

print("\nend_date data type:")
print(subscriptions["end_date"].dtype)

print("\nMissing start dates:")
print(subscriptions["start_date"].isna().sum())

print("\nMissing end dates:")
print(subscriptions["end_date"].isna().sum())

# --------------------------------------------------
# Validate ARR = MRR × 12
# --------------------------------------------------

arr_difference = (
    subscriptions["arr_amount"]
    - (subscriptions["mrr_amount"] * 12)
)

print("\nARR VALIDATION")
print("-" * 50)

print("Non-zero ARR differences:")
print((arr_difference != 0).sum())

print("Maximum ARR difference:")
print(arr_difference.abs().max())

# --------------------------------------------------
# Validate end_date and churn_flag relationship
# --------------------------------------------------

print("\nEND DATE / CHURN FLAG VALIDATION")
print("-" * 50)

print("Churned subscriptions with missing end_date:")
print(
    (
        (subscriptions["churn_flag"] == True)
        & (subscriptions["end_date"].isna())
    ).sum()
)

print("Non-churned subscriptions with missing end_date:")
print(
    (
        (subscriptions["churn_flag"] == False)
        & (subscriptions["end_date"].isna())
    ).sum()
)

# --------------------------------------------------
# Save cleaned data
# --------------------------------------------------

subscriptions.to_csv(cleaned_path, index=False)

print("\nCLEANED SUBSCRIPTIONS DATA SAVED")
print("-" * 50)
print("Output:", cleaned_path)
print("Final shape:", subscriptions.shape)