@echo off
if not exist venv (
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

if not exist venv\Lib\site-packages\installed (
    if exist requirements.txt (
		echo installing wheel for faster installing
		pip install wheel
        echo Installing dependencies...
        pip install -r requirements.txt
        echo. > venv\Lib\site-packages\installed
    ) else (
        echo requirements.txt not found, skipping dependency installation.
    )
) 


:loop
python main.py
echo Restarting the program in 10 seconds...
timeout /t 10 /nobreak >nul
goto :loop
