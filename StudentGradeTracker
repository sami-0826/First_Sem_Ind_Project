def get_performance(total):
    if total >= 80:
        return "Outstanding"
    elif total >= 75:
        return "Excellent"
    elif total >= 70:
        return "Very Good"
    elif total >= 69:
        return "Good"
    elif total >= 60:
        return "Satisfactory"
    elif total >= 55:
        return "Developing"
    elif total >= 50:
        return "Fair"
    elif total >= 45:
        return "Bellow Average"
    elif total >= 40:
        return "At risk"
    else:
        return "Need Improvement"

def calc_total(attendance, quiz, assignment, final):
    return attendance + quiz + assignment + final

name = input("Enter Student's Name: ")
attendance = int(input("Enter Your Attendance marks (Out of 10): "))
quiz = int(input("Enter Your Quiz Mark (Out of 15): "))
assignment = int(input("Enter Your Assignment marks (out of 35): "))
final = int(input("Enter Your Final Marks (Out of 40): "))

total = calc_total(attendance, quiz, assignment, final)
level = get_performance(total)

print("\n Student's Name: ", name)
print("\n Total Score: ", total)
print("\n Performance: ", level)
