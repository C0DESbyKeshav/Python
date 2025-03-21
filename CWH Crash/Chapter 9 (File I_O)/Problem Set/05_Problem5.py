# Repeat program 4 for a list of such words to be censored.

import re

words = ["donkey", "live", "nice", "bad"]

with open("05_replace.txt") as file:
    content = file.read()
 
# Replace all case variations of "donkey" and other words with "######"
for word in words:
    content = re.sub(rf"(?i)\b{word}\b", '#' * len(word), content)
# (?i) for case-insensitive matching
# \b to match whole words only (avoiding replacing parts of other words, e.g., donkey123 would not be replaced)

with open("05_replace.txt", "w") as file:
    file.write(content)
