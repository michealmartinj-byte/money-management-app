# GitHub Setup Guide for Money Manager

This guide shows you how to push this project to GitHub.

## Prerequisites
- Git installed on your computer (download from https://git-scm.com/)
- GitHub account (create at https://github.com/)

## Steps to upload to GitHub

### 1. Create a new repository on GitHub
- Go to https://github.com/new
- Repository name: `money-manager-martingale` (or your preferred name)
- Description: "💰 Money Management App with percentage-based Martingale trading strategy"
- Visibility: Public (or Private if you prefer)
- **DO NOT** check "Initialize with README" (we already have one)
- Click "Create repository"

### 2. Initialize Git and push code

Open PowerShell in the project folder and run:

```pwsh
cd "C:\Users\Madhusudhan\Documents\money management app"

# Initialize git repository
git init

# Configure git (replace with your GitHub username and email)
git config user.name "Your GitHub Username"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Money Manager GUI with Martingale simulator"

# Add GitHub as remote (replace USERNAME/REPO with your GitHub username and repo name)
git remote add origin https://github.com/USERNAME/money-manager-martingale.git

# Push to GitHub (you'll be prompted for GitHub credentials)
git branch -M main
git push -u origin main
```

### 3. Authentication (first time only)
- If prompted for username/password, use your GitHub credentials
- Alternatively, generate a Personal Access Token for more secure authentication:
  - Go to https://github.com/settings/tokens
  - Click "Generate new token"
  - Select scopes: `repo` (full control of private repositories)
  - Copy the token and paste it when git asks for password

### 4. Verify upload
- Go to https://github.com/USERNAME/money-manager-martingale
- You should see your code there!

## Common Git Commands

```pwsh
# Check git status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature-name

# Commit changes
git add .
git commit -m "Your commit message"

# Push changes
git push origin main

# Pull latest changes
git pull origin main
```

## Optional: Use GitHub Desktop
If you prefer a GUI, download GitHub Desktop from https://desktop.github.com/ instead of command-line git.

---

**Questions?** Check GitHub's official guide: https://docs.github.com/en/get-started

