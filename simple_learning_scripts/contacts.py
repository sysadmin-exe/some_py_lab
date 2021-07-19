contacts = {
  "number":4,
  "students": 
  [
    {"name":"Victor Efedi", "email":"victor@gmail.com"},
    {"name":"Treasure Efedi", "email":"treasure@gmail.com"},
    {"name":"pi efedi", "email":"pi@gmail.com"},
    {"name":"child efedi", "email":"child@gmail.com"}
  ]
}

for student in contacts["students"]:
  print(student["email"])