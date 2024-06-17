#Mikayla Mitchell
#June 14 2023
#coffee shop simulator
#this program should calculate the price 

coffeePrice = 5
miffinPrice = 4
taxPercentage = .06

coffeeAmount= float(input("How many coffees do you want? "))
muffinAmount= float(input("How many muffins do you want? "))

coffeeTotal = coffeePrice * coffeeAmount
muffinTotal = muffinPrice * muffinAmount

totalPrice= coffeeTotal + muffinTotal
taxAmount= totalPrice * taxPercentage

finalPrice= totalPrice + taxAmount

print("Number of coffees bought: ",coffeeAmount)
print("Number of muffins bought: ",muffinAmount)

print(coffeeAmount," coffees at $",coffeePrice," each: $",coffeeTotal)
print(muffinAmount," muffins at $",muffinPrice," each: $",muffinTotal)

print("6% tax: ",taxAmount)
print("Total: ",finalPrice)
