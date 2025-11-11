# 🔧 MongoDB Connection Setup Guide

## The Error You're Seeing

```
Operation `users.findOne()` buffering timed out after 10000ms
```

This means the backend **cannot connect to MongoDB**. Let's fix it!

---

## ✅ Quick Fix Options

### Option 1: Use MongoDB Atlas (Cloud - Easiest!) ⭐ Recommended

1. **Go to MongoDB Atlas**: https://www.mongodb.com/cloud/atlas
2. **Sign up** for free account
3. **Create a cluster** (free tier is fine)
4. **Get connection string**:
   - Click "Connect" → "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your database password
5. **Update `.env` file** in `shield360-backend/`:
   ```env
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/shield360?retryWrites=true&w=majority
   ```
6. **Whitelist your IP**:
   - In Atlas, go to "Network Access"
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (for testing) or add your IP

### Option 2: Use Local MongoDB

1. **Install MongoDB**:
   - Linux: `sudo apt-get install mongodb` or use MongoDB's official installer
   - Mac: `brew install mongodb-community`
   - Windows: Download from mongodb.com

2. **Start MongoDB**:
   ```bash
   # Linux/Mac
   sudo systemctl start mongod
   # OR
   mongod
   
   # Windows
   # Start MongoDB service from Services
   ```

3. **Verify it's running**:
   ```bash
   mongosh  # or mongo (older versions)
   ```

4. **Update `.env` file**:
   ```env
   MONGODB_URI=mongodb://localhost:27017/shield360
   ```

---

## 🧪 Test Your Connection

Run this command to test if MongoDB connection works:

```bash
cd shield360-backend
npm run check-db
```

This will tell you if the connection is working or what's wrong.

---

## 🔍 Troubleshooting

### "Connection refused" or "ECONNREFUSED"
- **MongoDB is not running**
- Start MongoDB service
- Check if port 27017 is available

### "Authentication failed"
- **Wrong username/password** (for Atlas)
- Check your credentials in the connection string

### "IP not whitelisted" (Atlas)
- **Your IP is not allowed**
- Go to Atlas → Network Access → Add your IP

### "Timeout" errors
- **Firewall blocking connection**
- **Wrong connection string**
- **Network issues**

---

## 📝 Step-by-Step: MongoDB Atlas Setup

1. **Create Account**: https://www.mongodb.com/cloud/atlas/register

2. **Create Cluster**:
   - Choose "Free" tier
   - Select a region close to you
   - Click "Create Cluster"

3. **Create Database User**:
   - Go to "Database Access"
   - Click "Add New Database User"
   - Choose "Password" authentication
   - Username: `shield360` (or any name)
   - Password: Create a strong password (save it!)
   - Database User Privileges: "Read and write to any database"
   - Click "Add User"

4. **Whitelist IP**:
   - Go to "Network Access"
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (for testing)
   - Or add your specific IP
   - Click "Confirm"

5. **Get Connection String**:
   - Go to "Database" → Click "Connect"
   - Choose "Connect your application"
   - Copy the connection string
   - It looks like: `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`
   - Replace `<username>` and `<password>` with your database user credentials
   - Add database name: `...mongodb.net/shield360?retryWrites...`

6. **Update `.env` file**:
   ```env
   MONGODB_URI=mongodb+srv://shield360:your_password@cluster0.xxxxx.mongodb.net/shield360?retryWrites=true&w=majority
   ```

7. **Test Connection**:
   ```bash
   cd shield360-backend
   npm run check-db
   ```

---

## ✅ Verify It's Working

After setting up MongoDB:

1. **Test connection**:
   ```bash
   cd shield360-backend
   npm run check-db
   ```
   Should show: `✅ MongoDB connection successful!`

2. **Start backend**:
   ```bash
   npm start
   ```
   Should show: `✅ MongoDB connected successfully`

3. **Try login/register**:
   - Go to http://localhost:3000
   - Try to register a new account
   - Should work without timeout errors!

---

## 🆘 Still Having Issues?

1. **Check backend console** for specific error messages
2. **Run connection test**: `npm run check-db`
3. **Verify `.env` file** has correct `MONGODB_URI`
4. **Check MongoDB is running** (if using local)
5. **Check network/firewall** settings

---

## 💡 Pro Tips

- **Use MongoDB Atlas** - It's free and easier than local setup
- **Save your connection string** - You'll need it for deployment
- **Test connection first** - Use `npm run check-db` before starting server
- **Check backend logs** - They show connection status

---

**Once MongoDB is connected, login and register will work perfectly! 🎉**


