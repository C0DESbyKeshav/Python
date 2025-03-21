# Write a program to find out the line number where python is present from ques 6

wordSearch = "python"

with open("07_log.txt") as file:
    count = lines = 0
    lineNo = []
    for line in file:
        lines += 1
        for word in line.split():
            if (word.lower() == wordSearch):
                count += 1
                lineNo.append(lines)
print(f"The word '{wordSearch}' is present {count} times in the line numbers {lineNo} in the log file.")
