import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 10.1: LOAD CLEANED DATA
# ============================================================

accounts = pd.read_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_accounts_cleaned.csv"
)

subscriptions = pd.read_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_subscriptions_cleaned.csv"
)

feature_usage = pd.read_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_feature_usage_cleaned.csv"
)

support_tickets = pd.read_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_support_tickets_cleaned.csv"
)

churn_events = pd.read_csv(
    "d:/Projects/SaaS_Subscription_Customer_Success_Churn_Analytics/1.data/2.cleaned/ravenstack_churn_events_cleaned.csv"
)

print("\n===== PHASE 10: DESCRIPTIVE CHURN ANALYSIS =====")
print("\nDatasets loaded successfully.")

print("Accounts:", accounts.shape)
print("Subscriptions:", subscriptions.shape)
print("Feature Usage:", feature_usage.shape)
print("Support Tickets:", support_tickets.shape)
print("Churn Events:", churn_events.shape)

# ============================================================
# STEP 10.2: OVERALL CHURN PROFILE
# ============================================================

account_churn = (
    accounts["churn_flag"]
    .value_counts()
    .rename(index={
        False: "Not Churned",
        True: "Churned"
    })
)

subscription_churn = (
    subscriptions["churn_flag"]
    .value_counts()
    .rename(index={
        False: "Not Churned",
        True: "Churned"
    })
)

account_churn_rate = (
    accounts["churn_flag"].mean() * 100
)

subscription_churn_rate = (
    subscriptions["churn_flag"].mean() * 100
)

print("\n===== ACCOUNT-LEVEL CHURN =====")
print(account_churn.to_string())

print(
    f"\nAccount churn rate: "
    f"{account_churn_rate:.2f}%"
)

print("\n===== SUBSCRIPTION-LEVEL CHURN =====")
print(subscription_churn.to_string())

print(
    f"\nSubscription churn rate: "
    f"{subscription_churn_rate:.2f}%"
)

# ============================================================
# STEP 10.3: SUBSCRIPTION CHURN BY PLAN
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

churn_by_plan["non_churned_subscriptions"] = (
    churn_by_plan["total_subscriptions"]
    - churn_by_plan["churned_subscriptions"]
)

churn_by_plan["churn_rate"] = (
    churn_by_plan["churned_subscriptions"]
    / churn_by_plan["total_subscriptions"]
    * 100
)

churn_by_plan["churn_rate"] = (
    churn_by_plan["churn_rate"].round(2)
)

churn_by_plan = churn_by_plan.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY PLAN =====")
print(
    churn_by_plan.to_string(index=False)
)

# ============================================================
# STEP 10.4: ACCOUNT CHURN BY INDUSTRY
# ============================================================

churn_by_industry = (
    accounts
    .groupby("industry")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_industry["non_churned_accounts"] = (
    churn_by_industry["total_accounts"]
    - churn_by_industry["churned_accounts"]
)

churn_by_industry["churn_rate"] = (
    churn_by_industry["churned_accounts"]
    / churn_by_industry["total_accounts"]
    * 100
)

churn_by_industry["churn_rate"] = (
    churn_by_industry["churn_rate"].round(2)
)

churn_by_industry = churn_by_industry.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY INDUSTRY =====")
print(
    churn_by_industry.to_string(index=False)
)

# ============================================================
# STEP 10.5: ACCOUNT CHURN BY COUNTRY
# ============================================================

churn_by_country = (
    accounts
    .groupby("country")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_country["non_churned_accounts"] = (
    churn_by_country["total_accounts"]
    - churn_by_country["churned_accounts"]
)

churn_by_country["churn_rate"] = (
    churn_by_country["churned_accounts"]
    / churn_by_country["total_accounts"]
    * 100
)

churn_by_country["churn_rate"] = (
    churn_by_country["churn_rate"].round(2)
)

churn_by_country = churn_by_country.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY COUNTRY =====")
print(
    churn_by_country.to_string(index=False)
)

# ============================================================
# STEP 10.6: ACCOUNT CHURN BY REFERRAL SOURCE
# ============================================================

churn_by_referral = (
    accounts
    .groupby("referral_source")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_referral["non_churned_accounts"] = (
    churn_by_referral["total_accounts"]
    - churn_by_referral["churned_accounts"]
)

churn_by_referral["churn_rate"] = (
    churn_by_referral["churned_accounts"]
    / churn_by_referral["total_accounts"]
    * 100
)

churn_by_referral["churn_rate"] = (
    churn_by_referral["churn_rate"].round(2)
)

churn_by_referral = churn_by_referral.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY REFERRAL SOURCE =====")
print(
    churn_by_referral.to_string(index=False)
)

# ============================================================
# STEP 10.7: SUBSCRIPTION CHURN BY BILLING FREQUENCY
# ============================================================

churn_by_billing = (
    subscriptions
    .groupby("billing_frequency")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_billing["non_churned_subscriptions"] = (
    churn_by_billing["total_subscriptions"]
    - churn_by_billing["churned_subscriptions"]
)

churn_by_billing["churn_rate"] = (
    churn_by_billing["churned_subscriptions"]
    / churn_by_billing["total_subscriptions"]
    * 100
)

churn_by_billing["churn_rate"] = (
    churn_by_billing["churn_rate"].round(2)
)

churn_by_billing = churn_by_billing.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY BILLING FREQUENCY =====")
print(
    churn_by_billing.to_string(index=False)
)

# ============================================================
# STEP 10.8: SUBSCRIPTION CHURN BY TRIAL STATUS
# ============================================================

churn_by_trial = (
    subscriptions
    .groupby("is_trial")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum"),
        total_mrr=("mrr_amount", "sum")
    )
    .reset_index()
)

churn_by_trial["non_churned_subscriptions"] = (
    churn_by_trial["total_subscriptions"]
    - churn_by_trial["churned_subscriptions"]
)

churn_by_trial["churn_rate"] = (
    churn_by_trial["churned_subscriptions"]
    / churn_by_trial["total_subscriptions"]
    * 100
)

churn_by_trial["churn_rate"] = (
    churn_by_trial["churn_rate"].round(2)
)

churn_by_trial = churn_by_trial.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY TRIAL STATUS =====")
print(
    churn_by_trial.to_string(index=False)
)

# ============================================================
# STEP 10.9: SUBSCRIPTION CHURN BY UPGRADE STATUS
# ============================================================

churn_by_upgrade = (
    subscriptions
    .groupby("upgrade_flag")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_upgrade["non_churned_subscriptions"] = (
    churn_by_upgrade["total_subscriptions"]
    - churn_by_upgrade["churned_subscriptions"]
)

churn_by_upgrade["churn_rate"] = (
    churn_by_upgrade["churned_subscriptions"]
    / churn_by_upgrade["total_subscriptions"]
    * 100
)

churn_by_upgrade["churn_rate"] = (
    churn_by_upgrade["churn_rate"].round(2)
)

churn_by_upgrade = churn_by_upgrade.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY UPGRADE STATUS =====")
print(
    churn_by_upgrade.to_string(index=False)
)

# ============================================================
# STEP 10.10: SUBSCRIPTION CHURN BY DOWNGRADE STATUS
# ============================================================

churn_by_downgrade = (
    subscriptions
    .groupby("downgrade_flag")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_downgrade["non_churned_subscriptions"] = (
    churn_by_downgrade["total_subscriptions"]
    - churn_by_downgrade["churned_subscriptions"]
)

churn_by_downgrade["churn_rate"] = (
    churn_by_downgrade["churned_subscriptions"]
    / churn_by_downgrade["total_subscriptions"]
    * 100
)

churn_by_downgrade["churn_rate"] = (
    churn_by_downgrade["churn_rate"].round(2)
)

churn_by_downgrade = churn_by_downgrade.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY DOWNGRADE STATUS =====")
print(
    churn_by_downgrade.to_string(index=False)
)

# ============================================================
# STEP 10.11: SUBSCRIPTION CHURN BY AUTO-RENEW STATUS
# ============================================================

churn_by_auto_renew = (
    subscriptions
    .groupby("auto_renew_flag")
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_auto_renew["non_churned_subscriptions"] = (
    churn_by_auto_renew["total_subscriptions"]
    - churn_by_auto_renew["churned_subscriptions"]
)

churn_by_auto_renew["churn_rate"] = (
    churn_by_auto_renew["churned_subscriptions"]
    / churn_by_auto_renew["total_subscriptions"]
    * 100
)

churn_by_auto_renew["churn_rate"] = (
    churn_by_auto_renew["churn_rate"].round(2)
)

churn_by_auto_renew = churn_by_auto_renew.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== SUBSCRIPTION CHURN BY AUTO-RENEW STATUS =====")
print(
    churn_by_auto_renew.to_string(index=False)
)

# ============================================================
# STEP 10.12: CHURN BY PLAN AND BILLING FREQUENCY
# ============================================================

churn_by_plan_billing = (
    subscriptions
    .groupby(["plan_tier", "billing_frequency"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_billing["non_churned_subscriptions"] = (
    churn_by_plan_billing["total_subscriptions"]
    - churn_by_plan_billing["churned_subscriptions"]
)

churn_by_plan_billing["churn_rate"] = (
    churn_by_plan_billing["churned_subscriptions"]
    / churn_by_plan_billing["total_subscriptions"]
    * 100
)

churn_by_plan_billing["churn_rate"] = (
    churn_by_plan_billing["churn_rate"].round(2)
)

churn_by_plan_billing = churn_by_plan_billing.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== CHURN BY PLAN AND BILLING FREQUENCY =====")
print(
    churn_by_plan_billing.to_string(index=False)
)

# ============================================================
# STEP 10.13: ACCOUNT CHURN BY INDUSTRY AND PLAN
# ============================================================

churn_by_industry_plan = (
    accounts
    .groupby(["industry", "plan_tier"])
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_industry_plan["non_churned_accounts"] = (
    churn_by_industry_plan["total_accounts"]
    - churn_by_industry_plan["churned_accounts"]
)

churn_by_industry_plan["churn_rate"] = (
    churn_by_industry_plan["churned_accounts"]
    / churn_by_industry_plan["total_accounts"]
    * 100
)

churn_by_industry_plan["churn_rate"] = (
    churn_by_industry_plan["churn_rate"].round(2)
)

churn_by_industry_plan = churn_by_industry_plan.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY INDUSTRY AND PLAN =====")
print(
    churn_by_industry_plan.to_string(index=False)
)

# ============================================================
# STEP 10.14: ACCOUNT CHURN BY REFERRAL SOURCE AND INDUSTRY
# ============================================================

churn_by_referral_industry = (
    accounts
    .groupby(["referral_source", "industry"])
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_referral_industry["non_churned_accounts"] = (
    churn_by_referral_industry["total_accounts"]
    - churn_by_referral_industry["churned_accounts"]
)

churn_by_referral_industry["churn_rate"] = (
    churn_by_referral_industry["churned_accounts"]
    / churn_by_referral_industry["total_accounts"]
    * 100
)

churn_by_referral_industry["churn_rate"] = (
    churn_by_referral_industry["churn_rate"].round(2)
)

churn_by_referral_industry = churn_by_referral_industry.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY REFERRAL SOURCE AND INDUSTRY =====")
print(
    churn_by_referral_industry.to_string(index=False)
)

# ============================================================
# STEP 10.15: CHURN BY PLAN AND AUTO-RENEWAL
# ============================================================

churn_by_plan_auto = (
    subscriptions
    .groupby(["plan_tier", "auto_renew_flag"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_auto["non_churned_subscriptions"] = (
    churn_by_plan_auto["total_subscriptions"]
    - churn_by_plan_auto["churned_subscriptions"]
)

churn_by_plan_auto["churn_rate"] = (
    churn_by_plan_auto["churned_subscriptions"]
    / churn_by_plan_auto["total_subscriptions"]
    * 100
)

churn_by_plan_auto["churn_rate"] = (
    churn_by_plan_auto["churn_rate"].round(2)
)

churn_by_plan_auto = churn_by_plan_auto.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== CHURN BY PLAN AND AUTO-RENEWAL =====")
print(
    churn_by_plan_auto.to_string(index=False)
)

# ============================================================
# STEP 10.16: CHURN BY PLAN AND TRIAL STATUS
# ============================================================

churn_by_plan_trial = (
    subscriptions
    .groupby(["plan_tier", "is_trial"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_trial["non_churned_subscriptions"] = (
    churn_by_plan_trial["total_subscriptions"]
    - churn_by_plan_trial["churned_subscriptions"]
)

churn_by_plan_trial["churn_rate"] = (
    churn_by_plan_trial["churned_subscriptions"]
    / churn_by_plan_trial["total_subscriptions"]
    * 100
)

churn_by_plan_trial["churn_rate"] = (
    churn_by_plan_trial["churn_rate"].round(2)
)

churn_by_plan_trial = churn_by_plan_trial.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== CHURN BY PLAN AND TRIAL STATUS =====")
print(
    churn_by_plan_trial.to_string(index=False)
)

# ============================================================
# STEP 10.17: CHURN BY UPGRADE AND DOWNGRADE STATUS
# ============================================================

churn_by_changes = (
    subscriptions
    .groupby(["upgrade_flag", "downgrade_flag"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_changes["non_churned_subscriptions"] = (
    churn_by_changes["total_subscriptions"]
    - churn_by_changes["churned_subscriptions"]
)

churn_by_changes["churn_rate"] = (
    churn_by_changes["churned_subscriptions"]
    / churn_by_changes["total_subscriptions"]
    * 100
)

churn_by_changes["churn_rate"] = (
    churn_by_changes["churn_rate"].round(2)
)

churn_by_changes = churn_by_changes.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== CHURN BY UPGRADE AND DOWNGRADE STATUS =====")
print(
    churn_by_changes.to_string(index=False)
)

# ============================================================
# STEP 10.18: CHURN EVENTS BY REASON
# ============================================================

churn_by_reason = (
    churn_events
    .groupby("reason_code")
    .agg(
        churn_events=("churn_event_id", "count"),
        total_refund=("refund_amount_usd", "sum"),
        avg_refund=("refund_amount_usd", "mean")
    )
    .reset_index()
)

churn_by_reason["event_percentage"] = (
    churn_by_reason["churn_events"]
    / churn_by_reason["churn_events"].sum()
    * 100
)

churn_by_reason["total_refund"] = (
    churn_by_reason["total_refund"].round(2)
)

churn_by_reason["avg_refund"] = (
    churn_by_reason["avg_refund"].round(2)
)

churn_by_reason["event_percentage"] = (
    churn_by_reason["event_percentage"].round(2)
)

churn_by_reason = churn_by_reason.sort_values(
    "churn_events",
    ascending=False
)

print("\n===== CHURN EVENTS BY REASON =====")
print(
    churn_by_reason.to_string(index=False)
)

# ============================================================
# STEP 10.19: CHURN EVENTS BY REACTIVATION STATUS
# ============================================================

churn_by_reactivation = (
    churn_events
    .groupby("is_reactivation")
    .agg(
        churn_events=("churn_event_id", "count"),
        total_refund=("refund_amount_usd", "sum"),
        avg_refund=("refund_amount_usd", "mean")
    )
    .reset_index()
)

churn_by_reactivation["event_percentage"] = (
    churn_by_reactivation["churn_events"]
    / churn_by_reactivation["churn_events"].sum()
    * 100
)

churn_by_reactivation["total_refund"] = (
    churn_by_reactivation["total_refund"].round(2)
)

churn_by_reactivation["avg_refund"] = (
    churn_by_reactivation["avg_refund"].round(2)
)

churn_by_reactivation["event_percentage"] = (
    churn_by_reactivation["event_percentage"].round(2)
)

churn_by_reactivation = churn_by_reactivation.sort_values(
    "churn_events",
    ascending=False
)

print("\n===== CHURN EVENTS BY REACTIVATION STATUS =====")
print(
    churn_by_reactivation.to_string(index=False)
)

# ============================================================
# STEP 10.20: CHURN EVENTS BY PRECEDING UPGRADE/DOWNGRADE
# ============================================================

churn_by_preceding_changes = (
    churn_events
    .groupby(
        ["preceding_upgrade_flag", "preceding_downgrade_flag"]
    )
    .agg(
        churn_events=("churn_event_id", "count"),
        total_refund=("refund_amount_usd", "sum"),
        avg_refund=("refund_amount_usd", "mean")
    )
    .reset_index()
)

churn_by_preceding_changes["event_percentage"] = (
    churn_by_preceding_changes["churn_events"]
    / churn_by_preceding_changes["churn_events"].sum()
    * 100
)

churn_by_preceding_changes["total_refund"] = (
    churn_by_preceding_changes["total_refund"].round(2)
)

churn_by_preceding_changes["avg_refund"] = (
    churn_by_preceding_changes["avg_refund"].round(2)
)

churn_by_preceding_changes["event_percentage"] = (
    churn_by_preceding_changes["event_percentage"].round(2)
)

churn_by_preceding_changes = churn_by_preceding_changes.sort_values(
    "churn_events",
    ascending=False
)

print("\n===== CHURN EVENTS BY PRECEDING UPGRADE/DOWNGRADE =====")
print(
    churn_by_preceding_changes.to_string(index=False)
)

# ============================================================
# STEP 10.21: ACCOUNT CHURN BY SUPPORT ESCALATION
# ============================================================

support_escalation_by_account = (
    support_tickets
    .groupby("account_id")
    .agg(
        total_tickets=("ticket_id", "count"),
        escalated_tickets=("escalation_flag", "sum")
    )
    .reset_index()
)

support_escalation_by_account["has_escalation"] = (
    support_escalation_by_account["escalated_tickets"] > 0
)

account_support_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    support_escalation_by_account[
        ["account_id", "has_escalation"]
    ],
    on="account_id",
    how="left"
)

account_support_churn["has_escalation"] = (
    account_support_churn["has_escalation"]
    .fillna(False)
)

churn_by_escalation = (
    account_support_churn
    .groupby("has_escalation")
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_escalation["non_churned_accounts"] = (
    churn_by_escalation["total_accounts"]
    - churn_by_escalation["churned_accounts"]
)

churn_by_escalation["churn_rate"] = (
    churn_by_escalation["churned_accounts"]
    / churn_by_escalation["total_accounts"]
    * 100
)

churn_by_escalation["churn_rate"] = (
    churn_by_escalation["churn_rate"].round(2)
)

churn_by_escalation = churn_by_escalation.sort_values(
    "churn_rate",
    ascending=False
)

print("\n===== ACCOUNT CHURN BY SUPPORT ESCALATION =====")
print(
    churn_by_escalation.to_string(index=False)
)

# ============================================================
# STEP 10.22: ACCOUNT CHURN BY NUMBER OF SUPPORT TICKETS
# ============================================================

support_ticket_count = (
    support_tickets
    .groupby("account_id")
    .agg(
        total_tickets=("ticket_id", "count")
    )
    .reset_index()
)

account_ticket_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    support_ticket_count,
    on="account_id",
    how="left"
)

account_ticket_churn["total_tickets"] = (
    account_ticket_churn["total_tickets"]
    .fillna(0)
    .astype(int)
)

account_ticket_churn["ticket_group"] = pd.cut(
    account_ticket_churn["total_tickets"],
    bins=[-1, 2, 4, 6, float("inf")],
    labels=["0-2", "3-4", "5-6", "7+"]
)

churn_by_ticket_group = (
    account_ticket_churn
    .groupby("ticket_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_ticket_group["non_churned_accounts"] = (
    churn_by_ticket_group["total_accounts"]
    - churn_by_ticket_group["churned_accounts"]
)

churn_by_ticket_group["churn_rate"] = (
    churn_by_ticket_group["churned_accounts"]
    / churn_by_ticket_group["total_accounts"]
    * 100
)

churn_by_ticket_group["churn_rate"] = (
    churn_by_ticket_group["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY NUMBER OF SUPPORT TICKETS =====")
print(
    churn_by_ticket_group.to_string(index=False)
)

# ============================================================
# STEP 10.23: ACCOUNT CHURN BY SUPPORT SATISFACTION
# ============================================================

support_satisfaction_by_account = (
    support_tickets
    .groupby("account_id")
    .agg(
        avg_satisfaction=("satisfaction_score", "mean")
    )
    .reset_index()
)

account_satisfaction_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    support_satisfaction_by_account,
    on="account_id",
    how="left"
)

account_satisfaction_churn["satisfaction_group"] = pd.cut(
    account_satisfaction_churn["avg_satisfaction"],
    bins=[-0.01, 2.99, 3.99, 5.00],
    labels=["1-2.99", "3-3.99", "4-5"]
)

churn_by_satisfaction = (
    account_satisfaction_churn
    .groupby("satisfaction_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_satisfaction["non_churned_accounts"] = (
    churn_by_satisfaction["total_accounts"]
    - churn_by_satisfaction["churned_accounts"]
)

churn_by_satisfaction["churn_rate"] = (
    churn_by_satisfaction["churned_accounts"]
    / churn_by_satisfaction["total_accounts"]
    * 100
)

churn_by_satisfaction["churn_rate"] = (
    churn_by_satisfaction["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY SUPPORT SATISFACTION =====")
print(
    churn_by_satisfaction.to_string(index=False)
)

# ============================================================
# STEP 10.24: ACCOUNT CHURN BY AVERAGE RESOLUTION TIME
# ============================================================

support_resolution_by_account = (
    support_tickets
    .groupby("account_id")
    .agg(
        avg_resolution_hours=("resolution_time_hours", "mean")
    )
    .reset_index()
)

account_resolution_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    support_resolution_by_account,
    on="account_id",
    how="left"
)

account_resolution_churn["resolution_group"] = pd.cut(
    account_resolution_churn["avg_resolution_hours"],
    bins=[-0.01, 24, 48, float("inf")],
    labels=["0-24 hours", "24-48 hours", "48+ hours"]
)

churn_by_resolution = (
    account_resolution_churn
    .groupby("resolution_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_resolution["non_churned_accounts"] = (
    churn_by_resolution["total_accounts"]
    - churn_by_resolution["churned_accounts"]
)

churn_by_resolution["churn_rate"] = (
    churn_by_resolution["churned_accounts"]
    / churn_by_resolution["total_accounts"]
    * 100
)

churn_by_resolution["churn_rate"] = (
    churn_by_resolution["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY AVERAGE RESOLUTION TIME =====")
print(
    churn_by_resolution.to_string(index=False)
)

# ============================================================
# STEP 10.25: ACCOUNT CHURN BY AVERAGE FIRST RESPONSE TIME
# ============================================================

support_response_by_account = (
    support_tickets
    .groupby("account_id")
    .agg(
        avg_first_response_minutes=(
            "first_response_time_minutes",
            "mean"
        )
    )
    .reset_index()
)

account_response_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    support_response_by_account,
    on="account_id",
    how="left"
)

account_response_churn["response_group"] = pd.cut(
    account_response_churn["avg_first_response_minutes"],
    bins=[-0.01, 60, 120, float("inf")],
    labels=["0-60 minutes", "60-120 minutes", "120+ minutes"]
)

churn_by_response = (
    account_response_churn
    .groupby("response_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_response["non_churned_accounts"] = (
    churn_by_response["total_accounts"]
    - churn_by_response["churned_accounts"]
)

churn_by_response["churn_rate"] = (
    churn_by_response["churned_accounts"]
    / churn_by_response["total_accounts"]
    * 100
)

churn_by_response["churn_rate"] = (
    churn_by_response["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY AVERAGE FIRST RESPONSE TIME =====")
print(
    churn_by_response.to_string(index=False)
)

# ============================================================
# STEP 10.26: ACCOUNT CHURN BY FEATURE USAGE
# ============================================================

usage_by_subscription = (
    feature_usage
    .groupby("subscription_id")
    .agg(
        total_usage_count=("usage_count", "sum")
    )
    .reset_index()
)

subscription_account_map = subscriptions[
    ["subscription_id", "account_id"]
].drop_duplicates()

usage_by_account = (
    usage_by_subscription
    .merge(
        subscription_account_map,
        on="subscription_id",
        how="left"
    )
    .groupby("account_id")
    .agg(
        total_usage_count=("total_usage_count", "sum")
    )
    .reset_index()
)

account_usage_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    usage_by_account,
    on="account_id",
    how="left"
)

account_usage_churn["total_usage_count"] = (
    account_usage_churn["total_usage_count"]
    .fillna(0)
)

account_usage_churn["usage_group"] = pd.qcut(
    account_usage_churn["total_usage_count"],
    q=4,
    duplicates="drop"
)

churn_by_usage = (
    account_usage_churn
    .groupby("usage_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_usage["non_churned_accounts"] = (
    churn_by_usage["total_accounts"]
    - churn_by_usage["churned_accounts"]
)

churn_by_usage["churn_rate"] = (
    churn_by_usage["churned_accounts"]
    / churn_by_usage["total_accounts"]
    * 100
)

churn_by_usage["churn_rate"] = (
    churn_by_usage["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY FEATURE USAGE =====")
print(
    churn_by_usage.to_string(index=False)
)

# ============================================================
# STEP 10.27: ACCOUNT CHURN BY FEATURE USAGE DURATION
# ============================================================

duration_by_subscription = (
    feature_usage
    .groupby("subscription_id")
    .agg(
        total_usage_duration_secs=(
            "usage_duration_secs",
            "sum"
        )
    )
    .reset_index()
)

duration_by_account = (
    duration_by_subscription
    .merge(
        subscription_account_map,
        on="subscription_id",
        how="left"
    )
    .groupby("account_id")
    .agg(
        total_usage_duration_secs=(
            "total_usage_duration_secs",
            "sum"
        )
    )
    .reset_index()
)

account_duration_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    duration_by_account,
    on="account_id",
    how="left"
)

account_duration_churn["total_usage_duration_secs"] = (
    account_duration_churn[
        "total_usage_duration_secs"
    ].fillna(0)
)

account_duration_churn["duration_group"] = pd.qcut(
    account_duration_churn["total_usage_duration_secs"],
    q=4,
    duplicates="drop"
)

churn_by_duration = (
    account_duration_churn
    .groupby("duration_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_duration["non_churned_accounts"] = (
    churn_by_duration["total_accounts"]
    - churn_by_duration["churned_accounts"]
)

churn_by_duration["churn_rate"] = (
    churn_by_duration["churned_accounts"]
    / churn_by_duration["total_accounts"]
    * 100
)

churn_by_duration["churn_rate"] = (
    churn_by_duration["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY FEATURE USAGE DURATION =====")
print(
    churn_by_duration.to_string(index=False)
)

# ============================================================
# STEP 10.28: ACCOUNT CHURN BY FEATURE USAGE ERRORS
# ============================================================

errors_by_subscription = (
    feature_usage
    .groupby("subscription_id")
    .agg(
        total_error_count=("error_count", "sum")
    )
    .reset_index()
)

errors_by_account = (
    errors_by_subscription
    .merge(
        subscription_account_map,
        on="subscription_id",
        how="left"
    )
    .groupby("account_id")
    .agg(
        total_error_count=("total_error_count", "sum")
    )
    .reset_index()
)

account_errors_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    errors_by_account,
    on="account_id",
    how="left"
)

account_errors_churn["total_error_count"] = (
    account_errors_churn["total_error_count"]
    .fillna(0)
)

account_errors_churn["error_group"] = pd.qcut(
    account_errors_churn["total_error_count"],
    q=4,
    duplicates="drop"
)

churn_by_errors = (
    account_errors_churn
    .groupby("error_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_errors["non_churned_accounts"] = (
    churn_by_errors["total_accounts"]
    - churn_by_errors["churned_accounts"]
)

churn_by_errors["churn_rate"] = (
    churn_by_errors["churned_accounts"]
    / churn_by_errors["total_accounts"]
    * 100
)

churn_by_errors["churn_rate"] = (
    churn_by_errors["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY FEATURE USAGE ERRORS =====")
print(
    churn_by_errors.to_string(index=False)
)

# ============================================================
# STEP 10.29: ACCOUNT CHURN BY NUMBER OF SUBSCRIPTIONS
# ============================================================

subscriptions_by_account = (
    subscriptions
    .groupby("account_id")
    .agg(
        subscription_count=("subscription_id", "count")
    )
    .reset_index()
)

account_subscription_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    subscriptions_by_account,
    on="account_id",
    how="left"
)

account_subscription_churn["subscription_count"] = (
    account_subscription_churn["subscription_count"]
    .fillna(0)
)

account_subscription_churn["subscription_group"] = pd.cut(
    account_subscription_churn["subscription_count"],
    bins=[-0.01, 5, 10, 15, float("inf")],
    labels=[
        "1-5 subscriptions",
        "6-10 subscriptions",
        "11-15 subscriptions",
        "16+ subscriptions"
    ]
)

churn_by_subscription_count = (
    account_subscription_churn
    .groupby("subscription_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_subscription_count["non_churned_accounts"] = (
    churn_by_subscription_count["total_accounts"]
    - churn_by_subscription_count["churned_accounts"]
)

churn_by_subscription_count["churn_rate"] = (
    churn_by_subscription_count["churned_accounts"]
    / churn_by_subscription_count["total_accounts"]
    * 100
)

churn_by_subscription_count["churn_rate"] = (
    churn_by_subscription_count["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY NUMBER OF SUBSCRIPTIONS =====")
print(
    churn_by_subscription_count.to_string(index=False)
)

# ============================================================
# STEP 10.30: ACCOUNT CHURN BY ACCOUNT SEAT COUNT
# ============================================================

account_seat_churn = accounts[
    ["account_id", "seats", "churn_flag"]
].copy()

account_seat_churn["seat_group"] = pd.cut(
    account_seat_churn["seats"],
    bins=[0, 10, 25, 50, float("inf")],
    labels=[
        "1-10 seats",
        "11-25 seats",
        "26-50 seats",
        "51+ seats"
    ]
)

churn_by_seats = (
    account_seat_churn
    .groupby("seat_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_seats["non_churned_accounts"] = (
    churn_by_seats["total_accounts"]
    - churn_by_seats["churned_accounts"]
)

churn_by_seats["churn_rate"] = (
    churn_by_seats["churned_accounts"]
    / churn_by_seats["total_accounts"]
    * 100
)

churn_by_seats["churn_rate"] = (
    churn_by_seats["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY ACCOUNT SEAT COUNT =====")
print(
    churn_by_seats.to_string(index=False)
)

# ============================================================
# STEP 10.31: ACCOUNT CHURN BY ACCOUNT MRR
# ============================================================

mrr_by_account = (
    subscriptions
    .groupby("account_id")
    .agg(
        total_mrr=("mrr_amount", "sum")
    )
    .reset_index()
)

account_mrr_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    mrr_by_account,
    on="account_id",
    how="left"
)

account_mrr_churn["total_mrr"] = (
    account_mrr_churn["total_mrr"].fillna(0)
)

account_mrr_churn["mrr_group"] = pd.qcut(
    account_mrr_churn["total_mrr"],
    q=4,
    duplicates="drop"
)

churn_by_mrr = (
    account_mrr_churn
    .groupby("mrr_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_mrr["non_churned_accounts"] = (
    churn_by_mrr["total_accounts"]
    - churn_by_mrr["churned_accounts"]
)

churn_by_mrr["churn_rate"] = (
    churn_by_mrr["churned_accounts"]
    / churn_by_mrr["total_accounts"]
    * 100
)

churn_by_mrr["churn_rate"] = (
    churn_by_mrr["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY ACCOUNT MRR =====")
print(
    churn_by_mrr.to_string(index=False)
)

# ============================================================
# STEP 10.32: ACCOUNT CHURN BY ACCOUNT ARR
# ============================================================

arr_by_account = (
    subscriptions
    .groupby("account_id")
    .agg(
        total_arr=("arr_amount", "sum")
    )
    .reset_index()
)

account_arr_churn = accounts[
    ["account_id", "churn_flag"]
].merge(
    arr_by_account,
    on="account_id",
    how="left"
)

account_arr_churn["total_arr"] = (
    account_arr_churn["total_arr"].fillna(0)
)

account_arr_churn["arr_group"] = pd.qcut(
    account_arr_churn["total_arr"],
    q=4,
    duplicates="drop"
)

churn_by_arr = (
    account_arr_churn
    .groupby("arr_group", observed=False)
    .agg(
        total_accounts=("account_id", "count"),
        churned_accounts=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_arr["non_churned_accounts"] = (
    churn_by_arr["total_accounts"]
    - churn_by_arr["churned_accounts"]
)

churn_by_arr["churn_rate"] = (
    churn_by_arr["churned_accounts"]
    / churn_by_arr["total_accounts"]
    * 100
)

churn_by_arr["churn_rate"] = (
    churn_by_arr["churn_rate"].round(2)
)

print("\n===== ACCOUNT CHURN BY ACCOUNT ARR =====")
print(
    churn_by_arr.to_string(index=False)
)

# ============================================================
# STEP 10.33: SUBSCRIPTION CHURN BY SUBSCRIPTION MRR
# ============================================================

subscription_mrr_churn = subscriptions[
    ["subscription_id", "mrr_amount", "churn_flag"]
].copy()

subscription_mrr_churn["mrr_group"] = pd.qcut(
    subscription_mrr_churn["mrr_amount"],
    q=4,
    duplicates="drop"
)

churn_by_subscription_mrr = (
    subscription_mrr_churn
    .groupby("mrr_group", observed=False)
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_subscription_mrr["non_churned_subscriptions"] = (
    churn_by_subscription_mrr["total_subscriptions"]
    - churn_by_subscription_mrr["churned_subscriptions"]
)

churn_by_subscription_mrr["churn_rate"] = (
    churn_by_subscription_mrr["churned_subscriptions"]
    / churn_by_subscription_mrr["total_subscriptions"]
    * 100
)

churn_by_subscription_mrr["churn_rate"] = (
    churn_by_subscription_mrr["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY SUBSCRIPTION MRR =====")
print(
    churn_by_subscription_mrr.to_string(index=False)
)

# ============================================================
# STEP 10.34: SUBSCRIPTION CHURN BY SUBSCRIPTION SEATS
# ============================================================

subscription_seat_churn = subscriptions[
    ["subscription_id", "seats", "churn_flag"]
].copy()

subscription_seat_churn["seat_group"] = pd.qcut(
    subscription_seat_churn["seats"],
    q=4,
    duplicates="drop"
)

churn_by_subscription_seats = (
    subscription_seat_churn
    .groupby("seat_group", observed=False)
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_subscription_seats["non_churned_subscriptions"] = (
    churn_by_subscription_seats["total_subscriptions"]
    - churn_by_subscription_seats["churned_subscriptions"]
)

churn_by_subscription_seats["churn_rate"] = (
    churn_by_subscription_seats["churned_subscriptions"]
    / churn_by_subscription_seats["total_subscriptions"]
    * 100
)

churn_by_subscription_seats["churn_rate"] = (
    churn_by_subscription_seats["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY SUBSCRIPTION SEATS =====")
print(
    churn_by_subscription_seats.to_string(index=False)
)

# ============================================================
# STEP 10.35: SUBSCRIPTION CHURN BY PLAN + TRIAL STATUS
# ============================================================

churn_by_plan_trial = (
    subscriptions
    .groupby(["plan_tier", "is_trial"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_trial["non_churned_subscriptions"] = (
    churn_by_plan_trial["total_subscriptions"]
    - churn_by_plan_trial["churned_subscriptions"]
)

churn_by_plan_trial["churn_rate"] = (
    churn_by_plan_trial["churned_subscriptions"]
    / churn_by_plan_trial["total_subscriptions"]
    * 100
)

churn_by_plan_trial["churn_rate"] = (
    churn_by_plan_trial["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + TRIAL STATUS =====")
print(
    churn_by_plan_trial.to_string(index=False)
)

# ============================================================
# STEP 10.36: SUBSCRIPTION CHURN BY PLAN + BILLING FREQUENCY
# ============================================================

churn_by_plan_billing = (
    subscriptions
    .groupby(["plan_tier", "billing_frequency"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_billing["non_churned_subscriptions"] = (
    churn_by_plan_billing["total_subscriptions"]
    - churn_by_plan_billing["churned_subscriptions"]
)

churn_by_plan_billing["churn_rate"] = (
    churn_by_plan_billing["churned_subscriptions"]
    / churn_by_plan_billing["total_subscriptions"]
    * 100
)

churn_by_plan_billing["churn_rate"] = (
    churn_by_plan_billing["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + BILLING FREQUENCY =====")
print(
    churn_by_plan_billing.to_string(index=False)
)
# ============================================================
# STEP 10.37: SUBSCRIPTION CHURN BY PLAN + AUTO-RENEW
# ============================================================

churn_by_plan_autorenew = (
    subscriptions
    .groupby(["plan_tier", "auto_renew_flag"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_autorenew["non_churned_subscriptions"] = (
    churn_by_plan_autorenew["total_subscriptions"]
    - churn_by_plan_autorenew["churned_subscriptions"]
)

churn_by_plan_autorenew["churn_rate"] = (
    churn_by_plan_autorenew["churned_subscriptions"]
    / churn_by_plan_autorenew["total_subscriptions"]
    * 100
)

churn_by_plan_autorenew["churn_rate"] = (
    churn_by_plan_autorenew["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + AUTO-RENEW =====")
print(
    churn_by_plan_autorenew.to_string(index=False)
)

# ============================================================
# STEP 10.38: SUBSCRIPTION CHURN BY PLAN + UPGRADE STATUS
# ============================================================

churn_by_plan_upgrade = (
    subscriptions
    .groupby(["plan_tier", "upgrade_flag"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_upgrade["non_churned_subscriptions"] = (
    churn_by_plan_upgrade["total_subscriptions"]
    - churn_by_plan_upgrade["churned_subscriptions"]
)

churn_by_plan_upgrade["churn_rate"] = (
    churn_by_plan_upgrade["churned_subscriptions"]
    / churn_by_plan_upgrade["total_subscriptions"]
    * 100
)

churn_by_plan_upgrade["churn_rate"] = (
    churn_by_plan_upgrade["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + UPGRADE STATUS =====")
print(
    churn_by_plan_upgrade.to_string(index=False)
)

# ============================================================
# STEP 10.39: SUBSCRIPTION CHURN BY PLAN + DOWNGRADE STATUS
# ============================================================

churn_by_plan_downgrade = (
    subscriptions
    .groupby(["plan_tier", "downgrade_flag"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_downgrade["non_churned_subscriptions"] = (
    churn_by_plan_downgrade["total_subscriptions"]
    - churn_by_plan_downgrade["churned_subscriptions"]
)

churn_by_plan_downgrade["churn_rate"] = (
    churn_by_plan_downgrade["churned_subscriptions"]
    / churn_by_plan_downgrade["total_subscriptions"]
    * 100
)

churn_by_plan_downgrade["churn_rate"] = (
    churn_by_plan_downgrade["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + DOWNGRADE STATUS =====")
print(
    churn_by_plan_downgrade.to_string(index=False)
)

# ============================================================
# STEP 10.40: SUBSCRIPTION CHURN BY PLAN + ACCOUNT INDUSTRY
# ============================================================

subscription_industry = subscriptions[
    [
        "subscription_id",
        "account_id",
        "plan_tier",
        "churn_flag"
    ]
].merge(
    accounts[
        ["account_id", "industry"]
    ],
    on="account_id",
    how="left"
)

churn_by_plan_industry = (
    subscription_industry
    .groupby(["industry", "plan_tier"])
    .agg(
        total_subscriptions=("subscription_id", "count"),
        churned_subscriptions=("churn_flag", "sum")
    )
    .reset_index()
)

churn_by_plan_industry["non_churned_subscriptions"] = (
    churn_by_plan_industry["total_subscriptions"]
    - churn_by_plan_industry["churned_subscriptions"]
)

churn_by_plan_industry["churn_rate"] = (
    churn_by_plan_industry["churned_subscriptions"]
    / churn_by_plan_industry["total_subscriptions"]
    * 100
)

churn_by_plan_industry["churn_rate"] = (
    churn_by_plan_industry["churn_rate"].round(2)
)

print("\n===== SUBSCRIPTION CHURN BY PLAN + ACCOUNT INDUSTRY =====")
print(
    churn_by_plan_industry.to_string(index=False)
)

# ============================================================
# PHASE 10 FINAL VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("PHASE 10 FINAL VALIDATION")
print("=" * 60)

validation = {
    "Total Accounts": len(accounts),
    "Account Churned": int(accounts["churn_flag"].sum()),
    "Account Churn Rate (%)": round(
        accounts["churn_flag"].mean() * 100, 2
    ),

    "Total Subscriptions": len(subscriptions),
    "Churned Subscriptions": int(subscriptions["churn_flag"].sum()),
    "Subscription Churn Rate (%)": round(
        subscriptions["churn_flag"].mean() * 100, 2
    ),

    "Total Churn Events": len(churn_events),
    "Reactivation Events": int(
        churn_events["is_reactivation"].sum()
    ),

    "Support Tickets": len(support_tickets),
    "Support Escalations": int(
        support_tickets["escalation_flag"].sum()
    ),

    "Feature Usage Records": len(feature_usage),

    "Total MRR": subscriptions["mrr_amount"].sum(),
    "Total ARR": subscriptions["arr_amount"].sum(),

    "Churned MRR": subscriptions.loc[
        subscriptions["churn_flag"] == True,
        "mrr_amount"
    ].sum()
}

for key, value in validation.items():
    print(f"{key}: {value}")

print("\n===== VALIDATION CHECKS =====")

print(
    "Accounts check:",
    "PASS" if len(accounts) == 500 else "FAIL"
)

print(
    "Subscriptions check:",
    "PASS" if len(subscriptions) == 5000 else "FAIL"
)

print(
    "Feature usage check:",
    "PASS" if len(feature_usage) == 25000 else "FAIL"
)

print(
    "Support tickets check:",
    "PASS" if len(support_tickets) == 2000 else "FAIL"
)

print(
    "Churn events check:",
    "PASS" if len(churn_events) == 600 else "FAIL"
)

print(
    "ARR = MRR × 12 check:",
    "PASS"
    if (subscriptions["arr_amount"] == subscriptions["mrr_amount"] * 12).all()
    else "FAIL"
)

print("=" * 60)
print("PHASE 10 VALIDATION COMPLETED")
print("=" * 60)