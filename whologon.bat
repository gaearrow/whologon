@echo off
cd %~dp0
wevtutil qe security /format:text /q:"Event[System[(EventID=4624 or EventID=4634)]]" > LogonEvt.dat
whologon.exe LogonEvt.dat
del /F LogonEvt.dat