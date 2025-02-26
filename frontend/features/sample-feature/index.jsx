// features/sample-feature/index.js
import SamplePage from './pages/SamplePage';
import SampleFeatureAdmin from './admin/SampleFeatureAdmin';


const sampleFeature = {
  name: 'sample-feature',
  routes: [
    {
      path: '/sample',
      element: <SamplePage />,
      protected: true,
    }
  ],
  navItems: [
    {
      label: 'Sample Feature',
      path: '/sample',
      requiresAuth: true,
    },
  ],
  admin: {
    name: 'sample_feature',
    displayName: 'Sample Feature',
    description: 'Manage sample items and view statistics',
    component: SampleFeatureAdmin,
    path: '/admin/features/sample_feature',
    icon: 'chart-bar'
  }
};

export default sampleFeature;