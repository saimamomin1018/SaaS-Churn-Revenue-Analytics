import pandas as pd
import os

# --------------------------------------------------
# STEP 3.7 - FINAL CLEANED DATASET VALIDATION
# --------------------------------------------------

base_path = "1.data/2.cleaned"

files = {
    "Accounts": "ravenstack_accounts_cleaned.csv",
    "Subscriptions": "ravenstack_subscriptions_cleaned.csv",
    "Feature Usage": "ravenstack_feature_usage_cleaned.csv",
    "Support Tickets": "ravenstack_support_tickets_cleaned.csv",
    "Churn Events": "ravenstack_churn_events_cleaned.csv"
}

expected_shapes = {
    "Accounts": (500, 10),
    "Subscriptions": (5000, 14),
    "Feature Usage": (25000, 8),
    "Support Tickets": (2000, 9),
    "Churn Events": (600, 9)
}

# --------------------------------------------------
# 1. FILE EXISTENCE AND SHAPE CHECK
# --------------------------------------------------

print("FINAL CLEANED DATASET VALIDATION")
print("=" * 60)

all_shapes_correct = True

for dataset_name, filename in files.items():

    filepath = os.path.join(base_path, filename)

    print(f"\n{dataset_name}")
    print("-" * 60)

    if os.path.exists(filepath):
        print("File exists: YES")

        df = pd.read_csv(filepath)

        print("Shape:", df.shape)
        print("Expected shape:", expected_shapes[dataset_name])

        if df.shape == expected_shapes[dataset_name]:
            print("Shape validation: PASS")
        else:
            print("Shape validation: FAIL")
            all_shapes_correct = False

    else:
        print("File exists: NO")
        all_shapes_correct = False


# --------------------------------------------------
# 2. MISSING VALUE CHECK
# --------------------------------------------------

print("\n\nMISSING VALUE VALIDATION")
print("=" * 60)

for dataset_name, filename in files.items():

    filepath = os.path.join(base_path, filename)
    df = pd.read_csv(filepath)

    print(f"\n{dataset_name}")
    print("-" * 60)

    missing = df.isna().sum()

    print(missing[missing > 0])

    if missing.sum() == 0:
        print("Missing values: NONE")
    else:
        print("Missing values preserved where expected.")


# --------------------------------------------------
# 3. DATE COLUMN VALIDATION
# --------------------------------------------------

print("\n\nDATE COLUMN VALIDATION")
print("=" * 60)

accounts = pd.read_csv(
    os.path.join(base_path, files["Accounts"]),
    parse_dates=["signup_date"]
)

subscriptions = pd.read_csv(
    os.path.join(base_path, files["Subscriptions"]),
    parse_dates=["start_date", "end_date"]
)

feature_usage = pd.read_csv(
    os.path.join(base_path, files["Feature Usage"]),
    parse_dates=["usage_date"]
)

support_tickets = pd.read_csv(
    os.path.join(base_path, files["Support Tickets"]),
    parse_dates=["submitted_at", "closed_at"]
)

churn_events = pd.read_csv(
    os.path.join(base_path, files["Churn Events"]),
    parse_dates=["churn_date"]
)

print("Accounts signup_date missing:",
      accounts["signup_date"].isna().sum())

print("Subscriptions start_date missing:",
      subscriptions["start_date"].isna().sum())

print("Subscriptions end_date missing:",
      subscriptions["end_date"].isna().sum())

print("Feature Usage usage_date missing:",
      feature_usage["usage_date"].isna().sum())

print("Support Tickets submitted_at missing:",
      support_tickets["submitted_at"].isna().sum())

print("Support Tickets closed_at missing:",
      support_tickets["closed_at"].isna().sum())

print("Churn Events churn_date missing:",
      churn_events["churn_date"].isna().sum())


# --------------------------------------------------
# 4. SUBSCRIPTION REVENUE VALIDATION
# --------------------------------------------------

print("\n\nSUBSCRIPTION REVENUE VALIDATION")
print("=" * 60)

arr_difference = (
    subscriptions["arr_amount"]
    - subscriptions["mrr_amount"] * 12
)

print("Non-zero ARR differences:",
      (arr_difference != 0).sum())

print("Maximum absolute ARR difference:",
      arr_difference.abs().max())


# --------------------------------------------------
# 5. SUBSCRIPTION DATE / CHURN VALIDATION
# --------------------------------------------------

print("\n\nSUBSCRIPTION STATUS VALIDATION")
print("=" * 60)

invalid_end_dates = (
    subscriptions["end_date"] < subscriptions["start_date"]
).sum()

churned_missing_end = (
    subscriptions["churn_flag"]
    & subscriptions["end_date"].isna()
).sum()

non_churned_with_end = (
    (~subscriptions["churn_flag"])
    & subscriptions["end_date"].notna()
).sum()

print("End date before start date:", invalid_end_dates)
print("Churned subscriptions with missing end_date:",
      churned_missing_end)
print("Non-churned subscriptions with end_date:",
      non_churned_with_end)


# --------------------------------------------------
# 6. SUPPORT TICKET DATE VALIDATION
# --------------------------------------------------

print("\n\nSUPPORT TICKET VALIDATION")
print("=" * 60)

invalid_ticket_times = (
    support_tickets["closed_at"]
    < support_tickets["submitted_at"]
).sum()

print("Closed before submitted:", invalid_ticket_times)


# --------------------------------------------------
# 7. FOREIGN KEY VALIDATION
# --------------------------------------------------

print("\n\nRELATIONSHIP VALIDATION")
print("=" * 60)

subscription_accounts = set(accounts["account_id"])
subscription_ids = set(subscriptions["subscription_id"])

orphan_subscription_accounts = (
    ~subscriptions["account_id"].isin(subscription_accounts)
).sum()

orphan_support_accounts = (
    ~support_tickets["account_id"].isin(subscription_accounts)
).sum()

orphan_churn_accounts = (
    ~churn_events["account_id"].isin(subscription_accounts)
).sum()

orphan_usage_subscriptions = (
    ~feature_usage["subscription_id"].isin(subscription_ids)
).sum()

print("Orphan subscription account IDs:",
      orphan_subscription_accounts)

print("Orphan support ticket account IDs:",
      orphan_support_accounts)

print("Orphan churn event account IDs:",
      orphan_churn_accounts)

print("Orphan feature usage subscription IDs:",
      orphan_usage_subscriptions)


# --------------------------------------------------
# 8. FINAL RESULT
# --------------------------------------------------

print("\n\nFINAL VALIDATION RESULT")
print("=" * 60)

if (
    all_shapes_correct
    and (arr_difference != 0).sum() == 0
    and invalid_end_dates == 0
    and churned_missing_end == 0
    and non_churned_with_end == 0
    and invalid_ticket_times == 0
    and orphan_subscription_accounts == 0
    and orphan_support_accounts == 0
    and orphan_churn_accounts == 0
    and orphan_usage_subscriptions == 0
):
    print("FINAL VALIDATION: PASS")
    print("All cleaned datasets are ready for the next phase.")

else:
    print("FINAL VALIDATION: REVIEW REQUIRED")
    print("Check the validation results above.")