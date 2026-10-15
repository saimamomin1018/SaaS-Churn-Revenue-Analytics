import pandas as pd
import numpy as np

# ============================================================
# STEP 13.2: LOAD CLEANED RAVENSTACK DATA
# ============================================================

base_path = "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/"

accounts = pd.read_csv(base_path + "ravenstack_accounts_cleaned.csv")
subscriptions = pd.read_csv(base_path + "ravenstack_subscriptions_cleaned.csv")
feature_usage = pd.read_csv(base_path + "ravenstack_feature_usage_cleaned.csv")

print("===== DATA LOADED =====")

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Feature Usage:", feature_usage.shape)

# ============================================================
# STEP 13.3: FEATURE USAGE SUMMARY
# ============================================================

feature_summary = (
    feature_usage
    .groupby("feature_name")
    .agg(
        usage_records=("usage_id", "count"),
        total_usage_count=("usage_count", "sum"),
        total_duration_secs=("usage_duration_secs", "sum"),
        total_errors=("error_count", "sum"),
        avg_usage_count=("usage_count", "mean"),
        avg_duration_secs=("usage_duration_secs", "mean"),
        avg_errors=("error_count", "mean")
    )
    .reset_index()
)

feature_summary["error_rate_per_usage"] = (
    feature_summary["total_errors"]
    / feature_summary["total_usage_count"]
    * 100
).round(2)

print("\n===== FEATURE USAGE SUMMARY =====")
print(
    feature_summary
    .sort_values("total_usage_count", ascending=False)
    .to_string(index=False)
)

# ============================================================
# STEP 13.4: FEATURE USAGE BY CHURN STATUS
# ============================================================

feature_churn = (
    feature_usage
    .merge(
        subscriptions[
            ["subscription_id", "account_id"]
        ],
        on="subscription_id",
        how="left"
    )
    .merge(
        accounts[
            ["account_id", "churn_flag"]
        ],
        on="account_id",
        how="left"
    )
)

feature_usage_by_churn = (
    feature_churn
    .groupby("churn_flag")
    .agg(
        usage_records=("usage_id", "count"),
        total_usage_count=("usage_count", "sum"),
        total_duration_secs=("usage_duration_secs", "sum"),
        total_errors=("error_count", "sum"),
        avg_usage_count=("usage_count", "mean"),
        avg_duration_secs=("usage_duration_secs", "mean"),
        avg_errors=("error_count", "mean")
    )
    .reset_index()
)

print("\n===== FEATURE USAGE BY CHURN STATUS =====")
print(
    feature_usage_by_churn.to_string(index=False)
)

# ============================================================
# STEP 13.5: PHASE 13 FINAL VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("PHASE 13 FINAL VALIDATION")
print("=" * 60)

print("Total Feature Usage Records:", len(feature_usage))
print("Unique Features:", feature_usage["feature_name"].nunique())
print("Total Usage Count:", feature_usage["usage_count"].sum())
print("Total Usage Duration (secs):",
      feature_usage["usage_duration_secs"].sum())
print("Total Errors:", feature_usage["error_count"].sum())

print("\n===== VALIDATION CHECKS =====")

print(
    "Feature usage record check:",
    "PASS" if len(feature_usage) == 25000 else "FAIL"
)

print(
    "Unique feature check:",
    "PASS" if feature_usage["feature_name"].nunique() == 40 else "FAIL"
)

print(
    "Feature summary check:",
    "PASS" if len(feature_summary) == 40 else "FAIL"
)

print(
    "Churn comparison check:",
    "PASS" if len(feature_usage_by_churn) == 2 else "FAIL"
)

print(
    "Usage count non-negative check:",
    "PASS"
    if (feature_usage["usage_count"] >= 0).all()
    else "FAIL"
)

print(
    "Error count non-negative check:",
    "PASS"
    if (feature_usage["error_count"] >= 0).all()
    else "FAIL"
)

print("=" * 60)
print("PHASE 13 VALIDATION COMPLETED")
print("=" * 60)