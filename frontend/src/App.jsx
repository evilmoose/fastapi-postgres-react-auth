import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { AdminProvider } from './admin/context/AdminContext';
import Navbar from './components/layout/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import ProtectedRoute from './components/ProtectedRoute';
import AdminLayout from './admin/components/AdminLayout';
import AdminDashboard from './admin/pages/Dashboard';
import { getFeatureRoutes, getFeatureAdminComponents } from './featureRegistry';

const App = () => {
  const featureRoutes = getFeatureRoutes();
  const featureAdminComponents = getFeatureAdminComponents();

  return (
    <AuthProvider>
      <AdminProvider>
        <Router>
          <div className="min-h-screen bg-gray-50">
            <Routes>
              {/* Admin routes */}
              <Route 
                path="/admin" 
                element={
                  <ProtectedRoute requiredRoles={['admin']}>
                    <AdminLayout />
                  </ProtectedRoute>
                }
              >
                <Route index element={<AdminDashboard />} />
                {/*<Route path="users" element={<UserManagement />} />*/}
                
                {/* Dynamically render feature admin routes */}
                {featureAdminComponents.map((admin, index) => (
                  <Route 
                    key={index}
                    path={`features/${admin.name}`} 
                    element={admin.component} 
                  />
                ))}
              </Route>
              
              {/* Regular routes with navbar */}
              <Route path="/" element={<><Navbar /><Home /></>} />
              <Route path="/login" element={<><Navbar /><Login /></>} />
              <Route path="/register" element={<><Navbar /><Register /></>} />
              <Route 
                path="/dashboard" 
                element={
                  <ProtectedRoute>
                    <Navbar />
                    <Dashboard />
                  </ProtectedRoute>
                } 
              />
              
              {/* Dynamically render feature routes */}
              {featureRoutes.map((route, index) => (
                route.protected ? (
                  <Route 
                    key={index}
                    path={route.path} 
                    element={
                      <ProtectedRoute requiredRoles={route.requiredRoles || []}>
                        <Navbar />
                        {route.element}
                      </ProtectedRoute>
                    } 
                  />
                ) : (
                  <Route 
                    key={index}
                    path={route.path} 
                    element={<><Navbar />{route.element}</>} 
                  />
                )
              ))}
            </Routes>
          </div>
        </Router>
      </AdminProvider>
    </AuthProvider>
  );
}

export default App;
