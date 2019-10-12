@echo off
set /p percorso=Inserire il percorso da cui eliminare tutte le cartelle 
rmdir /S /Q "%percorso%"
mkdir "%percorso%"