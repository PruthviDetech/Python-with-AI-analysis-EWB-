"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
PASS_MARK = 40          # minimum marks required in EACH subject
MIN_ATTENDANCE = 75     # attendance (%) below this is flagged as shortage


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df, subjects=SUBJECTS):
    """Add Total and Average columns using NumPy (row-wise, axis=1)."""
    marks = df[subjects].to_numpy()
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average):
    """Grading rule based on the average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"


def get_result(row, subjects=SUBJECTS):
    """Pass only if the student scored at least PASS_MARK in every subject."""
    for subject in subjects:
        if row[subject] < PASS_MARK:
            return "Fail"
    return "Pass"


def add_grades_and_result(df):
    """Use loops to fill Result, Grade and Attendance_Status columns."""
    results, grades, att_status = [], [], []
    for _, row in df.iterrows():
        result = get_result(row)
        results.append(result)
        # A student who fails any subject gets grade F
        grades.append("F" if result == "Fail" else assign_grade(row["Average"]))
        att_status.append("Shortage" if row["Attendance"] < MIN_ATTENDANCE else "OK")
    df["Result"] = results
    df["Grade"] = grades
    df["Attendance_Status"] = att_status
    return df


def subject_analysis(df, subjects=SUBJECTS):
    """Highest, lowest, average and pass count for every subject."""
    rows = []
    for subject in subjects:
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Average": round(float(np.mean(col)), 2),
            "Passed": int(np.sum(col >= PASS_MARK)),
            "Failed": int(np.sum(col < PASS_MARK)),
        })
    return pd.DataFrame(rows)


def top_performers(df, n=3):
    """Return the top n students by average marks (only students who passed)."""
    passed = df[df["Result"] == "Pass"]
    return passed.sort_values("Average", ascending=False).head(n)


def department_analysis(df):
    """Average marks and pass count per department."""
    return df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Passed=("Result", lambda x: (x == "Pass").sum()),
    ).round(2)
