#task1
number=int(input("Enter a number to print odd or even"))
if number%2==0:
    print("number is even")
else:
    print("number is odd")
#task 2
number=int(input("Enter a number to vote"))
if number>=18:
    print("Eligible to vote")
else:
    print("not eligible to vote")

#task3
number =int(input("enter a number"))
if number%3==0 and number%5==0:
    print("fizz and buzz")
elif number%3==0:
    print("fizz")
elif number%5==0:
    print("buzz")
else:
    print("not divisible by both number")
