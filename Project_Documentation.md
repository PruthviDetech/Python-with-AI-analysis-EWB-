# Project Documentation

## 1. Project Title
**Student Performance Analytics System**
Student: Pruthvi Palve | Roll No.: B-49 | Course: Python with AI (EWB Courses)

## 2. Objective
Teachers usually have marks in raw tables and need to calculate totals, grades and pass/fail results by hand. This project automates that. It reads student data, processes it with NumPy and Pandas, and produces clear results: marks summary, averages, grades, pass/fail statistics, subject-wise performance and top performers.

## 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (DataFrame, filtering, grouping)
- CSV file for data storage
- Git and GitHub for version control and submission

## 4. Dataset Description
`students.csv` contains **20 student records** and **9 columns**:

| Column | Description |
|--------|-------------|
| Student_ID | Unique ID (S001 to S020) |
| Name | Student name |
| Department | CSE, IT, ENTC or Mechanical |
| Maths, Physics, Chemistry, English, Computer_Science | Marks out of 100 |
| Attendance | Attendance percentage |

The dataset is a self-created sample with realistic values, including a few failing students and low-attendance students so that every part of the analysis has something to show.

## 5. Implementation
1. **Load data:** `load_data()` reads `students.csv` into a DataFrame. The program prints the shape, columns, first rows and missing values.
2. **Totals and averages:** `calculate_total_and_average()` converts the subject columns into a NumPy array and uses `np.sum(axis=1)` and `np.mean(axis=1)`.
3. **Grades and result:** `add_grades_and_result()` loops over every student. `get_result()` checks each subject against the pass mark of 40, and `assign_grade()` applies the grading rule.
4. **Analysis:** `subject_analysis()` uses `np.max`, `np.min`, `np.mean` and comparison counts per subject. `top_performers()` sorts passed students by average. `department_analysis()` uses `groupby`.
5. **Output:** `main.py` prints nine clearly labelled sections and saves the processed data to `students_result.csv`.

## 6. Key Features
- `load_data()`: reads the CSV
- `calculate_total_and_average()`: NumPy totals and averages
- `assign_grade()`: grading rule
- `get_result()`: pass/fail condition
- `add_grades_and_result()`: loop-based result, grade and attendance status
- `subject_analysis()`: highest, lowest, average, pass and fail per subject
- `top_performers()`: top n students
- `department_analysis()`: department-wise comparison

## 7. Output / Screenshots
Run `python main.py` and add screenshots of the terminal here (for example in a `screenshots/` folder). The full text output of a sample run is in `sample_output.txt`. Key results:

- Overall class average: **70.11**
- Highest average: **Sneha Kulkarni (93.2)**
- Lowest average: Rohan Gupta (42.0)
- Passed: **18**, Failed: **2** (pass percentage 90%)
- Best subject: **English (73.95)**; weakest: Chemistry (67.30)
- Top 3: Sneha Kulkarni, Aarav Sharma, Meera Iyer
- Average attendance: 83.35%; 4 students below 75%

## 8. Final Outcome
The project reads the dataset and produces a complete, readable performance report without anyone needing to inspect the code. All required features were implemented: totals, averages, grades, pass/fail, highest/lowest/average performance, subject-wise analysis and top performers, using functions, loops, NumPy and Pandas.

## 9. Challenges & Learning
- **Defining pass/fail:** an average alone can hide a failed subject. I used a per-subject pass mark of 40, so a student failing any subject gets grade F.
- **Using NumPy and Pandas together:** I learned to convert DataFrame columns with `.to_numpy()` for fast calculations and to use `axis=1` for row-wise results.
- **Testing:** I checked the printed results against manual calculations for a few students.
- **Learned:** structuring code into reusable functions, keeping the main file clean, and organising a project for GitHub.

## 10. GitHub Repository
https://github.com/PruthviDetech/Python-with-AI-analysis-analysis-EWB-

