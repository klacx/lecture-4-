count = 1
num = 1

print("These are the all palindrome numbers from 1 to 200:")
while count < 200:
    temp = num
    oldN = num
    reverse = 0
    while num > 0:
        remainder = num % 10
        num = num // 10
        reverse = reverse * 10 + remainder
    if oldN == reverse:
        print(reverse)
    num = temp + 1
    count = count + 1
