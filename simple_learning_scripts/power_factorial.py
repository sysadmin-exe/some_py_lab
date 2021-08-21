# WHAT DOES THIS SCRIPT DO? 
# Uses recursion to get the power and factorial values on numbers

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num,  pwr-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

def main():
    num = int(input("Number to calculate: "))
    pwr = int(input("Power to raise number to: "))

    print ("{} raised to the power of {} is {}".format(num, pwr, power(num, pwr)))
    print("The factorial of {} is {}".format(num, factorial(num)))

main()