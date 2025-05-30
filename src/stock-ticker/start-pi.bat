@echo off
echo Starting Raspberry Pi script...
ssh pi@192.168.0.14 "cd led-raspberry-pi/src/stock-ticker && screen -dmS stock-ticker-session sudo python3 main.py --led-gpio-mapping=adafruit-hat"
echo Script launched in screen session named 'stock-ticker-session'.
pause
