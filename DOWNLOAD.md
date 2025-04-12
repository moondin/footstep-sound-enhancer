# Download Footstep Sound Enhancer

There are two ways to get the Footstep Sound Enhancer application:

## Option 1: Download the Pre-built Executable (Recommended)

The simplest way to get started is to download the ready-to-use executable file:

1. Go to the [Releases](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/releases) page
2. Find the latest release and download `FootstepSoundEnhancer.exe`
3. Run the downloaded file to start the application - no installation needed!

### System Requirements

- Windows 7/8/10/11 (64-bit recommended)
- Audio input and output devices

## Option 2: Build from Source Code

If you prefer to build the application yourself:

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/footstep-sound-enhancer.git
   ```
   
2. Install the required dependencies:
   ```
   pip install pyaudio numpy scipy pyinstaller
   ```
   
3. Build the executable:
   - Windows: Run `build_exe.bat` or `build_with_spec.bat`
   - macOS/Linux: Run `./build_exe.sh` or `./build_with_spec.sh`
   
4. Find the executable in the `dist` folder

## Latest Version

The current version is: **v1.0.0**

## Troubleshooting

If you encounter issues when running the application:

1. Make sure your audio devices are working properly
2. Try running as Administrator (on Windows)
3. Check the [User Guide](USER_GUIDE.md) for more detailed troubleshooting steps
4. Report issues in the [GitHub Issues](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/issues) section

## Feedback and Support

If you have questions or feedback, please:
- Open an issue on GitHub
- Contact support at [your-email@example.com]