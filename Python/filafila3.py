def printTable():
	print(" {:} | {:} | {:}".format(table[0],table[1],table[2]))
	print("-----------")
	print(" {:} | {:} | {:}".format(table[3],table[4],table[5]))
	print("-----------")
	print(" {:} | {:} | {:}".format(table[6],table[7],table[8]))
def haveWinner():
	for xo in 'XO':
		if table[0] == xo and table[1] == xo and table[2] == xo:
			return xo
		elif table[3] == xo and table[4] == xo and table[5] == xo:
			return xo
		elif table[6] == xo and table[7] == xo and table[8] == xo:
			return xo
		elif table[0] == xo and table[3] == xo and table[6] == xo:
			return xo
		elif table[1] == xo and table[4] == xo and table[7] == xo:
			return xo
		elif table[2] == xo and table[5] == xo and table[8] == xo:
			return xo
		elif table[0] == xo and table[4] == xo and table[8] == xo:
			return xo
		elif table[2] == xo and table[4] == xo and table[6] == xo:
			return xo
		else:
			return False


table=[1,2,3,4,5,6,7,8,9]
i=1

while True:
	printTable()

	if haveWinner():
		print("Il vincitore è", ("player 1" if winner()=='X' else "player 2"))
		break

	xo=('X' if i==1 else 'O')

	selezione=int(input("\nPlayer {} seleziona dove inserire {}\n".format(i, xo)))
	table[table.index(selezione)]=xo

	i=(1 if i == 2 else 2)




