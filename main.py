"""Student Performance Analytics System - main program.

Run:  python main.py
"""

import numpy as np
import pandas as pd

import functions as fn

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)


def heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1 & 2: Load and inspect data
    df = fn.load_data("students.csv")

    heading("1. DATASET OVERVIEW")
    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")
    print(f"Columns           : {list(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum().to_string())

    # Step 3: Process data
    df = fn.calculate_total_and_average(df)
    df = fn.add_grades_and_result(df)

    heading("2. STUDENT REPORT (Total, Average, Grade, Result)")
    report_cols = ["Student_ID", "Name", "Department", "Total", "Average",
                   "Grade", "Result", "Attendance"]
    print(df[report_cols].to_string(index=False))

    # Step 4: Analysis
    heading("3. OVERALL PERFORMANCE")
    avg_all = df["Average"].to_numpy()
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    print(f"Overall class average : {np.mean(avg_all):.2f}")
    print(f"Highest average       : {best['Name']} ({best['Average']})")
    print(f"Lowest average        : {worst['Name']} ({worst['Average']})")

    heading("4. PASS / FAIL STATISTICS")
    passed = int((df["Result"] == "Pass").sum())
    failed = int((df["Result"] == "Fail").sum())
    total = len(df)
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")
    print(f"Pass percentage : {passed / total * 100:.2f}%")
    print("\nFailed students:")
    print(df[df["Result"] == "Fail"][["Student_ID", "Name", "Average"]].to_string(index=False))

    heading("5. GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())

    heading("6. SUBJECT-WISE ANALYSIS")
    subject_df = fn.subject_analysis(df)
    print(subject_df.to_string(index=False))
    best_subject = subject_df.loc[subject_df["Average"].idxmax()]
    weak_subject = subject_df.loc[subject_df["Average"].idxmin()]
    print(f"\nBest subject (highest average)  : {best_subject['Subject']} ({best_subject['Average']})")
    print(f"Weakest subject (lowest average): {weak_subject['Subject']} ({weak_subject['Average']})")

    heading("7. TOP 3 PERFORMERS")
    print(fn.top_performers(df, 3)[["Student_ID", "Name", "Department", "Average", "Grade"]]
          .to_string(index=False))

    heading("8. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string())

    heading("9. ATTENDANCE ANALYSIS")
    print(f"Average attendance : {df['Attendance'].mean():.2f}%")
    short = df[df["Attendance_Status"] == "Shortage"]
    print(f"Students with attendance below {fn.MIN_ATTENDANCE}% : {len(short)}")
    print(short[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    # Save the processed data
    df.to_csv("students_result.csv", index=False)
    print("\nProcessed data saved to students_result.csv")


if __name__ == "__main__":
    main()
