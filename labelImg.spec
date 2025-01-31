# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['labelImg.py'],
             pathex=['./'],
             binaries=[],
             datas=[('data/.*', 'data'),
                    ('data/*', 'data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='样本标绘',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='resources\\icons\\k-app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=['qwindows.dll','qjpeg.dll'],
               name='样本标绘工具')
