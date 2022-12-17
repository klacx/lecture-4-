num = ' '
biggest = 0

while num != 0:
    num = int(input("please enter a number: "))
    if num > biggest:
        biggest = num

print("The largest number you have entered is ", biggest)
