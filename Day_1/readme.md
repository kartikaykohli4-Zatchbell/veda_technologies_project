# Veda Technology – Data Analytics Internship
### 🚀 Day 1: Data Cleaning & Preprocessing (Task 1)

**Intern Name:** Kartikay kohli
**Track:** Data Analytics Track  
**Dataset:** Sample Superstore Dataset  
**Task Level:** Level 1 · Day 1  

---

## 📌 1. Project Overview & Objectives
Raw datasets often suffer from integrity issues such as duplicate entries, malformed column names, trailing whitespaces, and unstandardized numeric precisions. The objective of Task 1 is to:
- Perform initial diagnostics using `df.info()`, `df.isnull().sum()`, and `df.duplicated()`.
- Systematically clean and preprocess the raw data into an analysis-ready format.
- Export both the sanitized dataset and an automated change log detailing every transformation.

---

## 🛠️ 2. Tech Stack & Environment
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, OpenPyXL
- **Version Control:** Git & GitHub
- **IDE / Environment:** VS Code / Terminal (Virtual Environment: `.venv`)

---

## 📂 3. Project Structure
```text
veda_technologies_projects/
│
├── .gitignore
├── requirements.txt
└── Day_1/
    ├── Dataset/
    │   └── SampleSuperstore/
    │       ├── SampleSuperstore.csv              # Raw dataset
    │       └── Cleaned_SampleSuperstore.csv      # Exported cleaned dataset
    ├── clean_superstore.py                       # Automated cleaning script
    ├── data_cleaning_changelog.txt               # Exported change log
    └── README.md                                 # Documentation & task write-up