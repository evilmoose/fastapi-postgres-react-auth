// frontend/src/features/sample-feature/admin/SampleFeatureAdmin.jsx
import React, { useState, useEffect } from 'react';
import api from '@/services/api';

const SampleFeatureAdmin = () => {
  const [stats, setStats] = useState(null);
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [statsResponse, itemsResponse] = await Promise.all([
          api.get('/api/v1/admin/features/sample_feature/stats'),
          api.get('/api/v1/admin/features/sample_feature/items')
        ]);
        
        setStats(statsResponse.data);
        setItems(itemsResponse.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching sample feature admin data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading sample feature data...</div>;
  }

  return (
    <div>
      <h1 className="text-2xl font-semibold mb-6">Sample Feature Administration</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-gray-500 text-sm font-medium uppercase mb-2">Total Items</h2>
          <div className="text-3xl font-bold">{stats?.total_items || 0}</div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-gray-500 text-sm font-medium uppercase mb-2">Top Users</h2>
          <ul className="mt-2 divide-y divide-gray-200">
            {stats?.top_users?.map((user) => (
              <li key={user.user_id} className="py-2">
                User ID: {user.user_id} - {user.item_count} items
              </li>
            )) || <li className="py-2">No data available</li>}
          </ul>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-medium">All Sample Items</h2>
        </div>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User ID</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {items.length > 0 ? (
                items.map((item) => (
                  <tr key={item.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.id}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{item.title}</td>
                    <td className="px-6 py-4 text-sm text-gray-500">{item.description}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.user_id}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" className="px-6 py-4 text-center text-sm text-gray-500">No items found</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default SampleFeatureAdmin;