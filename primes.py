import sympy as sp
#i want to have two functions, one that returns primes up to n and
#another that returns n first primes

#num = 500

#primes = [i for i in range(num) if sp.isprime(i)]

#print(primes)
def primes_to_n(n):
    return [i for i in range(n) if sp.isprime(i)]

def n_primes(n):
    primes = []
    i=1
    while len(primes)!=n:
        if sp.isprime(i):
            primes.append(i)

        i+=1
    return primes

print(n_primes(100))

