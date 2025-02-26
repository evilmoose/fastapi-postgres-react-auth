// frontend/src/components/ProtectedFeatureRoute.jsx
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const ProtectedFeatureRoute = ({ children, requiredRoles = [] }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!user) {
    return <Navigate to="/login" />;
  }

  // Check if user has required roles (if any are specified)
  const hasRequiredRole = 
    requiredRoles.length === 0 || 
    (user.roles && requiredRoles.some(role => user.roles.includes(role)));

  if (!hasRequiredRole) {
    return <div className="max-w-4xl mx-auto mt-8">
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
        <p>You don't have permission to access this page.</p>
      </div>
    </div>;
  }

  return children;
};

export default ProtectedFeatureRoute;