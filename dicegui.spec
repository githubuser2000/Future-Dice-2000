# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/home/alex/workspace-noneclipse/erodice/dicegui.py'],
             pathex=['/home/alex/workspace-noneclipse/erodice'],
             binaries=[],
             datas=[('/home/alex/workspace-noneclipse/erodice/dice-jp.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-cn.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-de.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-cz.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-il.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-pl.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-nl.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-kr.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-es.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-pt.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-fr.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-il.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-in.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-it.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dice-ru.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dicepy-en.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dicepy-de.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/dicepy-kr.qm', '.'), ('/home/alex/workspace-noneclipse/erodice/china.png', '.'), ('/home/alex/workspace-noneclipse/erodice/deutschland.png', '.'), ('/home/alex/workspace-noneclipse/erodice/frankreich.png', '.'), ('/home/alex/workspace-noneclipse/erodice/indien.png', '.'), ('/home/alex/workspace-noneclipse/erodice/israel.png', '.'), ('/home/alex/workspace-noneclipse/erodice/italien.png', '.'), ('/home/alex/workspace-noneclipse/erodice/japan.png', '.'), ('/home/alex/workspace-noneclipse/erodice/korea.png', '.'), ('/home/alex/workspace-noneclipse/erodice/niederlande.png', '.'), ('/home/alex/workspace-noneclipse/erodice/polen.png', '.'), ('/home/alex/workspace-noneclipse/erodice/portugal.png', '.'), ('/home/alex/workspace-noneclipse/erodice/russland.png', '.'), ('/home/alex/workspace-noneclipse/erodice/spanien.png', '.'), ('/home/alex/workspace-noneclipse/erodice/tschechien.png', '.'), ('/home/alex/workspace-noneclipse/erodice/usa.png', '.'), ('/home/alex/workspace-noneclipse/erodice/main.qml', '.'), ('/home/alex/workspace-noneclipse/erodice/dice.ui', '.'), ('/home/alex/workspace-noneclipse/erodice/dice.qm', '.')],
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
          name='dicegui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='/home/alex/workspace-noneclipse/erodice/wuerfel.png')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='dicegui')
