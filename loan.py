# get the loan details

money_owed = float(input("How much money do you owe, in Dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What is the monthly payment in Dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

#Divide apr by 100 to make it a percentage and by 12 to get the monthly rate
monthly_rate =  apr/100/12

for i in range(months):
  #add in the interest
  interest_paid = money_owed * monthly_rate
  money_owed = money_owed + interest_paid
  
  if (money_owed - payment < 0):
    print("The last payment is", money_owed)
    print("You paid off the loan in", i+1, "months")
    break
  
  #make payment
  money_owed = money_owed - payment

  #print the results after the month
  print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
  print("Now I owe", money_owed)