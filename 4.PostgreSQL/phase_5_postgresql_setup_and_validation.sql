-- ============================================================
-- PHASE 5: POSTGRESQL DATABASE SETUP & DATA LOADING
-- Project: SaaS Subscription, Customer Churn & Revenue Analytics
-- Database: saas_churn_analytics
-- ============================================================

-- Topics:
-- 1. Database Creation
-- 2. Table Creation
-- 3. Primary Keys
-- 4. Foreign Keys
-- 5. Data Loading
-- 6. Data Validation
-- 7. Relationship Validation
-- 8. Revenue & Subscription Validation


-- STEP 5.4: CREATE ACCOUNTS TABLE
CREATE TABLE accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    account_name VARCHAR(150),
    industry VARCHAR(50),
    country VARCHAR(10),
    signup_date DATE,
    referral_source VARCHAR(50),
    plan_tier VARCHAR(30),
    seats INTEGER,
    is_trial BOOLEAN,
    churn_flag BOOLEAN
);

-- STEP 5.5: CREATE SUBSCRIPTIONS TABLE
CREATE TABLE subscriptions (
    subscription_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20) NOT NULL,
    start_date DATE,
    end_date DATE,
    plan_tier VARCHAR(30),
    seats INTEGER,
    mrr_amount NUMERIC(12,2),
    arr_amount NUMERIC(14,2),
    is_trial BOOLEAN,
    upgrade_flag BOOLEAN,
    downgrade_flag BOOLEAN,
    churn_flag BOOLEAN,
    billing_frequency VARCHAR(20),
    auto_renew_flag BOOLEAN,
    CONSTRAINT fk_subscriptions_account
        FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)
);

-- STEP 5.6: CREATE FEATURE_USAGE TABLE
CREATE TABLE feature_usage (
    usage_id VARCHAR(20),
    subscription_id VARCHAR(20) NOT NULL,
    usage_date DATE,
    feature_name VARCHAR(100),
    usage_count INTEGER,
    usage_duration_secs INTEGER,
    error_count INTEGER,
    is_beta_feature BOOLEAN,
    CONSTRAINT fk_feature_usage_subscription
        FOREIGN KEY (subscription_id)
        REFERENCES subscriptions(subscription_id)
);

-- STEP 5.7: CREATE SUPPORT_TICKETS TABLE
CREATE TABLE support_tickets (
    ticket_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20) NOT NULL,
    submitted_at TIMESTAMP,
    closed_at TIMESTAMP,
    resolution_time_hours NUMERIC(8,2),
    priority VARCHAR(20),
    first_response_time_minutes NUMERIC(8,2),
    satisfaction_score NUMERIC(4,2),
    escalation_flag BOOLEAN,
    CONSTRAINT fk_support_tickets_account
        FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)
);

-- STEP 5.8: CREATE CHURN_EVENTS TABLE
CREATE TABLE churn_events (
    churn_event_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20) NOT NULL,
    churn_date DATE,
    reason_code VARCHAR(50),
    refund_amount_usd NUMERIC(12,2),
    preceding_upgrade_flag BOOLEAN,
    preceding_downgrade_flag BOOLEAN,
    is_reactivation BOOLEAN,
    feedback_text TEXT,
    CONSTRAINT fk_churn_events_account
        FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)
);


-- STEP 5.9: VALIDATE ACCOUNTS ROW COUNT
SELECT COUNT(*) AS total_accounts FROM accounts;

-- STEP 5.10: VALIDATE SUBSCRIPTIONS ROW COUNT
SELECT COUNT(*) AS total_subscriptions FROM subscriptions;

-- STEP 5.11: VALIDATE FEATURE USAGE ROW COUNT
SELECT COUNT(*) AS total_feature_usage FROM feature_usage;

-- STEP 5.12: VALIDATE SUPPORT TICKETS ROW COUNT
SELECT COUNT(*) AS total_support_tickets FROM support_tickets;

-- STEP 5.13: VALIDATE CHURN EVENTS ROW COUNT
SELECT COUNT(*) AS total_churn_events FROM churn_events;


-- STEP 5.14: VALIDATE SUBSCRIPTIONS -> ACCOUNTS
SELECT COUNT(*) AS orphan_subscriptions
FROM subscriptions s
LEFT JOIN accounts a ON s.account_id = a.account_id
WHERE a.account_id IS NULL;

-- STEP 5.15: VALIDATE FEATURE_USAGE -> SUBSCRIPTIONS
SELECT COUNT(*) AS orphan_feature_usage
FROM feature_usage f
LEFT JOIN subscriptions s ON f.subscription_id = s.subscription_id
WHERE s.subscription_id IS NULL;

-- STEP 5.16: VALIDATE SUPPORT_TICKETS -> ACCOUNTS
SELECT COUNT(*) AS orphan_support_tickets
FROM support_tickets st
LEFT JOIN accounts a ON st.account_id = a.account_id
WHERE a.account_id IS NULL;

-- STEP 5.17: VALIDATE CHURN_EVENTS -> ACCOUNTS
SELECT COUNT(*) AS orphan_churn_events
FROM churn_events ce
LEFT JOIN accounts a ON ce.account_id = a.account_id
WHERE a.account_id IS NULL;


-- STEP 5.18: VALIDATE ARR = MRR * 12
SELECT COUNT(*) AS arr_mismatch_count
FROM subscriptions
WHERE arr_amount <> (mrr_amount * 12);

-- STEP 5.19: VALIDATE SUBSCRIPTION CHURN STATUS
SELECT
    COUNT(*) FILTER (WHERE churn_flag = TRUE AND end_date IS NULL) AS churned_missing_end_date,
    COUNT(*) FILTER (WHERE churn_flag = FALSE AND end_date IS NOT NULL) AS active_with_end_date
FROM subscriptions;

-- STEP 5.20: VALIDATE SUPPORT TICKET TIMING
SELECT COUNT(*) AS invalid_support_timing
FROM support_tickets
WHERE closed_at < submitted_at;


-- FINAL DATABASE ROW COUNT VALIDATION
SELECT 'accounts' AS table_name, COUNT(*) AS row_count FROM accounts
UNION ALL
SELECT 'subscriptions', COUNT(*) FROM subscriptions
UNION ALL
SELECT 'feature_usage', COUNT(*) FROM feature_usage
UNION ALL
SELECT 'support_tickets', COUNT(*) FROM support_tickets
UNION ALL
SELECT 'churn_events', COUNT(*) FROM churn_events
ORDER BY table_name;
