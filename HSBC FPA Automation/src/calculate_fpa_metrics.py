import pandas as pd

# Load cleaned financial data
df = pd.read_csv("data/processed/hsbc_financials_clean.csv")

# Convert data into dictionary
financials = dict(zip(df["Item"], df["Amount"]))

# Extract values
profit_after_tax = financials["Profit after tax"]
operating_income = financials["Total operating income"]
operating_expenses = financials["Operating expenses"]
total_assets = financials["Total assets"]
shareholders_equity = financials["Shareholders' equity"]

# Calculate FP&A ratios
roe = profit_after_tax / shareholders_equity
roa = profit_after_tax / total_assets
cost_to_income = operating_expenses / operating_income
equity_ratio = shareholders_equity / total_assets

# Create results dataframe
ratios_df = pd.DataFrame({
    "Ratio": [
        "Return on Equity (ROE)",
        "Return on Assets (ROA)",
        "Cost-to-Income Ratio",
        "Equity Ratio"
    ],
    "Value": [
        roe,
        roa,
        cost_to_income,
        equity_ratio
    ]
})

# Save results
ratios_df.to_csv(
    "output/hsbc_financial_ratios.csv",
    index=False
)

print("Financial ratios calculated and saved successfully.")
