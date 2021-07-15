# Python code to reverse a string 
# using extended slice syntax
  
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

def main():
  string = str(input("Enter string to be reversed: "))
  print ("The original string  is : ", string)
  print ("The reversed string(extended slice syntax) is : ",end="")
  print (reverse(string))

main()

# Python code to reverse a string 
# using loop
  
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))