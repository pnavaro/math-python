n = 50
e = 0.
fact = 1.
for i in range(n):
    e += 1/fact
    fact *= i+1
print(e)

def exponential(x, n=50):
    e = 0.
    power = 1.
    fact = 1.
    for i in range(n):
        e += power/fact
        power *= x
        fact *= i+1
    return e

print(exponential(1))

