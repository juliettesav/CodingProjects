print(' ')
print("Welcome to The Office Trivia Game!")
print("(All answers should be in lowercase or a number)")
print(' ')
score=0
total_questions=5

answer=input("Question 1: Which employee does Michael hate? ")
if answer.lower()=="toby":
    score += 1
    print("Correct!")
    print(' ')
else:
    print("Wrong Answer :(")
    print("The correct answer was Toby.")
    print(' ')




answer=input("Question 2: How many acres is Shrute Farms? ")
if answer.lower()=='60':
    score += 1
    print("Correct!")
    print(' ')


else:
    print("Wrong Answer :(")
    print("The correct answer was 60.")
    print(' ')


answer=input("Question 3: What is Stanley's favorite day? ")
if answer.lower()=="pretzel day":
    score += 1
    print("Correct!")
    print(' ')
else:
    print("Wrong Answer :(")
    print("The correct answer was pretzel day.")
    print(' ')


answer=input("Question 4: What is the name of Jim's character in 'Threat Level Midnight'? ")
if answer.lower()=="goldenface":
    score += 1
    print("Correct!")
    print(' ')
else:
    print("Wrong Answer :(")
    print("The correct answer was goldenface.")
    print(' ')


answer=input("Question 5: What is the name of Angela's cat that Dwight kills? ")
if answer.lower()=="sprinkles":
    score += 1
    print("Correct!")
    print(' ')
else:
    print("Wrong Answer :(")
    print("The correct answer was sprinkles.")
    print(' ')

print("Thank you for playing The Office Trivia Game. You answered",score,"questions correctly!")
final_score=(score/total_questions)*100
print("Final Score: ",final_score,"%",sep='')
print(' ')
cont=input("Press Enter to select a new option.")
print(' ')