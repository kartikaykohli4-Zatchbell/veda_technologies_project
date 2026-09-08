import os
import numpy as np
import pandas as pd

# ==========================================
# 1. SETUP DYNAMIC PATHS
# ==========================================
# base_dir points to: ...\veda_technoglogies_project\Day_1
base_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(
    base_dir, "Dataset", "SampleSuperstore", "SampleSuperstore.csv"
)
output_path = os.path.join(
    base_dir, "Dataset", "SampleSuperstore", "Cleaned_SampleSuperstore.csv"
)
log_path = os.path.join(base_dir, "data_cleaning_changelog.txt")

change_log = []

# ==========================================
# 2. LOAD RAW DATASET
# ==========================================
print(f"Loading raw data from: {input_path}")
if not os.path.exists(input_path):
  raise FileNotFoundError(
      f"Could not locate the file at {input_path}. Please verify the path."
  )

df = pd.read_csv(input_path)

# ==========================================
# 3. INITIAL AUDIT & INVENTORY CHECKS
# ==========================================
print("\n--- Initial Audit ---")
print(f"Initial Shape: {df.shape} (rows, columns)")
print("Missing values per column:\n", df.isnull().sum())
duplicates_count = df.duplicated().sum()
print(f"Duplicate rows identified: {duplicates_count}")

# ==========================================
# 4. RESOLUTION: REMOVE DUPLICATE ROWS
# ==========================================
if duplicates_count > 0:
  df = df.drop_duplicates()
  change_log.append(
      f"Removed {duplicates_count} identical duplicate rows to prevent skewed aggregate sales/profit metrics."
  )
else:
  change_log.append("Checked for duplicate rows: No duplicates found.")

# ==========================================
# 5. RESOLUTION: STANDARDIZE COLUMN HEADERS
# ==========================================
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)
change_log.append(
    "Standardized column headers to lowercase snake_case (e.g., 'Ship Mode' ->"
    " 'ship_mode')."
)

# ==========================================
# 6. RESOLUTION: SANITIZE CATEGORICAL STRINGS
# ==========================================
text_cols = df.select_dtypes(include=["object"]).columns
for col in text_cols:
  df[col] = df[col].astype(str).str.strip()
change_log.append(
    "Trimmed leading and trailing whitespace across all string/categorical fields."
)

# ==========================================
# 7. RESOLUTION: FORMAT DATA TYPES & METRICS
# ==========================================
# Format postal code as 5-digit zero-padded string to preserve leading zeros
if "postal_code" in df.columns:
  df["postal_code"] = (
      df["postal_code"].fillna(0).astype(int).astype(str).str.zfill(5)
  )
  change_log.append(
      "Converted 'postal_code' to zero-padded 5-digit string format (e.g., preserving leading zeros)."
  )

# Round monetary and percentage metrics for consistent reporting
for num_col in ["sales", "profit", "discount"]:
  if num_col in df.columns:
    df[num_col] = df[num_col].round(2)
change_log.append(
    "Standardized financial metrics ('sales', 'profit', 'discount') to 2 decimal places."
)

# ==========================================
# 8. POST-CLEANING VALIDATION
# ==========================================
print("\n--- Post-Cleaning Validation ---")
print(f"Cleaned Dataset Shape: {df.shape}")
print(f"Remaining Missing Values: {df.isnull().sum().sum()}")
assert (
    df.duplicated().sum() == 0
), "Validation Error: Duplicate records still exist!"
assert df.isnull().sum().sum() == 0, "Validation Error: Null values detected!"
print("Validation Successful: 0 duplicates and 0 unhandled nulls.")

# ==========================================
# 9. EXPORT CLEANED DATASET & CHANGE LOG
# ==========================================
# Ensure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Export cleaned CSV
df.to_csv(output_path, index=False)

# Export Change Log
with open(log_path, "w", encoding="utf-8") as f:
  f.write("VEDA TECHNOLOGY DATA ANALYTICS INTERNSHIP - DAY 1\n")
  f.write("Task: Data Cleaning & Preprocessing\n")
  f.write("Dataset: Sample Superstore\n")
  f.write("=" * 60 + "\n\n")
  for entry in change_log:
    f.write(f"- {entry}\n")

print("\n--- Process Finished ---")
print(f"Cleaned dataset exported to: {output_path}")
print(f"Change log exported to:       {log_path}")