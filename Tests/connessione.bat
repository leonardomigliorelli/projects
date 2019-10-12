@echo on
set /p utente=Inserire il numero dello studente: Utente4d
net use Z: \\classe4d$\Utente4d$utente$\persistent:yes
:1
set /p comando=Inserire il comando 
%comando%
pause
cls
goto 1