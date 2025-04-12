# Footstep Sound Enhancer - Installation Guide

This guide will help you install and use the Footstep Sound Enhancer application.

## Download Options

### Option 1: Download the Pre-built Executable (Recommended for most users)

1. Download the `FootstepSoundEnhancer.exe` file from the latest release.
2. Save it to a location on your computer where you'll remember it.
3. Double-click the file to run the application.
4. No installation is required - the application will start immediately.

### Option 2: Build from Source (For developers or advanced users)

#### Prerequisites:
- Python 3.6 or higher installed
- Basic knowledge of command line operations

#### Windows:
1. Download or clone this repository to your computer.
2. Open Command Prompt and navigate to the downloaded folder.
3. Run the following commands:
```
pip install pyaudio numpy scipy pyinstaller
build_exe.bat
```
4. After the build completes, find the executable in the `dist` folder.

#### macOS/Linux:
1. Download or clone this repository to your computer.
2. Open Terminal and navigate to the downloaded folder.
3. Run the following commands:
```
pip install pyaudio numpy scipy pyinstaller
chmod +x build_exe.sh
./build_exe.sh
```
4. After the build completes, find the executable in the `dist` folder.

## Running the Application

1. When you first run the application, you might see a security warning from your operating system.
   - On Windows: Click "More info" and then "Run anyway".
   - On macOS: Right-click the file, select "Open", and then click "Open" in the dialog.

2. The application will show a simple interface with these controls:
   - **Start Enhancement**: Begin monitoring and enhancing footstep sounds.
   - **Stop Enhancement**: Stop the audio processing.
   - **Enhancement Factor**: Adjust how much the footstep sounds are amplified (1.0 to 5.0).
   - **Detection Threshold**: Adjust how sensitive the footstep detection is (0.01 to 0.2).

3. The application shows visual feedback:
   - A green indicator light when a footstep is detected.
   - An audio level meter showing the current sound level.

## Troubleshooting

### Common Issues:

1. **No sound enhancement**: 
   - Make sure your system audio is working properly.
   - Try increasing the Enhancement Factor.
   - Try decreasing the Detection Threshold to make it more sensitive.

2. **False positives (enhancing non-footstep sounds)**:
   - Increase the Detection Threshold to make it less sensitive.

3. **Application won't start**:
   - Make sure you have the necessary permissions to run applications.
   - On Windows, try running as Administrator.
   - On macOS, verify your security settings allow applications from identified developers.

### Windows-Specific Issues:

If you get a "VCRUNTIME140.dll is missing" error, you need to install the Microsoft Visual C++ Redistributable:
1. Download it from [Microsoft's website](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).
2. Install the package appropriate for your system (x86 for 32-bit, x64 for 64-bit Windows).
3. Restart your computer if necessary.

## Uninstalling

The Footstep Sound Enhancer does not modify your system or registry. To uninstall:
1. Simply delete the executable file.
2. Delete any shortcuts you may have created.