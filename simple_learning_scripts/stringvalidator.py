
'''
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
'''
def string_validator(s):
  print (any(i.isalnum() for i in s))
  print (any(i.isalpha() for i in s))
  print (any(i.isdigit() for i in s))
  print (any(i.islower() for i in s))
  print (any(i.isupper() for i in s))

def main():
  s = input("Enter text to validate: ")
  string_validator(s)

main()