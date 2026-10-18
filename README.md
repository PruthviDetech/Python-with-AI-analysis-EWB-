# Student Performance Analytics System

A Python data-analysis project that reads student records from a CSV file and uses **NumPy** and **Pandas** to calculate totals, averages, grades, pass/fail status, subject-wise performance and top performers.

**Student:** Pruthvi Palve (Roll No. B-49)
**Course:** Python with AI, EWB Courses

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Runs the project and prints the final analysis |
| `functions.py` | Reusable calculation and processing functions |
| `students.csv` | Dataset with 20 student records |
| `students_result.csv` | Generated output with totals, averages, grades and results |
| `sample_output.txt` | Output of a sample run |
| `Project_Documentation.md` | Full project documentation |
| `requirements.txt` | Required libraries |

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Rules Used

- **Grade (by average):** A+ >= 90, A >= 80, B >= 70, C >= 60, D >= 50, E >= 40, F < 40
- **Pass/Fail:** a student passes only if they score at least 40 in every subject; otherwise Fail (grade F)
- **Attendance shortage:** attendance below 75%

## Features

- Load and inspect data with a Pandas DataFrame
- Total and average marks per student (NumPy)
- Grade and pass/fail assignment (loops, functions, conditions)
- Highest, lowest and class average
- Subject-wise analysis, department-wise analysis, attendance analysis
- Top 3 performers

See `Project_Documentation.md` for the detailed documentation and `sample_output.txt` for the results.
