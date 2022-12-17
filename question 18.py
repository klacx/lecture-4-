n1 = int(input("please enter the first number: "))
n2 = int(input("please enter the second number: "))

gcd1 = n1
gcd2 = n2

while gcd1 != gcd2:
    while n1 % gcd1 != 0:
        gcd1 = gcd1 - 1

    while n2 % gcd2 != 0:
        gcd2 = gcd2 - 1

    if gcd1 != gcd2:
        if gcd1 > gcd2:
            gcd1 = gcd1 - 1
        else:
            gcd2 = gcd2 - 1

print("The greatest common divisor of the number is ", gcd2)
