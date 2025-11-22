# Deploying Your CV Website

This guide will help you deploy your new CV website to GitHub Pages so it's accessible to the world.

## Prerequisites
- A GitHub account.
- Git installed on your computer.

## Option 1: Quick Deployment (Command Line)

I've included a script to handle the deployment for you.

1.  **Initialize Git (if not already done):**
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2.  **Create a Repository on GitHub:**
    - Go to [GitHub.com/new](https://github.com/new).
    - Name your repository `cv` (or `username.github.io` for your main site).
    - Click "Create repository".

3.  **Link and Push:**
    - Copy the commands under "…or push an existing repository from the command line".
    - Run them in your terminal. It usually looks like:
      ```bash
      git remote add origin https://github.com/YOUR_USERNAME/cv.git
      git branch -M main
      git push -u origin main
      ```

4.  **Enable GitHub Pages:**
    - Go to your repository **Settings** > **Pages**.
    - Under **Source**, select `main` branch.
    - Click **Save**.
    - Your site will be live at `https://YOUR_USERNAME.github.io/cv/` shortly!

## Option 2: Manual Upload

1.  Go to [GitHub.com/new](https://github.com/new) and create a repository.
2.  Click "uploading an existing file".
3.  Drag and drop `index.html`, `styles.css`, and `script.js`.
4.  Commit changes.
5.  Enable GitHub Pages in Settings (same as above).

## Customizing Content

Open `index.html` and replace the placeholder text (e.g., `[Your Name]`, `[Job Title]`) with your actual information.
