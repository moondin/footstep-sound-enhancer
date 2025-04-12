#!/bin/bash

echo "Building Footstep Sound Enhancer executable..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH."
    echo "Please install Python from https://www.python.org/downloads/"
    echo
    exit 1
fi

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" &> /dev/null; then
    echo "PyInstaller not found. Attempting to install..."
    pip3 install pyinstaller
    if [ $? -ne 0 ]; then
        echo "Failed to install PyInstaller."
        exit 1
    fi
fi

# Create an icon for the application if it doesn't exist
if [ ! -f "generated-icon.png" ] && [ ! -f "generated-icon.svg" ]; then
    echo "Creating application icon..."
    cat > temp_icon.svg << EOF
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
<rect width="256" height="256" fill="#4A5568" rx="20" ry="20"/>
<circle cx="128" cy="128" r="96" fill="#2D3748" stroke="#A0AEC0" stroke-width="6"/>
<path d="M80,128 C88,100 100,85 128,85 C156,85 168,100 176,128 C168,156 156,171 128,171 C100,171 88,156 80,128 Z" fill="none" stroke="#4FD1C5" stroke-width="8"/>
<circle cx="128" cy="128" r="32" fill="#2D3748" stroke="#4FD1C5" stroke-width="4"/>
<path d="M200,60 L210,50 M46,205 L56,195 M200,195 L210,205 M46,50 L56,60" stroke="#A0AEC0" stroke-width="4"/>
<path d="M100,100 L70,70 M156,156 L186,186 M156,100 L186,70 M100,156 L70,186" stroke="#4FD1C5" stroke-width="4"/>
<circle cx="128" cy="128" r="8" fill="#4FD1C5"/>
</svg>
EOF
    
    # Try to convert SVG to PNG (requires ImageMagick, fallback to just using the SVG)
    if command -v convert &> /dev/null; then
        convert temp_icon.svg generated-icon.png
        rm temp_icon.svg
    else
        echo "Note: ImageMagick not found. Using SVG icon instead."
        mv temp_icon.svg generated-icon.svg
    fi
fi

# Build the executable
echo
echo "Building executable with PyInstaller..."
python3 -m PyInstaller --name=FootstepSoundEnhancer --onefile --noconsole --clean --hidden-import=pyaudio --hidden-import=numpy --hidden-import=scipy --hidden-import=scipy.signal main.py

# Check if build was successful
if [ ! -f "dist/FootstepSoundEnhancer" ]; then
    echo
    echo "Build failed! Executable not created."
    exit 1
fi

echo
echo "Build successful! Executable created at: dist/FootstepSoundEnhancer"
echo