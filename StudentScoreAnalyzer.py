import numpy as np
import pandas as pd

data = {
    "name": ["Mahir Ahmed", "Mehedi Hasan", "Nabila Jaman", "Ashik Sarkar",
             "Samina Akter", "Rafiza Afroz", "Jabir Hossain"],
    "attendance": [9, 8, 10, 7, 6, 10, 8],
    "quiz": [13, 11, 14, 10, 8, 15, 4],
    "assignment": [30, 28, 33, 25, 22, 34, 26],
    "final": [35, 32, 36, 28, 25, 38, 30]
}

df = pd.DataFrame(data)

df["total"] = df["attendance"] + df["quiz"] + df["assignment"] + df["final"]

highest_score = np.max(df["total"])
lowest_score = np.min(df["total"])
average_score = np.mean(df["total"])

highest_student = df[df["total"] == highest_score]["name"].values[0]
lowest_student = df[df["total"] == lowest_score]["name"].values[0]

print("Highest Scorer:", highest_student, "-", highest_score, "marks")
print("Lowest Scorer:", lowest_student, "-", lowest_score, "marks")
print("Average:", average_score, "marks")
