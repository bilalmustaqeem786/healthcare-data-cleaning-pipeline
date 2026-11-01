# Healthcare Data Cleaning Pipeline

A step-by-step data cleaning pipeline for a messy clinical-style dataset. It measures the mess first, then fixes it in four documented steps — de-duplication, label standardisation, median imputation, and outlier clipping — and finishes with a before/after QA summary.

> **Note:** This project is for learning and portfolio demonstration only. It is **not** clinical or medical advice, and it uses **no real patient data**. All data is **SYNTHETIC DEMO DATA — NOT REAL PATIENTS**.

## Features

- Generates a small, deliberately messy synthetic dataset (duplicates, inconsistent labels, missing values, impossible outliers)
- Step 1: removes exact duplicate rows
- Step 2: standardises category labels (`Male`/`male`/`M` → `Male`; `DIABETES`/`diabetes` → `Diabetes`)
- Step 3: fills missing numeric values with the median (age → 51.0, systolic_bp → 138.0)
- Step 4: clips impossible outliers (age above 110, systolic blood pressure above 250)
- Before/after QA summary table for every check

## Tech Stack

- Python
- pandas, NumPy

## Results

| Check | Before | After |
| --- | ---: | ---: |
| Rows | 16 | 15 |
| Missing values (total) | 4 | 0 |
| Exact duplicate rows | 1 | 0 |
| Distinct gender labels | 6 | 2 |
| Distinct diagnosis labels | 8 | 3 |
| Max age | 250 | 110 |
| Max systolic_bp | 320 | 250 |

## Project Structure

```
healthcare-data-cleaning-pipeline/
├── src/
│   └── clean_data.py     # Generates the demo data, cleans it, prints the QA summary
├── notebooks/
│   └── 03_healthcare_data_cleaning_pipeline.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

## How to Run

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the cleaning pipeline
python src/clean_data.py
```

The script prints the raw-data diagnosis, each cleaning step, and the before/after QA summary.

## Dataset

**SYNTHETIC DEMO DATA — NOT REAL PATIENTS.** Every row is invented inside `src/clean_data.py` to demonstrate cleaning steps. No real patient record is used anywhere in this project. In real work, fixes like these would be validated against the source system and documented in a data dictionary — never applied silently.

## Author

**Bilal Ahmad — Healthcare Data Analyst**

- [LinkedIn](https://www.linkedin.com/in/bilal-ahmad-7ab444250)
- [Kaggle](https://www.kaggle.com/bilalmustaqeem)

## License

MIT — see [LICENSE](LICENSE).
