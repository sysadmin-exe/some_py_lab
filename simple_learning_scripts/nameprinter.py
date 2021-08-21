#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
# Constraints: The length of the first and last names are each ≤ 10.
def print_full_name(first, last):
  if len(first) and len(last) <= 10:
    print ("Hello ", first, " ", last, "! You just delved into python.", sep="")
  else: 
    print ("The name is too long. It exceeds 10 characters")

if __name__ == '__main__':
  first = input(str("First Name: "))
  last = input(str("Last Name: "))
  print_full_name(first, last)
else: 
  first = input(str("First Name: "))
  last = input(str("Last Name: "))
  print_full_name(first, last)