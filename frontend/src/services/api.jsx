import axios from 'axios';

const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor to attach token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authApi = {
  login: async (credentials) => {
    // Convert credentials to FormData string
    const formData = new URLSearchParams();
    formData.append('username', credentials.email);  // FastAPI-Users expects 'username'
    formData.append('password', credentials.password);

    const response = await api.post('/auth/jwt/login', formData, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
    });

    // Set token immediately after receiving it
    const token = response.data.access_token;
    localStorage.setItem('token', token);

    // After successful login, immediately fetch user data
    const userData = await api.get('/users/me');

    return {
      access_token: response.data.access_token,
      user: userData.data
    };
  },
  register: async (userData) => {
    // Send as JSON instead of form data
    const response = await api.post('/auth/register', {
      email: userData.email,
      password: userData.password
  }, {
      headers: {
          'Content-Type': 'application/json',
      },
  });
  return response.data;
},
  getMe: async () => {
    const response = await api.get('/users/me');
    return response.data;
  },
  logout: async () => {
    const response = await api.post('/auth/jwt/logout');
    return response.data;
  },
};

export default api;