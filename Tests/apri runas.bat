@echo on
dir
echo
set /p utente=Inserire l'utente runas: utente
set /p file=Inserire il file da aprire
runas /utente:utente%utente%@gentili 
