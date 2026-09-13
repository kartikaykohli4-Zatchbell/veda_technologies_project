# Day 6: Excel Formulas & Functions Fundamentals

**Internship Track:** Data Analytics Track 
**Organization:** Veda Technology  
**Intern:** Kartikay kohli
**Dataset:** Sample Superstore (`Cleaned_SampleSuperstore.csv` — 9,977 verified records)
**Deliverable File:** `Excel_Formulas_Fundamentals.xlsx`  
**Task Level:** Level 1 · Day 6 of 45 

---

## 📌 Project Overview
Task 6 builds practical fluency with core analytical formulas and functions used in everyday analytics and financial modeling. Working directly with retail transaction data, this project implements and evaluates modern exact-match lookups, multi-criteria conditional aggregations, dynamic text manipulation pipelines, and nested decision logic.

---

## 📂 Workbook Architecture & Implementation

The deliverable workbook `Excel_Formulas_Fundamentals.xlsx` is structured across three dedicated worksheets:

1. **`Sheet1` (Transactions Master Table):**
   - Contains the 9,977 cleaned records formatted as an official Excel Table (`Ctrl + T`)[cite: 1, 3].
   - **`Location_Code`:** Standardizes geographical identifiers using `=CONCAT(LEFT([@[state]], 1), ".", LEFT(TEXT([@[postal_code]], "00000"), 3))`.
   - **`Category_Prefix`:** Creates composite entity codes using `=CONCAT(LEFT([@[category]], 3), "-", LEFT([@[segment]], 3))`.
   - **`SubCat_Clean`:** Cleans whitespace and standardizes casing using `=PROPER(TRIM([@[sub_category]]))`.
   - **`Extracted_Keyword`:** Isolates secondary keywords using `=IF(ISNUMBER(SEARCH(" ", [@[sub_category]])), MID([@[sub_category]], SEARCH(" ", [@[sub_category]]) + 1, LEN([@[sub_category]])), [@[sub_category]])`.
   - **`Margin_Status`:** Segments transactions into operational health tiers using `=IF([@[profit]] < 0, "Loss Maker", IF([@[profit]] / [@[sales]] >= 0.20, "High Margin", "Standard Margin"))`.

2. **`Lookup_Reference_sheet` & `Lookup_Reference_sheet1` (Dimension Tables):**
   - **Table 1 (Regional Leadership):** Maps sales territories (`Central`, `East`, `South`, `West`) to Regional Directors (`Chris Johnson`, `Sarah Smith`, `David Vance`, `Anna Andreadi`).
   - **Table 2 (Category Benchmarks):** Maps product categories to target margins and fulfillment SLAs (`Furniture`: 10% / 5 Days, `Office Supplies`: 15% / 3 Days, `Technology`: 18% / 2 Days).

3. **`Formula_Lab` / `Formula_Summary` (Testing & Aggregation Lab):**
   - Houses the comparative lookup testing suite and multi-condition aggregation cards.

---

## 📊 Summary of Implemented Formulas & Evaluated Outputs

### 1. Lookup & Reference Methods
| Function Family | Formula Implemented | Evaluated Output | When to Use & Technical Notes |
| :--- | :--- | :--- | :--- |
| **XLOOKUP** | `=XLOOKUP("Central", Lookup_Reference_sheet!A2:A5, Lookup_Reference_sheet!B2:B5, "Not Found", 0)` | `Chris Johnson` | **Primary modern choice:** Decouples lookup and return vectors; immune to column additions/deletions; defaults to exact match without manual index numbers. |
| **VLOOKUP** | `=VLOOKUP("Central", Lookup_Reference_sheet!$A$2:$B$5, 2, FALSE)` | `Chris Johnson` | **Legacy compatibility:** Use when supporting older `.xls` workbooks. Requires lookup key to reside in the leftmost column and uses rigid column index numbers. |
| **INDEX / MATCH** | `=INDEX(Lookup_Reference_sheet1!$F$2:$F$4, MATCH("Technology", Lookup_Reference_sheet1!$D$2:$D$4, 0))` | `2 Days` | **Matrix lookups:** Best alternative when `XLOOKUP` is unavailable and retrieving data to the left of the key, or when resolving two-dimensional dynamic coordinates. |

---

### 2. Conditional Aggregations (Multi-Criteria `*IFS`)
| Metric Description | Formula Implemented | Evaluated Output | Analytical Business Objective |
| :--- | :--- | :--- | :--- |
| **Central Region Tech Sales** | `=SUMIFS('Sheet1'!$J$2:$J$10000, 'Sheet1'!$H$2:$H$10000, "Technology", 'Sheet1'!$G$2:$G$10000, "Central")` | **$45,399.82** | Isolates top-line revenue for high-margin catalog lines within the Central territory. |
| **East Region Furniture Profit** | `=SUMIFS('Sheet1'!$M$2:$M$10000, 'Sheet1'!$H$2:$H$10000, "Furniture", 'Sheet1'!$G$2:$G$10000, "East")` | **$3,078.20** | Audits net dollar conversion of Furniture sales in the East region[cite: 3]. |
| **Loss Orders with Discount $\ge$ 20%** | `=COUNTIFS('Sheet1'!$L$2:$L$10000, ">=0.2", 'Sheet1'!$M$2:$M$10000, "<0")` | **1,438 Orders** | Flags transaction frequency where aggressive promotional pricing destroyed profitability. |
| **Corporate Orders with Qty $\ge$ 5** | `=COUNTIFS('Sheet1'!$B$2:$B$10000, "Corporate", 'Sheet1'!$K$2:$K$10000, ">=5")` | **1,146 Orders** | Audits enterprise bulk-purchasing volumes for logistics planning. |
| **Avg Profit on Loss Orders** | `=AVERAGEIFS('Sheet1'!$M$2:$M$10000, 'Sheet1'!$M$2:$M$10000, "<0")` | **-$83.45** | Establishes the baseline capital drain per unprofitable order line item. |

---

## 🛡️ Edge-Case Testing & Formula Resilience

- **Text-vs-Number Mismatch:** Postal codes were handled as strings via `TEXT([@[postal_code]], "00000")` to preserve leading zeros and prevent `#VALUE!` coercion issues.
- **Delimiter Bounding:** String extraction formulas incorporate `ISNUMBER(SEARCH(" ", ...))` checks to ensure single-word strings do not trigger `#VALUE!` errors when delimiters are absent.
- **Array Dimension Alignment:** Fixed potential `#VALUE!` errors in `SUMIFS` by locking equal row boundaries across all criteria arrays (`$2:$10000`).
- **Calculated Column Decoupling:** Replaced table-level autofill constraints in the summary sheet with a standard cell range (`Convert to Range`) to support independent metrics per row.

---

## 💡 Technical Interview Q&A

### Q1: What's the difference between SUMIF and SUMIFS?
- **Argument Order & Structure:** In `SUMIF`, the `sum_range` is an optional trailing parameter (`=SUMIF(criteria_range, criterion, [sum_range])`). In `SUMIFS`, the `sum_range` is the mandatory first argument (`=SUMIFS(sum_range, criteria_range1, criterion1, ...)`).
- **Condition Capacity:** `SUMIF` can only evaluate a single criterion. `SUMIFS` can evaluate up to 127 range/criteria pairs simultaneously using boolean `AND` logic.
- **Best Practice:** Analysts prioritize `SUMIFS` even for single-condition queries to enforce formula syntax consistency and future-proof models against scope expansion.

### Q2: How does XLOOKUP improve on VLOOKUP?
- **Directional Flexibility:** `VLOOKUP` strictly requires the lookup key to be in the leftmost column. `XLOOKUP` decouples lookup and return arrays, enabling searches in any direction (left, right, vertical, horizontal).
- **Schema Drift Resilience:** `VLOOKUP` relies on hardcoded column indices (e.g., `2`). If a user inserts or removes a column, the formula breaks. `XLOOKUP` binds directly to explicit ranges or table column headers, maintaining integrity.
- **Match Default & Error Trapping:** `VLOOKUP` defaults to approximate match (`TRUE`), leading to silent errors if exact match (`FALSE`) is omitted. `XLOOKUP` defaults to exact match (`0`) and provides an integrated `[if_not_found]` argument, eliminating nested `=IFERROR()` functions.

### Q3: When would you use INDEX/MATCH instead of VLOOKUP?
- **Leftward Lookups:** When retrieving values from columns located to the left of the identifier in older Excel versions that lack `XLOOKUP`.
- **Two-Dimensional Matrix Lookups:** When both the row and column coordinates must be determined dynamically across a 2D table (`=INDEX(matrix, MATCH(row_key, row_range, 0), MATCH(col_key, col_range, 0))`).
- **Computation Efficiency:** On massive spreadsheets with tens of thousands of rows, `INDEX/MATCH` uses less memory and computes faster than full-table `VLOOKUP` calls because it processes only the designated search and return vectors.