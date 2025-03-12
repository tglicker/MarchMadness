import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],  // ✅ Enables React support
  root: '.',  // Keeps the root as expected
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: 'index.html' // Ensures correct entry file
    }
  }
});
