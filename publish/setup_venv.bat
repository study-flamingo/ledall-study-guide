@echo off
REM Setup script for Windows Command Prompt

echo Setting up Python virtual environment for PDF conversion...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt

echo.
echo ✓ Virtual environment setup complete!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo Then run (from the publish/ directory):
echo   python convert_to_pdf.py
echo.
echo Or specify a file:
echo   python convert_to_pdf.py ..\Ledall_Longsword_manuscript.md

pause
