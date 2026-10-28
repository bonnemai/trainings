def fibonacci(n):   
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibionacci_expensive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibionacci_expensive(n - 1) + fibionacci_expensive(n - 2)    
