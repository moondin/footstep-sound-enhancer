@echo off
echo Building Footstep Sound Enhancer executable using spec file...
echo.

REM Check if Python is installed
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo PyInstaller not found. Attempting to install...
    pip install pyinstaller
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to install PyInstaller.
        pause
        exit /b 1
    )
)

REM Create an icon for the application if it doesn't exist
if not exist "generated-icon.png" (
    echo Creating application icon...
    echo ^<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256"^> > temp_icon.svg
    echo ^<rect width="256" height="256" fill="#4A5568" rx="20" ry="20"/^> >> temp_icon.svg
    echo ^<circle cx="128" cy="128" r="96" fill="#2D3748" stroke="#A0AEC0" stroke-width="6"/^> >> temp_icon.svg
    echo ^<path d="M80,128 C88,100 100,85 128,85 C156,85 168,100 176,128 C168,156 156,171 128,171 C100,171 88,156 80,128 Z" fill="none" stroke="#4FD1C5" stroke-width="8"/^> >> temp_icon.svg
    echo ^<circle cx="128" cy="128" r="32" fill="#2D3748" stroke="#4FD1C5" stroke-width="4"/^> >> temp_icon.svg
    echo ^<path d="M200,60 L210,50 M46,205 L56,195 M200,195 L210,205 M46,50 L56,60" stroke="#A0AEC0" stroke-width="4"/^> >> temp_icon.svg
    echo ^<path d="M100,100 L70,70 M156,156 L186,186 M156,100 L186,70 M100,156 L70,186" stroke="#4FD1C5" stroke-width="4"/^> >> temp_icon.svg
    echo ^<circle cx="128" cy="128" r="8" fill="#4FD1C5"/^> >> temp_icon.svg
    echo ^</svg^> >> temp_icon.svg
    
    REM Convert SVG to PNG (requires ImageMagick, fallback to just using the SVG)
    magick convert temp_icon.svg generated-icon.png > nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo Note: ImageMagick not found. Using SVG icon instead.
        copy temp_icon.svg generated-icon.svg > nul
    ) else (
        del temp_icon.svg
    )
)

REM Build the executable using the spec file
echo.
echo Building executable with PyInstaller using spec file...
pyinstaller --hidden-import=pyaudio --hidden-import=numpy --hidden-import=scipy --hidden-import=scipy.signal FootstepSoundEnhancer.spec

REM Check if build was successful
if not exist "dist\FootstepSoundEnhancer.exe" (
    echo.
    echo Build failed! Executable not created.
    pause
    exit /b 1
)

echo.
echo Build successful! Executable created at: dist\FootstepSoundEnhancer.exe
echo.
pause