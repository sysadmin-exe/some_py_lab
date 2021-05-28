# a = 1000
# b = 100

# if a < b:
#     print("a is LESS than b")
# elif a == b:
#     print("a is EQUAL to b")
# else:
#     print("a is GREATER than b")

#==================================
#=======BMI CALCULATOR=============
#==================================
name = input("What can I call you\n")
height_m = int(input("How tall are you in CM?\n")) / 100
weight_kg = int(input("How much do you weigh in KG?\n"))

bmi = weight_kg / (height_m ** 2)

print(name+"'s BMI is: ")
print(bmi)

if bmi > 25:
    print(name + " " "is overweight")
else:
    print(name + " " "is not overweight! GREAT JOB" + " " + name)
