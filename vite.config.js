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
        // In-person / local pages
        chess_classes_noida: resolve(__dirname, 'chess-classes-noida/index.html'),
        chess_home_tutor_noida: resolve(__dirname, 'chess-home-tutor-noida/index.html'),
        // Online class landing pages
        online_chess_classes: resolve(__dirname, 'online-chess-classes/index.html'),
        online_chess_classes_for_kids: resolve(__dirname, 'online-chess-classes-for-kids/index.html'),
        online_chess_classes_usa: resolve(__dirname, 'online-chess-classes-usa/index.html'),
        online_chess_classes_uk: resolve(__dirname, 'online-chess-classes-uk/index.html'),
        online_chess_classes_canada: resolve(__dirname, 'online-chess-classes-canada/index.html'),
        online_chess_classes_australia: resolve(__dirname, 'online-chess-classes-australia/index.html'),
        online_chess_classes_saudi_arabia: resolve(__dirname, 'online-chess-classes-saudi-arabia/index.html'),
        // Blog
        blog: resolve(__dirname, 'blog/index.html'),
        blog_improve_rating: resolve(__dirname, 'blog/how-to-improve-chess-rating-fast/index.html'),
        blog_academic_performance: resolve(__dirname, 'blog/chess-improves-academic-performance/index.html'),
        // Legal pages
        privacy: resolve(__dirname, 'privacy.html'),
        terms: resolve(__dirname, 'terms.html'),
        refund: resolve(__dirname, 'refund.html')
      }
    }
  }
})
