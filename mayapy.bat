@ECHO OFF

set MAYA_APP_DIR=%~dp0\temp\maya
set MAYA_MODULE_PATH=%~dp0;%MAYA_MODULE_PATH%
set PYTHONPATH=%~dp0\.venv\Lib\site-packages;%PYTHONPATH%

for /f "tokens=2*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\2023\Setup\InstallPath" /v MAYA_INSTALL_LOCATION') do set "MAYA_LOCATION=%%~b"
"%MAYA_LOCATION%\bin\mayapy.exe" %*