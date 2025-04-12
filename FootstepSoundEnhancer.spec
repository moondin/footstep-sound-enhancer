# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Footstep Sound Enhancer.
This file defines how PyInstaller should bundle the application.
"""

import os
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

# Base directory
base_dir = os.path.abspath(os.path.dirname(__file__))

# Icon path (if it exists)
icon_path = os.path.join(base_dir, 'generated-icon.png') if os.path.exists(os.path.join(base_dir, 'generated-icon.png')) else None

# Analysis stage - find all dependencies
a = Analysis(
    ['main.py'],
    pathex=[base_dir],
    binaries=[],
    datas=[],
    hiddenimports=['numpy', 'scipy.signal', 'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# PYZ stage - create the Python ZIP archive
pyz = PYZ(
    a.pure, 
    a.zipped_data,
    cipher=None
)

# EXE stage - create the executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FootstepSoundEnhancer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path if sys.platform == 'win32' and icon_path else None,
)