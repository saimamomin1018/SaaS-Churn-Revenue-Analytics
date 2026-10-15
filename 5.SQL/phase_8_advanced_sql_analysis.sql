-- ============================================================
-- PHASE 8: ADVANCED SQL ANALYSIS
-- Project: SaaS Subscription, Customer Churn & Revenue Analytics
-- Database: saas_churn_analytics
-- ============================================================

-- Topics:
-- 1. Advanced JOINs
-- 2. Common Table Expressions (CTEs)
-- 3. Window Functions
-- 4. Ranking
-- 5. Running Totals
-- 6. Monthly Trend Analysis
-- 7. Month-over-Month Analysis
-- 8. Advanced Churn & Revenue Analysis


-- Step 8.2: Advanced JOIN Analysis
-- Account Plan vs Subscription Revenue

SELECT
    a.plan_tier AS account_plan,
    COUNT(DISTINCT a.account_id) AS account_count,
    COUNT(s.subscription_id) AS subscription_count,
    ROUND(SUM(s.mrr_amount), 2) AS total_mrr,
    ROUND(
        SUM(s.mrr_amount) / COUNT(DISTINCT a.account_id),
        2
    ) AS mrr_per_account
FROM accounts a
INNER JOIN subscriptions s
    ON a.account_id = s.account_id
GROUP BY a.plan_tier
ORDER BY total_mrr DESC;


-- Step 8.3: CTE Analysis
-- Top Accounts by Total MRR

WITH account_revenue AS (
    SELECT
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier,
        SUM(s.mrr_amount) AS total_mrr
    FROM accounts a
    INNER JOIN subscriptions s
        ON a.account_id = s.account_id
    GROUP BY
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier
)

SELECT
    account_id,
    account_name,
    industry,
    plan_tier,
    ROUND(total_mrr, 2) AS total_mrr
FROM account_revenue
ORDER BY total_mrr DESC
LIMIT 10;


-- Step 8.4: Window Function
-- Rank Accounts by Total MRR

WITH account_revenue AS (
    SELECT
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier,
        SUM(s.mrr_amount) AS total_mrr
    FROM accounts a
    INNER JOIN subscriptions s
        ON a.account_id = s.account_id
    GROUP BY
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier
)

SELECT
    account_id,
    account_name,
    industry,
    plan_tier,
    ROUND(total_mrr, 2) AS total_mrr,
    RANK() OVER (
        ORDER BY total_mrr DESC
    ) AS mrr_rank
FROM account_revenue
ORDER BY mrr_rank
LIMIT 10;


-- Step 8.5: Window Function
-- Rank Accounts by MRR Within Each Industry

WITH account_revenue AS (
    SELECT
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier,
        SUM(s.mrr_amount) AS total_mrr
    FROM accounts a
    INNER JOIN subscriptions s
        ON a.account_id = s.account_id
    GROUP BY
        a.account_id,
        a.account_name,
        a.industry,
        a.plan_tier
)

SELECT
    account_id,
    account_name,
    industry,
    plan_tier,
    ROUND(total_mrr, 2) AS total_mrr,
    RANK() OVER (
        PARTITION BY industry
        ORDER BY total_mrr DESC
    ) AS industry_mrr_rank
FROM account_revenue
ORDER BY
    industry,
    industry_mrr_rank;


-- Step 8.6: Running Total
-- Monthly MRR and Cumulative MRR

WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', start_date)::DATE AS revenue_month,
        SUM(mrr_amount) AS monthly_mrr
    FROM subscriptions
    GROUP BY DATE_TRUNC('month', start_date)
)

SELECT
    revenue_month,
    ROUND(monthly_mrr, 2) AS monthly_mrr,
    ROUND(
        SUM(monthly_mrr) OVER (
            ORDER BY revenue_month
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ),
        2
    ) AS cumulative_mrr
FROM monthly_revenue
ORDER BY revenue_month;


-- Step 8.7: Month-over-Month MRR Change

WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', start_date)::DATE AS revenue_month,
        SUM(mrr_amount) AS monthly_mrr
    FROM subscriptions
    GROUP BY DATE_TRUNC('month', start_date)
),

monthly_comparison AS (
    SELECT
        revenue_month,
        monthly_mrr,
        LAG(monthly_mrr) OVER (
            ORDER BY revenue_month
        ) AS previous_month_mrr
    FROM monthly_revenue
)

SELECT
    revenue_month,
    ROUND(monthly_mrr, 2) AS monthly_mrr,
    ROUND(previous_month_mrr, 2) AS previous_month_mrr,
    ROUND(
        monthly_mrr - previous_month_mrr,
        2
    ) AS mrr_change,
    ROUND(
        (monthly_mrr - previous_month_mrr)
        * 100.0
        / NULLIF(previous_month_mrr, 0),
        2
    ) AS mrr_change_percentage
FROM monthly_comparison
ORDER BY revenue_month;


-- Step 8.8: CTE-Based Churn Analysis
-- Subscription Churn Rate by Plan

WITH plan_churn AS (
    SELECT
        plan_tier,
        COUNT(*) AS total_subscriptions,
        COUNT(*) FILTER (
            WHERE churn_flag = TRUE
        ) AS churned_subscriptions
    FROM subscriptions
    GROUP BY plan_tier
),

overall AS (
    SELECT
        COUNT(*) AS total_subscriptions
    FROM subscriptions
)

SELECT
    p.plan_tier,
    p.total_subscriptions,
    p.churned_subscriptions,
    ROUND(
        p.churned_subscriptions * 100.0
        / p.total_subscriptions,
        2
    ) AS churn_rate,
    ROUND(
        p.total_subscriptions * 100.0
        / o.total_subscriptions,
        2
    ) AS subscription_share
FROM plan_churn p
CROSS JOIN overall o
ORDER BY churn_rate DESC;


-- Step 8.9: Advanced Account-Level Subscription Summary

SELECT
    a.account_id,
    a.account_name,
    a.industry,
    a.plan_tier,
    COUNT(s.subscription_id) AS subscription_count,
    COUNT(s.subscription_id) FILTER (
        WHERE s.churn_flag = TRUE
    ) AS churned_subscription_count,
    ROUND(SUM(s.mrr_amount), 2) AS total_mrr,
    ROUND(AVG(s.mrr_amount), 2) AS average_subscription_mrr
FROM accounts a
INNER JOIN subscriptions s
    ON a.account_id = s.account_id
GROUP BY
    a.account_id,
    a.account_name,
    a.industry,
    a.plan_tier
ORDER BY total_mrr DESC
LIMIT 20;


-- Step 8.10: Account-Level Churn and Revenue Impact

SELECT
    a.account_id,
    a.account_name,
    a.industry,
    a.plan_tier,
    COUNT(s.subscription_id) AS total_subscriptions,
    COUNT(s.subscription_id) FILTER (
        WHERE s.churn_flag = TRUE
    ) AS churned_subscriptions,
    ROUND(SUM(s.mrr_amount), 2) AS total_mrr,
    ROUND(
        SUM(s.mrr_amount) FILTER (
            WHERE s.churn_flag = TRUE
        ),
        2
    ) AS churned_mrr
FROM accounts a
INNER JOIN subscriptions s
    ON a.account_id = s.account_id
GROUP BY
    a.account_id,
    a.account_name,
    a.industry,
    a.plan_tier
HAVING COUNT(s.subscription_id) FILTER (
    WHERE s.churn_flag = TRUE
) > 0
ORDER BY churned_mrr DESC
LIMIT 20;


-- Step 8.11: Monthly Churned MRR Analysis

SELECT
    DATE_TRUNC('month', end_date)::DATE AS churn_month,
    COUNT(*) AS churned_subscriptions,
    ROUND(SUM(mrr_amount), 2) AS churned_mrr
FROM subscriptions
WHERE churn_flag = TRUE
  AND end_date IS NOT NULL
GROUP BY DATE_TRUNC('month', end_date)
ORDER BY churn_month;


-- Step 8.12: Final Advanced SQL Validation
SELECT
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (
        WHERE churn_flag = TRUE
    ) AS churned_subscriptions,
    COUNT(*) FILTER (
        WHERE churn_flag = FALSE
    ) AS active_subscriptions,
    ROUND(SUM(mrr_amount), 2) AS total_mrr,
    ROUND(
        SUM(mrr_amount) FILTER (
            WHERE churn_flag = TRUE
        ),
        2
    ) AS churned_mrr,
    ROUND(
        COUNT(*) FILTER (
            WHERE churn_flag = TRUE
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM subscriptions;


