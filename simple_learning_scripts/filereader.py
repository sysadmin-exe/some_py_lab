countryFile = open('countries.txt', 'r')
for lines in countryFile.readlines():
  print(lines)
countryFile.close()

countryFile = open('states.txt', 'w')
countryFile.write('\nJapan')