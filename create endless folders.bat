@echo off
title Create folders
:inizio
cls
set /p percorso=Insert the directory to full of folders 
set /p testo=Insert an optional phrase to include in the name 
set /a massimo=-1
set /p massimo=Insert the maximum number of folder to create (default is infinite) 
set i=0
:loop
set /a i+=1
set file=%testo%%i%
echo Creating folder: %file%
md "%percorso%\%file%"
rem exit condition
if %massimo% gtr 0 set /a massimo-=1
if %massimo% equ 0 goto exit
goto loop
:exit
echo Finished
pause
goto inizio
