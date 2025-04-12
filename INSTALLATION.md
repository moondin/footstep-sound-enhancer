# Footstep Sound Enhancer - Installation Guide

This guide provides step-by-step instructions for installing and setting up the Footstep Sound Enhancer application.

## Windows Installation (Recommended)

### Prerequisites

- Windows 7, 8, 10, or 11 (64-bit recommended)
- Administrative privileges may be required
- Working audio input and output devices

### Method 1: Using the Executable (Easiest)

1. Download the latest `FootstepSoundEnhancer.exe` from the [Releases](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/releases) page
2. Double-click the downloaded file to run it
3. If Windows SmartScreen appears:
   - Click "More info"
   - Click "Run anyway"
4. No installation is required - the application will start immediately

### Method 2: Building from Source Code

If you prefer to build the application yourself:

1. Install Python 3.9 or newer from [python.org](https://www.python.org/downloads/)
   - Make sure to check the option "Add Python to PATH" during installation

2. Install the required dependencies:
   ```
   pip install pyaudio numpy scipy pyinstaller
   ```
   
   Note: PyAudio may require additional steps to install:
   - Windows: `pip install pipwin` followed by `pipwin install pyaudio`

3. Clone or download this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/footstep-sound-enhancer.git
   ```
   
4. Navigate to the project directory:
   ```
   cd footstep-sound-enhancer
   ```
   
5. Build the executable:
   - Run the `build_exe.bat` script, or
   - Run the command: `pyinstaller --name=FootstepSoundEnhancer --onefile --noconsole --clean main.py`
   
6. The executable will be created in the `dist` folder

## First-Time Setup

1. When you first run the application, you may need to:
   - Allow the application through your firewall
   - Grant permissions to access audio devices
   
2. Configure your audio settings:
   - Select the appropriate input device (your game audio source)
   - Adjust the enhancement and threshold levels to your preference

## Optional Configurations

### Creating a Desktop Shortcut

1. Right-click on `FootstepSoundEnhancer.exe` 
2. Select "Create shortcut"
3. Move the shortcut to your desktop

### Running at Startup

To have the application launch automatically when your computer starts:

1. Press `Win+R` to open the Run dialog
2. Type `shell:startup` and press Enter
3. Copy a shortcut to the application into this folder

## Troubleshooting

### Common Issues

1. **"Error accessing audio device"**
   - Make sure your audio devices are properly connected
   - Check if other applications are using the same audio device
   - Try selecting a different audio device in the application settings

2. **"DLL not found" error**
   - Install the Visual C++ Redistributable for Visual Studio 2015-2019:
     [Download from Microsoft](https://aka.ms/vs/16/release/vc_redist.x64.exe)

3. **Application appears unresponsive**
   - Close other applications that might be using audio devices
   - Restart your computer and try again

### Getting Help

If you encounter issues not covered in this guide:

1. Check the [User Guide](USER_GUIDE.md) for more detailed information
2. Open an issue on the [GitHub repository](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/issues)
3. Contact support at [your-email@example.com]