# 🚀 Quick Setup Guide - Shield 360

## Step 1: Fix MongoDB Connection

### Update `.env` file in `shield360-backend/`:

```env
PORT=5000
MONGODB_URI=mongodb+srv://shield360:3M8YWU1FKAIKNoZz@cluster0.szfu4vo.mongodb.net/shield360?retryWrites=true&w=majority
JWT_SECRET=shield360_secret_key_change_in_production
NODE_ENV=development
```

**Important:**
- Remove `<` and `>` brackets from username/password
- Add database name (`shield360`) before `?`
- Add connection options: `?retryWrites=true&w=majority`

### Test Connection:
```bash
cd shield360-backend
npm run check-db
```

Should show: `✅ MongoDB connection successful!`

---

## Step 2: Start the Server

```bash
cd shield360-backend
npm start
```

You should see:
```
✅ MongoDB connected successfully
📊 Database: shield360
🚀 Server running on port 5000
🌐 Frontend: http://localhost:5000
🔌 API: http://localhost:5000/api
```

---

## Step 3: Seed Database (Optional)

```bash
cd shield360-backend
node seed.js
```

---

## Step 4: Access the Application

Open your browser and go to: **http://localhost:5000**

You'll see the beautiful Shield 360 homepage!

---

## Step 5: Register/Login

1. Click "LOGIN" in the navigation
2. Choose "Parents Login" or "Teachers Login"
3. Or click "Get Started" to register a new account
4. Fill in the form and create your account

---

## 🎨 Features Available

✅ Beautiful HTML frontend with professional design
✅ Login/Registration system
✅ Parent and Teacher portals
✅ Learning modules
✅ Surveys
✅ News and articles
✅ Contact information
✅ All integrated with backend API

---

## 🔧 Troubleshooting

### MongoDB Connection Issues?

1. **Check your connection string format:**
   ```
   mongodb+srv://USERNAME:PASSWORD@CLUSTER.mongodb.net/DATABASE?retryWrites=true&w=majority
   ```

2. **Verify in MongoDB Atlas:**
   - Database Access: User exists and has correct password
   - Network Access: Your IP is whitelisted (or allow from anywhere)

3. **Test connection:**
   ```bash
   npm run check-db
   ```

### Server Won't Start?

- Check if port 5000 is already in use
- Make sure all dependencies are installed: `npm install`
- Check terminal for error messages

### Pages Not Loading?

- Make sure backend is running
- Check browser console (F12) for errors
- Verify you're accessing http://localhost:5000

---

## 📝 Next Steps

1. ✅ MongoDB connected
2. ✅ Backend running
3. ✅ Database seeded (optional)
4. ✅ Access http://localhost:5000
5. ✅ Register/Login
6. ✅ Explore the platform!

---

**Everything is now integrated and ready to use! 🎉**


