"""
PyInstaller hook for PyAudio
This ensures that PyAudio is properly included in the executable
"""
from PyInstaller.utils.hooks import collect_dynamic_libs

# Force inclusion of the PyAudio module
hiddenimports = ['pyaudio', '_portaudio', 'numpy', 'scipy', 'scipy.signal']

# Collect all binary dependencies
binaries = collect_dynamic_libs('pyaudio')
datas = []