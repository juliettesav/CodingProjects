print('')
print("Type L if your starting unit is in Pounds (Lbs)")
print("Type K if your starting unit is in Kilograms (Kg)")
print('')

unit = input("")
print('')

weight = float(input("Enter your weight: "))
lbsweight = 0 
kgweight = 0
print('')

if unit == "L":
    lbsweight = weight 
    kgweight = round((weight / 2.205), 2)
    print(f'Your weight in Kilograms is {kgweight} Kg.')

if unit == "K":
    kgweight = weight
    lbsweight = round((weight * 2.205), 2)
    print(f'Your weight in Pounds is {lbsweight} Lbs.')

print(f'In conclusion, your weight in lbs is {lbsweight} lbs and your weight in kg is {kgweight} kg.')
print('')