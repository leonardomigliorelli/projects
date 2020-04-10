i=0
tasso=int(input("Inserire il numero percentuale (vuoto per 25%):\n").replace('%','') or 25)
casi=int(input("Inserire il numero dei casi attuali:\n").replace(',','').replace('.',''))
popolazione=int(input("Inserire la popolazione totale:\n").replace(',','').replace('.',''))
print("Attualmente ci sono {:,} casi confermati su una popolazione di {:,}".format(casi, popolazione))
while casi<popolazione:
	i+=1
	casi*=1+(tasso/100)
	if casi<popolazione:
		print("Giorno n. {:02} contagiati: {:14,}".format(i, int(casi)))
	else:
		print("Giorno n. {:02} contagiati: {:14,}".format(i, popolazione))