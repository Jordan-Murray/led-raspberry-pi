@echo off
echo Stopping Raspberry Pi stock ticker...

ssh pi@192.168.0.14 "screen -S stock-ticker-session -X quit"

echo Stock ticker screen session terminated.
pause
