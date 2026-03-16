# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the QPython website and documentation repository (www.qpython.org). QPython is a Python script engine for Android devices. The site is built with [Sphinx](https://www.sphinx-doc.org/) using reStructuredText (.rst) source files.

## Build Commands

All build commands should be run from the `qpython-docs/` directory:

```bash
cd qpython-docs
```

### Development Build (Local Testing)

Build HTML documentation for local testing:

```bash
make html
```

Output will be in `qpython-docs/build/html/`. Open `build/html/index.html` in a browser to preview.

### Production Build (Deployment)

Build the full site including analytics, static file processing, and copy to the deployment directory:

```bash
./build.sh
```

This script:
1. Removes the existing `docs/` folder at the repository root
2. Runs `make html` to build the documentation
3. Adds Google Analytics and Facebook comments via `add-analytics.py`
4. Renames `_static/` to `static/` and `_images/` to `images/`
5. Copies additional static files (CNAME, favicon.ico, index.html, privacy pages, etc.)
6. Outputs final site to `/docs/` (which is deployed via GitHub Pages)

### Other Useful Commands

```bash
make clean          # Remove build artifacts
make linkcheck      # Check for broken external links
make doctest        # Run doctests in documentation
```

## Project Architecture

### Directory Structure

```
qpython-docs/
├── source/                 # Documentation source files (.rst)
│   ├── document.rst        # Main toctree (entry point)
│   ├── conf.py             # Sphinx configuration
│   ├── _static/            # Static assets (CSS, images)
│   ├── en/                 # English documentation
│   │   ├── guide.rst
│   │   ├── faq.rst
│   │   └── ...
│   ├── zh/                 # Chinese documentation
│   └── qpython_theme/      # Custom Sphinx theme
│       └── __init__.py
├── build.sh                # Production build script
├── add-analytics.py        # Post-processor for analytics injection
├── extra.txt               # Analytics code template
├── requirements.txt        # Python dependencies
└── Makefile                # Sphinx build commands

docs/                       # Built site (deployment target)
├── index.html              # Site homepage
├── document.html           # Documentation homepage
├── en/                     # Built English docs
├── _sources/               # Source archives (for Sphinx)
└── ...
```

### Key Files

- **`qpython-docs/source/conf.py`**: Sphinx configuration including theme (`qpython_theme`), version, and extensions
- **`qpython-docs/source/document.rst`**: Main documentation entry point with toctree
- **`qpython-docs/build.sh`**: Production build script that processes the Sphinx output and prepares it for deployment
- **`qpython-docs/extra.txt`**: Template for injecting Google Analytics and Facebook comments into HTML
- **`docs/CNAME`**: Configures custom domain (www.qpython.org) for GitHub Pages

### Custom Theme

The documentation uses a custom Sphinx theme located at `qpython-docs/source/qpython_theme/`. The theme path is registered in `conf.py` via the `qpython_theme` package.

### Documentation Languages

- English: `qpython-docs/source/en/`
- Chinese: `qpython-docs/source/zh/`

Each language has its own toctree structure. The master document (`document.rst`) includes the English guide by default and links to Chinese content via `zhindex.rst`.

### Deployment

The `docs/` folder at the repository root is the deployment target. It is served via GitHub Pages. After making changes:

1. Run `./build.sh` to rebuild the site
2. Commit the changes in both `qpython-docs/source/` (source) and `docs/` (built output)
3. Push to deploy
