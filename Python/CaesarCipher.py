alfabeto = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
text = input('Inserire il testo: ').lower()
textList = [text[i] for i in range(len(text))]  # Creo una lista partendo dal text

while True:  # Inserimento della key con controllo -25<key<25
	try:
		key = int(input('Inserire la chiave(-25:25) (lasciare vuoto o inserire 0 per elencare tutte le combinazioni): ') or 0)
		if key > 25:
			key = int(input('ERRORE valore troppo elevato: Inserire la chiave(-26:26): '))
		elif key < -25:
			key = int(input('ERRORE valore troppo basso: Inserire la chiave(-26:26): '))
	except ValueError:
		print('ERRORE bisogna inserire un numero')
	else:
		break

key = (key+26 if key < 0 else key)

for n in range(25):
	for textId in range(len(text)):
		for alfabetoId in range(26):
			if textList[textId] == alfabeto[alfabetoId]:
				textList[textId] = alfabeto[alfabetoId+1]
				break
	newText = ""
	for t in range(len(text)):
		newText += textList[t]
		
	if key == 0:
		print("Spostamento di", n+1, "spazi/o:", newText)
	elif key == n+1:
		print("Spostamento di", n+1, "spazi/o:", newText)
		break
