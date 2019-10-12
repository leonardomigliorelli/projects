@echo off
set /p percorso=Inserire il percorso da cui eliminare tutte le cartelle 
cls
echo Sto mantenendo pulita la cartella..
:inizio
rmdir /S /Q "%percorso%" > NUL 2>&1
mkdir "%percorso%" > NUL 2>&1
timeout /t 2 /nobreak > NUL 2>&1
goto inizio