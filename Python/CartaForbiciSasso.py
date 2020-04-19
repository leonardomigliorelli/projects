import random
import time

values=('sasso', 'carta', 'forbici')

while True:
	player=input("Inserire Sasso Carta o Forbici\n").lower().strip()
	pc=random.choice(values)
	
	time.sleep(1)

	if player in values:
		if player=="sasso" and pc=="forbici" or player=="carta" and pc=="sasso" or player=="forbici" and pc=="carta":
			print("Hai vinto")
		elif player==pc:
			print("Pareggio")
		else:
			print("Hai perso")
	else:
		print("Errore,", end=' ')
		continue
	time.sleep(1)