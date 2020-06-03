import time
import random

operations = "-+*"
easy = range(1,25)
medium = range(25,100)
hard = range(100,200)
veryhard = range(200,500)

space="----------------------------------------------\n"

while True:
	print(space, "\nScegliere il livello di difficoltà\n")
	print("1) Easy")
	print("2) Medium")
	print("3) Hard")
	print("4) Very Hard")
	option=input(" ").lower().replace(' ','')

	operator=random.choice(operations)

	if option=='1' or option=='easy':
		value1=str(random.choice(easy))
		value2=str(random.choice(easy))
	elif option=='2' or option=='medium':
		value1=str(random.choice(medium))
		value2=str(random.choice(medium))
	elif option=='3' or option=='hard':
		value1=str(random.choice(hard))
		value2=str(random.choice(hard))
	elif option=='4' or option=='veryhard':
		value1=str(random.choice(veryhard))
		value2=str(random.choice(veryhard))
	else:
		print("ERRORE, scelta non riconosciuta:",option)
		continue

	operazione=value1+operator+value2
	risultato=str(eval(operazione))

	print("\nInserire il risultato")
	
	tempoInizio=int(time.time())

	risposta=input(" {} = ".format(operazione)).strip()

	tempoFine=int(time.time())

	tempoImpiegato=tempoFine-tempoInizio

	time.sleep(1)

	if risposta==risultato:
		print("\nRisposta CORRETTA:", risultato)
	else:
		print("\nRisposta NON CORRETTA: {}\nLa risposta corretta era {}".format(risposta, risultato))
	
	time.sleep(0.5)
	print("Tempo impiegato: {} secondi\n".format(tempoImpiegato))

	time.sleep(1)
