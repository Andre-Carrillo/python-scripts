import matplotlib.pyplot as plt
import sympy
numbers = 1000
numberlist = range(1, numbers+1)
def satisfies(n):
    """
    Esta función verifica si un numero cumple 
    En esta función quiero chequear si el valor es el mismo que el anterior para no tener que 
    compararlo con 1
    """
    i=0
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        i+=1
    return False, i

list_of_iterations = [satisfies(i)[1] for i in numberlist]
maxfrecuency = max(list_of_iterations)
frecuencylist = [0 for i in range(maxfrecuency+2)]

for it in list_of_iterations:
    frecuencylist[it+1]+=1

plt.plot(range(maxfrecuency+2), frecuencylist)
# plt.plot(range(1, numbers+1), list_of_iterations)
# plt.hist(list_of_iterations)
plt.savefig("graph1")
# plt.show()
