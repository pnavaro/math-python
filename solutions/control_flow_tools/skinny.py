def reverse(n):
    return int(str(n)[::-1])

def skinny(N):
    for n in range(10,N):
        if reverse(n**2)==reverse(n)**2 and n != reverse(n):

print(skinny(200))
