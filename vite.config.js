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

export default defineConfig({
  base: '/',
  build: {
    rollupOptions: {
      input: getHtmlEntries(__dirname)
    }
  }
})
