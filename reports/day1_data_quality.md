# Day 1 Data Quality Summary

## Data Ingestion Status

Successfully loaded and profiled 10 datasets.

## Dataset Overview

| Dataset | Rows | Columns |
|----------|------|---------|
| fund_master | 40 | 15 |
| nav_history | 46000 | 3 |
| aum_by_fund_house | 90 | 5 |
| monthly_sip_inflows | 48 | 6 |
| category_inflows | 144 | 3 |
| industry_folio_count | 21 | 6 |
| scheme_performance | 40 | 19 |
| investor_transactions | 32778 | 13 |
| portfolio_holdings | 322 | 8 |
| benchmark_indices | 8050 | 3 |

## Missing Values Analysis

Only one column contains missing values:

Dataset:
monthly_sip_inflows

Column:
yoy_growth_pct

Missing Values:
12

Reason:
Year-over-Year growth cannot be calculated for the first 12 months of data.

All remaining datasets contain zero missing values.

## Fund Master Exploration

Unique Fund Houses: 10

Categories:
- Equity
- Debt

Sub Categories:
- Large Cap
- Mid Cap
- Small Cap
- Flexi Cap
- ELSS
- Index
- Index ETF
- Liquid
- Gilt
- Short Duration
- Value
- Large & Mid Cap

Risk Categories:
- Low
- Moderate
- Moderately High
- High
- Very High

## AMFI Code Validation

Fund Master Codes: 40

NAV History Codes: 40

Missing Codes: 0

Result:
All AMFI scheme codes from fund_master are present in nav_history.

## Conclusion

Data quality is excellent.
No critical data quality issues found.
AMFI mapping validation passed successfully.
Datasets are ready for EDA and analytics.
