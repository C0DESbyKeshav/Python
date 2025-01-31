
# *STRING FUNCTIONS
# Some of the mostly used functions to perform operations on or manipulate strings are:

# 1. len() -> This function returns the length of the string.
# len("Keshav")  # returns 6
name = "Keshav"
print(f"Length of the string '{name}' is ", len(name))  # returns 6

print("\n")

# 2. String.endswith("av") -> This function tells whether the variable string ends with the string "av" or not. If string is "Keshav", it returns true for "av" since "Keshav" ends with "av".
MyString = "Keshav"
print(MyString)
print(f"String '{MyString}' starts with 'Ke': ", MyString.startswith("Ke"))  # returns True
print(f"String '{MyString}' ends with 'av': ", MyString.endswith("av"))  # returns True

print("\n")

# 3. string.count("a") -> counts the total number of occurrences of any character.
string = "abracadabra"
count = string.count("a")
print(f"In string '{string}', letter 'a' occurs {count} times")  # Output: 5

print("\n")

# 4. string.capitalize() -> This function capitalizes the first character of a given string.
s = "hello world"
print(s)
capitalized_string = s.capitalize()
print("After capitalizing the first letter, the above string becomes:  ", capitalized_string)  # Output: "Hello world"

print("\n")

# 5. string.find(word) -> This function finds a word and returns the index of first occurence of that word in the string.
sentence = "EVERYONE DIES BUT NOT EVERYONE LIVES"
print(sentence)
print(f"The starting index number of first letter of the first occurence of word 'EVERYONE' in the above sentence = ", sentence.find("EVERYONE"))  # this will return the index of the first occurence of the word 'EVERYONE' (i.e. 0)

print("\n")

# 6. string.replace(oldword, newword) -> This function replaces all the occurences of old word with the newword in the entire string.
think = "Nothing changes untill you do"
print(think)
think.replace("you", "YOU")
print("After replacing 'you' by 'YOU', the above phrase becomes:  ", think)

print("\n")

# 7. string.lower() -> This function converts all the characters in a string to lower case.
print("HeLlO".lower())

print("\n")

# 8. string.upper() -> This function converts all the characters in a string to upper case.
print("HeLlO".upper())

print("\n")

# 9. string.title() -> This function capitalizes the first character of each word in a string.
print("hello world".title())

print("\n")

# 10. casefold() -> Converts a string to lowercase (more aggressive than lower()).
print("The snake whispers ßßß".casefold())   # Also converts special characters to english lowercase

print("\n")

# 11. swapcase() -> Swaps uppercase to lowercase and vice versa.
print("mY nAME IS keshav.".swapcase())

print("\n")

# 12. center(width, [fillchar]) -> Centers the string, padded with spaces or a specified character.
print(" ONE PIECE ".center(200,'-'))

print("\n")

# 13. ljust(width, [fillchar]) -> Left-aligns the string, padded with spaces or a specified character.
print("I am the King".ljust(200, '-'))

print("\n")

# 14. rjust(width, [fillchar]) -> Right-aligns the string, padded with spaces or a specified character.
print("I am the King".rjust(200, '-'))

print("\n")

# 15. zfill(width) -> Pads the string on the left with zeros.
print("I am the King".zfill(200))

print("\n")

# 16. isalpha() -> Checks if all characters are alphabetic.
str1 = "Yohohohoho"
print(f"All the characters in the string '{str1}' are alphabetic: ",str1.isalpha())    # returns True if all characters are alphabetic and False (even if there is a space or apostrophe or any other characters) otherwise.

print("\n")

# 17. isalnum() -> Checks if all characters are alphanumeric.
str2 = "Pass123"
print(f"All the characters in the string '{str2}' are alphanumeric: ",str2.isalnum())    # returns True if all characters are alphanumeric and False (even if there is a space or apostrophe or any other characters) otherwise.

print("\n")

# 18. isdigit() -> Checks if all characters are digits.
str3 = "10649"
print(f"All the characters in the string '{str3}' are numeric: ",str3.isdigit())    # returns True if all characters are numeric and False (even if there is a space or apostrophe or any other characters) otherwise.

print("\n")

# 19. isidentifier() -> Checks if the string is a valid Python identifier.
str5 = "str"
print(f"'{str5}' is a valid identifier in python: ",str5.isidentifier())

print("\n")

# 20. islower() -> Checks if all characters are lowercase.
str6 = "abcdevwxyz"
print(f"'{str6}' contains lowercase characters only: ",str6.islower())   

print("\n")

# 21. isupper() -> Checks if all characters are uppercase.
str7 = "ASDFJKL"
print(f"'{str7}' contains uppercase characters only: ",str7.isupper())

print("\n")

# 22. istitle() -> Checks if the string is in title case.
str8 = "I Will Become The Best."
print(f"'{str8}' contains titlecase characters: ",str8.istitle())

print("\n")

# 23. isspace() -> Checks if all characters are whitespace.
str9 = "    "
print(f"'{str9}' contains all whitespace characters only: ",str9.isspace())

print("\n")

# 24. split() -> Splits the string into a list using a delimiter.
str10 = "Luffy,Zoro,Ussop,Sanji,Nami,Chopper,Robin,Franky,Brook,Jimbey"
print(str10.split(","))

print("\n")

# 25. strip() -> Removes leading and trailing characters (defaults to whitespace).
onepiece = "      MONKEY .D. LUFFY       "
print(onepiece.strip())

print("\n")

# *Escape Sequence Characters
# Sequence of characters after backslash '\'
# Escape sequence character comprises of more than one characters but represents one character when used within the strings.
# Examples:
# \n -> newline
print("Rather than consuming,\nStart CREATING !!")  # print() function by default comes with a new line character at the end of the content.
print("\n")

# \t -> tab
print("Name\tPlace\tAnimal\tThing")
print("John\tDelhi\tLizard\tTable")
print("\n")

# \\ -> backslash
print("That guy is so \thi\n")  # This doesn't prints '\thi\n'.
print("That guy is so \\thi\\n")  # This will print '\thi\n' in one go.
print("\n")

# \' -> Single quote
print('Hii, It\'s me')
print("\n")

# \" -> Double quote
print("It's spelled as \"KING\"")
print("\n")

# \b -> Backspace
print("It's Im\b\bpossible")
print("\n")

# \v -> Vertical tab
print("Hello\vWorld")
print("\n")

# Raw Strings
print(r"Hello\nWorld")
print("\n")

# \0 -> Null character
print("Hello\0World")  # Output: Hello World (null is invisible)
print("\n")

# \a -> Bell/alert (produces a beep sound in some terminals)
print("\a")  # Produces a sound in supported terminals

# \N{name} -> Unicode character by its name
print("\N{GREEK CAPITAL LETTER DELTA}")  # Output: Δ
print("\n")

# \xhh -> Character with a hex value hh
print("\x48\x65\x6c\x6c\x6f")  # Output: Hello
print("\n")

# \uhhhh -> Unicode character with a 16-bit hex value hhhh
print("\u0048\u0065\u006c\u006c\u006f")  # Output: Hello
print("\n")

# \Uhhhhhhhh - Unicode character with a 32-bit hex value hhhhhhhh
print("\U0001F600")  # Output: 😀
print("\n")

# \ooo - Character with an octal value ooo
print("\101\102\103")  # Output: ABC
print("\n")
