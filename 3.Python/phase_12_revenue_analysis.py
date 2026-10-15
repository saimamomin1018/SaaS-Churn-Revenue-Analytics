import pandas as pd
import numpy as np

# ============================================================
# STEP 12.2: LOAD CLEANED RAVENSTACK DATA
# ============================================================

base_path = "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/"

accounts = pd.read_csv(base_path + "ravenstack_accounts_cleaned.csv")
subscriptions = pd.read_csv(base_path + "ravenstack_subscriptions_cleaned.csv")
churn_events = pd.read_csv(base_path + "ravenstack_churn_events_cleaned.csv")

print("===== DATA LOADED =====")

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Churn Events:", churn_events.shape)

# ============================================================
# STEP 12.3: REVENUE BY PLAN
# ============================================================

revenue_by_plan = (
    subscriptions
    .groupby("plan_tier")
    .agg(
        subscriptions=("subscription_id", "count"),
        total_mrr=("mrr_amount", "sum"),
        total_arr=("arr_amount", "sum"),
        avg_mrr=("mrr_amount", "mean")
    )
    .reset_index()
)

revenue_by_plan["mrr_share_pct"] = (
    revenue_by_plan["total_mrr"]
    / revenue_by_plan["total_mrr"].sum()
    * 100
).round(2)

revenue_by_plan["arr_share_pct"] = (
    revenue_by_plan["total_arr"]
    / revenue_by_plan["total_arr"].sum()
    * 100
).round(2)

print("\n===== REVENUE BY PLAN =====")
print(
    revenue_by_plan.to_string(index=False)
)

# ============================================================
# STEP 12.4: REVENUE BY BILLING FREQUENCY
# ============================================================

revenue_by_billing = (
    subscriptions
    .groupby("billing_frequency")
    .agg(
        subscriptions=("subscription_id", "count"),
        total_mrr=("mrr_amount", "sum"),
        total_arr=("arr_amount", "sum"),
        avg_mrr=("mrr_amount", "mean")
    )
    .reset_index()
)

revenue_by_billing["mrr_share_pct"] = (
    revenue_by_billing["total_mrr"]
    / revenue_by_billing["total_mrr"].sum()
    * 100
).round(2)

print("\n===== REVENUE BY BILLING FREQUENCY =====")
print(
    revenue_by_billing.to_string(index=False)
)

# ============================================================
# STEP 12.5: CHURNED REVENUE BY PLAN
# ============================================================

churned_revenue_by_plan = (
    subscriptions
    .groupby("plan_tier")
    .agg(
        total_mrr=("mrr_amount", "sum"),
        churned_mrr=(
            "mrr_amount",
            lambda x: x[subscriptions.loc[x.index, "churn_flag"]].sum()
        ),
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churned_revenue_by_plan["churned_mrr_pct"] = (
    churned_revenue_by_plan["churned_mrr"]
    / churned_revenue_by_plan["total_mrr"]
    * 100
).round(2)

print("\n===== CHURNED REVENUE BY PLAN =====")
print(
    churned_revenue_by_plan.to_string(index=False)
)

# ============================================================
# STEP 12.6: MONTHLY MRR TREND
# ============================================================

subscriptions["start_date"] = pd.to_datetime(
    subscriptions["start_date"]
)

monthly_mrr = (
    subscriptions
    .groupby(
        subscriptions["start_date"].dt.to_period("M")
    )
    .agg(
        total_mrr=("mrr_amount", "sum"),
        subscriptions=("subscription_id", "count")
    )
    .reset_index()
)

monthly_mrr["month"] = (
    monthly_mrr["start_date"]
    .astype(str)
)

monthly_mrr = monthly_mrr[
    ["month", "total_mrr", "subscriptions"]
]

print("\n===== MONTHLY MRR TREND =====")
print(
    monthly_mrr.to_string(index=False)
)

# ============================================================
# STEP 12.7: PHASE 12 FINAL VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("PHASE 12 FINAL VALIDATION")
print("=" * 60)

total_mrr = subscriptions["mrr_amount"].sum()
total_arr = subscriptions["arr_amount"].sum()

churned_mrr = subscriptions.loc[
    subscriptions["churn_flag"] == True,
    "mrr_amount"
].sum()

print("Total Subscriptions:", len(subscriptions))
print("Total MRR:", total_mrr)
print("Total ARR:", total_arr)
print("Churned MRR:", churned_mrr)
print("Revenue by Plan Records:", len(revenue_by_plan))
print("Billing Frequency Records:", len(revenue_by_billing))
print("Monthly MRR Records:", len(monthly_mrr))

print("\n===== VALIDATION CHECKS =====")

print(
    "Subscription count check:",
    "PASS" if len(subscriptions) == 5000 else "FAIL"
)

print(
    "Total MRR check:",
    "PASS" if total_mrr == 11338747 else "FAIL"
)

print(
    "Total ARR check:",
    "PASS" if total_arr == 136064964 else "FAIL"
)

print(
    "Churned MRR check:",
    "PASS" if churned_mrr == 1179139 else "FAIL"
)

print(
    "ARR = MRR × 12 check:",
    "PASS"
    if (subscriptions["arr_amount"] == subscriptions["mrr_amount"] * 12).all()
    else "FAIL"
)

print(
    "Monthly coverage check:",
    "PASS" if len(monthly_mrr) == 24 else "FAIL"
)

print("=" * 60)
print("PHASE 12 VALIDATION COMPLETED")
print("=" * 60)