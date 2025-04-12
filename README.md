# Footstep Sound Enhancer

![GitHub release (latest by date)](https://img.shields.io/github/v/release/YOUR_USERNAME/footstep-sound-enhancer)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A desktop application that enhances footstep sounds in games by analyzing and selectively amplifying audio in real-time.

<p align="center">
  <img src="generated-icon.png" alt="Footstep Sound Enhancer Logo" width="200"/>
</p>

## Features

- **Real-time Audio Analysis**: Instantly detects footstep sounds in game audio
- **Selective Enhancement**: Amplifies only footstep frequencies, not all game audio
- **Customizable Sensitivity**: Adjust detection threshold to optimize for your game
- **Simple Interface**: User-friendly controls with visual indicators
- **Zero Latency**: Processes audio with minimal delay for competitive gaming
- **Standalone Application**: No installation required - just download and run

## Why Use Footstep Sound Enhancer?

Gaming is all about gaining a competitive edge, and in first-person shooters and battle royale games, hearing enemy footsteps can make the difference between winning and losing. The Footstep Sound Enhancer helps you:

- Detect approaching enemies sooner
- Identify the direction of movement more clearly
- Focus on important audio cues without turning the volume painfully high
- Maintain awareness of your surroundings in chaotic gameplay moments

## Download

**[Download the latest release](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/releases/latest)**

For detailed download and installation instructions, see the [Download Guide](DOWNLOAD.md).

## Quick Start

1. Download the .exe file from the [Releases](https://github.com/YOUR_USERNAME/footstep-sound-enhancer/releases) page
2. Run the application
3. Start your game
4. Use the sliders to adjust the enhancement level and detection threshold
5. Click the power button to activate enhancement

For detailed usage instructions, see the [User Guide](USER_GUIDE.md).

## Documentation

- [Installation Guide](INSTALLATION.md) - Detailed steps to get the application running
- [User Guide](USER_GUIDE.md) - How to use the application effectively
- [GitHub Release Guide](GITHUB_RELEASE_GUIDE.md) - For developers: publishing releases
- [Download Guide](DOWNLOAD.md) - How to download and verify the application

## Development

### Requirements

- Python 3.9 or higher
- Libraries: NumPy, SciPy, PyAudio
- PyInstaller (for building the executable)

### Building from Source

To build the application from source:

1. Clone this repository
2. Install dependencies: `pip install pyaudio numpy scipy pyinstaller`
3. Run the build script:
   - Windows: `build_exe.bat` or `build_with_spec.bat`
   - macOS/Linux: `./build_exe.sh` or `./build_with_spec.sh`
4. Find the executable in the `dist` folder

## How It Works

The Footstep Sound Enhancer uses advanced signal processing techniques to:

1. **Capture** the audio stream from your game
2. **Analyze** the frequency spectrum in real-time
3. **Identify** patterns that match footstep sounds
4. **Enhance** those specific frequencies
5. **Output** the modified audio to your headphones or speakers

The application uses bandpass filtering to isolate the frequency range typical of footstep sounds (typically 200-800 Hz) and a dynamic threshold detection algorithm to identify transient sounds characteristic of footsteps.

## Contributing

Contributions are welcome! If you'd like to help improve the Footstep Sound Enhancer:

1. Fork the repository
2. Create a feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the NumPy and SciPy communities for their excellent signal processing libraries
- PyAudio for providing the audio I/O functionality
- PyInstaller for enabling the creation of standalone executables