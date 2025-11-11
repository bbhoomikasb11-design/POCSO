# ✅ Next Steps - MongoDB Connected!

Great! MongoDB is connected. Now let's get Shield 360 running!

## 🚀 Step-by-Step Guide

### Step 1: Seed the Database (Recommended)
This will add sample learning modules to your database:

```bash
cd shield360-backend
node seed.js
```

You should see:
```
✅ MongoDB connected successfully
Cleared existing modules
Seeded modules successfully
```

### Step 2: Start the Backend Server

**Terminal 1 - Backend:**
```bash
cd shield360-backend
npm start
```

You should see:
```
✅ MongoDB connected successfully
📊 Database: shield360
Server running on port 5000
```

**Keep this terminal open!** The backend needs to keep running.

### Step 3: Start the Frontend Server

**Terminal 2 - Frontend (Open a NEW terminal):**
```bash
cd shield360-frontend
npm run dev
```

You should see:
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:3000/
➜  Network: use --host to expose
```

### Step 4: Open the Application

1. Open your browser
2. Go to: **http://localhost:3000**
3. You should see the Shield 360 landing page!

### Step 5: Create Your First Account

1. Click **"Register"** or **"Create Account"**
2. Fill in the form:
   - Name: Your name
   - Email: your@email.com
   - Password: (choose a password)
   - Role: Choose one:
     - **Child** - For learning modules
     - **Guardian** - To monitor children
     - **Teacher** - Similar to guardian
     - **Admin** - For analytics
3. Click **"Register"**
4. You should be automatically logged in!

---

## 🎯 What to Test

### 1. ✅ Login/Register
- Register a new account
- Log out and log back in
- Should work without timeout errors!

### 2. ✅ Learning Modules
- Go to "Modules" or "Start Learning"
- View available modules
- Complete a module and take the quiz
- Earn badges!

### 3. ✅ SafeSpace Chatbot
- Click "SafeSpace" or "Chat"
- Type messages like:
  - "I'm feeling happy today"
  - "I'm stressed about school"
  - "I need help"
- See emotion detection in action!

### 4. ✅ SOS Button
- When logged in, you'll see a red SOS button (bottom right)
- Click it to test emergency alerts
- Try the different options

### 5. ✅ Guardian Dashboard (if you're a guardian)
- View children's progress
- See alerts and analytics
- Monitor learning progress

### 6. ✅ Legal Aid Portal
- Submit incident reports
- View your reports
- See case IDs

### 7. ✅ Accessibility Features
- Change language (English, Hindi, Kannada)
- Adjust font size
- Enable high contrast mode
- Test text-to-speech

### 8. ✅ Admin Dashboard (if you're admin)
- View analytics
- See user statistics
- Check module engagement

---

## 📋 Quick Checklist

- [ ] MongoDB connected ✅
- [ ] Database seeded (run `node seed.js`)
- [ ] Backend running on port 5000
- [ ] Frontend running on port 3000
- [ ] Can access http://localhost:3000
- [ ] Can register a new account
- [ ] Can login
- [ ] Can view modules
- [ ] Can use SafeSpace chatbot
- [ ] SOS button appears when logged in

---

## 🔧 Troubleshooting

### Backend won't start?
- Check if port 5000 is already in use
- Make sure MongoDB is still connected
- Check backend terminal for errors

### Frontend won't start?
- Check if you're in the `shield360-frontend` directory
- Make sure backend is running first
- Check for port conflicts

### Can't register/login?
- Check backend terminal for errors
- Verify MongoDB connection: `npm run check-db`
- Check browser console for errors (F12)

### Modules not showing?
- Make sure you ran `node seed.js`
- Check backend console for errors
- Try refreshing the page

---

## 🎉 You're All Set!

Your Shield 360 application should now be fully functional!

### Quick Commands Reference:

**Test MongoDB:**
```bash
cd shield360-backend
npm run check-db
```

**Seed Database:**
```bash
cd shield360-backend
node seed.js
```

**Start Backend:**
```bash
cd shield360-backend
npm start
```

**Start Frontend:**
```bash
cd shield360-frontend
npm run dev
```

**Check Health:**
- Backend: http://localhost:5000/api/health
- Frontend: http://localhost:3000

---

## 💡 Pro Tips

1. **Keep both terminals open** - Backend and frontend need to run simultaneously
2. **Check the backend console** - It shows important logs and errors
3. **Use browser dev tools** - Press F12 to see frontend errors
4. **Test different roles** - Register multiple accounts with different roles
5. **Seed database first** - Makes testing much easier with sample data

---

**Happy coding! 🚀**

If you encounter any issues, check the terminal outputs and browser console for error messages.


