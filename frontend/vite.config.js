import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  root: 'src', // ✅ Set root to "src"
  build: {
    outDir: '../dist', // ✅ Build output outside of src
    rollupOptions: {
      input: 'src/main.jsx' // ✅ Ensure entry file is set correctly
    }
  }
});
