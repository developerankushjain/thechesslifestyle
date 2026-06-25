const fs = require('fs');
const path = require('path');

function walk(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const stat = fs.statSync(path.join(dir, file));
    if (stat.isDirectory()) {
      if (file !== 'node_modules' && file !== 'dist' && !file.startsWith('.')) {
        walk(path.join(dir, file), fileList);
      }
    } else {
      if (file.endsWith('.html')) {
        fileList.push(path.join(dir, file));
      }
    }
  }
  return fileList;
}

const htmlFiles = walk(__dirname);

let updatedFiles = 0;

for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  // 1. Fix missing logo img
  // Pattern: match <div class="logo"> ... </div>
  const logoRegex = /<div class="logo">([\s\S]*?)<\/div>/g;
  content = content.replace(logoRegex, (match, inner) => {
    if (!inner.includes('<img')) {
      changed = true;
      // Inject img
      const newInner = `\n        <img src="/favicon.svg" alt="TheChessLifestyle" class="logo-icon" width="28" height="31" loading="lazy"/>` + inner;
      return `<div class="logo">${newInner}</div>`;
    }
    return match;
  });

  // 2. Fix lp.js paths and module types
  // Some have ../lp.js, some might have lp.js without type="module"
  const lpJsRegex = /<script\s+src="[^"]*lp\.js"><\/script>/g;
  if (lpJsRegex.test(content)) {
    content = content.replace(lpJsRegex, '<script type="module" src="/lp.js"></script>');
    changed = true;
  } else if (!content.includes('/lp.js') && !content.includes('lp.js')) {
    // 3. Inject lp.js if entirely missing
    content = content.replace('</body>', '  <script type="module" src="/lp.js"></script>\n  </body>');
    changed = true;
  }

  // 4. Update the schema logo from favicon.png to favicon.svg
  if (content.includes('favicon.png') && content.includes('"@type": "ImageObject"')) {
    content = content.replace(/"url":\s*"https:\/\/www\.thechesslifestyle\.com\/favicon\.png"/g, '"url": "https://www.thechesslifestyle.com/favicon.svg"');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(file, content, 'utf8');
    updatedFiles++;
    console.log(`Updated: ${file}`);
  }
}

console.log(`\nFinished updating ${updatedFiles} files.`);
