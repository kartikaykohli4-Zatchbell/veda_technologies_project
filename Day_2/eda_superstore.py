import os 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sns


sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)


# Setup directories
base_dir = os.path.dirname(os.path.abspath(__file__))
# Loading the cleaned dataset from Day 1
data_path = os.path.join(
    base_dir,
    "..",
    "Day_1",
    "Dataset",
    "SampleSuperstore",
    "Cleaned_SampleSuperstore.csv",
)

if not os.path.exists(data_path):
  # Fallback to local raw if path differs
  data_path = os.path.join(
      base_dir,
      "..",
      "Day_1",
      "Dataset",
      "SampleSuperstore",
      "SampleSuperstore.csv",
  )

plots_dir = os.path.join(base_dir, "plots")
os.makedirs(plots_dir, exist_ok=True)

print(f"Loading data from: {data_path}")
df = pd.read_csv(data_path)

# Ensure snake_case headers
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ==========================================
# 1. SUMMARY STATISTICS & CORRELATION
# ==========================================
print("\n--- Numerical Summary Statistics (.describe()) ---")
print(df.describe())

numeric_cols = df.select_dtypes(include=[np.number]).columns

# ==========================================
# CHART 1: Correlation Heatmap
# Question: How do Sales, Discount, Profit, and Quantity correlate?
# ==========================================
plt.figure(figsize=(8, 6))
corr = df[numeric_cols].corr()
sns.heatmap(
    corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, vmin=-1, vmax=1
)
plt.title(
    "1. Correlation Heatmap (Sales, Discount, Profit, Quantity)",
    fontsize=14,
    pad=12,
)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "1_correlation_heatmap.png"), dpi=300)
plt.close()
print("Saved Chart 1: Correlation Heatmap")

# ==========================================
# CHART 2: Sales & Profit Distribution (Histograms/KDE)
# Question: Are Sales and Profits normally distributed or heavily skewed?
# ==========================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(
    df["sales"],
    bins=40,
    kde=True,
    ax=axes[0],
    color="#2b5c8f",
    log_scale=(True, False),
)
axes[0].set_title("Sales Distribution (Log Scaled X-axis)")
axes[0].set_xlabel("Sales ($)")

sns.histplot(df["profit"], bins=50, kde=True, ax=axes[1], color="#2a9d8f")
axes[1].set_title("Profit Distribution")
axes[1].set_xlabel("Profit ($)")
axes[1].set_xlim(-1000, 1500)  # Zoom in on main distribution
plt.suptitle(
    "2. Distribution of Key Monetary Metrics", fontsize=14, y=1.02
)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "2_distribution_histograms.png"), dpi=300)
plt.close()
print("Saved Chart 2: Distribution Histograms")

# ==========================================
# CHART 3: Profitability Across Sub-Categories (Boxplot for Outliers)
# Question: Which sub-categories suffer extreme negative profit outliers?
# ==========================================
plt.figure(figsize=(14, 7))
sns.boxplot(
    data=df,
    x="sub_category",
    y="profit",
    palette="Set2",
    showfliers=True,
    hue="sub_category",
    legend=False,
)
plt.axhline(0, color="red", linestyle="--", linewidth=1.2, alpha=0.7)
plt.xticks(rotation=45, ha="right")
plt.title(
    "3. Profit Spread & Outliers by Sub-Category", fontsize=14, pad=12
)
plt.xlabel("Sub-Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "3_sub_category_profit_boxplot.png"), dpi=300)
plt.close()
print("Saved Chart 3: Sub-Category Boxplot")

# ==========================================
# CHART 4: Discount vs. Profit Relationship
# Question: Does giving larger discounts destroy margins?
# ==========================================
discount_perf = (
    df.groupby("discount")
    .agg(avg_profit=("profit", "mean"), total_orders=("sales", "count"))
    .reset_index()
)

plt.figure(figsize=(10, 5))
sns.lineplot(
    data=discount_perf,
    x="discount",
    y="avg_profit",
    marker="o",
    color="#e76f51",
    linewidth=2.5,
)
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.title(
    "4. Impact of Discount Levels on Average Profitability",
    fontsize=14,
    pad=12,
)
plt.xlabel("Discount Rate")
plt.ylabel("Average Profit ($)")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "4_discount_vs_profit_trend.png"), dpi=300)
plt.close()
print("Saved Chart 4: Discount vs Profit Analysis")

# ==========================================
# CHART 5: Total Sales and Profit by Category & Region
# Question: Which region and product category drives the highest profitability?
# ==========================================
cat_reg = (
    df.groupby(["category", "region"])[["sales", "profit"]]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=cat_reg,
    x="category",
    y="profit",
    hue="region",
    palette="Blues_d",
    edgecolor="black",
)
plt.title("5. Net Profit by Category and Region", fontsize=14, pad=12)
plt.xlabel("Category")
plt.ylabel("Cumulative Profit ($)")
plt.legend(title="Region")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "5_profit_by_category_region.png"), dpi=300)
plt.close()
print("Saved Chart 5: Category & Region Barplot")

# ==========================================
# TOP 3 INSIGHTS SUMMARY
# ==========================================
print("\n" + "=" * 50)
print("TOP 3 STRATEGIC INSIGHTS")
print("=" * 50)
print(
    "1. Heavy Discounts Directly Erode Profits: Any discount greater than 20%"
    " consistently shifts average profit margins into negative territory,"
    " despite driving sales volume."
)
print(
    "2. Sub-Category Risk in Furniture (Tables & Bookcases): Tables and"
    " Bookcases generate severe negative profit outliers and high cumulative"
    " losses due to excessive discount dependencies."
)
print(
    "3. Regional Discrepancies: The West and East regions yield the highest"
    " profit conversions, whereas the Central region struggles with lower"
    " margins in Furniture and Office Supplies."
)
print("=" * 50)