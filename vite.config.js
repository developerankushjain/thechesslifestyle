import { defineConfig } from 'vite'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        packages: resolve(__dirname, 'packages/index.html'),
        tournaments: resolve(__dirname, 'tournaments/index.html'),
        chess_classes_noida: resolve(__dirname, 'chess-classes-noida/index.html'),
        chess_home_tutor_noida: resolve(__dirname, 'chess-home-tutor-noida/index.html')
      }
    }
  }
})
