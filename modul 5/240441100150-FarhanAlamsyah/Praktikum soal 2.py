n = int(input("fibonacci ke "))

def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")