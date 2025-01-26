# WAP to detect double space in a string.
sentence = input("Enter a sentence: ")
if sentence.find("  ") >=0:
    print("Double space was detected in your sentence at position ",sentence.find("  ")+1)
else:
    print("Double space was not detected in your sentence.")