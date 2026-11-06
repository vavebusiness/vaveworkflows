@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py HQ_LOCAL_SERVER.py
) else (
  python HQ_LOCAL_SERVER.py
)
pause