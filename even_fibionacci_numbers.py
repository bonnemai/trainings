def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def even_fib(n):
    return sum(fib(i) for i in range(n) if fib(i) % 2 == 0)
print(even_fib(4_000_000))

# i=1: 1: odd
# i=2: 1: odd
# i=3: 2: even
# i=4: 3: odd
# i=5: 5: odd
# i=6: 8: even
# i=7: 13: odd
# i=8: 21: odd
# i=9: 34: even
# i=10: 55: odd
# i=11: 89: odd
# i=12: 144: even
# i=13: 233: odd
# i=14: 377: odd