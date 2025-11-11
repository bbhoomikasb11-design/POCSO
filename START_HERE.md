

# 🎯 START HERE - Complete Setup Guide

## ✅ Step 1: Verify MongoDB Connection

```bash
cd shield360-backend
npm run check-db
```

**Expected Output:**
```
✅ MongoDB connection successful!
📊 Database: shield360
```

**If you see an error**, you need to set up MongoDB first:
- See `SETUP_MONGODB_ATLAS.md` for MongoDB Atlas setup
- Or see `QUICK_FIX.md` for troubleshooting




---

## ✅ Step 2: Seed the Database

This adds sample learning modules to your database:

```bash
cd shield360-backend
node seed.js
```

**Expected Output:**
```
✅ MongoDB connected successfully
Cleared existing modules
Seeded modules successfully
```

---

## ✅ Step 3: Start Backend Server

**Open Terminal 1:**

```bash
cd shield360-backend
npm start
```

**Expected Output:**
```
✅ MongoDB connected successfully
📊 Database: shield360
Server running on port 5000
```

**⏸️ Keep this terminal open!** The backend needs to keep running.

---

## ✅ Step 4: Start Frontend Server

**Open Terminal 2 (NEW TERMINAL):**

```bash
cd shield360-frontend
npm run dev
```

**Expected Output:**
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:3000/
➜  Network: use --host to expose
```

---

## ✅ Step 5: Open the Application

1. Open your web browser
2. Go to: **http://localhost:3000**
3. You should see the Shield 360 landing page! 🎉

---

## ✅ Step 6: Create Your First Account

1. Click **"Register"** button
2. Fill in the form:
   - **Name**: Your name
   - **Email**: your@email.com
   - **Password**: (choose a password)
   - **Role**: Choose one:
     - `Child` - For learning modules
     - `Guardian` - To monitor children
     - `Teacher` - Similar to guardian
     - `Admin` - For analytics dashboard
3. Click **"Register"**
4. You'll be automatically logged in and redirected! ✅

---

## 🎮 What to Test

### ✅ Login/Register
- Register a new account
- Log out and log back in
- Should work perfectly!

### ✅ Learning Modules
- Click "Modules" or "Start Learning"
- View available modules
- Complete a module and take the quiz
- Earn badges!

### ✅ SafeSpace Chatbot
- Click "SafeSpace" or "Chat"
- Type messages and see emotion detection
- Try: "I'm feeling happy" or "I'm stressed"

### ✅ SOS Button
- When logged in, see red SOS button (bottom right)
- Click it to test emergency alerts

### ✅ Guardian Dashboard
- If you registered as guardian/teacher
- View children's progress
- See alerts and analytics

### ✅ Legal Aid Portal
- Submit incident reports
- View your reports with case IDs

### ✅ Accessibility
- Change language (English, Hindi, Kannada)
- Adjust font size
- Enable high contrast mode

---

## 📋 Quick Reference

### Test MongoDB:
```bash
cd shield360-backend
npm run check-db
```

### Seed Database:
```bash
cd shield360-backend
node seed.js
```

### Start Backend:
```bash
cd shield360-backend
npm start
```

### Start Frontend:
```bash
cd shield360-frontend
npm run dev
```

### Check Health:
- Backend: http://localhost:5000/api/health
- Frontend: http://localhost:3000

---

## 🔧 Troubleshooting

### Can't connect to MongoDB?
- See `SETUP_MONGODB_ATLAS.md` for Atlas setup
- See `QUICK_FIX.md` for quick solutions

### Backend won't start?
- Check if port 5000 is in use
- Verify MongoDB is connected
- Check backend terminal for errors

### Frontend won't start?
- Make sure backend is running first
- Check for port conflicts
- Verify you're in `shield360-frontend` directory

### Can't register/login?
- Check backend terminal for errors
- Verify MongoDB connection
- Check browser console (F12) for errors

---

## 🎉 Success Checklist

- [ ] MongoDB connected (`npm run check-db` shows ✅)
- [ ] Database seeded (`node seed.js` completed)
- [ ] Backend running (port 5000)
- [ ] Frontend running (port 3000)
- [ ] Can access http://localhost:3000
- [ ] Can register account
- [ ] Can login
- [ ] Can view modules
- [ ] Can use SafeSpace chatbot
- [ ] SOS button appears when logged in

---

## 💡 Pro Tips

1. **Keep both terminals open** - Backend and frontend need to run simultaneously
2. **Check terminal outputs** - They show important logs and errors
3. **Use browser dev tools** - Press F12 to see frontend errors
4. **Test different roles** - Register multiple accounts with different roles
5. **Seed database first** - Makes testing easier with sample data

---

**Ready? Follow the steps above and you'll have Shield 360 running in minutes! 🚀**

For detailed MongoDB setup, see `SETUP_MONGODB_ATLAS.md`


