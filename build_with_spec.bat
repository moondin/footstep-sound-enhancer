@echo off
echo Building Footstep Sound Enhancer executable using spec file...
echo.

:: Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo Failed to install PyInstaller.
        echo Please install PyInstaller manually: pip install pyinstaller
        pause
        exit /b 1
    )
)

:: Run PyInstaller with our spec file
echo Running PyInstaller with spec file...
pyinstaller FootstepSoundEnhancer.spec

:: Check if build was successful
if %errorlevel% neq 0 (
    echo.
    echo Build failed.
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo.
echo The executable can be found in the "dist" folder:
echo %CD%\dist\FootstepSoundEnhancer.exe
echo.
pause