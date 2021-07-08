def evenNumber(a):
    if a%2 == 0:
        print(a, "is an even number")
    else:
        print(a, "is NOT an even number")

def main():
	a = int(input("enter the number you want to check: "))
	evenNumber(a)

main()
