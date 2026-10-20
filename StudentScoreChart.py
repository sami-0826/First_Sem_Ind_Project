import matplotlib.pyplot as plt

names = ["Mahir Ahmed", "Mehedi Hasan", "Nabila Jaman", "Ashik Sarkar",
         "Samina Akter", "Rafia Afroz", "Jabir Hossain"]

attendance = [9, 8, 10, 7, 6, 10, 8]
quiz = [13, 11, 14, 10, 8, 15, 11]
assignment = [30, 20, 33, 25, 22, 34, 26]
final = [35, 32, 36, 28, 25, 38, 30]

total = [attendance[i] + quiz[i] + assignment[i] + final[i] for i in range(len(names))]

plt.bar(names, total)
plt.title("Students Total Scores")
plt.xlabel("Student Name")
plt.ylabel("Total Score")
plt.xticks(rotation=90)
plt.show()

print("Students who may need academic support: ")

for i in range(len(names)):
    if total[i] < 65:
        print(names[i], "-", total[i], "marks")
