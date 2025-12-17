import pandas as pd

# Load raw financial data
raw_df = pd.read_csv("data/extracted/hsbc_financials_raw.csv")

# Remove spaces and convert Amount column to numbers
raw_df["Amount"] = (
    raw_df["Amount"]
    .astype(str)
    .str.strip()
    .str.replace(",", "")
    .astype(float)
)

# Save cleaned data
raw_df.to_csv(
    "data/processed/hsbc_financials_clean.csv",
    index=False
)

print("Cleaned financial data saved successfully.")
