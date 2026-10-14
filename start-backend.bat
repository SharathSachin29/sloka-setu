@echo off
title SlokaSetu Backend API (Port 5000)
cd /d "%~dp0backend"
echo ========================================================
echo   Starting SlokaSetu Backend API on http://localhost:5000
echo ========================================================
npm run dev
pause
