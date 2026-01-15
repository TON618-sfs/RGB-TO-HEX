# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['c:\\\\Users\\filem\\Desktop\\RGB-TO-HEX\\RGB TO HEX GUI\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='RGB TO HEX',
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
    version='C:\\Users\\filem\\AppData\\Local\\Temp\\bb23a949-32b0-41dd-9362-6b09946b4034',
    icon=['C:\\Users\\filem\\Desktop\\RGB-TO-HEX\\RGB TO HEX GUI\\icone.ico'],
)
