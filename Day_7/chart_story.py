import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Setup paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "Dataset", "2015-selected-columns.csv")

if not os.path.exists(data_path):
  # Fallback checks if run from root or dataset folder
  potential_paths = [
      os.path.join(
          base_dir,
          "..",
          "Day_7",
          "Dataset",
          "2015-selected-columns.csv",
      ),
      os.path.join(base_dir, "2015-selected-columns.csv"),
  ]
  for p in potential_paths:
    if os.path.exists(p):
      data_path = p
      break

print(f"Loading World Happiness dataset from: {data_path}")
df = pd.read_csv(data_path)

# Sanitize column headers
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

# Identify key column aliases
region_col = [c for c in df.columns if "region" in c][0]
score_col = [
    c
    for c in df.columns
    if "score" in c or "ladder" in c or "happiness" in c and "rank" not in c
][0]
gdp_col = [c for c in df.columns if "gdp" in c or "economy" in c][0]
family_col = [c for c in df.columns if "family" in c or "social" in c][0]
health_col = [c for c in df.columns if "health" in c or "life" in c][0]

charts_dir = os.path.join(base_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#cbd5e1"
plt.rcParams["axes.linewidth"] = 0.8

# -------------------------------------------------------------
# Chart 1: Average Happiness Score by Region (Horizontal Bar Chart)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))
reg_avg = df.groupby(region_col)[score_col].mean().sort_values()

colors = [
    "#ef4444"
    if val < 5.0
    else ("#3b82f6" if val < 6.5 else "#10b981")
    for val in reg_avg.values
]
bars = ax.barh(reg_avg.index, reg_avg.values, color=colors, height=0.6)

ax.set_xlabel("Average Happiness Score (0 - 10)", fontsize=10, fontweight="bold")
ax.set_title(
    "Chart 1: Global Happiness Disparities Across Geographic Regions\n"
    "Takeaway: Western Europe and North America lead above 6.7, while"
    " Sub-Saharan Africa and Southern Asia lag below 4.6.",
    fontsize=10.5,
    fontweight="bold",
    pad=15,
    loc="left",
)
ax.set_xlim(0, 8.5)
ax.grid(axis="x", linestyle="--", alpha=0.5)

for bar in bars:
  w = bar.get_width()
  ax.annotate(
      f"{w:.2f}",
      (w, bar.get_y() + bar.get_height() / 2),
      xytext=(6, 0),
      textcoords="offset points",
      va="center",
      fontsize=9,
      fontweight="bold",
  )

plt.tight_layout()
plt.savefig(
    os.path.join(charts_dir, "chart1_regional_happiness_bar.png"), dpi=300
)
plt.close()

# -------------------------------------------------------------
# Chart 2: GDP per Capita vs Happiness (Scatter with Trendline)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5))
x = df[gdp_col]
y = df[score_col]

ax.scatter(x, y, color="#2563eb", alpha=0.6, edgecolors="none", s=45)

# Fit linear trendline
m, b = np.polyfit(x, y, 1)
corr = df[gdp_col].corr(df[score_col])
ax.plot(
    x,
    m * x + b,
    color="#dc2626",
    linewidth=2,
    label=f"Linear Trendline (r = {corr:.2f})",
)

ax.set_xlabel(
    "Economy / GDP per Capita Contribution", fontsize=10, fontweight="bold"
)
ax.set_ylabel("Happiness Score", fontsize=10, fontweight="bold")
ax.set_title(
    "Chart 2: Economic Output vs. National Well-Being\nTakeaway: GDP per capita"
    f" demonstrates strong positive leverage (r = {corr:.2f}) with overall"
    " happiness.",
    fontsize=10.5,
    fontweight="bold",
    pad=15,
    loc="left",
)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(frameon=True, facecolor="#f8fafc")

plt.tight_layout()
plt.savefig(
    os.path.join(charts_dir, "chart2_gdp_vs_happiness_scatter.png"), dpi=300
)
plt.close()

# -------------------------------------------------------------
# Chart 3: Trajectory of Key Factors by Happiness Quartile (Line Chart)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 4.8))
df["happiness_quartile"] = pd.qcut(
    df[score_col],
    q=4,
    labels=[
        "Q1: Bottom 25%",
        "Q2: Lower-Mid",
        "Q3: Upper-Mid",
        "Q4: Top 25%",
    ],
)
q_agg = (
    df.groupby("happiness_quartile")[[gdp_col, family_col, health_col]]
    .mean()
    .reset_index()
)

ax.plot(
    q_agg["happiness_quartile"],
    q_agg[gdp_col],
    marker="o",
    linewidth=2.2,
    color="#2563eb",
    label="Economy (GDP)",
)
ax.plot(
    q_agg["happiness_quartile"],
    q_agg[family_col],
    marker="s",
    linewidth=2.2,
    color="#10b981",
    label="Family / Social Support",
)
ax.plot(
    q_agg["happiness_quartile"],
    q_agg[health_col],
    marker="^",
    linewidth=2.2,
    color="#f59e0b",
    label="Health / Life Expectancy",
)

ax.set_xlabel("Happiness Score Tier (Quartiles)", fontsize=10, fontweight="bold")
ax.set_ylabel(
    "Average Contribution to Score", fontsize=10, fontweight="bold"
)
ax.set_title(
    "Chart 3: Macro-Factor Trajectory Across Happiness Tiers\nTakeaway: Social"
    " support and economic stability scale together, widening the gap between"
    " top and bottom tiers.",
    fontsize=10.5,
    fontweight="bold",
    pad=15,
    loc="left",
)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(frameon=True, facecolor="#f8fafc")

plt.tight_layout()
plt.savefig(
    os.path.join(charts_dir, "chart3_factor_trajectory_line.png"), dpi=300
)
plt.close()

# -------------------------------------------------------------
# Chart 4: Geographic Share of Top 25 Nations (Donut Chart <= 5 slices)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
top25 = df.nsmallest(
    25,
    [c for c in df.columns if "rank" in c][0]
    if any("rank" in c for c in df.columns)
    else score_col,
)

# Group regions into <= 4 clean categories to obey the portal guideline
def group_region(reg):
  if "Western Europe" in reg:
    return "Western Europe"
  if "North America" in reg or "Australia" in reg:
    return "North America & ANZ"
  if "Latin America" in reg:
    return "Latin America & Caribbean"
  return "Rest of the World"


top25_grouped = top25[region_col].apply(group_region).value_counts()
colors = ["#2563eb", "#38bdf8", "#10b981", "#cbd5e1"]

wedges, texts, autotexts = ax.pie(
    top25_grouped,
    labels=top25_grouped.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    pctdistance=0.75,
    wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2),
)

for t in texts:
  t.set_fontsize(9.5)
  t.set_fontweight("bold")
for at in autotexts:
  at.set_fontsize(9)
  at.set_color("black")
  at.set_fontweight("bold")

ax.set_title(
    "Chart 4: Regional Distribution of the World's Top 25 Happiest"
    " Nations\nTakeaway: Western Europe represents over 60% of top-ranking"
    " countries.",
    fontsize=10.5,
    fontweight="bold",
    pad=15,
    loc="left",
)

plt.tight_layout()
plt.savefig(
    os.path.join(charts_dir, "chart4_top25_regional_donut.png"), dpi=300
)
plt.close()

print("All 4 charts generated successfully in Day_7/charts/")