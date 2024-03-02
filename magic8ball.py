import random
print(' ')
print("Welcome to the Magic 8 Ball!")

while True: 
    query=input("What is your query? ")
    eb = ["Yes","No","Maybe","Ask again later","Signs point to yes"]
    eb_result = random.sample(eb, 1)[0]
    print(f'The Magic 8 Ball says: {eb_result}')
    print(' ')
    cont=input("Press Enter ask again. ")
    print(' ')