import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Flask Backend URL
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // Set timeout for requests
});

// Request interceptor (for authentication or logging)
apiClient.interceptors.request.use(
  (config) => {
    console.log('Request:', config);
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor (for handling errors globally)
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

export default apiClient;
