# ============================================================
# PHASE 9: PYTHON EXPLORATORY DATA ANALYSIS (EDA)
# Project: SaaS Subscription, Customer Churn & Revenue Analytics
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 9.3: LOAD CLEANED DATASETS
# ============================================================

accounts = pd.read_csv("d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_accounts_cleaned.csv")

subscriptions = pd.read_csv("d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_subscriptions_cleaned.csv")

feature_usage = pd.read_csv("d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_feature_usage_cleaned.csv")

support_tickets = pd.read_csv("d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_support_tickets_cleaned.csv")

churn_events = pd.read_csv("d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_churn_events_cleaned.csv")

# ============================================================
# STEP 9.4: VALIDATE LOADED DATASETS
# ============================================================

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Feature Usage:", feature_usage.shape)
print("Support Tickets:", support_tickets.shape)
print("Churn Events:", churn_events.shape)

# ============================================================
# STEP 9.5: DATASET STRUCTURE AND DATA TYPES
# ============================================================

print("\n===== ACCOUNTS INFO =====")
accounts.info()

print("\n===== SUBSCRIPTIONS INFO =====")
subscriptions.info()

print("\n===== FEATURE USAGE INFO =====")
feature_usage.info()

print("\n===== SUPPORT TICKETS INFO =====")
support_tickets.info()

print("\n===== CHURN EVENTS INFO =====")
churn_events.info()

# ============================================================
# STEP 9.6: CONVERT DATE/TIME COLUMNS
# ============================================================

accounts["signup_date"] = pd.to_datetime(accounts["signup_date"])

subscriptions["start_date"] = pd.to_datetime(
    subscriptions["start_date"]
)

subscriptions["end_date"] = pd.to_datetime(
    subscriptions["end_date"]
)

feature_usage["usage_date"] = pd.to_datetime(
    feature_usage["usage_date"]
)

support_tickets["submitted_at"] = pd.to_datetime(
    support_tickets["submitted_at"]
)

support_tickets["closed_at"] = pd.to_datetime(
    support_tickets["closed_at"]
)

churn_events["churn_date"] = pd.to_datetime(
    churn_events["churn_date"]
)

# ============================================================
# STEP 9.7: VERIFY DATE/TIME CONVERSIONS
# ============================================================

print("\n===== DATE COLUMN DATA TYPES =====")

print("Accounts signup_date:", accounts["signup_date"].dtype)
print("Subscriptions start_date:", subscriptions["start_date"].dtype)
print("Subscriptions end_date:", subscriptions["end_date"].dtype)
print("Feature Usage usage_date:", feature_usage["usage_date"].dtype)
print("Support submitted_at:", support_tickets["submitted_at"].dtype)
print("Support closed_at:", support_tickets["closed_at"].dtype)
print("Churn Events churn_date:", churn_events["churn_date"].dtype)

# ============================================================
# STEP 9.8: DESCRIPTIVE STATISTICS
# ============================================================

print("\n===== ACCOUNTS NUMERIC SUMMARY =====")
print(accounts[["seats"]].describe())

print("\n===== SUBSCRIPTIONS NUMERIC SUMMARY =====")
print(
    subscriptions[
        ["seats", "mrr_amount", "arr_amount"]
    ].describe()
)

print("\n===== FEATURE USAGE NUMERIC SUMMARY =====")
print(
    feature_usage[
        [
            "usage_count",
            "usage_duration_secs",
            "error_count"
        ]
    ].describe()
)

print("\n===== SUPPORT TICKETS NUMERIC SUMMARY =====")
print(
    support_tickets[
        [
            "resolution_time_hours",
            "first_response_time_minutes",
            "satisfaction_score"
        ]
    ].describe()

)

print("\n===== CHURN EVENTS NUMERIC SUMMARY =====")
print(
    churn_events[
        ["refund_amount_usd"]
    ].describe()
)

# ============================================================
# STEP 9.9: CATEGORICAL DISTRIBUTION ANALYSIS
# ============================================================

print("\n===== ACCOUNT PLAN DISTRIBUTION =====")
print(accounts["plan_tier"].value_counts())

print("\n===== ACCOUNT INDUSTRY DISTRIBUTION =====")
print(accounts["industry"].value_counts())

print("\n===== ACCOUNT COUNTRY DISTRIBUTION =====")
print(accounts["country"].value_counts())

print("\n===== REFERRAL SOURCE DISTRIBUTION =====")
print(accounts["referral_source"].value_counts())

print("\n===== SUBSCRIPTION PLAN DISTRIBUTION =====")
print(subscriptions["plan_tier"].value_counts())

print("\n===== BILLING FREQUENCY DISTRIBUTION =====")
print(subscriptions["billing_frequency"].value_counts())

print("\n===== SUPPORT PRIORITY DISTRIBUTION =====")
print(support_tickets["priority"].value_counts())

print("\n===== CHURN REASON DISTRIBUTION =====")
print(churn_events["reason_code"].value_counts())

# ============================================================
# STEP 9.10: CHURN DISTRIBUTION ANALYSIS
# ============================================================

print("\n===== ACCOUNT CHURN DISTRIBUTION =====")
print(accounts["churn_flag"].value_counts())

print("\n===== ACCOUNT CHURN PERCENTAGE =====")
print(
    accounts["churn_flag"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\n===== SUBSCRIPTION CHURN DISTRIBUTION =====")
print(subscriptions["churn_flag"].value_counts())

print("\n===== SUBSCRIPTION CHURN PERCENTAGE =====")
print(
    subscriptions["churn_flag"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# ============================================================
# STEP 9.11: CHURN RATE BY SUBSCRIPTION PLAN
# ============================================================

plan_churn = (
    subscriptions
    .groupby("plan_tier")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
)

plan_churn["churn_rate"] = (
    plan_churn["churned_subscriptions"]
    / plan_churn["total_subscriptions"]
    * 100
)

plan_churn["churn_rate"] = plan_churn["churn_rate"].round(2)

plan_churn = plan_churn.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== CHURN RATE BY SUBSCRIPTION PLAN =====")
print(plan_churn)

# ============================================================
# STEP 9.12: MRR ANALYSIS BY SUBSCRIPTION PLAN
# ============================================================

plan_revenue = (
    subscriptions
    .groupby("plan_tier")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        total_mrr=("mrr_amount", "sum"),
        average_mrr=("mrr_amount", "mean")
    )
)

plan_revenue["total_arr"] = plan_revenue["total_mrr"] * 12

plan_revenue["total_mrr"] = plan_revenue["total_mrr"].round(2)
plan_revenue["average_mrr"] = plan_revenue["average_mrr"].round(2)
plan_revenue["total_arr"] = plan_revenue["total_arr"].round(2)

plan_revenue = plan_revenue.sort_values(
    "total_mrr",
    ascending=False
)

print("\n===== MRR ANALYSIS BY SUBSCRIPTION PLAN =====")
print(plan_revenue)

# ============================================================
# STEP 9.13: MONTHLY MRR TREND
# ============================================================

monthly_mrr = (
    subscriptions
    .groupby(
        subscriptions["start_date"].dt.to_period("M")
    )["mrr_amount"]
    .sum()
    .reset_index()
)

monthly_mrr["start_date"] = monthly_mrr["start_date"].astype(str)

monthly_mrr = monthly_mrr.rename(
    columns={
        "start_date": "month",
        "mrr_amount": "total_mrr"
    }
)

print("\n===== MONTHLY MRR TREND =====")
print(monthly_mrr)

# ============================================================
# STEP 9.14: MONTHLY MRR VISUALIZATION
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_mrr["month"],
    monthly_mrr["total_mrr"],
    marker="o"
)

plt.title("Monthly MRR Trend")
plt.xlabel("Month")
plt.ylabel("MRR")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ============================================================
# STEP 9.15: CHURN REASONS ANALYSIS
# ============================================================

churn_reasons = (
    churn_events["reason_code"]
    .value_counts()
    .reset_index()
)

churn_reasons.columns = ["reason_code", "churn_events"]

churn_reasons["percentage"] = (
    churn_reasons["churn_events"]
    / churn_reasons["churn_events"].sum()
    * 100
)

churn_reasons["percentage"] = (
    churn_reasons["percentage"].round(2)
)

print("\n===== CHURN REASONS ANALYSIS =====")
print(churn_reasons)

# ============================================================
# STEP 9.16: CHURN REASONS VISUALIZATION
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    churn_reasons["reason_code"],
    churn_reasons["churn_events"]
)

plt.title("Churn Events by Reason")
plt.xlabel("Churn Reason")
plt.ylabel("Number of Churn Events")

plt.tight_layout()
plt.show()

# ============================================================
# STEP 9.17: SUPPORT TICKET ANALYSIS BY PRIORITY
# ============================================================

support_priority = (
    support_tickets
    .groupby("priority")
    .agg(
        total_tickets=("ticket_id", "count"),
        average_resolution_hours=("resolution_time_hours", "mean"),
        average_first_response_minutes=("first_response_time_minutes", "mean"),
        average_satisfaction=("satisfaction_score", "mean")
    )
)

support_priority["average_resolution_hours"] = (
    support_priority["average_resolution_hours"].round(2)
)

support_priority["average_first_response_minutes"] = (
    support_priority["average_first_response_minutes"].round(2)
)

support_priority["average_satisfaction"] = (
    support_priority["average_satisfaction"].round(2)
)

support_priority = support_priority.sort_values(
    "total_tickets",
    ascending=False
)

print("\n===== SUPPORT TICKET ANALYSIS BY PRIORITY =====")
print(support_priority)
print(support_priority.to_string())

# ============================================================
# STEP 9.18: FEATURE USAGE ANALYSIS
# ============================================================

feature_usage_summary = (
    feature_usage
    .groupby("feature_name")
    .agg(
        total_usage=("usage_count", "sum"),
        average_usage=("usage_count", "mean"),
        total_errors=("error_count", "sum")
    )
)

feature_usage_summary["average_usage"] = (
    feature_usage_summary["average_usage"].round(2)
)

feature_usage_summary = feature_usage_summary.sort_values(
    "total_usage",
    ascending=False
)

print("\n===== TOP FEATURES BY TOTAL USAGE =====")
print(feature_usage_summary.head(10).to_string())

# ============================================================
# STEP 9.19: BILLING FREQUENCY ANALYSIS
# ============================================================

billing_analysis = (
    subscriptions
    .groupby("billing_frequency")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        total_mrr=("mrr_amount", "sum"),
        average_mrr=("mrr_amount", "mean"),
        churned_subscriptions=("churn_flag", "sum")
    )
)

billing_analysis["churn_rate"] = (
    billing_analysis["churned_subscriptions"]
    / billing_analysis["total_subscriptions"]
    * 100
)

billing_analysis["total_mrr"] = (
    billing_analysis["total_mrr"].round(2)
)

billing_analysis["average_mrr"] = (
    billing_analysis["average_mrr"].round(2)
)

billing_analysis["churn_rate"] = (
    billing_analysis["churn_rate"].round(2)
)

print("\n===== BILLING FREQUENCY ANALYSIS =====")
print(billing_analysis.to_string())

# ============================================================
# STEP 9.20: UPGRADE & DOWNGRADE ANALYSIS
# ============================================================

upgrade_analysis = (
    subscriptions
    .groupby("upgrade_flag")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
)

upgrade_analysis["churn_rate"] = (
    upgrade_analysis["churned_subscriptions"]
    / upgrade_analysis["total_subscriptions"]
    * 100
)

upgrade_analysis["churn_rate"] = (
    upgrade_analysis["churn_rate"].round(2)
)

downgrade_analysis = (
    subscriptions
    .groupby("downgrade_flag")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
)

downgrade_analysis["churn_rate"] = (
    downgrade_analysis["churned_subscriptions"]
    / downgrade_analysis["total_subscriptions"]
    * 100
)

downgrade_analysis["churn_rate"] = (
    downgrade_analysis["churn_rate"].round(2)
)

print("\n===== UPGRADE ANALYSIS =====")
print(upgrade_analysis.to_string())

print("\n===== DOWNGRADE ANALYSIS =====")
print(downgrade_analysis.to_string())

# ============================================================
# STEP 9.21: TRIAL VS NON-TRIAL CHURN ANALYSIS
# ============================================================

trial_analysis = (
    subscriptions
    .groupby("is_trial")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum"),
        total_mrr=("mrr_amount", "sum"),
        average_mrr=("mrr_amount", "mean")
    )
)

trial_analysis["churn_rate"] = (
    trial_analysis["churned_subscriptions"]
    / trial_analysis["total_subscriptions"]
    * 100
)

trial_analysis["total_mrr"] = (
    trial_analysis["total_mrr"].round(2)
)

trial_analysis["average_mrr"] = (
    trial_analysis["average_mrr"].round(2)
)

trial_analysis["churn_rate"] = (
    trial_analysis["churn_rate"].round(2)
)

print("\n===== TRIAL VS NON-TRIAL ANALYSIS =====")
print(trial_analysis.to_string())

# ============================================================
# STEP 9.22: ACCOUNT CHURN BY INDUSTRY
# ============================================================

industry_churn = (
    accounts
    .groupby("industry")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
)

industry_churn["churn_rate"] = (
    industry_churn["churned_accounts"]
    / industry_churn["total_accounts"]
    * 100
)

industry_churn["churn_rate"] = (
    industry_churn["churn_rate"].round(2)
)

industry_churn = industry_churn.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY INDUSTRY =====")
print(industry_churn.to_string())

# ============================================================
# STEP 9.23: ACCOUNT CHURN BY COUNTRY
# ============================================================

country_churn = (
    accounts
    .groupby("country")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
)

country_churn["churn_rate"] = (
    country_churn["churned_accounts"]
    / country_churn["total_accounts"]
    * 100
)

country_churn["churn_rate"] = (
    country_churn["churn_rate"].round(2)
)

country_churn = country_churn.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY COUNTRY =====")
print(country_churn.to_string())

# ============================================================
# STEP 9.24: ACCOUNT CHURN BY REFERRAL SOURCE
# ============================================================

referral_churn = (
    accounts
    .groupby("referral_source")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
)

referral_churn["churn_rate"] = (
    referral_churn["churned_accounts"]
    / referral_churn["total_accounts"]
    * 100
)

referral_churn["churn_rate"] = (
    referral_churn["churn_rate"].round(2)
)

referral_churn = referral_churn.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY REFERRAL SOURCE =====")
print(referral_churn.to_string())

# ============================================================
# STEP 9.25: FEATURE ERROR ANALYSIS
# ============================================================

feature_errors = (
    feature_usage
    .groupby("feature_name")
    .agg(
        total_usage=("usage_count", "sum"),
        total_errors=("error_count", "sum"),
        average_errors=("error_count", "mean")
    )
)

feature_errors["average_errors"] = (
    feature_errors["average_errors"].round(2)
)

feature_errors = feature_errors.sort_values(
    "total_errors",
    ascending=False
)

print("\n===== TOP FEATURES BY TOTAL ERRORS =====")
print(feature_errors.head(10).to_string())

# ============================================================
# STEP 9.26: SUPPORT ESCALATION ANALYSIS
# ============================================================

escalation_analysis = (
    support_tickets
    .groupby("escalation_flag")
    .agg(
        total_tickets=("ticket_id", "count"),
        average_resolution_hours=("resolution_time_hours", "mean"),
        average_first_response_minutes=("first_response_time_minutes", "mean"),
        average_satisfaction=("satisfaction_score", "mean")
    )
)

escalation_analysis["average_resolution_hours"] = (
    escalation_analysis["average_resolution_hours"].round(2)
)

escalation_analysis["average_first_response_minutes"] = (
    escalation_analysis["average_first_response_minutes"].round(2)
)

escalation_analysis["average_satisfaction"] = (
    escalation_analysis["average_satisfaction"].round(2)
)

print("\n===== SUPPORT ESCALATION ANALYSIS =====")
print(escalation_analysis.to_string())

# ============================================================
# STEP 9.27: ACCOUNT-LEVEL CHURN & SUBSCRIPTION SUMMARY
# ============================================================

account_subscription_summary = (
    subscriptions
    .groupby("account_id")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum"),
        total_mrr=("mrr_amount", "sum"),
        churned_mrr=("mrr_amount", lambda x: x[
            subscriptions.loc[x.index, "churn_flag"]
        ].sum())
    )
    .reset_index()
)

account_subscription_summary = account_subscription_summary.merge(
    accounts[
        [
            "account_id",
            "account_name",
            "industry",
            "plan_tier",
            "churn_flag"
        ]
    ],
    on="account_id",
    how="left"
)

account_subscription_summary = account_subscription_summary.rename(
    columns={
        "churn_flag": "account_churn_flag"
    }
)

account_subscription_summary = account_subscription_summary.sort_values(
    "total_mrr",
    ascending=False
)

print("\n===== ACCOUNT-LEVEL CHURN & SUBSCRIPTION SUMMARY =====")
print(
    account_subscription_summary.head(20).to_string(index=False)
)

# ============================================================
# STEP 9.28: CHURN EVENT ANALYSIS
# ============================================================

churn_event_analysis = (
    churn_events
    .groupby(["reason_code", "is_reactivation"])
    .agg(
        churn_events=("churn_event_id", "count"),
        total_refund=("refund_amount_usd", "sum"),
        average_refund=("refund_amount_usd", "mean")
    )
    .reset_index()
)

churn_event_analysis["total_refund"] = (
    churn_event_analysis["total_refund"].round(2)
)

churn_event_analysis["average_refund"] = (
    churn_event_analysis["average_refund"].round(2)
)

churn_event_analysis = churn_event_analysis.sort_values(
    ["reason_code", "is_reactivation"]
)

print("\n===== CHURN EVENT ANALYSIS BY REASON & REACTIVATION =====")
print(
    churn_event_analysis.to_string(index=False)
)

# ============================================================
# STEP 9.29: PYTHON EDA FINAL VALIDATION
# ============================================================

print("\n===== PYTHON EDA FINAL VALIDATION =====")

print("Accounts:", len(accounts))
print("Subscriptions:", len(subscriptions))
print("Feature Usage:", len(feature_usage))
print("Support Tickets:", len(support_tickets))
print("Churn Events:", len(churn_events))

print(
    "Total MRR:",
    subscriptions["mrr_amount"].sum()
)

print(
    "Churned Subscriptions:",
    subscriptions["churn_flag"].sum()
)

print(
    "Churned MRR:",
    subscriptions.loc[
        subscriptions["churn_flag"],
        "mrr_amount"
    ].sum()
)

print(
    "Account Churned:",
    accounts["churn_flag"].sum()
)

print(
    "Reactivation Events:",
    churn_events["is_reactivation"].sum()
)

print(
    "Support Escalations:",
    support_tickets["escalation_flag"].sum()
)

# ============================================================
# STEP 9.30: SAVE PYTHON EDA VALIDATION RESULTS
# ============================================================

eda_validation = pd.DataFrame({
    "metric": [
        "Accounts",
        "Subscriptions",
        "Feature Usage",
        "Support Tickets",
        "Churn Events",
        "Total MRR",
        "Churned Subscriptions",
        "Churned MRR",
        "Churned Accounts",
        "Reactivation Events",
        "Support Escalations"
    ],
    "value": [
        len(accounts),
        len(subscriptions),
        len(feature_usage),
        len(support_tickets),
        len(churn_events),
        subscriptions["mrr_amount"].sum(),
        subscriptions["churn_flag"].sum(),
        subscriptions.loc[
            subscriptions["churn_flag"],
            "mrr_amount"
        ].sum(),
        accounts["churn_flag"].sum(),
        churn_events["is_reactivation"].sum(),
        support_tickets["escalation_flag"].sum()
    ]
})

eda_validation.to_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/phase_9_python_eda_validation.csv",
    index=False
)

print("\n===== EDA VALIDATION FILE SAVED =====")
print(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/phase_9_python_eda_validation.csv"
)

# ============================================================
# STEP 9.31: SUBSCRIPTION CHURN RATE BY PLAN VISUALIZATION
# ============================================================

churn_by_plan = (
    subscriptions
    .groupby("plan_tier")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan["churn_rate"] = (
    churn_by_plan["churned_subscriptions"]
    / churn_by_plan["total_subscriptions"]
    * 100
)

churn_by_plan["churn_rate"] = (
    churn_by_plan["churn_rate"].round(2)
)

print("\n===== CHURN RATE BY PLAN =====")
print(churn_by_plan.to_string(index=False))

plt.figure(figsize=(8, 5))

sns.barplot(
    data=churn_by_plan,
    x="plan_tier",
    y="churn_rate"
)

plt.title("Subscription Churn Rate by Plan")
plt.xlabel("Plan Tier")
plt.ylabel("Churn Rate (%)")

plt.tight_layout()

plt.savefig(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/7.images/2.python/Phase 9/phase_9_python_churn_rate_by_plan.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(
    "\nVisualization saved:"
    "\nd:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/7.images/2.python/Phase 9/phase_9_python_churn_rate_by_plan.png"
)