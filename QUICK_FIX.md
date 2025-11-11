# ⚡ Quick Fix - Get Shield 360 Running Now!

## 🎯 Current Situation
- MongoDB local service is not working
- You need to use MongoDB Atlas (Cloud) instead

## 🚀 Fastest Solution (10 minutes)

### Option 1: MongoDB Atlas (Recommended - Free Cloud Database)

1. **Sign up**: https://www.mongodb.com/cloud/atlas/register
2. **Create cluster**: Choose FREE tier, select region, click Create
3. **Create user**: Database Access → Add User → Username: `shield360`, set password
4. **Whitelist IP**: Network Access → Add IP → Allow from anywhere
5. **Get connection string**: Database → Connect → Connect your application → Copy string
6. **Update .env**: 
   ```bash
   cd shield360-backend
   nano .env  # or use any text editor
   ```
   Change:
   ```env
   MONGODB_URI=mongodb+srv://shield360:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/shield360?retryWrites=true&w=majority
   ```
7. **Test**: `npm run check-db`
8. **Done!** Proceed to next steps below

### Option 2: Fix Local MongoDB (If you prefer local)

```bash
# Install MongoDB (if not installed)
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install -y mongodb

# Or download from: https://www.mongodb.com/try/download/community

# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod

# Test
npm run check-db
```

---

## ✅ After MongoDB is Connected

### Step 1: Seed Database
```bash
cd shield360-backend
node seed.js
```

### Step 2: Start Backend (Terminal 1)
```bash
cd shield360-backend
npm start
```
Wait for: `✅ MongoDB connected successfully`

### Step 3: Start Frontend (Terminal 2 - NEW TERMINAL)
```bash
cd shield360-frontend
npm run dev
```

### Step 4: Open Browser
Go to: **http://localhost:3000**

### Step 5: Register Account
- Click "Register"
- Fill form and create account
- You're in! 🎉

---

## 📝 Quick Commands

```bash
# Test MongoDB connection
cd shield360-backend && npm run check-db

# Seed database
cd shield360-backend && node seed.js

# Start backend
cd shield360-backend && npm start

# Start frontend (new terminal)
cd shield360-frontend && npm run dev
```

---

## 🎯 What You'll See When Working

**Backend Terminal:**
```
✅ MongoDB connected successfully
📊 Database: shield360
Server running on port 5000
```

**Frontend Terminal:**
```
VITE v5.x.x  ready in xxx ms
➜  Local:   http://localhost:3000/
```

**Browser:**
- Shield 360 landing page
- Can register/login
- Can access all features

---

**Recommended: Use MongoDB Atlas - it's free, easy, and works everywhere! 🚀**

Follow the detailed guide in `SETUP_MONGODB_ATLAS.md` for step-by-step instructions.


