"""
Build script for creating a standalone executable of the Footstep Sound Enhancer.
This script uses PyInstaller to package the application into an .exe file.
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path

def create_icon():
    """Create an icon for the application if it doesn't exist."""
    if os.path.exists("generated-icon.png") or os.path.exists("generated-icon.svg"):
        return
    
    print("Creating application icon...")
    
    # SVG icon content
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
<rect width="256" height="256" fill="#4A5568" rx="20" ry="20"/>
<circle cx="128" cy="128" r="96" fill="#2D3748" stroke="#A0AEC0" stroke-width="6"/>
<path d="M80,128 C88,100 100,85 128,85 C156,85 168,100 176,128 C168,156 156,171 128,171 C100,171 88,156 80,128 Z" fill="none" stroke="#4FD1C5" stroke-width="8"/>
<circle cx="128" cy="128" r="32" fill="#2D3748" stroke="#4FD1C5" stroke-width="4"/>
<path d="M200,60 L210,50 M46,205 L56,195 M200,195 L210,205 M46,50 L56,60" stroke="#A0AEC0" stroke-width="4"/>
<path d="M100,100 L70,70 M156,156 L186,186 M156,100 L186,70 M100,156 L70,186" stroke="#4FD1C5" stroke-width="4"/>
<circle cx="128" cy="128" r="8" fill="#4FD1C5"/>
</svg>"""
    
    # Write SVG content to a file
    with open("temp_icon.svg", "w") as f:
        f.write(svg_content)
    
    # Try to convert to PNG if ImageMagick is available
    try:
        # Try different ImageMagick commands for different platforms
        if platform.system() == "Windows":
            subprocess.run(["magick", "convert", "temp_icon.svg", "generated-icon.png"], check=True)
        else:
            subprocess.run(["convert", "temp_icon.svg", "generated-icon.png"], check=True)
        os.remove("temp_icon.svg")
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Note: ImageMagick not found. Using SVG icon instead.")
        os.rename("temp_icon.svg", "generated-icon.svg")

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Attempting to install...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        except subprocess.SubprocessError:
            print("Failed to install PyInstaller. Please install it manually.")
            return False
    
    # Check if other dependencies are installed
    required_modules = ["numpy", "scipy", "pyaudio"]
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"The following dependencies are missing: {', '.join(missing_modules)}")
        print("Please install them using: pip install " + " ".join(missing_modules))
        return False
    
    return True

def build_executable():
    """Build the executable using PyInstaller."""
    # Create the icon
    create_icon()
    
    # Check if dependencies are installed
    if not check_dependencies():
        return False
    
    # Clean previous build artifacts
    for dir_name in ["build", "dist"]:
        if os.path.exists(dir_name):
            print(f"Cleaning {dir_name} directory...")
            shutil.rmtree(dir_name)
    
    # Build the executable
    print("\nBuilding executable with PyInstaller...")
    
    # Check if spec file exists
    if os.path.exists("FootstepSoundEnhancer.spec"):
        # Build using spec file
        pyinstaller_args = ["pyinstaller", "FootstepSoundEnhancer.spec"]
    else:
        # Build directly
        icon_path = "generated-icon.png" if os.path.exists("generated-icon.png") else "generated-icon.svg"
        pyinstaller_args = [
            "pyinstaller",
            "--name=FootstepSoundEnhancer",
            "--onefile",
            "--noconsole",
            "--clean",
            "--hidden-import=pyaudio",
            "--hidden-import=numpy", 
            "--hidden-import=scipy",
            "--hidden-import=scipy.signal"
        ]
        
        if os.path.exists(icon_path):
            pyinstaller_args.append(f"--icon={icon_path}")
        
        pyinstaller_args.append("main.py")
    
    try:
        subprocess.run(pyinstaller_args, check=True)
    except subprocess.SubprocessError as e:
        print(f"Error building executable: {e}")
        return False
    
    # Check if build was successful
    if platform.system() == "Windows":
        exe_path = Path("dist") / "FootstepSoundEnhancer.exe"
    else:
        exe_path = Path("dist") / "FootstepSoundEnhancer"
    
    if not exe_path.exists():
        print("Build failed! Executable not created.")
        return False
    
    print(f"\nBuild successful! Executable created at: {exe_path}")
    return True

if __name__ == "__main__":
    print("Building Footstep Sound Enhancer executable...")
    success = build_executable()
    sys.exit(0 if success else 1)