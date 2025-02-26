import { useAuth } from '../context/AuthContext';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="max-w-4xl mx-auto mt-8">
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <div className="bg-white shadow rounded-lg p-6">
        <h3 className="text-lg font-medium mb-2">Welcome!</h3>
        <p className="text-gray-600">
          You are logged in as: {user?.email}
        </p>
      </div>
    </div>
  );
}

export default Dashboard;