def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

n = int(input("How many numbers of the Fibonacci sequence do you want to see? "))
fibonacci_sequence = fibonacci(n)
print(f"The Fibonacci sequence is {fibonacci_sequence}.")