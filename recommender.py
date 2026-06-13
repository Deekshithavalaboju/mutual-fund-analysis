import pandas as pd

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

filtered = perf[
    perf["risk_category"]
    .str.lower()
    ==
    risk.lower()
]

top3 = filtered.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(
    top3[
        [
            "scheme_name",
            "sharpe_ratio",
            "risk_category"
        ]
    ]
)