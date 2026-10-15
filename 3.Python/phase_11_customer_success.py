import pandas as pd
import numpy as np

# ============================================================
# STEP 11.2: LOAD CLEANED RAVENSTACK DATA
# ============================================================

base_path = "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/"

accounts = pd.read_csv(base_path + "ravenstack_accounts_cleaned.csv")
subscriptions = pd.read_csv(base_path + "ravenstack_subscriptions_cleaned.csv")
feature_usage = pd.read_csv(base_path + "ravenstack_feature_usage_cleaned.csv")
support_tickets = pd.read_csv(base_path + "ravenstack_support_tickets_cleaned.csv")
churn_events = pd.read_csv(base_path + "ravenstack_churn_events_cleaned.csv")

print("===== DATA LOADED =====")

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Feature Usage:", feature_usage.shape)
print("Support Tickets:", support_tickets.shape)
print("Churn Events:", churn_events.shape)

# ============================================================
# STEP 11.3: CUSTOMER SUCCESS PROFILE
# ============================================================

support_summary = (
    support_tickets
    .groupby("account_id")
    .agg(
        support_tickets=("ticket_id", "count"),
        avg_resolution_hours=("resolution_time_hours", "mean"),
        avg_first_response_minutes=("first_response_time_minutes", "mean"),
        avg_satisfaction=("satisfaction_score", "mean"),
        escalations=("escalation_flag", "sum")
    )
    .reset_index()
)

usage_summary = (
    feature_usage
    .merge(
        subscriptions[["subscription_id", "account_id"]],
        on="subscription_id",
        how="left"
    )
    .groupby("account_id")
    .agg(
        usage_records=("usage_id", "count"),
        total_usage_count=("usage_count", "sum"),
        total_usage_duration_secs=("usage_duration_secs", "sum"),
        total_errors=("error_count", "sum")
    )
    .reset_index()
)

customer_success = (
    accounts[
        [
            "account_id",
            "industry",
            "plan_tier",
            "churn_flag"
        ]
    ]
    .merge(
        support_summary,
        on="account_id",
        how="left"
    )
    .merge(
        usage_summary,
        on="account_id",
        how="left"
    )
)

print("\n===== CUSTOMER SUCCESS PROFILE =====")
print(customer_success.head(10).to_string(index=False))

print("\nCustomer success records:", len(customer_success))

# ============================================================
# STEP 11.4: CUSTOMER SUCCESS METRICS BY CHURN STATUS
# ============================================================

customer_success_by_churn = (
    customer_success
    .groupby("churn_flag")
    .agg(
        accounts=("account_id", "count"),
        avg_support_tickets=("support_tickets", "mean"),
        avg_resolution_hours=("avg_resolution_hours", "mean"),
        avg_first_response_minutes=("avg_first_response_minutes", "mean"),
        avg_satisfaction=("avg_satisfaction", "mean"),
        avg_escalations=("escalations", "mean"),
        avg_usage_count=("total_usage_count", "mean"),
        avg_usage_duration_secs=("total_usage_duration_secs", "mean"),
        avg_errors=("total_errors", "mean")
    )
    .reset_index()
)

print("\n===== CUSTOMER SUCCESS METRICS BY CHURN STATUS =====")
print(
customer_success_by_churn.to_string(index=False)
)

# ============================================================
# STEP 11.5: SUPPORT ESCALATION & ACCOUNT CHURN
# ============================================================

escalation_churn = (
    customer_success
    .assign(
        has_escalation=customer_success["escalations"] > 0
    )
    .groupby("has_escalation")
    .agg(
        accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

escalation_churn["non_churned_accounts"] = (
    escalation_churn["accounts"]
    - escalation_churn["churned_accounts"]
)

escalation_churn["churn_rate"] = (
    escalation_churn["churned_accounts"]
    / escalation_churn["accounts"]
    * 100
).round(2)

print("\n===== SUPPORT ESCALATION & ACCOUNT CHURN =====")
print(
    escalation_churn.to_string(index=False)
)

# ============================================================
# STEP 11.6: PHASE 11 FINAL VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("PHASE 11 FINAL VALIDATION")
print("=" * 60)

print("Total Accounts:", len(customer_success))
print(
    "Accounts with Support Data:",
    customer_success["support_tickets"].notna().sum()
)
print(
    "Accounts with Usage Data:",
    customer_success["usage_records"].notna().sum()
)
print(
    "Churned Accounts:",
    int(customer_success["churn_flag"].sum())
)

print("\n===== VALIDATION CHECKS =====")

print(
    "Account grain check:",
    "PASS" if len(customer_success) == 500 else "FAIL"
)

print(
    "Duplicate account check:",
    "PASS"
    if customer_success["account_id"].nunique() == 500
    else "FAIL"
)

print(
    "Churn count check:",
    "PASS"
    if customer_success["churn_flag"].sum() == 110
    else "FAIL"
)

print(
    "Support escalation check:",
    "PASS"
    if customer_success["escalations"].sum() == 95
    else "FAIL"
)

print("=" * 60)
print("PHASE 11 VALIDATION COMPLETED")
print("=" * 60)

