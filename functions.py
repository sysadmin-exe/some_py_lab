#define functions

def add_numbers(num1, num2):
    print("Hello there, the addition of ", num1, " and ", num2,  " is =>")
    return num1+num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(add_numbers(num1, num2))

main()