import pandas as pd

# --------------------------------------------------
# STEP 3.5 - CLEAN SUPPORT TICKETS DATASET
# --------------------------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

raw_path = PROJECT_ROOT / "1.data" / "1.raw" / "ravenstack_support_tickets.csv"
raw_path = "1.data/1.raw/ravenstack_support_tickets.csv"
cleaned_path = "1.data/2.cleaned/ravenstack_support_tickets_cleaned.csv"

# Load raw data
support_tickets = pd.read_csv(raw_path)

print("RAW SUPPORT TICKETS DATA")
print("-" * 50)
print("Shape:", support_tickets.shape)

print("\nMissing values:")
print(support_tickets.isna().sum())

# --------------------------------------------------
# Convert date/time columns to datetime
# --------------------------------------------------

support_tickets["submitted_at"] = pd.to_datetime(
    support_tickets["submitted_at"],
    errors="coerce"
)

support_tickets["closed_at"] = pd.to_datetime(
    support_tickets["closed_at"],
    errors="coerce"
)

# --------------------------------------------------
# Validate date conversion
# --------------------------------------------------

print("\nAFTER DATETIME CONVERSION")
print("-" * 50)

print("submitted_at data type:")
print(support_tickets["submitted_at"].dtype)

print("closed_at data type:")
print(support_tickets["closed_at"].dtype)

print("\nMissing submitted_at:")
print(support_tickets["submitted_at"].isna().sum())

print("Missing closed_at:")
print(support_tickets["closed_at"].isna().sum())

# --------------------------------------------------
# Validate ticket timing
# --------------------------------------------------

invalid_ticket_times = (
    support_tickets["closed_at"] < support_tickets["submitted_at"]
).sum()

print("\nTICKET TIME VALIDATION")
print("-" * 50)

print("Closed before submitted:")
print(invalid_ticket_times)

# --------------------------------------------------
# Validate numeric columns
# --------------------------------------------------

print("\nNUMERIC RANGE VALIDATION")
print("-" * 50)

print("Minimum resolution_time_hours:")
print(support_tickets["resolution_time_hours"].min())

print("Maximum resolution_time_hours:")
print(support_tickets["resolution_time_hours"].max())

print("Minimum first_response_time_minutes:")
print(support_tickets["first_response_time_minutes"].min())

print("Maximum first_response_time_minutes:")
print(support_tickets["first_response_time_minutes"].max())

print("Minimum satisfaction_score:")
print(support_tickets["satisfaction_score"].min())

print("Maximum satisfaction_score:")
print(support_tickets["satisfaction_score"].max())

# --------------------------------------------------
# Check satisfaction score missing values
# --------------------------------------------------

print("\nSATISFACTION SCORE VALIDATION")
print("-" * 50)

print("Missing satisfaction scores:")
print(support_tickets["satisfaction_score"].isna().sum())

# --------------------------------------------------
# Save cleaned data
# --------------------------------------------------

support_tickets.to_csv(cleaned_path, index=False)

print("\nCLEANED SUPPORT TICKETS DATA SAVED")
print("-" * 50)
print("Output:", cleaned_path)
print("Final shape:", support_tickets.shape)