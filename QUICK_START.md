# 🚀 Shield 360 - Quick Start Guide

## The Easiest Way to Run Shield 360

### Option 1: Using Start Scripts (Recommended) ⚡

#### For Linux/Mac:
```bash
chmod +x start.sh
./start.sh
```

#### For Windows:
```bash
start.bat
```

The script will:
- ✅ Install dependencies automatically
- ✅ Create .env files if they don't exist
- ✅ Start both backend and frontend servers
- ✅ Open the application in your browser

---

### Option 2: Manual Setup (Step by Step) 📝

#### Step 1: Install MongoDB
Choose one:
- **Local MongoDB**: Install from [mongodb.com](https://www.mongodb.com/try/download/community)
- **MongoDB Atlas** (Cloud - Recommended): Free at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)

#### Step 2: Setup Backend
```bash
cd shield360-backend
npm install
```

Create `.env` file:
```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/shield360
# OR for MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/shield360
JWT_SECRET=shield360_secret_key_change_in_production
NODE_ENV=development
```

Start backend:
```bash
npm start
```

#### Step 3: Setup Frontend (New Terminal)
```bash
cd shield360-frontend
npm install
```

Create `.env` file:
```env
VITE_API_URL=http://localhost:5000/api
```

Start frontend:
```bash
npm run dev
```

#### Step 4: Seed Database (Optional but Recommended)
In backend directory:
```bash
node seed.js
```

#### Step 5: Access the Application
- 🌐 Frontend: http://localhost:3000
- 🔌 Backend API: http://localhost:5000

---

## 🎯 What to Do After Starting

1. **Register an Account**
   - Go to http://localhost:3000
   - Click "Register"
   - Choose a role (Child, Guardian, Teacher, or Admin)

2. **Test the Features**
   - ✅ Complete learning modules
   - ✅ Chat with SafeSpace chatbot
   - ✅ Test SOS button (when logged in)
   - ✅ View guardian dashboard (if guardian role)
   - ✅ Submit reports in Legal Aid portal
   - ✅ Try accessibility features

---

## 🔧 Troubleshooting

### MongoDB Connection Error?
**Solution 1: Use MongoDB Atlas (Cloud)**
1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a cluster
4. Get connection string
5. Update `MONGODB_URI` in backend `.env` file

**Solution 2: Start Local MongoDB**
```bash
# Linux/Mac
sudo systemctl start mongod

# Windows
# Start MongoDB service from Services
```

### Port Already in Use?
- Backend: Change `PORT` in backend `.env` file
- Frontend: Vite will auto-use next available port

### Dependencies Installation Failed?
```bash
# Try with legacy peer deps
npm install --legacy-peer-deps

# Or clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Module Not Found Errors?
```bash
# Make sure you're in the correct directory
cd shield360-backend  # or shield360-frontend
npm install
```

---

## 📋 Prerequisites Checklist

- [ ] Node.js installed (v18+) - [Download](https://nodejs.org/)
- [ ] MongoDB running (local or Atlas)
- [ ] Port 3000 and 5000 available
- [ ] Internet connection (for npm packages)

---

## 🎓 Quick Test Accounts

After seeding the database, you can register accounts:
1. **Child Account**: Register with role "child"
2. **Guardian Account**: Register with role "guardian" 
3. **Admin Account**: Register with role "admin"

---

## 📞 Need Help?

- Check `SETUP.md` for detailed setup
- Check `README.md` for project overview
- Check browser console for errors
- Check terminal for backend errors

---

## ✅ Success Checklist

When everything is working, you should see:
- ✅ Backend running on http://localhost:5000
- ✅ Frontend running on http://localhost:3000
- ✅ Can register/login
- ✅ Can view modules
- ✅ Can access dashboard
- ✅ SOS button appears when logged in

---

**Happy coding! 🚀**


