import pandas as pd

# Load calculated ratios
df = pd.read_csv("output/hsbc_financial_ratios.csv")

# Convert ratios to percentage format
df["Value"] = df["Value"] * 100

# Export to Excel
output_path = "output/hsbc_fpna_ratios.xlsx"
df.to_excel(output_path, index=False)

print("FP&A Excel report created successfully.")
