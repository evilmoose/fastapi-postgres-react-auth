// frontend/src/admin/context/AdminContext.jsx
import React, { createContext, useContext, useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext';
import api from '@/services/api';

const AdminContext = createContext();

export const AdminProvider = ({ children }) => {
  const { user } = useAuth();
  const [features, setFeatures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAdminFeatures = async () => {
      if (!user || !user.roles.includes('admin')) {
        setLoading(false);
        return;
      }

      try {
        const response = await api.get('/api/v1/admin/features');
        setFeatures(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchAdminFeatures();
  }, [user]);

  return (
    <AdminContext.Provider value={{ features, loading, error }}>
      {children}
    </AdminContext.Provider>
  );
};

export const useAdminFeatures = () => useContext(AdminContext);