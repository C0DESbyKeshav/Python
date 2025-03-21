# Write a program to mine a log file and find out whether it contains the word 'python'

wordSearch = "python"

with open("06_log.txt") as file:
    count = 0
    for line in file:
        for word in line.split():
            if (word.lower() == wordSearch):
                count += 1
print(f"The word '{wordSearch}' is present {count} times in the log file.")
