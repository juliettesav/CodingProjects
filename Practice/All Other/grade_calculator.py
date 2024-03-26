def grade_calculator(age, name): 
    if age < 5: 
        print(f'{name} is only {age} years old!')
        grade = "Pre-school"
        return grade
    elif age == 5: 
        print(f'{name} is {age} years old.')
        grade = "Kindergarden" 
        return grade 
    else: 
        print("They grow up so fast!")
        grade = "a grade above kindergarden or not in school"
        return grade

name = input("What is your child's name? ")
age = int(input("What is your child's age? "))

grade = grade_calculator(age,name) 

print(f'It appears that {name} is in {grade}!')