import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/layout/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import ProtectedRoute from './components/ProtectedRoute';
import { getFeatureRoutes } from './featureRegistry';

const App = () => {
  const featureRoutes = getFeatureRoutes();

  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          <main className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route 
                path="/dashboard" 
                element={
                  <ProtectedRoute>
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
                      <ProtectedRoute>
                        {route.element}
                      </ProtectedRoute>
                    } 
                  />
                ) : (
                  <Route 
                    key={index}
                    path={route.path} 
                    element={route.element} 
                  />
                )
              ))}
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
