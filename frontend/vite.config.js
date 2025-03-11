import { defineConfig } from 'vite';

export default defineConfig({
  root: '.',  // Ensures Vite looks in the correct place
  build: {
    outDir: 'dist'
  }
});
