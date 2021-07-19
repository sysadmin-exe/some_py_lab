print('Create new account')
username = str(input('Enter Username: '))
password = str(input('Enter Password: '))

print('Your account has been created successfully! :)')
print('Login in ...')

username2 = str(input('Enter Username: '))
password2 = str(input('Enter Password: '))

if username == username2 and password == password2: 
  print('Logged in successfully')
else:
  print('Invalid Credentials :(')