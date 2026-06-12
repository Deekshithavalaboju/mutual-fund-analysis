import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill NAV
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(nav.shape)
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(txn.shape)
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(txn.shape)
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(
    perf["expense_flag"].sum()
)
import shutil

files = [
"01_fund_master.csv",
"03_aum_by_fund_house.csv",
"04_monthly_sip_inflows.csv",
"05_category_inflows.csv",
"06_industry_folio_count.csv",
"09_portfolio_holdings.csv",
"10_benchmark_indices.csv"
]

for f in files:
    shutil.copy(
        f"data/raw/{f}",
        f"data/processed/{f}"
    )