#change a letter in a string in a particular position

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

def main():
  string = str(input("What string do you want to work on: "))
  position = int(input("What letter postion do you want to change: "))
  character = str(input("What character do you want to change it to: "))
  print(mutate_string(string, position, character))

main()