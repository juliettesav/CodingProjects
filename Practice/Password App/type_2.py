def play():
    print(' ')
    print("You have chosen Magic 8 Ball!")
    query=input("What is your query? ")
    import random
    eb = ["Yes","No","Maybe","Ask again later","Signs point to yes"]
    eb_result = random.sample(eb, 1)
    print("The Magic 8 Ball says:",eb_result)
    print(' ')