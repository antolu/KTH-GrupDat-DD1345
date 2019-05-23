def primes(n): 
    ps, såll = [], [True] * (n + 1)            #Definiera tom lista, och en med n+1 element
    for p in range(2, n + 1):                  #Repetera för alla tal
        if såll[p]:                            #Om elementet i sållet är sant, kör kommandona
           ps.append(p)                        #Lägg till talet p (primtal) listan med primtal
           for i in range(p*2, n + 1, p):      #Stryk alla multiplar av talet p i sållet
               såll[i] = False
    return ps

import time

n = int(input("n = "))
print()

start = time.time()

såll = primes(n)

end = time.time()

if n < 10000:
    print(såll)
print()
print(end-start," sekunder")