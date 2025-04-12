# Footstep Sound Enhancer - User Guide

## Introduction

Footstep Sound Enhancer is a desktop application designed to help gamers hear footstep sounds more clearly. It analyzes audio in real-time and selectively amplifies frequencies typically associated with footsteps, providing a competitive advantage in games where hearing enemy movement is important.

## Getting Started

### System Requirements

- Windows 7, 8, 10, or 11 (64-bit recommended)
- macOS 10.13 or later
- Audio input and output devices

### Starting the Application

1. Double-click the `FootstepSoundEnhancer.exe` file (Windows) or `FootstepSoundEnhancer` file (macOS/Linux).
2. The application will open with a simple interface showing controls and status information.

## User Interface Overview

![Application Interface](interface_diagram.png)

The interface consists of:

1. **Status Indicator**: Shows whether the enhancement is active or stopped.
2. **Footstep Detection Indicator**: A circular light that turns green when footsteps are detected.
3. **Audio Level Meter**: Shows the current audio level being analyzed.
4. **Enhancement Controls**:
   - **Enhancement Factor**: Controls how much footstep sounds are amplified.
   - **Detection Threshold**: Controls the sensitivity of footstep detection.
5. **Control Buttons**:
   - **Start Enhancement**: Begins the audio analysis and enhancement.
   - **Stop Enhancement**: Stops the audio processing.
6. **Information Text**: Provides a brief explanation of the application's function.

## Using the Application

### Basic Operation

1. Launch the application.
2. Click the **Start Enhancement** button to begin analyzing audio.
3. Play your game as normal. The application will automatically detect and enhance footstep sounds.
4. When you're done, click the **Stop Enhancement** button.

### Adjusting Settings

#### Enhancement Factor (1.0 - 5.0)

This controls how much the detected footstep sounds are amplified:
- **1.0**: No enhancement (original volume)
- **2.0**: Default setting (double volume)
- **3.0 - 5.0**: Higher enhancement (useful for very quiet footsteps)

Recommendation: Start with the default 2.0 setting and adjust as needed. Higher values may cause distortion.

#### Detection Threshold (0.01 - 0.2)

This controls how sensitive the footstep detection is:
- **Lower values** (0.01 - 0.05): More sensitive, may detect more footsteps but also more false positives
- **Higher values** (0.1 - 0.2): Less sensitive, fewer false positives but might miss quiet footsteps

Recommendation: Start with the default 0.05 setting and adjust based on your game and audio setup.

### Visual Feedback

- **Footstep Indicator**: Turns green when potential footstep sounds are detected.
- **Audio Level Meter**: Shows the current audio level in the footstep frequency range.
  - Green/Yellow: Normal levels
  - Red: High volume levels

## Optimal Setup for Gaming

### Game Audio Settings

For best results:
1. In your game settings, set audio to stereo (not surround).
2. Reduce music volume and increase sound effects volume.
3. If available, enable "footstep sounds" or similar options in the game settings.

### Physical Setup

1. Use headphones for best directional audio perception.
2. Ensure your microphone (if any) won't pick up sounds from your speakers to prevent feedback loops.

## Troubleshooting

### Common Issues

#### No Enhancement Effect

- Check if the status shows "Running"
- Try increasing the Enhancement Factor
- Try lowering the Detection Threshold

#### False Positives (Too Many Sounds Enhanced)

- Increase the Detection Threshold
- Reduce the Enhancement Factor

#### Application Not Starting

- Make sure your system meets the requirements
- Check if you have the necessary permissions to run applications
- Windows: Try running as Administrator

#### Audio Distortion

- Lower the Enhancement Factor
- Make sure your system volume is not too high

### Error Messages

- **"Audio stream error"**: Check your audio devices and ensure no other application has exclusive access to your audio.
- **"Failed to initialize audio"**: Restart the application or your computer.

## Support

If you encounter issues not covered in this guide, please:
1. Check the README file for additional information
2. Contact support at [support@footstepenhancer.com](mailto:support@footstepenhancer.com)

## Legal Considerations

This application does not modify game files or memory. It only processes audio output from your system. However, be aware that some games' terms of service may prohibit the use of third-party software that provides gameplay advantages. Use at your own risk.