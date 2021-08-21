# WHAT DOES THIS SCRIPT DO? 
# Use recursion to implement a countdown counter

def countdown(x):
    if x == 0:
        print("DONE!")
        return
    else:
        print(x, "...")
        countdown(x-1)

def main():
    x = int(input("Countdown starts from: "))
    countdown(x)

main()