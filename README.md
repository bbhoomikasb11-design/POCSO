# Shield 360 - Child Safety Web Portal

A holistic, tech-driven child safety web portal that integrates awareness, safety, and support systems under one platform.

## 🎯 Overview

Shield 360 is a comprehensive web application designed to empower children with safety knowledge, provide emotional support, and enable guardians and teachers to monitor and protect children effectively.

## ✨ Key Features

### 1. 🎮 Gamified Awareness Modules
- Interactive lessons on Personal Safety, Digital Safety, Mental Health, and Legal Rights
- Quizzes with scores and badges
- Progress tracking for learners
- Digital safety badges on completion

### 2. 🤖 AI-Powered Emotional Support Chatbot (SafeSpace)
- Text and voice input support
- Emotion detection (happy/sad/stressed/anxious)
- Automatic alert to guardian dashboard when distress is detected
- Option to connect with real counselors

### 3. 👨‍👩‍👧‍👦 Guardian/Teacher Dashboard
- Monitor child's learning progress
- Receive emotional alerts
- Access educational resources
- Report concerns
- Analytics with charts for quiz performance and alerts

### 4. 🚨 SOS & Emergency Module
- Floating SOS button across all pages
- GPS location sharing
- Direct call to ChildLine 1098
- Alert to guardian with location

### 5. ♿ Accessibility & Inclusivity Tools
- Sign language lessons
- Self-defense training modules
- Multilingual interface (English, Hindi, Kannada)
- High-contrast mode
- Text-to-speech support
- Adjustable font sizes

### 6. ⚖️ Legal Aid & Reporting Portal
- Integration with NALSA and ChildLine
- Incident report form
- Legal FAQs and help resources
- Auto-generated case IDs (anonymized)

### 7. 📊 Admin/Analytics Dashboard
- View anonymous case trends
- Alert analytics
- Quiz engagement data
- Awareness impact metrics
- CRUD access to update learning materials

## 🛠️ Tech Stack

### Frontend
- React 18
- TailwindCSS
- React Router
- Zustand (State Management)
- React i18next (Internationalization)
- Recharts (Data Visualization)
- Leaflet (Maps)
- Lucide React (Icons)

### Backend
- Node.js
- Express.js
- MongoDB (Mongoose)
- JWT (Authentication)
- Bcrypt (Password Hashing)

### Deployment
- Frontend: Vercel/Netlify
- Backend: Render/Heroku

## 🚀 Getting Started

### Prerequisites
- Node.js (v18 or higher)
- MongoDB (local or cloud instance)
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd project
```

2. **Set up the Backend**
```bash
cd shield360-backend
npm install
cp .env.example .env
# Edit .env with your configuration
npm start
```

3. **Seed the database (optional)**
```bash
node seed.js
```

4. **Set up the Frontend**
```bash
cd ../shield360-frontend
npm install
# Create .env file with VITE_API_URL=http://localhost:5000/api
npm run dev
```

5. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## 📁 Project Structure

```
project/
├── shield360-frontend/     # React frontend application
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── store/          # State management
│   │   └── utils/          # Utility functions
│   └── package.json
│
├── shield360-backend/      # Node.js backend API
│   ├── models/             # MongoDB models
│   ├── routes/             # API routes
│   ├── middleware/         # Auth middleware
│   └── server.js           # Entry point
│
└── README.md
```

## 🔐 User Roles

- **Child**: Access to learning modules, SafeSpace chatbot, SOS button
- **Guardian**: Dashboard to monitor children, receive alerts, report concerns
- **Teacher**: Similar to guardian, can monitor multiple children
- **Admin**: Full access to analytics, module management, and all data

## 🌐 Supported Languages

- English
- Hindi (हिंदी)
- Kannada (ಕನ್ನಡ)

## 📱 Features in Detail

### Learning Modules
Each module includes:
- Educational content
- Interactive quizzes
- Progress tracking
- Badge rewards
- Video/Animation support

### SafeSpace Chatbot
- Real-time emotion detection
- Contextual responses
- Automatic alert generation
- Counselor connection option

### SOS System
- One-click emergency access
- GPS location capture
- Multi-channel alert (guardian, ChildLine)
- Always accessible floating button

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- Role-based access control
- Anonymous reporting option
- Secure API endpoints

## 📊 Analytics & Reporting

- User engagement metrics
- Module completion rates
- Alert trends
- Report statistics
- Performance charts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 📞 Support

- ChildLine: 1098
- Emergency: 112
- Email: support@shield360.com

## 🙏 Acknowledgments

- ChildLine India
- NALSA (National Legal Services Authority)
- All contributors and supporters

---

**Shield 360 - Protecting Children, Empowering Futures**


