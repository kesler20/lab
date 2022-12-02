

# exponential O(2^n) : n<= 45
def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))

# squared O(n^2) : n <= 100
def nested_for_loops(n):
    for i in range(n):
        for i in range(n):
            i + 1

# linear O(n) : n <= 10,000
def for_loop(n):
    for i in range(n):
        i + 1


# constant time O(1) <= 100,000
# initialise val to be an array of length n + 1
val = [i for i in range(1001)]
def constant_lookup(n):
    x = val[n]
