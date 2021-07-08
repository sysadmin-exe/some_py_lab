def evenNumber(a):
    if a%2 == 0:
        print(a, "is an even number")
    elif a > 100:
        print(a, "is greater than 100")
    else:
        print(a, "is NOT an even number")

def main():
	a = int(input("enter the number you want to check: "))
	evenNumber(a)

main()
