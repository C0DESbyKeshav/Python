# A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.
import re

with open("04_donkey.txt") as file:
    content = file.read()
 
# Replace all case variations of "donkey" with "######"
content = re.sub(r'(?i)\bdonkey\b', '######', content)
# (?i) for case-insensitive matching
# \b to match whole words only (avoiding replacing parts of other words, e.g., donkey123 would not be replaced)

with open("04_donkey.txt", "w") as file:
    file.write(content)
