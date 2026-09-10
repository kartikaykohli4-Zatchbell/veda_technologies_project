# Day 3: Simple Sales Dashboard Design (Power BI)

**Internship Track:** Data Analytics  
**Organization:** Veda Technology  
**Intern:** Kartikay kohli
**Tool Used:** Microsoft Power BI Desktop  
**Dataset:** Cleaned Sample Superstore  
**Deliverable File:** `Superstore_Sales_Dashboard.pbix`  

---

## 📌 Dashboard Overview
An executive dashboard designed to turn cleaned transactional data into actionable business intelligence. It provides high-level visibility into total sales, profitability margins, product sub-category drivers, and regional variations.

![Dashboard Preview](dashboard_screenshot.png)

---

## 🎯 Executive KPIs
- **Total Revenue:** $2,296,195.59
- **Total Profit:** $286,241.42
- **Profit Margin:** 12.47%
- **Units Sold:** 37,873 units

---

## 📄 One-Page User Guide: How to Read the Dashboard
1. **Executive KPI Ribbon:** Read from left to right across the top cards to assess total revenue velocity and confirm the net profit margin meets the 12% operational benchmark.
2. **Sub-Category Revenue (Bar Chart):** Ranks product lines by total sales volume. Hover to see individual profit contributions; watch for high sales lines that generate weak profit.
3. **Regional Comparison (Column Chart):** Directly compares gross sales against net profit across Central, East, South, and West territories.
4. **Segment Contribution (Donut Chart):** Displays customer demand distribution across Consumer (~50%), Corporate (~30%), and Home Office (~20%).
5. **Interactive Filtering:** Use the **Region** and **Category** slicer tiles to cross-filter the visuals dynamically.

---

## 💡 Technical Interview Q&A

### Q1: How do you decide which KPIs belong on a dashboard vs. in a detailed report?
- **Dashboard KPIs:** Real-time or high-level summary metrics (e.g., Total Sales, Net Margin %, Unit Volume) that instantly show whether business objectives are being met. If a stakeholder cannot take action or evaluate performance within 5 seconds of viewing, the metric does not belong on a dashboard.
- **Detailed Report KPIs:** Granular, diagnostic line-item data (e.g., individual SKU return rates, zip-code-level transit delay logs). These belong in detailed operational tables or paginated reports for root-cause analysis.

### Q2: What makes a dashboard 'interactive' rather than just a static chart?
- **Bidirectional Cross-Filtering:** Selecting an element (e.g., clicking 'Central' or 'Consumer') dynamically updates all related visuals and KPI cards across the canvas.
- **User Autonomy:** Slicers allow stakeholders to filter by time, territory, or product line without writing queries or asking the data team.
- **Contextual Tooltips & Drill-Downs:** Detailed transaction metrics are revealed on hover without cluttering the main screen.

### Q3: How would you design a dashboard differently for an executive vs. an operations manager?
- **For an Executive:** Focused on macro trends and strategic KPIs (Revenue, Net Profit Margin, YoY Growth). Layout is clean and uncluttered with minimal slicers and high-level visuals.
- **For an Operations Manager:** Focused on day-to-day tactical throughput, fulfillment cycle time, stock-out frequencies, and inventory bottlenecks. Layout features granular drill-downs, exception alerts, and table views for real-time triaging.