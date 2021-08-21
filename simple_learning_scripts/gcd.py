# WHAT DOES THIS SCRIPT DO?
# Finds the greatest common denominator of 2 numbers using Euclid's Algorightm

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

def main():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))

    print(gcd(a, b))

main()