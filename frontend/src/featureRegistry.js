// src/featureRegistry.js
const registeredFeatures = [];

export function registerFeature(feature) {
  registeredFeatures.push(feature);
}

export function getRegisteredFeatures() {
  return registeredFeatures;
}

export function getFeatureRoutes() {
  return registeredFeatures.flatMap(feature => feature.routes || []);
}

export function getFeatureNavItems() {
  return registeredFeatures.flatMap(feature => feature.navItems || []);
}