-- ============================================================
-- PHASE 6: SQL FUNDAMENTALS & BUSINESS ANALYSIS
-- Project: SaaS Subscription, Customer Churn & Revenue Analytics
-- Database: saas_churn_analytics
-- ============================================================

-- Topics:
-- 1. SELECT Statements
-- 2. Filtering with WHERE
-- 3. Sorting with ORDER BY
-- 4. GROUP BY Analysis
-- 5. Aggregate Functions
-- 6. JOIN Analysis
-- 7. Subscription Analysis
-- 8. Revenue Analysis
-- 9. Churn Analysis
-- 10. Support Analysis
-- 11. Feature Usage Analysis

-- Step 6.1 — Confirm PostgreSQL Database Connection
SELECT current_database();

-- Step 6.2 — Basic SELECT Query: View Accounts
SELECT * FROM accounts LIMIT 10;

-- Step 6.3 — Select Specific Columns
SELECT
    account_id,
    account_name,
    industry,
    country,
    plan_tier,
    seats,
    churn_flag
FROM accounts
LIMIT 10;

-- Step 6.4 — Count Total Accounts
SELECT COUNT(*) AS total_accounts
FROM accounts;

-- Step 6.5 — Count Total Subscriptions
SELECT COUNT(*) AS total_subscriptions
FROM subscriptions;

-- Step 6.6 — Accounts by Plan Tier 
SELECT
    plan_tier,
    COUNT(*) AS account_count
FROM accounts
GROUP BY plan_tier
ORDER BY account_count DESC;

-- Step 6.7 — Count Churned vs Non-Churned Accounts
SELECT
    churn_flag,
    COUNT(*) AS account_count
FROM accounts
GROUP BY churn_flag
ORDER BY churn_flag;

-- Step 6.8 — Total MRR and ARR
SELECT
    SUM(mrr_amount) AS total_mrr,
    SUM(arr_amount) AS total_arr
FROM subscriptions;

-- Step 6.9 — Subscription Count by Plan Tier
SELECT
    plan_tier,
    COUNT(*) AS subscription_count
FROM subscriptions
GROUP BY plan_tier
ORDER BY subscription_count DESC;

-- Step 6.10 — MRR by Plan Tier 
SELECT
    plan_tier,
    SUM(mrr_amount) AS total_mrr
FROM subscriptions
GROUP BY plan_tier
ORDER BY total_mrr DESC;

-- Step 6.11 — Churned Subscriptions by Plan Tier 
SELECT
    plan_tier,
    COUNT(*) AS churned_subscriptions
FROM subscriptions
WHERE churn_flag = TRUE
GROUP BY plan_tier
ORDER BY churned_subscriptions DESC;

-- Step 6.12 — Churn Rate by Plan Tier 
SELECT
    plan_tier,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),2
    ) AS churn_rate_percent
FROM subscriptions
GROUP BY plan_tier 
ORDER BY churn_rate_percent DESC;

-- Step 6.13 — Revenue by Billing Frequency 
SELECT
    billing_frequency,
    COUNT(*) AS subscription_count,
    SUM(mrr_amount) AS total_mrr
FROM subscriptions
GROUP BY billing_frequency
ORDER BY total_mrr DESC;

-- Step 6.14 — Subscription Status 
SELECT
    churn_flag,
    COUNT(*) AS subscription_count,
    SUM(mrr_amount) AS total_mrr
FROM subscriptions
GROUP BY churn_flag
ORDER BY churn_flag;

-- Step 6.15 — Average MRR by Plan Tier 
SELECT
    plan_tier,
    COUNT(*) AS subscription_count,
    ROUND(AVG(mrr_amount), 2) AS average_mrr
FROM subscriptions
GROUP BY plan_tier
ORDER BY average_mrr DESC;

-- Step 6.16 — Churned Subscriptions by Billing Frequency 
SELECT
    billing_frequency,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),2
) AS churn_rate_percent
FROM subscriptions
GROUP BY billing_frequency
ORDER BY churn_rate_percent DESC;

-- Step 6.17 — Churn Events by Reason 
SELECT
    reason_code,
    COUNT(*) AS churn_event_count
FROM churn_events
GROUP BY reason_code
ORDER BY churn_event_count DESC;

-- Step 6.18 — Churn Events by Reason with Percentage 
SELECT
    reason_code,
    COUNT(*) AS churn_event_count,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(),2
    ) AS percentage_of_events
FROM churn_events
GROUP BY reason_code
ORDER BY churn_event_count DESC;

-- Step 6.19 — Support Tickets by Priority
SELECT
    priority,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY priority
ORDER BY ticket_count DESC;

-- Step 6.20 — Average Support Resolution Time by Priority 
SELECT
    priority,
    COUNT(*) AS ticket_count,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY priority
ORDER BY avg_resolution_hours DESC;

-- Step 6.21 — Average Customer Satisfaction by Priority 
SELECT
    priority,
    COUNT(satisfaction_score) AS rated_tickets,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM support_tickets
GROUP BY priority
ORDER BY avg_satisfaction DESC;

-- Step 6.22 — Feature Usage by Feature 
SELECT
    feature_name,
    SUM(usage_count) AS total_usage
FROM feature_usage
GROUP BY feature_name
ORDER BY total_usage DESC
LIMIT 10;

-- Step 6.23 — Subscription Counts by Trial Status 
SELECT
    is_trial,
    COUNT(*) AS subscription_count
FROM subscriptions
GROUP BY is_trial
ORDER BY is_trial;

-- Step 6.24 — Churn Rate by Trial Status 
SELECT
    is_trial,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),2
    ) AS churn_rate_percent
FROM subscriptions
GROUP BY is_trial
ORDER BY churn_rate_percent DESC;

-- Step 6.25 — Upgrade and Downgrade Activity 
SELECT
    COUNT(*) FILTER (WHERE upgrade_flag = TRUE) AS upgraded_subscriptions,
    COUNT(*) FILTER (WHERE downgrade_flag = TRUE) AS downgraded_subscriptions
FROM subscriptions;

-- Step 6.26 — Churn Events with Previous Upgrade/Downgrade 
SELECT
    COUNT(*) FILTER (WHERE preceding_upgrade_flag = TRUE) AS preceded_by_upgrade,
    COUNT(*) FILTER (WHERE preceding_downgrade_flag = TRUE) AS preceded_by_downgrade
FROM churn_events;

-- Step 6.27 — Reactivation Events 
SELECT
    is_reactivation,
    COUNT(*) AS churn_event_count
FROM churn_events
GROUP BY is_reactivation
ORDER BY is_reactivation;

-- Step 6.28 — Churn Events by Reason and Reactivation Status 
SELECT
    reason_code,
    is_reactivation,
    COUNT(*) AS churn_event_count
FROM churn_events
GROUP BY reason_code, is_reactivation
ORDER BY reason_code, is_reactivation;

-- Step 6.29 — Final SQL Validation
SELECT
    (SELECT COUNT(*) FROM accounts) AS accounts,
    (SELECT COUNT(*) FROM subscriptions) AS subscriptions,
    (SELECT COUNT(*) FROM feature_usage) AS feature_usage_rows,
    (SELECT COUNT(*) FROM support_tickets) AS support_tickets,
    (SELECT COUNT(*) FROM churn_events) AS churn_events;
	