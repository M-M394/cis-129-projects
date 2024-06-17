#Mikayla Mitchell
#lab4
#June 17 2024
# calculating bonus
 
monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
#this code determines the store bonus
monthlySale = float(input("What were the monthly sales?"))

if monthlySales >= 110000:
	   storeAmount = 6000
elif monthlySales >= 100,000:
		   storeAmount = 5,000
elif monthlySales >= 90,000:
		   storeAmount = 4,000
elif monthlySales >= 80,000:
		   storeAmount = 3,000
else:
		 storeAmount = 0
# this code will get the employee bonus
salePercent = float(input("What was the sale increase?"))
saleIncrease = salePercent / 100

if salesIncrease >= .05:
		empAmount = 75
elif salesIncrease >= .04:
		empAmount = 50
elif salesIncrease >= .03:
		empAmount = 40
else:
		empAmount = 0

#print information

print("The store bonus amount is $",storeAmount)
print("The employee bonus amount is $",empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
		print('Congrats! You have reached the highest bonus amounts possible! ')




