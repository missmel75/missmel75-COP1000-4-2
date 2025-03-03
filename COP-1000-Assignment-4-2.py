# Initialize the variables
eeName = "Kim Smith"
numShifts = 25
numTransactions = 75
transactionDollars = 40000.00

#Input Values
eeName = input("Enter Employee Name: ")
numShifts = int(input("Enter number of shifts: "))
numTransactions = int(input("Enter number of transactions: "))
transactionDollars = float(input("Enter transaction dollar value: "))

#Find the Productivity Score using an EEs transactions dollar value
prodScore = (transactionDollars / numTransactions)/numShifts

#Find Bonus using Productivity Score
if prodScore <=30:
    Bonus = 50.00
elif 30 < prodScore <70:
    Bonus = 75.00
elif 70 <= prodScore <200:
    Bonus = 100.00
else:
    Bonus = 200.00

#Output Results
print ("Employee Name: " + eeName)
print ("Employee Bonus: " + str(Bonus))