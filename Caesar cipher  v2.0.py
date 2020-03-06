def decipher(text, key):
	# Verifico che il testo non sia vuoto
	i=1
	while i:
		if not text:
			text=input('ERRORE il testo è vuoto: Inserire il testo: ')
		else:
			i=0

	# Verifico che la chiave passi correttamente

	i=1
	while i:
		if key > 25:
			j=1
			while j:
				try:
					key=int(input('ERRORE valore troppo elevato: Inserire la chiave(-26:26): '))
				except ValueError:
					print('ERRORE bisogna inserire un numero')
				else:
					j=0
		elif key < -25:
			j=1
			while j:
				try:
					key=int(input('ERRORE valore troppo basso: Inserire la chiave(-26:26): '))
				except ValueError:
					print('ERRORE bisogna inserire un numero')
				else:
					j=0
		else:
			i=0

	text=text.lower() # Trasformo il testo in modo che abbia solo caratteri minuscoli
	# Setto i tipi di queste variabili
	textList=[]
	textFinal=""
	textLength=len(text)

	# Trasformo il testo dato in input in un'array e lo metto dentro textList
	for i in range(textLength):
		textList.append(text[i])


	if key == 0: # Se la chiave è 0 controllo tutte le possibilità
		toPrint=""
		for n in range(25):
			for textId in range(len(text)):
				for alfabetoId in range(26):
					if textList[textId]==alfabeto[alfabetoId]:
						textList[textId]=alfabeto[alfabetoId+1]
						break
			newText=""
			for t in range(len(textList)):
				newText+=textList[t]
			toPrint+="Spostamento di "+str(n+1)+" spazi/o: "+newText+'\n'
	else:
		# Eseguo lo spostamento dei caratteri dell'array in base agli spazi dati in input
		for textId in range(textLength):
			for alfabetoId in range(26):
				if textList[textId]==alfabeto[alfabetoId]:
					textList[textId]=alfabeto[alfabetoId+key]
					break

		for i in range(textLength):
			textFinal+=textList[i]

		toPrint="Spostamento di "+str(key)+" spazi eseguito: "+textFinal

	print(toPrint)
	return toPrint

###################################################################


alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

text=input('Inserire il testo: ')

i=1
while i:
	try:
		key=int(input('Inserire la chiave(-25:25) (Inserire 0 per elencare tutte le possibilità): '))
	except ValueError:
		print('ERRORE bisogna inserire un numero')
	else:
		i=0

decipher(text, key)