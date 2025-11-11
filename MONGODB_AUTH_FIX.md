# 🔐 MongoDB Authentication Fix

## ❌ Current Error: "bad auth : authentication failed"

This means the username or password is incorrect. Let's fix it!

---

## ✅ Solution Steps

### Step 1: Verify Your MongoDB Atlas Credentials

1. **Go to MongoDB Atlas**: https://cloud.mongodb.com
2. **Login** to your account
3. **Go to "Database Access"** (left sidebar)
4. **Check your database user:**
   - Username: Should be `shield360` (or whatever you created)
   - Password: Make sure you know the correct password

### Step 2: Create/Reset Database User (If Needed)

If you don't have a user or forgot the password:

1. **Go to "Database Access"**
2. **Click "Add New Database User"**
3. **Choose "Password" authentication**
4. **Set:**
   - Username: `shield360`
   - Password: Create a strong password (save it!)
   - Database User Privileges: **"Read and write to any database"**
5. **Click "Add User"**

### Step 3: Update .env File

Open `shield360-backend/.env` and update with your **actual credentials**:

```env
MONGODB_URI=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@cluster0.szfu4vo.mongodb.net/shield360?retryWrites=true&w=majority
```

**Replace:**
- `YOUR_USERNAME` with your actual MongoDB username
- `YOUR_PASSWORD` with your actual MongoDB password

**Important:** If your password has special characters, they need to be URL-encoded:
- `@` becomes `%40`
- `#` becomes `%23`
- `$` becomes `%24`
- `%` becomes `%25`
- etc.

### Step 4: Whitelist Your IP

1. **Go to "Network Access"** in MongoDB Atlas
2. **Click "Add IP Address"**
3. **Click "Allow Access from Anywhere"** (for testing)
   - Or add your specific IP address
4. **Click "Confirm"**

### Step 5: Test Connection

```bash
cd shield360-backend
npm run check-db
```

Should show: `✅ MongoDB connection successful!`

---

## 🔍 How to Get Your Connection String

1. **Go to MongoDB Atlas**
2. **Click "Database"** → Click **"Connect"** on your cluster
3. **Choose "Connect your application"**
4. **Copy the connection string**
5. **Replace `<password>` with your actual password**
6. **Add database name** before `?`: `...mongodb.net/shield360?retryWrites...`

---

## 📝 Example Connection String

```
mongodb+srv://shield360:MyPassword123@cluster0.szfu4vo.mongodb.net/shield360?retryWrites=true&w=majority
```

**Format:**
```
mongodb+srv://USERNAME:PASSWORD@CLUSTER.mongodb.net/DATABASE?retryWrites=true&w=majority
```

---

## 🆘 Still Having Issues?

1. **Double-check username and password** in MongoDB Atlas
2. **Make sure IP is whitelisted**
3. **Try creating a new database user** with a simple password
4. **Check if password has special characters** that need encoding
5. **Verify cluster is running** in MongoDB Atlas

---

## 💡 Quick Fix: Create New User

1. MongoDB Atlas → Database Access
2. Add New Database User
3. Username: `shield360`
4. Password: `Shield3602024!` (or any strong password)
5. Privileges: Read and write to any database
6. Update `.env` with new credentials
7. Test: `npm run check-db`

---

**Once authentication works, you're all set! 🎉**


