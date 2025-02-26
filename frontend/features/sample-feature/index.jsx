// features/sample-feature/index.js
import SamplePage from './pages/SamplePage';

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
    }
  ],
};

export default sampleFeature;