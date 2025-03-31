# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Ridhav, his marks is 100 and phone number is 143143143".

name = input("Enter the name of the student: ")
marks = int(input("Enter the marks of the student: "))
phone_number = input("Enter the phone number of the student: ")

formatted_string = "The name of the student is {}, his marks is {} and phone number is {}".format(name, marks, phone_number)
print(formatted_string)
