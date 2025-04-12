"""
Build script for creating a standalone executable of the Footstep Sound Enhancer.
This script uses PyInstaller to package the application into an .exe file.
"""

import os
import sys
import PyInstaller.__main__

def build_executable():
    """Build the executable using PyInstaller."""
    # Define icon file path if available
    icon_path = os.path.abspath("generated-icon.png") if os.path.exists("generated-icon.png") else None
    
    # Base arguments for PyInstaller
    args = [
        "main.py",  # Main script
        "--name=FootstepSoundEnhancer",  # Output executable name
        "--onefile",  # Bundle everything into a single executable
        "--noconsole",  # Don't show console window when running
        "--clean",  # Clean PyInstaller cache before building
    ]
    
    # Add icon if available
    if icon_path:
        args.append(f"--icon={icon_path}")
    
    # Add data files if needed
    # args.append("--add-data=path/to/file;destination/folder")
    
    print(f"Building executable with arguments: {args}")
    
    # Run PyInstaller with our arguments
    PyInstaller.__main__.run(args)
    
    print("\nBuild completed!")
    print("The executable can be found in the 'dist' directory.")

if __name__ == "__main__":
    try:
        build_executable()
    except Exception as e:
        print(f"Error building executable: {e}")
        sys.exit(1)