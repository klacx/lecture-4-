num = int(input("Please enter a number: "))

length = len(str(num))
oldN = num
newN = 0

while num > 0:
    remainder = num % 10
    newN = newN + (remainder ** length)
    num = num // 10

if newN == oldN:
    reverseOldN = oldN
    reverse1 = 0
    num = oldN

    print("This is an armstrong number")
    print("The reverse of ", reverseOldN, "is")

    while num > 0:
        remain = num % 10
        num = num // 10
        reverse1 = (reverse1 * 10) + remain

    print(reverse1)

else:
    num = oldN
    palinOldN = num
    reverse2 = 0


    while num > 0:
        remainder = num % 10
        num = num // 10
        reverse2 = (reverse2 * 10) + remainder

    print("This is not an armstrong number,")
    if reverse2 == oldN:
        print("This is not an armstrong number, but it is a palindrome")
    else:
        print("This is not an armstrong number, and also not a palindrome")
