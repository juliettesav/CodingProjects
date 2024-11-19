print("Welcome to the coffee shop! \nWhat would you like to order?")
print("")
print("Select an option to see the price: ")
print("Espresso\nCoffee\nFrappicino\nMocha\nCappucino")
print("\nType your selection: ")
selection = input("")

prices = {"Espresso": "$2", "Coffee": "$4", "Frappicino": "$6", "Mocha": "$7", "Cappucino": "$4"}

print(prices[selection])

