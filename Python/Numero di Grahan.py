import timeit

tempoImpiegato=0
valore=3
def c():
	global valore
	valore**=3


for i in range(14):
	print("Livello", i)

	tempoFine=tempoImpiegato
	tempoImpiegato=timeit.timeit(c, number=1)
	diff=tempoImpiegato-tempoFine

	print("Ci ha impiegato {:.3} secondi con un incremento del {}%".format(tempoImpiegato, diff))

print("Sto salvando il valore nel file Grahan_Number")
file=open("Grahan_Number.txt", "w")
file.write(str(valore))
file.close()