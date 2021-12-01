@echo OFF
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "BO darbi" /min "%~f0" %* && exit
:: Process starts here
python app.py
:: Process ends here
exit