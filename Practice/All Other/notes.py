# Notes 

print("MENU")
print("Vanilla\nChocolate\nStrawberry")
flavor = input("What flavor would you like? ")
print(f"Here is your {flavor} ice cream!")

print()
print(f"Would you like to hear what toppings we recomend with your {flavor} ice cream?")
reply = input("Type y for Yes and n for No ")

if reply == 'y':
    print("Here are the toppings we recommend: ")
    if flavor == "Strawberry":
        print("Strawberries\nWhipped Cream")
    if flavor == "Chocolate": 
        print("Chocolate Fudge\nChocolate Sprinkles")
    if flavor == "Vanilla":
        print("Rainbow Sprinkles\nRasberry Syrup")

    print("")
    print("Would you like to add any toppings?")
    reply2 = input("Type y for Yes and n for No ")

    if reply2 == "y":
        input("What kind of toppings would you like? ")
        print("Cool!")
    
    if reply2 == "n":
        reply = 'n'

if reply == 'n':
    print("No problem! Enjoy your ice cream!")
