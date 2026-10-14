@echo off
title SlokaSetu Frontend UI (Port 5173)
cd /d "%~dp0frontend"
echo ========================================================
echo   Starting SlokaSetu Frontend UI on http://localhost:5173
echo ========================================================
npm run dev
pause
