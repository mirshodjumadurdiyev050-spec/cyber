@echo off
setlocal enabledelayedexpansion
echo ==========================================
echo   CRYPTOGRAPHIC LAB STARTUP SCRIPT
echo ==========================================
echo.

:: 1. Try to find a working Python with pip
set "PYTHON_EXE=python"

echo [1/3] Python va Pip-ni tekshirish...

:: Check default python
!PYTHON_EXE! -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Default 'python' da pip topilmadi. Boshqa versiyalarni qidiryapman...
    
    :: Try the one we found in research
    set "ALT_PY=C:\Users\HP\AppData\Local\Python\pythoncore-3.14-64\python.exe"
    if exist "!ALT_PY!" (
        set "PYTHON_EXE=!ALT_PY!"
        echo Python 3.14 topildi: !PYTHON_EXE!
    ) else (
        :: Try 'pip' to find its python
        for /f "delims=" %%i in ('where pip 2^>nul') do (
            set "PIP_PATH=%%i"
            :: Usually pip is in Scripts, and python is one level up
            set "POTENTIAL_PY=%%~dpi"
            set "POTENTIAL_PY=!POTENTIAL_PY:Scripts\=!"
            if exist "!POTENTIAL_PY!python.exe" (
                set "PYTHON_EXE=!POTENTIAL_PY!python.exe"
                echo Pip orqali Python topildi: !PYTHON_EXE!
            )
        )
    )
)

:: Final check
!PYTHON_EXE! -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Ishlaydigan Python topilmadi! 
    echo Maslahat: Python-ni o'rnatayotganda 'Add to PATH' va 'pip' opsiyalarini tanlang.
    pause
    exit /b
)

echo [2/3] Kutubxonalarni o'rnatish (pip install)...
echo Iltimos kuting...
"!PYTHON_EXE!" -m pip install streamlit sympy cryptography pycryptodome fpdf2

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Kutubxonalarni o'rnatib bo'lmadi.
    pause
    exit /b
)

echo.
echo [3/3] Ilovani ishga tushirish (Streamlit)...
"!PYTHON_EXE!" -m streamlit run main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Ilovani ishga tushirib bo'lmadi.
    pause
)

pause
