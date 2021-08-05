'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string. The next line contains the substring.

Constraints
Each character in the string is an ascii character.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.
'''

def count_substring(string, sub_string):
  count = 0
  for i in range(0, len(string)):
    if string[i:].startswith(sub_string):
      count += 1
  return count

def main():
  string = input("What string are you checking: ")
  sub_string = input("What substring are you searching for in string: ")
  print("The substring appears " + str(count_substring(string, sub_string)) + " times in the string")

main()

