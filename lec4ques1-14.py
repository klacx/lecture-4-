########Question 2
#num = 1
#count = 2

#while count != 11:
#    print(num, '+', count)
#    num = num + count
#    count = count + 1

#print("total: ",num)

#########Question 3

#num = 2

#while num != 22 :
#    print (num)
#    num = num + 2

########Question 4

#even = 0
#odd = -1

#print("even number: ")
#while even != 20 :
#    even = even + 2
#    print(even)

#print("odd number: ")
#while odd != 19 :
#    odd = odd + 2
#    print(odd)

#########Question 5

#count = 1

#num = int(input("please enter the number: "))

#while count != 11 :
#    print(num, ' x', count, '=', (num*count))
#    count = count + 1

########Question 6

#even = 0
#odd = -1
#sumEven = 0
#sumOdd = 0

#while even != 10:
#    even = even + 2
#    sumEven = sumEven + even

#print("sum of even number is ", sumEven)
#while odd != 9:
#    odd = odd + 2
#    sumOdd = sumOdd + odd

#print("sum of odd number is ", sumOdd)


#########Question 7

#num = int(input("Please enter a number: "))
#fac = 1

#while num != 0:
#    fac = fac*num
#    num = num - 1
    
#print("factotial of the number is ", fac)

########Question 8

#num = int(input("Please enter a number: "))
  
#reverse = 0
  
#print("the reverse of ", num, "is")  
#while num > 0 :
#    remain = num%10
#    num = num//10
#    reverse = (reverse*10) + remain

#print(reverse)
#######Question 9

#num=int(input("Enter number:"))
#oldN = num
#newN = 0
#length = len(str(num))

#while num>0:
#    remain = num%10
#    newN = newN + (remain ** length)
#    num = num//10

#if newN == oldN:
#    print("this is an armstrong number")
#else :
#    print("this is not an armstrong number")
  
#######Question 10 (need review agn)

#reverse = 0
#number = int(input("Get number"))

#originalNumber = number


#while number > 0:
#    remainder = number % 10
#    reverse = (reverse *10) + remainder
#    number = number //10

#if reverse == originalNumber:
#    print("This is a Palindrome")
#else :
#    print("This is not a palindrome")
    
#######Question 11

#n = 0
#n2 = 1
#count = 0
  
#print("Fibonacci series up to 10 of is")
#while count < 10:
#    print(n)
#    total = n + n2
#    n = n2
#    n2 = total
#    count = count + 1

#######Question 12

#num = int(input("please enter a number: "))
#oldN = num
#sum = 0
  
#while num > 0 :
#    remain = num%10
#    num = num//10
#    sum = sum + remain
	
#print("The SUM-OF-DIGIT of", oldN, " is", sum)

#######Question 13

#num=int(input("Enter number:"))

#count = 2

#while True:
#    if num%count != 0:
#        count = count + 1
#        continue
#    else :
#        break

#if num == count :
#    print("This is a prime number")
#else :
#    print("This is not a prime number")
 

#num=int(input("Enter number:"))
#oldN = num
#newN = 0
#length = len(str(num))

#while num>0:
#    remain = num%10
#    newN = newN + (remain ** length)
#    num = num//10

#if newN == oldN:
#    print("this is an armstrong number")
#else :
#    print("this is not an armstrong number")

########Question 14

number = 100
length = len(str(number))
oldN= number
count = 100

while count < 999:
  temp = number
  oldNumber = number
  newNumber = 0
  while number > 0:
      remainder = number%10
      newNumber = newNumber + (remainder**length)
      number = number//10
  if newNumber == oldNumber:
      print(newNumber, count)
  count= count+1
  number = temp + 1
