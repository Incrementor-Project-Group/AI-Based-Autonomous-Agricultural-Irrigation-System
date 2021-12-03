@echo OFF
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "BO darbi" /min "%~f0" %* && exit
:: Process starts here
SET GPIOZERO_PIN_FACTORY=pigpio
SET PIGPIO_ADDR=192.168.2.203
python app.py
:: Process ends here
exit