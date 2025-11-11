# 🐍 Django Backend Setup Guide

## ✅ Backend Converted to Django!

The entire backend has been converted from Node.js/Express to Django (Python).

---

## 🚀 Quick Start

### Step 1: Install Python Dependencies

```bash
cd shield360-backend-django

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure MongoDB

Create `.env` file:

```env
PORT=5000
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/shield360?retryWrites=true&w=majority
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Step 3: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Seed Database (Optional)

```bash
python seed_data.py
```

### Step 5: Start Server

```bash
python manage.py runserver 0.0.0.0:5000
```

Or use the start script:

```bash
./start.sh
```

---

## 📁 Project Structure

```
shield360-backend-django/
├── shield360/          # Django project
│   ├── settings.py     # Settings
│   ├── urls.py         # Main URLs
│   └── wsgi.py         # WSGI config
├── api/                # Main app
│   ├── models.py       # Database models
│   ├── views.py        # API views
│   ├── serializers.py  # DRF serializers
│   ├── urls.py         # API URLs
│   └── admin.py        # Admin interface
├── manage.py           # Django management
├── requirements.txt    # Python dependencies
└── seed_data.py        # Seed script
```

---

## 🔄 Changes from Node.js to Django

### Authentication
- **Before**: JWT tokens
- **Now**: Django REST Framework Token Authentication
- **Frontend**: Updated to use `Token` instead of `Bearer`

### API Endpoints
- All endpoints remain the same
- Response format is identical
- Frontend code works with minimal changes

### Database
- Still using MongoDB
- Models converted to Django ORM
- Can use djongo or pymongo

---

## 🔧 Key Differences

1. **Authentication Header**:
   - Node.js: `Authorization: Bearer <token>`
   - Django: `Authorization: Token <token>`

2. **User Registration**:
   - Django uses `username`, `first_name`, `last_name` instead of just `name`
   - Frontend automatically maps fields

3. **Response Format**:
   - Same JSON structure
   - Direct access to `response.token` and `response.user` (not `response.data`)

---

## 📡 API Endpoints (Same as Before)

All endpoints work the same:

- `POST /api/auth/register` - Register
- `POST /api/auth/login` - Login
- `GET /api/users/profile` - Get profile
- `GET /api/modules` - Get modules
- `POST /api/chatbot/chat` - Chatbot
- `POST /api/sos/send` - SOS alert
- etc.

---

## 🎯 Next Steps

1. **Install Python dependencies**
2. **Set up MongoDB connection** in `.env`
3. **Run migrations**
4. **Start server**
5. **Test with frontend**

---

## 🆘 Troubleshooting

### Import Errors?
```bash
pip install -r requirements.txt
```

### MongoDB Connection Issues?
- Check `.env` file
- Verify MongoDB URI format
- Test connection separately

### Migration Errors?
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ✅ Frontend Integration

The frontend has been updated to work with Django:
- Token authentication (instead of JWT Bearer)
- API calls remain the same
- Response handling updated

**Everything should work seamlessly!**

---

**Your Django backend is ready! 🎉**

