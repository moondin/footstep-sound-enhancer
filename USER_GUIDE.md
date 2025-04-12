# Footstep Sound Enhancer - User Guide

This guide will help you get the most out of the Footstep Sound Enhancer application, which enhances footstep sounds in games for better awareness.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Main Interface](#main-interface)
3. [Audio Settings](#audio-settings)
4. [Enhancing Footsteps](#enhancing-footsteps)
5. [Advanced Settings](#advanced-settings)
6. [Performance Tips](#performance-tips)
7. [Troubleshooting](#troubleshooting)

## Getting Started

1. Download and install the application by following the [Installation Guide](INSTALLATION.md)
2. Launch the application (FootstepSoundEnhancer.exe)
3. Set up your audio devices and preferences (see below)

## Main Interface

The main window of the application includes:

- **Power Button**: Turns the enhancement on/off
- **Enhancement Slider**: Controls how much the footstep sounds are amplified
- **Threshold Slider**: Adjusts how sensitive the detection is
- **Status Indicator**: Shows if the enhancer is currently active
- **Audio Level Meter**: Displays the current audio input level
- **Footstep Detection Indicator**: Lights up when footsteps are detected

## Audio Settings

For optimal performance:

1. **Select Input Device**: Choose the audio source where your game sound is playing
   - This could be your default audio output, a virtual audio cable, or a specific device

2. **Input Level**: Adjust your game volume so the audio level meter shows good activity
   - Too low: The application might miss footstep sounds
   - Too high: The audio might sound distorted when enhanced

3. **Output Device**: By default, the enhanced audio goes to your default playback device
   - For advanced setups, you can configure this in the settings menu

## Enhancing Footsteps

Follow these steps to get the best footstep enhancement:

1. **Start a Game**: Launch your game and go to an area with footstep sounds
2. **Turn On Enhancement**: Click the power button to activate enhancement
3. **Adjust Enhancement Level**:
   - Start at a lower level (around 30%)
   - Gradually increase until footsteps are clearly audible but not overwhelming
   - Recommended range: 30-70% (higher values might cause distortion)
4. **Set Threshold**:
   - Higher threshold: Only stronger footstep sounds are enhanced (fewer false positives)
   - Lower threshold: More sensitive detection (might enhance unwanted sounds)
   - Find the right balance for your game and environment

## Advanced Settings

Access advanced settings by clicking the gear icon:

- **Frequency Range**: Fine-tune the frequency range for footstep detection
  - Lower range (50-300 Hz): Better for heavy footsteps, explosions
  - Mid range (300-800 Hz): Optimal for most footsteps
  - Higher range (800-2000 Hz): Better for light footsteps, stealth movement
  
- **Processing Mode**:
  - Balance: Standard processing (recommended)
  - Performance: Lower CPU usage but less precise
  - Quality: Higher precision but more CPU intensive

## Performance Tips

To get the best experience:

1. **Close unnecessary applications** to free up CPU resources
2. **Use headphones** for better directional audio
3. **Adjust game audio mix** to reduce music and increase effect volume
4. If you experience audio lag, try:
   - Lowering the enhancement level
   - Switching to Performance mode
   - Reducing other audio processes running on your system

## Troubleshooting

### Common Issues

1. **No sound enhancement**:
   - Check if the power button is on (glowing)
   - Make sure the enhancement level is set high enough
   - Verify your audio devices are correctly selected
   - Try increasing the threshold sensitivity

2. **Distorted sound**:
   - Lower the enhancement level
   - Reduce your game volume
   - Check for conflicting audio software

3. **High CPU usage**:
   - Switch to Performance mode
   - Close other CPU-intensive applications
   - Update your audio drivers

4. **Application doesn't start**:
   - Make sure you have the required Visual C++ Redistributable installed
   - Run as administrator
   - Check if your antivirus is blocking the application

### Getting Help

If you encounter issues not covered in this guide:

1. Check the [Installation Guide](INSTALLATION.md) for system requirements
2. Visit our [GitHub repository](https://github.com/YOUR_USERNAME/footstep-sound-enhancer) for updates
3. Open an issue on GitHub to report bugs or request features
4. Contact support at [your-email@example.com]