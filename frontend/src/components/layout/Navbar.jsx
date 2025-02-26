import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { getFeatureNavItems } from '../../featureRegistry';

const Navbar = () => {
  const { user, logout } = useAuth();
  const featureNavItems = getFeatureNavItems();

  // Helper function to check if user has required roles
  const hasRequiredRoles = (item) => {
    if (!item.requiredRoles || item.requiredRoles.length === 0) return true;
    if (!user || !user.roles) return false;
    return item.requiredRoles.some(role => user.roles.includes(role));
  };

  return (
    <nav className="bg-white shadow">
      <div className="container mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="text-xl font-bold text-gray-800">
              Your App
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            {user ? (
              <>
                <Link to="/dashboard" className="text-gray-600 hover:text-gray-900">
                  Dashboard
                </Link>
                {/* Render feature nav items */}
                {featureNavItems
                  .filter(item => (!item.requiresAuth || user) && hasRequiredRoles(item))
                  .map((item, index) => (
                    <Link 
                      key={index}
                      to={item.path} 
                      className="text-gray-600 hover:text-gray-900"
                    >
                      {item.label}
                    </Link>
                  ))
                }
                
                <button
                  onClick={logout}
                  className="text-gray-600 hover:text-gray-900"
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link to="/login" className="text-gray-600 hover:text-gray-900">
                  Login
                </Link>
                <Link to="/register" className="text-gray-600 hover:text-gray-900">
                  Register
                </Link>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;