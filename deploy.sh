#!/bin/bash

# Deploy script for QPython documentation
# Builds the site and deploys to gh-pages branch

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Run build first
echo "Building site..."
./build.sh

# Check if git repository
if [ ! -d .git ]; then
    echo "Error: Not a git repository"
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"

# Check if there are uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "Warning: You have uncommitted changes. Please commit them first."
    echo "Uncommitted files:"
    git status --short
    read -p "Do you want to continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

# Deploy to gh-pages
echo ""
echo "Deploying to gh-pages branch..."

# Create a temporary directory for the site
TEMP_DIR=$(mktemp -d)
cp -r site/* "$TEMP_DIR/"

# Switch to gh-pages branch (create if doesn't exist)
if git show-ref --verify --quiet refs/heads/gh-pages; then
    git checkout gh-pages
else
    git checkout --orphan gh-pages
    git rm -rf .
fi

# Remove old files (except .git)
find . -maxdepth 1 ! -name '.git' ! -name '.' ! -name '..' -exec rm -rf {} \;

# Copy new site content
cp -r "$TEMP_DIR"/* .

# Add all files
git add -A

# Commit
COMMIT_MSG="Deploy site - $(date '+%Y-%m-%d %H:%M:%S')"
if git diff --cached --quiet; then
    echo "No changes to commit"
else
    git commit -m "$COMMIT_MSG"
    echo "Committed: $COMMIT_MSG"
fi

# Push to remote
read -p "Push to origin/gh-pages? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push origin gh-pages
    echo ""
    echo "Deployed successfully!"
    echo "Site will be available at: https://qpython-android.github.io/qpython.org/"
else
    echo "Push aborted. You can push manually with: git push origin gh-pages"
fi

# Cleanup
rm -rf "$TEMP_DIR"

# Switch back to original branch
git checkout "$CURRENT_BRANCH"

echo ""
echo "Done!"
