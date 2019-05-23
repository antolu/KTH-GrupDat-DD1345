from radix import radixsort
import random

#thelist = open("randn.txt", encoding ="utf-8").read().split()

antaltal = int(input("Antal heltal som ska sorteras: "))
maxtal = int(input("Största tal som ska sorteras: "))

thelist = []
for i in range(antaltal):
	thelist.append(random.randrange(maxtal))

print("Listan som skall sorteras:")
print(thelist)
print()
print("Sorterad lista:")
print(radixsort(thelist))