@echo off
REM AI-Driven Assessment of Student Performance Trends
REM Windows Startup Script

echo.
echo ============================================================
echo AI-Driven Assessment of Student Performance Trends
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Checking dependencies...
pip list | find "Flask" >nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo Starting Flask server...
echo.
echo Visit: http://localhost:5000
echo.
echo Demo Credentials:
echo   Email: arjun@gmail.com
echo   Password: any password
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
