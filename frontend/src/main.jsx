import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { registerFeature } from './featureRegistry.js'
// import App from './App.jsx'

// Import features
import sampleFeature from '../features/sample-feature'

// Register features
registerFeature(sampleFeature)

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
