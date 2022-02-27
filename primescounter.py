import sympy as sp
# import matplotlib.pyplot as plt
import math

numbers=10

def primecounter(n):
    """
    Counts the number of prime numbers under a certain number.
    """
    counter=0
    for i in range(1, n+1):
        if sp.isprime(i):
            counter+=1
    return counter

primescounted = [primecounter(i) for i in range(2, numbers+1)]
primestheorem = [n/math.log(n) for n in range(2, numbers+1)]
# plt.plot(range(2, numbers+1), primestheorem)
# plt.plot(range(2, numbers+1), primescounted)
# plt.show()
print(primescounted)
