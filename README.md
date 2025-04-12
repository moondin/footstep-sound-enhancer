# Footstep Sound Enhancer

A desktop application that enhances footstep sounds in games by analyzing and selectively amplifying audio in real-time.

## Features

- Real-time audio processing to enhance footstep sounds
- Adjustable enhancement factor to control amplification
- Configurable detection threshold for sound sensitivity
- Clean, modern user interface with visual feedback

## Requirements

- Python 3.6 or higher
- PyAudio
- NumPy
- SciPy
- PyInstaller (for creating executable)

## Installation

### Method 1: Running from Source

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install required libraries:
   ```
   pip install pyaudio numpy scipy
   ```
3. Clone or download this repository
4. Run the application:
   ```
   python main.py
   ```

### Method 2: Create an Executable

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Run the build script:
   ```
   python build_exe.py
   ```
3. The executable will be available in the `dist` folder
4. Double-click `FootstepSoundEnhancer.exe` to run the application

## Usage

1. Start the application
2. Click "Start Enhancement" to begin processing audio
3. Adjust the "Enhancement Factor" slider to control how much footstep sounds are amplified
4. Adjust the "Detection Threshold" slider to set the sensitivity for footstep detection
5. The green indicator light will illuminate when a potential footstep is detected
6. Click "Stop Enhancement" when you're done

## How It Works

The application uses bandpass filtering to isolate the typical frequency range of footsteps (200-800 Hz). When the energy in this frequency band exceeds the detection threshold, the sound is amplified by the enhancement factor. This selective amplification makes footsteps more audible without increasing background noise or other game sounds.

## Limitations

- The audio detection is not perfect and may sometimes detect other sounds in the footstep frequency range
- Does not connect to game memory or modify game files in any way
- Processes all system audio, so it works with any game

## Troubleshooting

### No Audio Input/Output
- Ensure your audio devices are properly connected and enabled
- Make sure no other application is exclusively using your audio devices

### Performance Issues
- Try lowering the enhancement factor
- Close other CPU-intensive applications

## License

This project is educational in nature. Use responsibly and in accordance with the terms of service of any games you play.

## Disclaimer

This application does not modify any game files or interact with game memory. It simply processes audio output. However, using any third-party tools with competitive games may violate the terms of service of those games. Use at your own risk.