class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = person('Victor', '28')
del p1.age
print(p1.age)
