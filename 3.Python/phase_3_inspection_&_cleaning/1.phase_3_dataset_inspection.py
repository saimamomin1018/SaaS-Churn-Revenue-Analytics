import pandas as pd
from pathlib import Path

# Project paths - adjusted to step back from the '3.Python/inspection' folder structure
project_path = Path(__file__).resolve().parents[2]
raw_path = project_path / "1.Data" / "1.raw"

# Load raw datasets
accounts = pd.read_csv(raw_path / "ravenstack_accounts.csv")
subscriptions = pd.read_csv(raw_path / "ravenstack_subscriptions.csv")
feature_usage = pd.read_csv(raw_path / "ravenstack_feature_usage.csv")
support_tickets = pd.read_csv(raw_path / "ravenstack_support_tickets.csv")
churn_events = pd.read_csv(raw_path / "ravenstack_churn_events.csv")

# Display basic dataset information
print("RAVENSTACK DATASET LOADING CHECK")
print("-" * 50)

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Feature Usage:", feature_usage.shape)
print("Support Tickets:", support_tickets.shape)
print("Churn Events:", churn_events.shape)

print("\nDataset loading completed successfully.")

#COLUMN NAMES
print("\nCOLUMN NAMES")
print("-" * 50)

print("\nAccounts:")
print(accounts.columns.tolist())

print("\nSubscriptions:")
print(subscriptions.columns.tolist())

print("\nFeature Usage:")
print(feature_usage.columns.tolist())

print("\nSupport Tickets:")
print(support_tickets.columns.tolist())

print("\nChurn Events:")
print(churn_events.columns.tolist())

#DATA TYPES
print("\nDATA TYPES")
print("-" * 50)

print("\nAccounts:")
print(accounts.dtypes)

print("\nSubscriptions:")
print(subscriptions.dtypes)

print("\nFeature Usage:")
print(feature_usage.dtypes)

print("\nSupport Tickets:")
print(support_tickets.dtypes)

print("\nChurn Events:")
print(churn_events.dtypes)

#MISSING VALUES
print("\nMISSING VALUES")
print("-" * 50)

print("\nAccounts:")
print(accounts.isnull().sum())

print("\nSubscriptions:")
print(subscriptions.isnull().sum())

print("\nFeature Usage:")
print(feature_usage.isnull().sum())

print("\nSupport Tickets:")
print(support_tickets.isnull().sum())

print("\nChurn Events:")
print(churn_events.isnull().sum())

#DUPLICATE ROWS
print("\nDUPLICATE ROWS")
print("-" * 50)

print("\nAccounts:")
print(accounts.duplicated().sum())

print("\nSubscriptions:")
print(subscriptions.duplicated().sum())

print("\nFeature Usage:")
print(feature_usage.duplicated().sum())

print("\nSupport Tickets:")
print(support_tickets.duplicated().sum())

print("\nChurn Events:")
print(churn_events.duplicated().sum())

#UNIQUE ID CHECK
print("\nUNIQUE ID CHECK")
print("-" * 50)

print("\nAccounts - account_id:")
print("Total:", len(accounts))
print("Unique:", accounts["account_id"].nunique())

print("\nSubscriptions - subscription_id:")
print("Total:", len(subscriptions))
print("Unique:", subscriptions["subscription_id"].nunique())

print("\nFeature Usage - usage_id:")
print("Total:", len(feature_usage))
print("Unique:", feature_usage["usage_id"].nunique())

print("\nSupport Tickets - ticket_id:")
print("Total:", len(support_tickets))
print("Unique:", support_tickets["ticket_id"].nunique())

print("\nChurn Events - churn_event_id:")
print("Total:", len(churn_events))
print("Unique:", churn_events["churn_event_id"].nunique())

#DUPLICATE USAGE IDs
print("\nDUPLICATE USAGE IDs")
print("-" * 50)

duplicate_usage_ids = feature_usage[
    feature_usage["usage_id"].duplicated(keep=False)
].sort_values("usage_id")

print(duplicate_usage_ids.to_string(index=False))

#FOREIGN KEY RELATIONSHIP CHECK
print("\nFOREIGN KEY RELATIONSHIP CHECK")
print("-" * 50)

# Accounts → Subscriptions
subscription_accounts = set(subscriptions["account_id"])
account_ids = set(accounts["account_id"])

print("\nSubscriptions → Accounts:")
print("Orphan account_ids:", len(subscription_accounts - account_ids))

# Accounts → Support Tickets
ticket_accounts = set(support_tickets["account_id"])

print("\nSupport Tickets → Accounts:")
print("Orphan account_ids:", len(ticket_accounts - account_ids))

# Accounts → Churn Events
churn_accounts = set(churn_events["account_id"])

print("\nChurn Events → Accounts:")
print("Orphan account_ids:", len(churn_accounts - account_ids))

# Subscriptions → Feature Usage
usage_subscriptions = set(feature_usage["subscription_id"])
subscription_ids = set(subscriptions["subscription_id"])

print("\nFeature Usage → Subscriptions:")
print("Orphan subscription_ids:", len(usage_subscriptions - subscription_ids))

#BOOLEAN / FLAG VALUE CHECK
print("\nBOOLEAN / FLAG VALUE CHECK")
print("-" * 50)

print("\nAccounts:")
print("is_trial:", accounts["is_trial"].value_counts(dropna=False).to_dict())
print("churn_flag:", accounts["churn_flag"].value_counts(dropna=False).to_dict())

print("\nSubscriptions:")
print("is_trial:", subscriptions["is_trial"].value_counts(dropna=False).to_dict())
print("upgrade_flag:", subscriptions["upgrade_flag"].value_counts(dropna=False).to_dict())
print("downgrade_flag:", subscriptions["downgrade_flag"].value_counts(dropna=False).to_dict())
print("churn_flag:", subscriptions["churn_flag"].value_counts(dropna=False).to_dict())
print("auto_renew_flag:", subscriptions["auto_renew_flag"].value_counts(dropna=False).to_dict())

print("\nFeature Usage:")
print("is_beta_feature:", feature_usage["is_beta_feature"].value_counts(dropna=False).to_dict())

print("\nSupport Tickets:")
print("escalation_flag:", support_tickets["escalation_flag"].value_counts(dropna=False).to_dict())

print("\nChurn Events:")
print("preceding_upgrade_flag:", churn_events["preceding_upgrade_flag"].value_counts(dropna=False).to_dict())
print("preceding_downgrade_flag:", churn_events["preceding_downgrade_flag"].value_counts(dropna=False).to_dict())
print("is_reactivation:", churn_events["is_reactivation"].value_counts(dropna=False).to_dict())

#CATEGORICAL VALUE CHECK
print("\nCATEGORICAL VALUE CHECK")
print("-" * 50)

print("\nAccounts - industry:")
print(accounts["industry"].value_counts(dropna=False))

print("\nAccounts - country:")
print(accounts["country"].value_counts(dropna=False))

print("\nAccounts - referral_source:")
print(accounts["referral_source"].value_counts(dropna=False))

print("\nAccounts - plan_tier:")
print(accounts["plan_tier"].value_counts(dropna=False))

print("\nSubscriptions - plan_tier:")
print(subscriptions["plan_tier"].value_counts(dropna=False))

print("\nSubscriptions - billing_frequency:")
print(subscriptions["billing_frequency"].value_counts(dropna=False))

print("\nFeature Usage - feature_name:")
print(feature_usage["feature_name"].value_counts(dropna=False))

print("\nSupport Tickets - priority:")
print(support_tickets["priority"].value_counts(dropna=False))

print("\nChurn Events - reason_code:")
print(churn_events["reason_code"].value_counts(dropna=False))

#NUMERIC DATA RANGE CHECK
print("\nNUMERIC DATA RANGE CHECK")
print("-" * 50)

print("\nAccounts:")
print("seats - min:", accounts["seats"].min(), "| max:", accounts["seats"].max())

print("\nSubscriptions:")
print("seats - min:", subscriptions["seats"].min(), "| max:", subscriptions["seats"].max())
print("mrr_amount - min:", subscriptions["mrr_amount"].min(), "| max:", subscriptions["mrr_amount"].max())
print("arr_amount - min:", subscriptions["arr_amount"].min(), "| max:", subscriptions["arr_amount"].max())

print("\nFeature Usage:")
print("usage_count - min:", feature_usage["usage_count"].min(), "| max:", feature_usage["usage_count"].max())
print("usage_duration_secs - min:", feature_usage["usage_duration_secs"].min(), "| max:", feature_usage["usage_duration_secs"].max())
print("error_count - min:", feature_usage["error_count"].min(), "| max:", feature_usage["error_count"].max())

print("\nSupport Tickets:")
print("resolution_time_hours - min:", support_tickets["resolution_time_hours"].min(), "| max:", support_tickets["resolution_time_hours"].max())
print("first_response_time_minutes - min:", support_tickets["first_response_time_minutes"].min(), "| max:", support_tickets["first_response_time_minutes"].max())
print("satisfaction_score - min:", support_tickets["satisfaction_score"].min(), "| max:", support_tickets["satisfaction_score"].max())

print("\nChurn Events:")
print("refund_amount_usd - min:", churn_events["refund_amount_usd"].min(), "| max:", churn_events["refund_amount_usd"].max())

#DATE / DATETIME RANGE CHECK
print("\nDATE / DATETIME RANGE CHECK")
print("-" * 50)

print("\nAccounts - signup_date:")
print("Min:", accounts["signup_date"].min())
print("Max:", accounts["signup_date"].max())

print("\nSubscriptions - start_date:")
print("Min:", subscriptions["start_date"].min())
print("Max:", subscriptions["start_date"].max())

print("\nSubscriptions - end_date:")
print("Min:", subscriptions["end_date"].min())
print("Max:", subscriptions["end_date"].max())

print("\nFeature Usage - usage_date:")
print("Min:", feature_usage["usage_date"].min())
print("Max:", feature_usage["usage_date"].max())

print("\nSupport Tickets - submitted_at:")
print("Min:", support_tickets["submitted_at"].min())
print("Max:", support_tickets["submitted_at"].max())

print("\nSupport Tickets - closed_at:")
print("Min:", support_tickets["closed_at"].min())
print("Max:", support_tickets["closed_at"].max())

print("\nChurn Events - churn_date:")
print("Min:", churn_events["churn_date"].min())
print("Max:", churn_events["churn_date"].max())

#LOGICAL DATE VALIDATION
print("\nLOGICAL DATE VALIDATION")
print("-" * 50)

# Convert temporary copies of date columns for validation
subscription_start = pd.to_datetime(subscriptions["start_date"], errors="coerce")
subscription_end = pd.to_datetime(subscriptions["end_date"], errors="coerce")

ticket_submitted = pd.to_datetime(support_tickets["submitted_at"], errors="coerce")
ticket_closed = pd.to_datetime(support_tickets["closed_at"], errors="coerce")

account_signup = pd.to_datetime(accounts["signup_date"], errors="coerce")
churn_date = pd.to_datetime(churn_events["churn_date"], errors="coerce")

# 1. Subscription end date before start date
invalid_subscription_dates = (
    subscription_end.notna()
    & (subscription_end < subscription_start)
)

print("\nSubscriptions - end_date before start_date:")
print(invalid_subscription_dates.sum())

# 2. Ticket closed before submitted
invalid_ticket_dates = ticket_closed < ticket_submitted

print("\nSupport Tickets - closed_at before submitted_at:")
print(invalid_ticket_dates.sum())

# 3. Churn date before account signup date
churn_with_signup = churn_events[["account_id", "churn_date"]].merge(
    accounts[["account_id", "signup_date"]],
    on="account_id",
    how="left"
)

churn_with_signup["churn_date"] = pd.to_datetime(
    churn_with_signup["churn_date"],
    errors="coerce"
)

churn_with_signup["signup_date"] = pd.to_datetime(
    churn_with_signup["signup_date"],
    errors="coerce"
)

invalid_churn_dates = (
    churn_with_signup["churn_date"]
    < churn_with_signup["signup_date"]
)

print("\nChurn Events - churn_date before account signup_date:")
print(invalid_churn_dates.sum())

#SUBSCRIPTION REVENUE VALIDATION
print("\nSUBSCRIPTION REVENUE VALIDATION")
print("-" * 50)

subscriptions["expected_arr"] = subscriptions["mrr_amount"] * 12

subscriptions["arr_difference"] = (
    subscriptions["arr_amount"] - subscriptions["expected_arr"]
)

print("\nMRR × 12 vs ARR:")
print("Matching records:", (subscriptions["arr_difference"] == 0).sum())
print("Non-matching records:", (subscriptions["arr_difference"] != 0).sum())

print("\nARR difference:")
print("Min:", subscriptions["arr_difference"].min())
print("Max:", subscriptions["arr_difference"].max())

#SUBSCRIPTION STATUS CONSISTENCY
print("\nSUBSCRIPTION STATUS CONSISTENCY")
print("-" * 50)

missing_end_date = subscriptions["end_date"].isna()

print("\nChurned subscriptions with missing end_date:")
print(
    (
        subscriptions["churn_flag"]
        & missing_end_date
    ).sum()
)

print("\nNon-churned subscriptions with missing end_date:")
print(
    (
        (~subscriptions["churn_flag"])
        & missing_end_date
    ).sum()
)

print("\nChurned subscriptions with an end_date:")
print(
    (
        subscriptions["churn_flag"]
        & subscriptions["end_date"].notna()
    ).sum()
)

print("\nNon-churned subscriptions with an end_date:")
print(
    (
        (~subscriptions["churn_flag"])
        & subscriptions["end_date"].notna()
    ).sum()
)

#ACCOUNT vs SUBSCRIPTION CHURN CHECK
print("\nACCOUNT vs SUBSCRIPTION CHURN CHECK")
print("-" * 50)

account_subscription_churn = subscriptions.groupby("account_id")["churn_flag"].agg(
    total_subscriptions="count",
    churned_subscriptions="sum"
).reset_index()

account_subscription_churn = account_subscription_churn.merge(
    accounts[["account_id", "churn_flag"]],
    on="account_id",
    how="left"
)

print("\nAccounts with account-level churn_flag = True:")
print(
    (
        account_subscription_churn["churn_flag"] == True
    ).sum()
)

print("\nAccounts with account-level churn_flag = False:")
print(
    (
        account_subscription_churn["churn_flag"] == False
    ).sum()
)

print("\nChurned accounts with zero churned subscriptions:")
print(
    (
        (account_subscription_churn["churn_flag"] == True)
        & (account_subscription_churn["churned_subscriptions"] == 0)
    ).sum()
)

print("\nNon-churned accounts with at least one churned subscription:")
print(
    (
        (account_subscription_churn["churn_flag"] == False)
        & (account_subscription_churn["churned_subscriptions"] > 0)
    ).sum()
)

#ACCOUNT vs CHURN EVENT CHECK
print("\nACCOUNT vs CHURN EVENT CHECK")
print("-" * 50)

account_churn_events = churn_events.groupby("account_id").size().reset_index(
    name="churn_event_count"
)

account_churn_events = accounts[["account_id", "churn_flag"]].merge(
    account_churn_events,
    on="account_id",
    how="left"
)

account_churn_events["churn_event_count"] = (
    account_churn_events["churn_event_count"].fillna(0)
)

print("\nAccounts with account-level churn_flag = True:")
print(
    (
        account_churn_events["churn_flag"] == True
    ).sum()
)

print("\nAccounts with account-level churn_flag = False:")
print(
    (
        account_churn_events["churn_flag"] == False
    ).sum()
)

print("\nChurned accounts with zero churn events:")
print(
    (
        (account_churn_events["churn_flag"] == True)
        & (account_churn_events["churn_event_count"] == 0)
    ).sum()
)

print("\nNon-churned accounts with at least one churn event:")
print(
    (
        (account_churn_events["churn_flag"] == False)
        & (account_churn_events["churn_event_count"] > 0)
    ).sum()
)

print("\nTotal churn event records:")
print(len(churn_events))

#CHURN EVENT ACCOUNT COVERAGE CHECK
print("\nCHURN EVENT ACCOUNT COVERAGE CHECK")
print("-" * 50)

churn_event_accounts = churn_events["account_id"].nunique()
accounts_with_churn_events = churn_events["account_id"].unique()

print("\nDistinct accounts appearing in Churn Events:")
print(churn_event_accounts)

print("\nAccounts table total:")
print(accounts["account_id"].nunique())

print("\nChurn events per account - minimum:")
print(
    churn_events.groupby("account_id").size().min()
)

print("\nChurn events per account - maximum:")
print(
    churn_events.groupby("account_id").size().max()
)

print("\nAccounts with multiple churn events:")
print(
    (
        churn_events.groupby("account_id").size() > 1
    ).sum()
)

#FINAL RAW DATASET SIZE CHECK
print("\nFINAL RAW DATASET SIZE CHECK")
print("-" * 50)

expected_shapes = {
    "Accounts": (500, 10),
    "Subscriptions": (5000, 14),
    "Feature Usage": (25000, 8),
    "Support Tickets": (2000, 9),
    "Churn Events": (600, 9)
}

actual_shapes = {
    "Accounts": accounts.shape,
    "Subscriptions": subscriptions.shape,
    "Feature Usage": feature_usage.shape,
    "Support Tickets": support_tickets.shape,
    "Churn Events": churn_events.shape
}

for dataset_name in expected_shapes:
    expected = expected_shapes[dataset_name]
    actual = actual_shapes[dataset_name]

    print(f"\n{dataset_name}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Match:    {expected == actual}")

#REMOVING TEMPORARY VALIDATION COLUMNS
print("\nREMOVING TEMPORARY VALIDATION COLUMNS")
print("-" * 50)

subscriptions.drop(
    columns=["expected_arr", "arr_difference"],
    inplace=True
)

print("Temporary validation columns removed.")

print("\nSubscriptions shape after removal:")
print(subscriptions.shape)