#!/bin/bash

echo "🚀 Starting deployment..."

# Check if git is initialized
if [ ! -d .git ]; then
    echo "Initializing git..."
    git init
    git config user.email "ksx2412@gmail.com"
    git config user.name "Ksx"
fi

# Check if remote exists
if ! git remote | grep -q "origin"; then
    echo "Adding GitHub remote..."
    git remote add origin git@github.com:ksx2412-sys/digitalpower-site.git
fi

# Stage and commit changes
echo "Committing changes..."
git add -A
git commit -m "SEO & Geo-targeting improvements" 2>/dev/null || echo "No new changes to commit"

# Ensure SSH key is in agent
echo "Setting up SSH authentication..."
ssh-add ~/.ssh/id_ed25519 2>/dev/null || true

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main

echo "✅ Deployment pushed! Vercel will auto-deploy from GitHub."
echo "Check your Vercel dashboard: https://vercel.com/dashboard"
