fac = 1
num = 0
oldN = num

# check number
while True:
    num = (input("please enter a number: "))
    if num.isdigit():
        break
    else:
        print("Wrong value, please try again")
        continue

# calculate factorial
while num != 0:
    fac = fac * int(num)
    num = int(num) - 1

print("The factorial number of ", oldN, "is ", fac)

if fac > 500:

    # calculate sum of digit

    facOldN = fac
    total = 0

    while fac > 0:
        remain = fac % 10
        fac = fac // 10
        total = total + remain

    print("The SUM-OF-DIGIT of", facOldN, " is", total)

else:

    # reverse

    reverseOldN = fac
    reverse = 0

    while fac > 0:
        remain = fac % 10
        fac = fac // 10
        reverse = (reverse * 10) + remain

    print("The reverse of ", reverseOldN, "is", reverse)
