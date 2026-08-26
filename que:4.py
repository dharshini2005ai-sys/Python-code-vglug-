units = int(input("Enter the units consumed: "))

if units <= 100:
    bill = units * 5
    print("Total bill is", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Total bill is", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Total bill is", bill)
