import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// Em desenvolvimento (npm run dev), o Vite repassa /api para o backend.
// API_URL permite apontar para outro endereço; o padrão é a API local.
const apiUrl = process.env.API_URL ?? 'http://localhost:8000'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': { target: apiUrl },
    },
  },
})
