// frontend/src/utils/authUtils.js
import { useAuth } from '../context/AuthContext';
import ProtectedRoute from '../components/ProtectedRoute';

// Re-export the useAuth hook for features to use
export { useAuth };

// Export the ProtectedRoute component
export { ProtectedRoute };

// Create a higher-order component for role-based access control
export const withRoleCheck = (Component, requiredRoles = []) => {
  const RoleProtectedComponent = (props) => {
    const { user } = useAuth();
    
    // If no roles are required, or user has one of the required roles
    const hasRequiredRole = 
      requiredRoles.length === 0 || 
      (user?.roles && requiredRoles.some(role => user.roles.includes(role)));
    
    if (!hasRequiredRole) {
      return <div>You don't have permission to access this page.</div>;
    }
    
    return <Component {...props} />;
  };
  
  return RoleProtectedComponent;
};