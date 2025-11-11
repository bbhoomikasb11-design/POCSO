// Authentication helper functions
window.Shield360Auth = {
  // Check if user is logged in
  isAuthenticated: function() {
    return !!localStorage.getItem('shield360-token');
  },

  // Get current user
  getCurrentUser: function() {
    const userStr = localStorage.getItem('shield360-user');
    return userStr ? JSON.parse(userStr) : null;
  },

  // Login handler
  handleLogin: async function(email, password, role) {
    try {
      const response = await Shield360API.auth.login(email, password);
      
      // Store token and user
      Shield360API.setAuthToken(response.token);
      localStorage.setItem('shield360-user', JSON.stringify(response.user));
      
      // Redirect based on role
      if (response.user.role === 'admin') {
        window.location.href = '/admin.html';
      } else if (response.user.role === 'guardian' || response.user.role === 'teacher') {
        window.location.href = role === 'teacher' ? '/teacher.html' : '/parent.html';
      } else {
        window.location.href = '/dashboard.html';
      }
      
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Register handler
  handleRegister: async function(userData) {
    try {
      // Map fields for Django (first_name, last_name instead of name)
      const djangoData = {
        username: userData.email.split('@')[0], // Use email prefix as username
        email: userData.email,
        password: userData.password,
        first_name: userData.name.split(' ')[0] || userData.name,
        last_name: userData.name.split(' ').slice(1).join(' ') || '',
        role: userData.role,
      };
      
      if (userData.age) {
        djangoData.age = userData.age;
      }
      
      if (userData.guardianId) {
        djangoData.guardian = userData.guardianId;
      }
      
      const response = await Shield360API.auth.register(djangoData);
      
      // Store token and user
      Shield360API.setAuthToken(response.token);
      localStorage.setItem('shield360-user', JSON.stringify(response.user));
      
      // Redirect based on role
      if (response.user.role === 'admin') {
        window.location.href = '/admin.html';
      } else if (response.user.role === 'guardian' || response.user.role === 'teacher') {
        window.location.href = response.user.role === 'teacher' ? '/teacher.html' : '/parent.html';
      } else {
        window.location.href = '/dashboard.html';
      }
      
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Logout handler
  logout: function() {
    Shield360API.removeAuthToken();
    window.location.href = '/home.html';
  },
};


