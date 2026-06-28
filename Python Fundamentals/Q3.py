# WAP to check if 2 numbers have same last digit

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

if x % 10 == y % 10:
     print(True)
else:
    print(False)