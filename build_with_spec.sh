#!/bin/bash

echo "Building Footstep Sound Enhancer executable using spec file..."
echo ""

# Check if PyInstaller is installed
if ! pip show pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
    if [ $? -ne 0 ]; then
        echo "Failed to install PyInstaller."
        echo "Please install PyInstaller manually: pip install pyinstaller"
        exit 1
    fi
fi

# Run PyInstaller with our spec file
echo "Running PyInstaller with spec file..."
pyinstaller FootstepSoundEnhancer.spec

# Check if build was successful
if [ $? -ne 0 ]; then
    echo ""
    echo "Build failed."
    exit 1
fi

echo ""
echo "Build completed successfully!"
echo ""
echo "The executable can be found in the 'dist' folder:"
echo "$(pwd)/dist/FootstepSoundEnhancer"
echo ""