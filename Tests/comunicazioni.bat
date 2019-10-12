@echo off
title Comunicator
set /p classe=Inserire classe e sezione 
set /p studente=Inserire lo studente 
set su=runas /user:gentili\utente%classe%%studente% 
echo %classe%%studente%>psw
cd Z:\Utente%classe%%studente%
cls
:inizio
set /p risultato=Vuoi [SP]ostarti tra i file [SC]rivere, [L]eggere? 
if /i %risultato%=="SP" (
	cls
	set /p nome=Scrivi il nome della cartella nella quale vuoi spostarti (.. farà salire di una cartella) 
	%su% cd %nome% < psw
)
if /i %risultato%=="SC" (
	cls
	set /p risultato=Vuoi [C]reare o [E]liminare?
	if /i "%risultato%"=="C" (
		cls
		set /p risultato=Vuoi creare un [F]ile o una [C]artella? 
		if /i "%risultato%"=="F" (
			cls
			set /p nome=Scrivi il nome con cui vuoi salvare il file 
			set /p contenuto=Scrivi il contenuto del file 
			%su% echo %contenuto%>%nome% < psw
		)
		if /i "%risultato%"=="C" (
			cls
			set /p nome=Scrivi il nome con cui vuoi salvare il file 
			%su% mkdir %nome% < psw
		)
	)
	if /i "%risultato%"=="E" (
		cls
		set /p risultato=Vuoi eliminare un [F]ile o una [C]artella? 
		if /i "%risultato%"=="F" (
			cls
			set /p nome=Scrivi il nome del file che vuoi eliminare 
			%su% del %nome% < psw
		)
		if /i "%risultato%"=="C" (
			cls
			set /p nome=Scrivi il nome della cartella che vuoi eliminare 
			%su% rmdir %nome% < psw
		)	
	)
if /i %risultato%=="L" (
	cls
	%su% dir < psw
	pause
	goto inizio
)
pause
cls
goto inizio