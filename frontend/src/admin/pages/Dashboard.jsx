// frontend/src/admin/pages/Dashboard.jsx
import React, { useState, useEffect } from 'react';
import api from '@/services/api';

const AdminDashboard = () => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const response = await api.get('/api/v1/admin/dashboard');
        setStats(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching admin dashboard data:', error);
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return <div>Loading dashboard data...</div>;
  }

  return (
    <div>
      <h1 className="text-2xl font-semibold mb-6">Admin Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-gray-500 text-sm font-medium uppercase mb-2">Total Users</h2>
          <div className="text-3xl font-bold">{stats?.total_users || 0}</div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-gray-500 text-sm font-medium uppercase mb-2">Active Features</h2>
          <div className="text-3xl font-bold">{stats?.active_features?.length || 0}</div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-gray-500 text-sm font-medium uppercase mb-2">System Status</h2>
          <div className="text-3xl font-bold">{stats?.system_status || 'Unknown'}</div>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-medium mb-4">Active Features</h2>
        <ul className="divide-y divide-gray-200">
          {stats?.active_features?.map((feature) => (
            <li key={feature} className="py-3">{feature}</li>
          )) || <li className="py-3">No active features</li>}
        </ul>
      </div>
    </div>
  );
};

export default AdminDashboard;