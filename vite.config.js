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
        chess_home_tutor_noida: resolve(__dirname, 'chess-home-tutor-noida/index.html'),
        online_chess_classes: resolve(__dirname, 'online-chess-classes/index.html'),
        online_chess_classes_for_kids: resolve(__dirname, 'online-chess-classes-for-kids/index.html'),
        online_chess_classes_usa: resolve(__dirname, 'online-chess-classes-usa/index.html'),
        online_chess_classes_uk: resolve(__dirname, 'online-chess-classes-uk/index.html'),
        online_chess_classes_canada: resolve(__dirname, 'online-chess-classes-canada/index.html'),
        online_chess_classes_australia: resolve(__dirname, 'online-chess-classes-australia/index.html'),
        online_chess_classes_saudi_arabia: resolve(__dirname, 'online-chess-classes-saudi-arabia/index.html')
      }
    }
  }
})
