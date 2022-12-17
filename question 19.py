num = int(input("please enter a number: "))

count = 2

while True:
    if num % (count) != 0:
        count = count + 1
        continue
    else:
        break

if num == count:
    fac = 1

    while num != 0:
        fac = fac * num
        num = num - 1

    print("factorial of the number is", fac)

else:
    oldN = num
    total = 0

    while num > 0:
        remain = num % 10
        num = num // 10
        total = total + remain

    print("SUM-OF-DIGIT of", oldN, " is", total)
