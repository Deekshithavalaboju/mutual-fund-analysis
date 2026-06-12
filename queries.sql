-- Top 5 funds by AUM
SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Expense ratio below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Transactions by state
SELECT
state,
COUNT(*) total_txn
FROM fact_transactions
GROUP BY state;

-- Average NAV
SELECT
AVG(nav)
FROM fact_nav;

-- Total SIP transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Sip';