'''A spam comment is defined as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this"
Write a program to detect this spams.'''

comment = input("Enter a comment:\n")

s1 = "make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

if((s1 in comment) or (s2 in comment) or (s3 in comment) or (s4 in comment)):
	print("You entered a spam comment.")
else:
	print("You entered a safe comment.")