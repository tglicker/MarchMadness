import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],  // ✅ Now Vite knows it's a React project
  root: ".",  
  build: {
    outDir: "dist",
    rollupOptions: {
      input: "index.html"
    }
  }
});
