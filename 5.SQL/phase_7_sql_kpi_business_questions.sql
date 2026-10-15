-- ============================================================
-- PHASE 7: SQL KPI & BUSINESS QUESTIONS
-- Project: SaaS Subscription, Customer Churn & Revenue Analytics
-- Database: saas_churn_analytics
-- ============================================================

-- Topics:
-- 1. Overall Subscription Churn Rate
-- 2. Churned MRR
-- 3. Revenue Contribution by Plan
-- 4. Churn Rate & Churned MRR by Plan
-- 5. MRR per Account
-- 6. Account Churn by Industry
-- 7. Account Churn by Country
-- 8. Account Churn by Referral Source
-- 9. Churn by Upgrade Status
-- 10. Churn by Downgrade Status
-- 11. Churn by Auto-Renew Status
-- 12. Support Satisfaction by Escalation
-- 13. Support Resolution Time by Escalation
-- 14. Churn Events & Refund Analysis
-- 15. Churn Events by Year
-- 16. Churn Events by Reactivation
-- 17. Churn Events by Upgrade/Downgrade
-- 18. Monthly Churn Events
-- 19. Final Validation


-- KPI 1: Overall Subscription Churn Rate
SELECT
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS overall_churn_rate_percent
FROM subscriptions;

-- KPI 2: Churned MRR
SELECT
    SUM(mrr_amount) AS total_mrr,
    SUM(mrr_amount) FILTER (WHERE churn_flag = TRUE) AS churned_mrr,
    ROUND(
        SUM(mrr_amount) FILTER (WHERE churn_flag = TRUE) * 100.0
        / SUM(mrr_amount),
        2
    ) AS churned_mrr_percent
FROM subscriptions;

-- KPI 3: Revenue Contribution by Subscription Plan
SELECT
    plan_tier,
    SUM(mrr_amount) AS plan_mrr,
    ROUND(
        SUM(mrr_amount) * 100.0 / SUM(SUM(mrr_amount)) OVER (),
        2
    ) AS mrr_contribution_percent
FROM subscriptions
GROUP BY plan_tier
ORDER BY plan_mrr DESC;

-- KPI 4: Churn Rate and Churned MRR by Subscription Plan
SELECT
    plan_tier,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent,
    SUM(mrr_amount) FILTER (WHERE churn_flag = TRUE) AS churned_mrr
FROM subscriptions
GROUP BY plan_tier
ORDER BY churned_mrr DESC;

-- Business Question 5: MRR per Account by Account Plan
SELECT
    a.plan_tier,
    COUNT(DISTINCT a.account_id) AS account_count,
    SUM(s.mrr_amount) AS total_mrr,
    ROUND(
        SUM(s.mrr_amount) / COUNT(DISTINCT a.account_id),
        2
    ) AS mrr_per_account
FROM accounts a
JOIN subscriptions s
    ON a.account_id = s.account_id
GROUP BY a.plan_tier
ORDER BY mrr_per_account DESC;

-- Business Question 6: Account-Level Churn by Industry
SELECT
    industry,
    COUNT(*) AS total_accounts,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_accounts,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM accounts
GROUP BY industry
ORDER BY churn_rate_percent DESC;

-- Business Question 7: Account-Level Churn by Country
SELECT
    country,
    COUNT(*) AS total_accounts,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_accounts,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM accounts
GROUP BY country
ORDER BY churn_rate_percent DESC;

-- Business Question 8: Account-Level Churn by Referral Source
SELECT
    referral_source,
    COUNT(*) AS total_accounts,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_accounts,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM accounts
GROUP BY referral_source
ORDER BY churn_rate_percent DESC;

-- Business Question 9: Churn Rate by Upgrade Status
SELECT
    upgrade_flag,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM subscriptions
GROUP BY upgrade_flag
ORDER BY upgrade_flag;

-- Business Question 10: Churn Rate by Downgrade Status
SELECT
    downgrade_flag,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM subscriptions
GROUP BY downgrade_flag
ORDER BY downgrade_flag;

-- Business Question 11: Churn Rate by Auto-Renew Status
SELECT
    auto_renew_flag,
    COUNT(*) AS total_subscriptions,
    COUNT(*) FILTER (WHERE churn_flag = TRUE) AS churned_subscriptions,
    ROUND(
        COUNT(*) FILTER (WHERE churn_flag = TRUE) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percent
FROM subscriptions
GROUP BY auto_renew_flag
ORDER BY auto_renew_flag;

-- Business Question 12: Support Satisfaction by Escalation Status
SELECT
    escalation_flag,
    COUNT(*) AS ticket_count,
    COUNT(satisfaction_score) AS rated_tickets,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM support_tickets
GROUP BY escalation_flag
ORDER BY escalation_flag;

-- Business Question 13: Average Support Resolution Time by Escalation
SELECT
    escalation_flag,
    COUNT(*) AS ticket_count,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY escalation_flag
ORDER BY escalation_flag;

-- Business Question 14: Churn Events by Reason and Refund Amount
SELECT
    reason_code,
    COUNT(*) AS churn_event_count,
    ROUND(SUM(refund_amount_usd), 2) AS total_refund_usd,
    ROUND(AVG(refund_amount_usd), 2) AS avg_refund_usd
FROM churn_events
GROUP BY reason_code
ORDER BY total_refund_usd DESC;

-- Business Question 15: Churn Events by Year
SELECT
    EXTRACT(YEAR FROM churn_date) AS churn_year,
    COUNT(*) AS churn_event_count,
    ROUND(SUM(refund_amount_usd), 2) AS total_refund_usd
FROM churn_events
GROUP BY EXTRACT(YEAR FROM churn_date)
ORDER BY churn_year;

-- Business Question 16: Churn Events by Reactivation Status
SELECT
    is_reactivation,
    COUNT(*) AS churn_event_count,
    ROUND(SUM(refund_amount_usd), 2) AS total_refund_usd
FROM churn_events
GROUP BY is_reactivation
ORDER BY is_reactivation;

-- Business Question 17: Churn Events by Preceding Upgrade/Downgrade
SELECT
    preceding_upgrade_flag,
    preceding_downgrade_flag,
    COUNT(*) AS churn_event_count,
    ROUND(SUM(refund_amount_usd), 2) AS total_refund_usd
FROM churn_events
GROUP BY
    preceding_upgrade_flag,
    preceding_downgrade_flag
ORDER BY
    preceding_upgrade_flag,
    preceding_downgrade_flag;

-- Business Question 18: Monthly Churn Events
SELECT
    DATE_TRUNC('month', churn_date)::DATE AS churn_month,
    COUNT(*) AS churn_event_count,
    ROUND(SUM(refund_amount_usd), 2) AS total_refund_usd
FROM churn_events
GROUP BY DATE_TRUNC('month', churn_date)
ORDER BY churn_month;

-- Phase 7 Final Validation: Table Row Counts
SELECT 'accounts' AS table_name, COUNT(*) AS row_count
FROM accounts
UNION ALL
SELECT 'subscriptions', COUNT(*)
FROM subscriptions
UNION ALL
SELECT 'feature_usage', COUNT(*)
FROM feature_usage
UNION ALL
SELECT 'support_tickets', COUNT(*)
FROM support_tickets
UNION ALL
SELECT 'churn_events', COUNT(*)
FROM churn_events
ORDER BY table_name;
