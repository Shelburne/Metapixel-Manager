@echo off
python -m PyInstaller --onefile --icon="myicon.ico" duck_tool.py

:: Move the EXE to the main folder and delete the leftovers
move /y dist\duck_tool.exe .
rd /s /q build
rd /s /q dist
del /q duck_tool.spec

echo Build Complete! Your EXE is in the main folder.
pause
