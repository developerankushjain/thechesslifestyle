import { defineConfig } from 'vite'
import { resolve, dirname, relative } from 'path'
import { fileURLToPath } from 'url'
import fs from 'fs'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

function getHtmlEntries(dir) {
  const entries = {}
  function walk(currentDir) {
    const files = fs.readdirSync(currentDir)
    for (const file of files) {
      if (file === 'node_modules' || file === '.git' || file === '.agent' || file === 'dist' || file === 'public') continue

      const fullPath = resolve(currentDir, file)
      const stat = fs.statSync(fullPath)

      if (stat.isDirectory()) {
        walk(fullPath)
      } else if (file.endsWith('.html')) {
        let key = relative(__dirname, fullPath).replace(/\.html$/, '').replace(/[\/\\]/g, '_')
        if (key === 'index') key = 'main'
        entries[key] = fullPath
      }
    }
  }
  walk(__dirname)
  return entries
}

// Vite plugin: copy static asset directories into dist/ after build
function copyStaticDirs(dirs) {
  return {
    name: 'copy-static-dirs',
    closeBundle() {
      for (const { src, dest } of dirs) {
        const srcPath = resolve(__dirname, src)
        const destPath = resolve(__dirname, dest)
        if (!fs.existsSync(srcPath)) continue
        function copyDir(from, to) {
          fs.mkdirSync(to, { recursive: true })
          for (const item of fs.readdirSync(from)) {
            const fromItem = resolve(from, item)
            const toItem = resolve(to, item)
            if (fs.statSync(fromItem).isDirectory()) {
              copyDir(fromItem, toItem)
            } else {
              fs.copyFileSync(fromItem, toItem)
            }
          }
        }
        copyDir(srcPath, destPath)
        console.log(`[copy-static-dirs] Copied ${src} → ${dest}`)
      }
    }
  }
}

export default defineConfig({
  base: '/',
  plugins: [
    copyStaticDirs([
      { src: 'gallery', dest: 'dist/gallery' },
      { src: 'coaches', dest: 'dist/coaches' },
    ])
  ],
  build: {
    rollupOptions: {
      input: getHtmlEntries(__dirname)
    }
  }
})
