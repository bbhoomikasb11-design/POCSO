@echo off
REM Shield 360 - Easy Start Script for Windows
REM This script will start both backend and frontend servers

echo.
echo 🚀 Starting Shield 360...
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js is not installed. Please install Node.js first.
    pause
    exit /b 1
)

REM Start Backend
echo 📦 Starting Backend Server...
cd shield360-backend

REM Check if node_modules exists
if not exist "node_modules" (
    echo ⚠️  Installing backend dependencies...
    call npm install
)

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  Creating .env file...
    (
        echo PORT=5000
        echo MONGODB_URI=mongodb://localhost:27017/shield360
        echo JWT_SECRET=shield360_secret_key_change_in_production
        echo NODE_ENV=development
    ) > .env
    echo ✅ Created .env file
    echo ⚠️  Please update MONGODB_URI if using MongoDB Atlas
)

echo ✅ Backend starting on http://localhost:5000
start "Shield360 Backend" cmd /k "npm start"
cd ..

REM Wait a bit for backend to start
timeout /t 3 /nobreak >nul

REM Start Frontend
echo.
echo 🎨 Starting Frontend Server...
cd shield360-frontend

REM Check if node_modules exists
if not exist "node_modules" (
    echo ⚠️  Installing frontend dependencies...
    call npm install
)

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  Creating .env file...
    echo VITE_API_URL=http://localhost:5000/api > .env
    echo ✅ Created .env file
)

echo ✅ Frontend starting on http://localhost:3000
start "Shield360 Frontend" cmd /k "npm run dev"
cd ..

echo.
echo ✅ Shield 360 is starting!
echo.
echo 📍 Frontend: http://localhost:3000
echo 📍 Backend API: http://localhost:5000
echo.
echo 💡 Tips:
echo    - Make sure MongoDB is running (or use MongoDB Atlas)
echo    - To seed the database, run: cd shield360-backend ^&^& node seed.js
echo    - Close the command windows to stop the servers
echo.
pause


