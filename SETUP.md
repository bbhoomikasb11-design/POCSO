# Shield 360 Setup Guide

## Quick Start

### 1. Prerequisites
- Node.js (v18 or higher) - [Download](https://nodejs.org/)
- MongoDB - [Download](https://www.mongodb.com/try/download/community) or use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (free)

### 2. Backend Setup

```bash
# Navigate to backend directory
cd shield360-backend

# Install dependencies
npm install

# Create .env file
echo "PORT=5000
MONGODB_URI=mongodb://localhost:27017/shield360
JWT_SECRET=shield360_secret_key_change_in_production
NODE_ENV=development" > .env

# Start MongoDB (if using local MongoDB)
# On Linux/Mac:
sudo systemctl start mongod
# On Windows:
# Start MongoDB service from Services

# Seed the database (optional but recommended)
node seed.js

# Start the backend server
npm start
# or for development with auto-reload
npm run dev
```

The backend will run on `http://localhost:5000`

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd shield360-frontend

# Install dependencies
npm install

# Create .env file
echo "VITE_API_URL=http://localhost:5000/api" > .env

# Start the development server
npm run dev
```

The frontend will run on `http://localhost:3000`

### 4. Access the Application

- Open your browser and go to `http://localhost:3000`
- Register a new account (choose role: child, guardian, teacher, or admin)
- Start exploring Shield 360!

## Default Test Accounts

After seeding, you can create accounts through the registration page:

1. **Child Account**: Register with role "child"
2. **Guardian Account**: Register with role "guardian"
3. **Admin Account**: Register with role "admin"

## Features to Test

1. **Landing Page**: View features and language selector
2. **Registration/Login**: Create accounts for different roles
3. **Learning Modules**: Complete modules and earn badges
4. **SafeSpace Chatbot**: Chat and test emotion detection
5. **SOS Button**: Test emergency alert (appears when logged in)
6. **Guardian Dashboard**: Monitor children's progress (login as guardian)
7. **Admin Dashboard**: View analytics (login as admin)
8. **Legal Aid Portal**: Submit reports and view case IDs
9. **Accessibility Settings**: Change language, font size, contrast

## Troubleshooting

### MongoDB Connection Issues
- Make sure MongoDB is running: `mongod` or check MongoDB service
- Verify connection string in `.env` file
- For MongoDB Atlas, use the connection string from your cluster

### Port Already in Use
- Backend: Change `PORT` in `.env` file
- Frontend: Vite will automatically use the next available port

### Module Not Found Errors
- Run `npm install` in both frontend and backend directories
- Delete `node_modules` and `package-lock.json`, then run `npm install` again

### API Connection Issues
- Verify backend is running on the correct port
- Check `VITE_API_URL` in frontend `.env` file
- Check browser console for CORS errors

## Production Deployment

### Backend (Render/Heroku)
1. Set environment variables in your hosting platform
2. Deploy the backend
3. Update `VITE_API_URL` in frontend to point to your backend URL

### Frontend (Vercel/Netlify)
1. Set `VITE_API_URL` environment variable
2. Deploy the frontend
3. The build will be automatically generated

## Support

For issues or questions:
- Check the README.md files in frontend and backend directories
- Review the API documentation in backend/README.md
- Contact support@shield360.com

Happy coding! 🚀

