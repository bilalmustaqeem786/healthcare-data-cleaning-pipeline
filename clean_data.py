"""Clean a messy clinical-style dataset (SYNTHETIC DEMO DATA).

Generates a small, deliberately messy synthetic dataset — NOT real
patients — and cleans it step by step:
  1. Remove exact duplicates
  2. Standardise category labels
  3. Fill missing numeric values with the median
  4. Clip impossible outliers (age > 110, systolic_bp > 250)

Prints a before/after QA summary.

For learning and portfolio demonstration only — not clinical or
medical advice.

Usage:
    python src/clean_data.py
"""

import numpy as np
import pandas as pd


def generate_messy_demo_data() -> pd.DataFrame:
    """SYNTHETIC DEMO DATA — invented for teaching; not real patients."""
    return pd.DataFrame(
        {
            "patient_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15],
            "age": [45, 62, np.nan, 34, 250, 58, 41, np.nan, 73, 29, 29, 51, 38, 66, 47, 55],
            "gender": [
                "Male", "female", "M", "Female", "male", "F", "Male", "Female",
                "female", "Male", "Male", "F", "M", "Female", "male", "Female",
            ],
            "diagnosis": [
                "Diabetes", "hypertension", "Diabetes", "DIABETES", "Hypertension",
                "diabetes", "Asthma", "asthma", "Hypertension", "Diabetes",
                "Diabetes", "ASTHMA", "hypertension", "Diabetes", "Asthma", "diabetes",
            ],
            "systolic_bp": [
                130, 145, 118, np.nan, 320, 152, 121, 138,
                160, 115, 115, 142, np.nan, 155, 128, 133,
            ],
        }
    )


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the four cleaning steps and return the cleaned DataFrame."""
    df = df.drop_duplicates().reset_index(drop=True)
    df["gender"] = (
        df["gender"].str.strip().str.lower().map(
            {"male": "Male", "m": "Male", "female": "Female", "f": "Female"}
        )
    )
    df["diagnosis"] = df["diagnosis"].str.strip().str.lower().str.title()
    for col in ["age", "systolic_bp"]:
        n_missing = int(df[col].isna().sum())
        df[col] = df[col].fillna(df[col].median())
        print(f"{col}: filled {n_missing} missing value(s) with median {df[col].median():.1f}")
    df["age"] = df["age"].clip(upper=110)
    df["systolic_bp"] = df["systolic_bp"].clip(upper=250)
    return df


def qa_summary(raw: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """Before/after comparison table."""
    return pd.DataFrame(
        {
            "Check": [
                "Rows",
                "Missing values (total)",
                "Exact duplicate rows",
                "Distinct gender labels",
                "Distinct diagnosis labels",
                "Max age",
                "Max systolic_bp",
            ],
            "Before": [
                len(raw),
                int(raw.isna().sum().sum()),
                int(raw.duplicated().sum()),
                raw["gender"].nunique(),
                raw["diagnosis"].nunique(),
                raw["age"].max(),
                raw["systolic_bp"].max(),
            ],
            "After": [
                len(df),
                int(df.isna().sum().sum()),
                int(df.duplicated().sum()),
                df["gender"].nunique(),
                df["diagnosis"].nunique(),
                df["age"].max(),
                df["systolic_bp"].max(),
            ],
        }
    )


def main() -> None:
    raw = generate_messy_demo_data()
    print("Raw shape:", raw.shape)
    print("\nMissing values per column:")
    print(raw.isna().sum())
    print("\nExact duplicate rows:", int(raw.duplicated().sum()))
    print("\nUnique gender labels:", sorted(raw["gender"].unique()))
    print("Unique diagnosis labels:", sorted(raw["diagnosis"].unique()))

    df = clean(raw)
    print("\nShape after cleaning:", df.shape)

    print("\nBefore / After QA Summary:")
    print(qa_summary(raw, df).to_string(index=False))
    print("\nCleaned dataset preview:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
