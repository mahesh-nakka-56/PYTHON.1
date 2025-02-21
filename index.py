
# Write a program to check if a given number is positive, 
#  negative,or zero.

num1 = float(input("enter a number"))
if num1 > 0:
    print("Postive")
elif num1 == 0:
    print("Zero")
else:
    print("negative number")

# 2.Determine if a number is odd or even.

print("even")if num1 % 2 == 0 else print("Odd")

#3. Check if a person is eligible to vote (age >= 18)
age = 22
print("eligible") if age >= 18 else print("Not eligibile")

# Write a program to find the greatest of two numbers. 
n1 = int (input("enter a number"))
n2 = int (input("enter another"))
if n1 > n2:
    print ("n1 is geatest")
else:
    print ("n2 is greatest")


score=35
if score >=40:
    print("pass")
else:
    print("fail")


    day = int(input("enter the number:"))
if  day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")    
elif day == 4:
    print("Thursaday")    
elif day == 5:
    print("Friday")     
elif day == 6:
    print("Saturday")  
elif day == 7:
    print("Sunday")         
else:
    print("Invalid day")

# 7. Implement a simple calculator to perform addition,
# #  subtraction, multiplication, and division
operation = input("Enter operation to Perform") #add,mul,div,sub
op1 = float(input("Enter first number"))
op2 = float(input("Enter second number"))

if operation == 'add':
   print(op1 + op2)

elif operation == 'sub':
   print(op1 - op2)

elif operation == 'mul':
    print(op1 * op2)

elif operation == 'div':
    if op2 == 0:
       print("Division by zero is not possible")
    else:
        print(op1/op2)
else:
    print('invalid operation')

# 8)Write a program to display the name of a month based on
# the month number (1 for January, 2 for February, etc.).
Month = int(input("Enter the number:"))
if  Month == 1:
    print("Jan")
elif Month == 2:
    print("Feb")
elif Month == 3:
    print("March")    
elif Month == 4:
    print("April")    
elif Month == 5:
    print("May")     
elif Month == 6:
    print("June")  
elif Month == 7:
    print("July") 
elif Month == 8:
    print("August")   
elif Month == 9:
    print("September")  
elif Month == 10:
    print("October") 
elif Month == 11:
    print("November")  
elif Month == 12:
    print("December")                
else:
    print("Invalid Month")

    # Medium codings
# 1)Write a program to find the greatest of three numbers.
n1 = int (input("Enter a number"))
n2 = int (input("Enter a number"))
n3 = int (input("Enter another"))
if n1 > n2 and n1 > n3:
    print ("Greatest is",n1)
elif  n2 > n1 and n2 > n3:
    print ("Greatest is",n2)  
else:
    print ("Greatest is",n3)    

# 2)Check if a year is a leap year
year = int(input("Enter a year"))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is leap year")
elif (year %4 == 0) and  (year %100 != 0):
    print (year,"is leap year")
else:
    print(year,"is not leap year")  

    # Write a program to classify a character entered by the user
#  asvowel,consonent or neither
n = input("Enter a alpha :")
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
neither = ['!','@','#','$','&']
for i in n:
    if n in vowels:
        print ("vowel")
    elif n in consonants:
        print ("consonant")  
    else:    
        print ("neither")
  
# 4)Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail

score = int (input("Enter the students score:"))
if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'   
else:
    grade = 'Fail'   
print(grade) 

# 5)Write a program to check if three sides length form a valid
# triangle.
s1 = float(input("Enter the first side length : "))
s2 = float(input("Enter the second side length : "))
s3 = float(input("Enter the third side length : "))
if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("The given sides are  valid triangle.")
else:
    print("The given sides are not valid triangle.")
