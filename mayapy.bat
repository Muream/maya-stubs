@ECHO OFF

set MAYA_APP_DIR=%~dp0temp\maya
set MAYA_MODULE_PATH=%~dp0;%MAYA_MODULE_PATH%

@REM We only add the current dir to the PYTHONPATH so that the sitecustomize.py gets 
@REM executed. This is where we add the .venv's site-packages to the PYTHONPATH with
@REM `site.addsitedir` so that it handles `.pth` files properly
set PYTHONPATH=%~dp0;%PYTHONPATH%

mayapy.exe -2023 %*
