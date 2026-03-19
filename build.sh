#!/bin/bash

# Build script for QPython documentation
# Supports both English and Chinese

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="python3.12"

echo "Building QPython documentation..."
echo ""

# Clean previous build
echo "Cleaning previous build..."
rm -rf site

# Build English site
echo "Building English site..."
$PYTHON -m mkdocs build

# Build Chinese site
echo "Building Chinese site..."
$PYTHON -m mkdocs build -f mkdocs-zh.yml

# Create root index.html
echo "Creating root index.html..."
cat > site/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>QPython Documentation</title>
    <meta http-equiv="refresh" content="1; url=en/">
    <style>
        body {
            font-family: Roboto, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #000;
            color: #fff;
        }
        .container {
            text-align: center;
        }
        .logo {
            margin-bottom: 30px;
        }
        .logo img {
            height: 80px;
        }
        h1 {
            font-weight: 300;
            margin-bottom: 40px;
        }
        .languages {
            display: flex;
            gap: 20px;
            justify-content: center;
        }
        .lang-btn {
            padding: 15px 40px;
            border: 2px solid #49B300;
            color: #49B300;
            text-decoration: none;
            border-radius: 5px;
            transition: all 0.3s;
            font-size: 18px;
        }
        .lang-btn:hover {
            background: #49B300;
            color: #000;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="en/static/img_logo.png" alt="QPython">
        </div>
        <h1>Choose your language / 选择语言</h1>
        <div class="languages">
            <a href="en/" class="lang-btn">English</a>
            <a href="zh/" class="lang-btn">中文</a>
        </div>
    </div>
</body>
</html>
EOF

# Copy additional HTML files from source to site
if ls source/*.html 1> /dev/null 2>&1; then
    echo "Copying additional HTML files..."
    cp source/*.html site/
fi

# Copy CNAME file if exists
if [ -f source/CNAME ]; then
    echo "Copying CNAME file..."
    cp source/CNAME site/
fi

echo ""
echo "Build complete!"
echo ""
echo "Output directories:"
echo "  - English: site/en/"
echo "  - Chinese: site/zh/"
echo "  - Root: site/index.html"
echo ""
echo "To preview locally:"
echo "  cd site && python -m http.server 8000"
