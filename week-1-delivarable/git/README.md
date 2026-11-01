# Learning Git and GitHub 🚀

This repository serves as a personal log and documentation of my journey learning Git version control and GitHub. 

---

## 🛠️ Git (Local Version Control)

### What is Git?
Git is a distributed version control system designed to track changes in source code during software development. It allows multiple developers to work together on the same project without overwriting each other's work.

### Git Configuration & Setup
Before getting started, you need to configure your identity (username and email) so Git can attribute commits to you:

```bash
# Set your global username
git config --global user.name "Your Name"

# Set your global email address
git config --global user.email "your.email@example.com"
```

### Essential Git Commands
* **`git init`**: Initializes a brand new, empty local Git repository.
* **`git status`**: Shows the state of the working directory and the staging area (which files are tracked, untracked, or modified).
* **`git add <file>`**: Adds files from the working directory to the staging area, preparing them to be committed.
* **`git commit -m "your message"`**: Saves the staged snapshot of changes to the project history with a descriptive message.
* **`git log`**: Displays a chronological list of all commits made in the repository.

---

## 🌐 GitHub (Remote Collaboration)

Here are the key workflows and concepts covered during my GitHub learning journey:

* **Creating a Repository**: Learnt how to create a new remote repository on GitHub to host project files.
* **Connecting Local to Remote**: Linked the local Git repository to GitHub using:
  ```bash
  git remote add origin <repository-url>
  ```
* **Pushing Changes**: Uploaded local commits to the remote GitHub repository using:
  ```bash
  git push -u origin main
  ```
* **Branching & Switching**: Learnt how to isolate features by creating and switching between branches safely:
  ```bash
  # Create a new branch
  git branch new-feature
  
  # Switch to the new branch
  git checkout new-feature
  ```
* **Cloning a Repository**: Learnt how to download an existing remote repository onto a new local folder on a computer:
  ```bash
  git clone <repository-url>
  ```
* **Ignoring Files (`.gitignore`)**: Set up a `.gitignore` file to tell Git which files or folders (like environment variables, `node_modules`, or system logs) should be ignored and never tracked.
* **Documenting Projects (`README.md`)**: Discovered how to use Markdown syntax to write project descriptions, documentation, and user guides (just like this file!).
