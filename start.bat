@REM Option 1: start django server with webgui.py
@REM Option 2: start django server with webgui.py and debug mode
@REM Option 3: Add a new component with startapp


@REM Echo all options
@echo off
@echo 1. Start django server with webgui.py
@echo 2. Start django server with webgui.py and debug mode
@echo 3. Add a new component with startapp

@REM Recieves the option as a parameter
set /p option=Enter your option: 


@REM Option 1: start django server with webgui.py
if %option%==1 (
    cd %~dp0
    python webgui.py
)


@REM Option 2: start django server with webgui.py and debug mode
if %option%==2 (
    cd %~dp0
    python webgui.py --debug
)


@REM Option 3: Add a new component with startapp
if %option%==3 (
    set /p app=Enter your component name:
    cd %~dp0
    python manage.py startapp %app%
)
