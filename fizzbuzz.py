#Take input from the user. If the input is divisible by 3 then print "Fizz", if
#the input it divisible by 5 then print "Buzz". If the input is divisible by 3
#and 5 then print "Fizz Buzz".

buzz_fizz_num = int(input("Enter number here: "))

def buzz_fizz():
    if buzz_fizz_num % 3 == 0 and buzz_fizz_num % 5 == 0:
        print ("Fizz Buzz")
    elif buzz_fizz_num % 3 == 0:
        print("Fizz")
    elif buzz_fizz_num % 5 == 0:
        print("Buzz")
    else:
        print("Not divisible by either 3 or 5")

buzz_fizz() 
