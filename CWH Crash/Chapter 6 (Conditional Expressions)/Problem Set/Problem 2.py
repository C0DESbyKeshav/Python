# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks = []
sub = ["Physics", "Chemistry", "Maths"]

for i in range(0, 3):
    marks.append(int(input(f"Enter the marks obtained in {sub[i]}: ")))

# Let's assume that the target marks of each paper is 100
total_marks = 300

total_per = ((marks[0] + marks[1] + marks[2]) / total_marks) * 100

if (marks[0] > 100 or marks[1] > 100 or marks[2] > 100):
    print("You can't score marks more than the maximum 100 marks in a subject.")
elif (marks[0] >= 33 and marks[1] >= 33 and marks[2] >= 33):
    if (total_per >= 40):
        print("Omedetou!! You have passed the exam.")
    else:
        print("You passed in all the subjects individually but have FAILED in the exam overall.")
        print("Better Luck next time !!")
elif (marks[0] < 0 or marks[1] < 0 or marks[2] < 0):
    print("Marks cannot be negative.")
    print("Invalid marks")
elif (marks[0] < 33 and marks[1] < 33 and marks[2] < 33):
    print("You failed in all the subjects.")
    print("Better Luck next time !!")
elif (marks[0] < 33 and marks[1] < 33):
    print(f"You failed in both {sub[0]} and {sub[1]}")
    print("Better Luck next time !!")
elif (marks[1] < 33 and marks[2] < 33):
    print(f"You failed in both {sub[1]} and {sub[2]}")
    print("Better Luck next time !!")
elif (marks[0] < 33 and marks[2] < 33):
    print(f"You failed in both {sub[0]} and {sub[2]}")
    print("Better Luck next time !!")
elif (marks[0] < 33):
    print(f"You failed in {sub[0]} by {33-marks[0]} marks.")
    print("Better Luck next time !!")
elif (marks[1] < 33):
    print(f"You failed in {sub[1]} by {33-marks[1]} marks.")
    print("Better Luck next time !!")
elif (marks[2] < 33):
    print(f"You failed in {sub[2]} by {33-marks[2]} marks.")
    print("Better Luck next time !!")
