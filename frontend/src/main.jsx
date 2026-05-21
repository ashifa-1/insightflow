import './App.css';
import React from 'react';
import { AuthProvider } from './features/auth/AuthContext';
import ReactDOM from 'react-dom/client';
import {
  QueryClient,
  QueryClientProvider
} from '@tanstack/react-query';
import App from './App.jsx';
const queryClient = new QueryClient();

ReactDOM.createRoot(
  document.getElementById('root')
).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <App />
      </AuthProvider>
    </QueryClientProvider>
  </React.StrictMode>
);