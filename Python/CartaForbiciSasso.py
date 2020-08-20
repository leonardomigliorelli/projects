import random
import time

space = "--------------------------------------------------------\n"
values = ('sasso', 'carta', 'forbici')

while True:
	player = input("\nInserire Sasso Carta o Forbici\n").lower().strip()
	pc = random.choice(values)
	
	time.sleep(1)

	if player in values:
		if player == "sasso"\
				and pc == "forbici" or player == "carta"\
				and pc == "sasso" or player == "forbici"\
				and pc == "carta":
			print("Hai vinto")
		elif player == pc:
			print("Pareggio")
		else:
			print("Hai perso")
	else:
		print(space, "Errore,", end=' ')
		continue
	time.sleep(1)
