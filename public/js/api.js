// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Django uses Token authentication instead of Bearer JWT
const getAuthToken = () => {
  return localStorage.getItem('shield360-token');
};

const setAuthToken = (token) => {
  localStorage.setItem('shield360-token', token);
};

const removeAuthToken = () => {
  localStorage.removeItem('shield360-token');
  localStorage.removeItem('shield360-user');
};

// API Request Helper
async function apiRequest(endpoint, options = {}) {
  const token = getAuthToken();
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  if (token) {
    headers['Authorization'] = `Token ${token}`;  // Django uses Token, not Bearer
  }

  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || 'Request failed');
    }

    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}

// Auth API
const authAPI = {
  register: async (userData) => {
    return apiRequest('/auth/register', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  },
  login: async (email, password) => {
    return apiRequest('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  },
};

// User API
const userAPI = {
  getProfile: async () => {
    return apiRequest('/users/profile');
  },
  updatePreferences: async (preferences) => {
    return apiRequest('/users/preferences', {
      method: 'PUT',
      body: JSON.stringify(preferences),
    });
  },
};

// Module API
const moduleAPI = {
  getAll: async () => {
    return apiRequest('/modules');
  },
  getById: async (id) => {
    return apiRequest(`/modules/${id}`);
  },
  getProgress: async (userId) => {
    return apiRequest(`/modules/progress/${userId}`);
  },
  submitProgress: async (moduleId, quizResults, score) => {
    return apiRequest(`/modules/${moduleId}/progress`, {
      method: 'POST',
      body: JSON.stringify({ quizResults, score }),
    });
  },
};

// Chatbot API
const chatbotAPI = {
  chat: async (message) => {
    return apiRequest('/chatbot/chat', {
      method: 'POST',
      body: JSON.stringify({ message }),
    });
  },
  getHistory: async () => {
    return apiRequest('/chatbot/history');
  },
};

// SOS API
const sosAPI = {
  send: async (location, message) => {
    return apiRequest('/sos/send', {
      method: 'POST',
      body: JSON.stringify({ location, message }),
    });
  },
  getAlerts: async () => {
    return apiRequest('/sos/alerts');
  },
};

// Report API
const reportAPI = {
  create: async (reportData) => {
    return apiRequest('/reports', {
      method: 'POST',
      body: JSON.stringify(reportData),
    });
  },
  getMyReports: async () => {
    return apiRequest('/reports/my-reports');
  },
};

// Export for use in HTML files
window.Shield360API = {
  auth: authAPI,
  user: userAPI,
  module: moduleAPI,
  chatbot: chatbotAPI,
  sos: sosAPI,
  report: reportAPI,
  getAuthToken,
  setAuthToken,
  removeAuthToken,
};


