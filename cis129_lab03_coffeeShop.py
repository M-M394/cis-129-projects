#Mikayla Mitchell
#June 14 2023
#coffee shop simulator
#this program should calculate the price 

coffeePrice = 5
miffinPrice = 4
teaPrice = 3
pasteryPrice = 6
taxPercentage = .06

coffeeAmount= float(input("How many coffees do you want? "))
muffinAmount= float(input("How many muffins do you want? "))
teaAmount= float(input("How many teas do you want? "))
pasteryAmount= float(input("How many pasteries do you want"))

coffeeTotal = coffeePrice * coffeeAmount 
muffinTotal = muffinPrice * muffinAmount
teaTotal = teaPrice * teaAmount
pasteryTotal = pasteryPrice * pasteryAmount

totalPrice= coffeeTotal + muffinTotal + teaTotal + pasteryTotal
taxAmount= totalPrice * taxPercentage

finalPrice= totalPrice + taxAmount

print("Number of coffees bought: ",coffeeAmount)
print("Number of muffins bought: ",muffinAmount)
print("Number of teas bought: ",teaAmount)
print("Number of pasteries bought: ",pasteryAmount)

print(coffeeAmount," coffees at $",coffeePrice," each: $",coffeeTotal)
print(muffinAmount," muffins at $",muffinPrice," each: $",muffinTotal)
print(teaAmount," teas at $",teaPrice," each: $",teaTotal)
print(pasteryAmount,"pasteries at $",pasteryPrice," each: $",pasteryTotal)

print("6% tax: ",taxAmount)
print("Total: ",finalPrice)
print("Come back again")
