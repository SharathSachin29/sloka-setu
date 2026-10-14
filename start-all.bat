@echo off
echo ========================================================
echo   Launching SlokaSetu Full Stack Application
echo ========================================================
start "SlokaSetu Backend API" cmd /k "cd /d ""%~dp0backend"" && npm run dev"
timeout /t 3 /nobreak >nul
start "SlokaSetu Frontend UI" cmd /k "cd /d ""%~dp0frontend"" && npm run dev"
echo Backend and Frontend launched in dedicated windows.
echo - Backend:  http://localhost:5000
echo - Frontend: http://localhost:5173
