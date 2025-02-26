// frontend/src/admin/components/AdminSidebar.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAdminFeatures } from '../context/AdminContext';

const AdminSidebar = () => {
  const location = useLocation();
  const { features } = useAdminFeatures();
  
  return (
    <div className="hidden md:flex md:flex-shrink-0">
      <div className="flex flex-col w-64">
        <div className="flex flex-col h-0 flex-1 bg-gray-800">
          <div className="flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
            <div className="flex items-center flex-shrink-0 px-4">
              <span className="text-white text-xl font-semibold">Admin Dashboard</span>
            </div>
            <nav className="mt-5 flex-1 px-2 bg-gray-800 space-y-1">
              <Link
                to="/admin"
                className={`${
                  location.pathname === '/admin'
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
              >
                Dashboard
              </Link>
              <Link
                to="/admin/users"
                className={`${
                  location.pathname === '/admin/users'
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
              >
                User Management
              </Link>
              
              <div className="pt-4 pb-2">
                <div className="px-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">
                  Features
                </div>
              </div>
              
              {/* Dynamically render feature admin links */}
              {features.map((feature) => (
                <Link
                  key={feature.name}
                  to={`/admin/features/${feature.name}`}
                  className={`${
                    location.pathname.startsWith(`/admin/features/${feature.name}`)
                      ? 'bg-gray-900 text-white'
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                  } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
                >
                  {feature.displayName}
                </Link>
              ))}
            </nav>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminSidebar;