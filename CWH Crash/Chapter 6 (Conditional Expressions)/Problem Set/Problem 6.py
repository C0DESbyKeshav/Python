'''Write a program to calculate the grade of a student from his marks from the following scheme:
91 - 100 => Excellent
81 - 90 => A
71 - 80 => B
61 - 70 => C
50 - 60 => D
<50 => Fail'''

marks = int(input("Enter your marks: "))

if ((marks < 0) or (marks > 100)):
    print("Please Enter valid marks")
elif ((marks > 90) and (marks <= 100)):
    print("Excellent !! Subharashi !! Anata wa atamagaii desu ka ?!!")
elif ((marks > 80) and (marks <= 90)):
    print("Your passed with grade 'A'")
elif ((marks > 70) and (marks <= 80)):
    print("Your passed with grade 'B'")
elif ((marks > 60) and (marks <= 70)):
    print("Your passed with grade 'C'")
elif ((marks >= 50) and (marks <= 60)):
    print("Your passed with grade 'D'")
elif (marks < 50):
    print("Your nailed your exams From Behind 🤭")
