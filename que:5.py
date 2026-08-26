ch = input("Enter a character: ")

if len(ch) == 1:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
