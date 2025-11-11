# 🚀 Quick MongoDB Atlas Setup (5 Minutes!)

Since local MongoDB isn't working, let's use **MongoDB Atlas** (Cloud - Free & Easy!)

## Step 1: Create MongoDB Atlas Account

1. Go to: **https://www.mongodb.com/cloud/atlas/register**
2. Sign up with your email (it's FREE!)
3. Verify your email

## Step 2: Create a Cluster

1. After signing in, click **"Build a Database"**
2. Choose **"FREE"** tier (M0)
3. Select a region closest to you (e.g., Mumbai, Singapore)
4. Click **"Create"**
5. Wait 3-5 minutes for cluster to deploy

## Step 3: Create Database User

1. Go to **"Database Access"** (left sidebar)
2. Click **"Add New Database User"**
3. Choose **"Password"** authentication
4. Username: `shield360` (or any name you like)
5. Password: Create a strong password (save it!)
6. Database User Privileges: **"Read and write to any database"**
7. Click **"Add User"**

## Step 4: Whitelist Your IP

1. Go to **"Network Access"** (left sidebar)
2. Click **"Add IP Address"**
3. Click **"Allow Access from Anywhere"** (for testing)
   - Or click "Add Current IP Address"
4. Click **"Confirm"**

## Step 5: Get Connection String

1. Go back to **"Database"** (left sidebar)
2. Click **"Connect"** button on your cluster
3. Choose **"Connect your application"**
4. Driver: **Node.js**, Version: **5.5 or later**
5. Copy the connection string
   - It looks like: `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`

## Step 6: Update Your .env File

1. Open: `shield360-backend/.env`
2. Replace the `MONGODB_URI` line with:

```env
MONGODB_URI=mongodb+srv://shield360:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/shield360?retryWrites=true&w=majority
```

**Important:**
- Replace `YOUR_PASSWORD` with the password you created in Step 3
- Replace `cluster0.xxxxx` with your actual cluster address
- Make sure `shield360` (database name) is in the URL before `?`

## Step 7: Test Connection

```bash
cd shield360-backend
npm run check-db
```

You should see:
```
✅ MongoDB connection successful!
📊 Database: shield360
```

## ✅ Done!

Now you can proceed with the next steps:
1. Seed the database: `node seed.js`
2. Start backend: `npm start`
3. Start frontend: `npm run dev`

---

## 🆘 Troubleshooting

### "Authentication failed"
- Check your username and password in the connection string
- Make sure you created the database user correctly

### "IP not whitelisted"
- Go to Network Access and add your IP
- Or allow access from anywhere (0.0.0.0/0)

### "Connection timeout"
- Check your internet connection
- Verify the connection string is correct
- Make sure the cluster is deployed (wait a few minutes)

---

**Need help? Check the connection string format carefully and make sure all credentials are correct!**

