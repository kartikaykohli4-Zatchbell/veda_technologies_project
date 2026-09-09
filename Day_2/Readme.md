# Day 2: Exploratory Data Analysis (EDA)

**Internship Track:** Data Analytics  
**Organization:** Veda Technology  
**Intern:** Kartikay kohli
**Dataset:** Sample Superstore Dataset  
**Task Level:** Level 1 · Day 2 of 45  

---

## 📌 Project Overview
Exploratory Data Analysis (EDA) builds the discipline of questioning data visually and statistically before drawing business conclusions. For Task 2, we analyzed relationships, detected distribution skews, isolated outliers, and evaluated profitability across multiple operational dimensions.

---

## 🛠️ Tools & Libraries
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Version Control:** Git & GitHub

---

## 📊 Summary Statistics & Visualizations

### 1. Correlation Heatmap (`plots/1_correlation_heatmap.png`)
- **Question Answered:** How do financial and transactional features correlate?
- **Observation:** Discount displays a noticeable negative correlation with profit (-0.22), confirming that aggressive discount strategies cannibalize profit margins.

### 2. Distribution of Key Metrics (`plots/2_distribution_histograms.png`)
- **Question Answered:** Are Sales and Profits normally distributed?
- **Observation:** Both Sales and Profit are severely right-skewed with high kurtosis, meaning most transactions are small purchases, while a few high-value enterprise sales dictate total revenue.

### 3. Profit Spread & Outliers by Sub-Category (`plots/3_sub_category_profit_boxplot.png`)
- **Question Answered:** Which sub-categories generate extreme loss-making outliers?
- **Observation:** **Tables**, **Bookcases**, and **Supplies** exhibit heavy negative outlier spikes, dragging down overall store performance despite acceptable top-line sales.

### 4. Discount Impact on Profitability (`plots/4_discount_vs_profit_trend.png`)
- **Question Answered:** At what threshold does a discount become destructive?
- **Observation:** Discounts from 0% to 20% remain profitable. Any discount exceeding 20% leads to steep average net losses per transaction.

### 5. Profit by Category and Region (`plots/5_profit_by_category_region.png`)
- **Question Answered:** Which regions and product categories drive bottom-line margin?
- **Observation:** **Technology** delivers the highest profit across all regions. The **Central** region performs poorest, generating negative returns on Furniture.

---

## 💡 Top 3 Strategic Insights
1. **The 20% Discount Trap:** Discounting above 20% erodes gross margin and leads to predictable losses. Discounting policies must be capped or tied to minimum basket values.
2. **Furniture Line Restructuring:** The Furniture segment (particularly Tables) produces regular loss-making transactions. Pricing and vendor contracts for these items need immediate review.
3. **Regional Prioritization:** The West and East regions represent high-margin strongholds for Technology and Office Supplies, whereas Central requires operational intervention to eliminate negative Furniture margins.

---

## 💡 Technical Interview Q&A

### Q1: How do you distinguish a genuine outlier from a data entry error?
- **Domain Sanity Checks:** Verify whether values exceed impossible physical or business thresholds (e.g., negative age, discount > 100%, sales < 0). Impossible values are data entry errors.
- **Contextual Triangulation:** If a transaction has an unusually high sales amount, verify if `Quantity` is also unusually high or if the item belongs to an expensive category (e.g., Copiers). If attributes align logically, it is a genuine outlier representing enterprise sales.
- **Frequency & Pattern:** Entry errors often show patterns like duplicated digits (e.g., typing `99999` or shifting decimal points by 100x).

### Q2: What's the difference between correlation and causation, and why does it matter in EDA?
- **Correlation:** Measures the statistical association or strength of linear co-movement between two variables (e.g., higher discounts correlate with lower profits).
- **Causation:** Proves that an action directly causes the observed outcome (e.g., giving a discount *caused* the customer to purchase).
- **Why it matters in EDA:** EDA discovers correlations and potential patterns, but mistaking correlation for causation can lead to disastrous business decisions (e.g., cutting all marketing spend because higher ad spend was correlated with a slower sales season caused by macroeconomic factors).

### Q3: Which chart type would you use to show a trend over 12 months, and why?
- **Recommended Chart:** A **Line Chart** (e.g., `sns.lineplot`).
- **Reasoning:** Line charts leverage spatial continuity along the horizontal axis, making temporal patterns, seasonality, peaks, and troughs immediately readable to human cognition compared to disconnected bar charts or scattered plots.