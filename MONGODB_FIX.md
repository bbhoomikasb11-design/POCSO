# 🔧 MongoDB Connection Fix

## Your MongoDB Connection String

I noticed you have a MongoDB Atlas connection string. Here's how to fix it:

### Step 1: Update .env file

Open `shield360-backend/.env` and update the `MONGODB_URI`:

**If using MongoDB Atlas:**
```env
MONGODB_URI=mongodb+srv://shield360:3M8YWU1FKAIKNoZz@cluster0.szfu4vo.mongodb.net/shield360?retryWrites=true&w=majority
```

**Important Notes:**
1. Remove the `<` and `>` brackets around username and password
2. Add database name (`shield360`) before the `?`
3. Add connection options: `?retryWrites=true&w=majority`

### Step 2: Verify Connection String Format

The format should be:
```
mongodb+srv://USERNAME:PASSWORD@CLUSTER.mongodb.net/DATABASE_NAME?retryWrites=true&w=majority
```

### Step 3: Test Connection

```bash
cd shield360-backend
npm run check-db
```

### Step 4: Common Issues

**If you get "Authentication failed":**
- Check username and password are correct
- Make sure special characters in password are URL-encoded

**If you get "IP not whitelisted":**
- Go to MongoDB Atlas → Network Access
- Click "Add IP Address"
- Click "Allow Access from Anywhere" (for testing)
- Or add your specific IP address

**If you get "Connection timeout":**
- Check your internet connection
- Verify the cluster is running in Atlas
- Check firewall settings

### Step 5: After Fixing

Once the connection works:
1. Start the backend: `npm start`
2. Seed the database: `node seed.js`
3. Access the app: http://localhost:5000

---

**Your connection string should look like this (with your actual credentials):**
```
mongodb+srv://shield360:YOUR_PASSWORD@cluster0.szfu4vo.mongodb.net/shield360?retryWrites=true&w=majority
```


