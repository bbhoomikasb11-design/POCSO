# 🚀 How to Run Shield 360 - SUPER EASY!

## ⚡ Quickest Way (One Command!)

### Linux/Mac:
```bash
./start.sh
```

### Windows:
```bash
start.bat
```

**That's it!** The script will automatically:
- ✅ Install all dependencies
- ✅ Create configuration files
- ✅ Start backend and frontend
- ✅ Open in your browser

---

## 📋 What You Need First

1. **Node.js** - [Download here](https://nodejs.org/) (v18 or higher)
2. **MongoDB** - Choose one:
   - **MongoDB Atlas** (Cloud - Easiest!) - [Free at mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
   - **Local MongoDB** - [Download here](https://www.mongodb.com/try/download/community)

---

## 🎯 Step-by-Step (If Scripts Don't Work)

### 1. Setup MongoDB
**Option A: MongoDB Atlas (Recommended - No Installation!)**
1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up for free
3. Create a cluster
4. Click "Connect" → "Connect your application"
5. Copy the connection string (looks like: `mongodb+srv://user:pass@cluster.mongodb.net/...`)

**Option B: Local MongoDB**
- Install MongoDB from mongodb.com
- Start MongoDB service
- Use: `mongodb://localhost:27017/shield360`

### 2. Setup Backend

```bash
cd shield360-backend
npm install
```

Create `.env` file:
```env
PORT=5000
MONGODB_URI=your_mongodb_connection_string_here
JWT_SECRET=shield360_secret_key
NODE_ENV=development
```

Start backend:
```bash
npm start
```

### 3. Setup Frontend (New Terminal)

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

### 4. Seed Database (Optional)

```bash
cd shield360-backend
node seed.js
```

### 5. Open Browser

Go to: **http://localhost:3000**

---

## 🎉 You're Done!

1. Register an account
2. Choose a role (Child, Guardian, Teacher, or Admin)
3. Start exploring!

---

## 🔧 Common Issues & Fixes

### "Cannot find module" Error
```bash
# In the directory with the error:
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

### MongoDB Connection Error
- **If using Atlas**: Make sure your IP is whitelisted in Atlas (0.0.0.0/0 for testing)
- **If using local**: Make sure MongoDB service is running

### Port Already in Use
- Backend: Change `PORT=5000` to `PORT=5001` in backend `.env`
- Frontend: Vite will auto-use next port

### Scripts Don't Work
- Make scripts executable: `chmod +x start.sh` (Linux/Mac)
- Run manually using Step-by-Step guide above

---

## 📱 What to Test

✅ Register and login  
✅ Complete learning modules  
✅ Chat with SafeSpace chatbot  
✅ Test SOS button  
✅ View guardian dashboard  
✅ Submit reports  
✅ Try accessibility features  

---

## 💡 Pro Tips

1. **Use MongoDB Atlas** - It's free and easier than local setup
2. **Run seed.js** - Gets you sample data to test with
3. **Check browser console** - For frontend errors
4. **Check terminal** - For backend errors

---

## 🆘 Still Having Issues?

1. Check `QUICK_START.md` for more details
2. Check `SETUP.md` for detailed setup
3. Make sure Node.js and MongoDB are installed
4. Check all `.env` files are created correctly

---

**Ready? Run `./start.sh` (Linux/Mac) or `start.bat` (Windows) and you're good to go! 🚀**


