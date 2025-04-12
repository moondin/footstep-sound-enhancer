# Downloading and Building the Footstep Sound Enhancer

## 🔍 Fixing PyAudio Import Issues

If you encounter a `ModuleNotFoundError: No module named 'pyaudio'` when running the executable, follow these instructions:

### Option 1: Build with Hidden Imports

When building the executable, add the `--hidden-import` flags:

```bash
pyinstaller --name=FootstepSoundEnhancer --onefile --noconsole --clean --hidden-import=pyaudio --hidden-import=numpy --hidden-import=scipy --hidden-import=scipy.signal main.py
```

### Option 2: Use the Updated Build Scripts

The repository has been updated with build scripts that include the necessary hidden imports:

- **Windows**: Run `build_exe.bat` or `build_with_spec.bat`
- **Linux/Mac**: Run `build_exe.sh` or `build_with_spec.sh`
- **Cross-platform**: Run `python build_exe.py`

### Option 3: Use the Spec File

The `FootstepSoundEnhancer.spec` file has been updated to include the required modules. Build with:

```bash
pyinstaller FootstepSoundEnhancer.spec
```

## 📥 Downloading the Pre-built Executable

You can download the latest pre-built executable from the GitHub releases page:

[https://github.com/moondin/footstep-sound-enhancer/releases](https://github.com/moondin/footstep-sound-enhancer/releases)

## 🔧 GitHub Actions Workflow Updates

If you're using GitHub Actions to build the executable, make sure to update your workflow files. Add these hidden imports to your PyInstaller command:

```yaml
- name: Build executable
  run: |
    pyinstaller --name=FootstepSoundEnhancer --onefile --noconsole --clean --hidden-import=pyaudio --hidden-import=numpy --hidden-import=scipy --hidden-import=scipy.signal main.py
```

## ✅ Verifying the Fix

To verify that the executable works correctly:

1. Build the executable using one of the methods above
2. Run the executable without requiring administrator privileges
3. Confirm that it launches without any "module not found" errors