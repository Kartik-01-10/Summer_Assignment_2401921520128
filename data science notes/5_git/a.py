# # 🔧 Initialize a new Git repository
# git init  # Create a new local Git repo

# # 🔗 Clone an existing repository
# git clone <repo_url>  # Clone remote repo to local

# # 📂 Check current repo status
# git status  # Show staged, unstaged, and untracked files

# # ➕ Add files to staging area
# git add <file_name>  # Stage a specific file
# git add .            # Stage all changes

# # 📝 Commit staged changes
# git commit -m "message"  # Commit with message
# git commit -a -m "message"  # Stage and commit tracked files

# # 🔄 View commit history
# git log  # Full commit history
# git log --oneline  # Compact view
# git log --graph  # Visual branch structure
# git log -p  # Show diffs with each commit

# # 🔍 View differences
# git diff  # Show unstaged changes
# git diff --staged  # Show staged changes
# git diff <branch1> <branch2>  # Compare branches

# # 🧹 Unstage or undo changes
# git reset <file>  # Unstage file
# git checkout -- <file>  # Discard changes in file
# git restore <file>  # Restore file to last commit

# # 🧽 Undo commits
# git reset --soft HEAD~1  # Undo last commit, keep changes staged
# git reset --mixed HEAD~1  # Undo last commit, keep changes unstaged
# git reset --hard HEAD~1  # Undo last commit, discard changes

# # 🔁 Revert a commit (safe undo)
# git revert <commit_hash>  # Create a new commit that undoes changes

# # 📤 Push changes to remote
# git push origin <branch>  # Push commits to remote branch
# git push -u origin <branch>  # Set upstream for branch

# # 📥 Pull latest changes
# git pull origin <branch>  # Fetch and merge remote changes
# git fetch  # Download changes without merging
# git merge origin/<branch>  # Merge fetched changes

# # 🌿 Branching
# git branch  # List local branches
# git branch <name>  # Create new branch
# git checkout <name>  # Switch to branch
# git checkout -b <name>  # Create and switch
# git branch -d <name>  # Delete branch (safe)
# git branch -D <name>  # Force delete branch

# # 🔀 Merge branches
# git merge <branch>  # Merge into current branch
# git merge --no-ff <branch>  # Force merge commit

# # 🧼 Stash changes
# git stash  # Save changes temporarily
# git stash list  # View stashes
# git stash apply  # Reapply stash
# git stash pop  # Apply and delete stash
# git stash drop  # Delete stash
# git stash clear  # Remove all stashes

# # 🧭 Remote management
# git remote -v  # Show remote URLs
# git remote add origin <url>  # Add remote
# git remote remove origin  # Remove remote
# git remote rename <old> <new>  # Rename remote

# # 🏷️ Tags
# git tag  # List tags
# git tag <name>  # Create tag
# git tag -a <name> -m "message"  # Annotated tag
# git show <tag>  # Show tag details
# git push origin <tag>  # Push tag
# git push origin --tags  # Push all tags

# # 🧠 Configuration
# git config --global user.name "Your Name"  # Set global username
# git config --global user.email "you@example.com"  # Set global email
# git config --list  # Show config
# git config --global core.editor "code --wait"  # Set VS Code as editor

# # 🧾 File history
# git log <file>  # History of a file
# git blame <file>  # Line-by-line author info

# # 🧪 Clean repo
# git clean -n  # Preview files to be deleted
# git clean -f  # Delete untracked files
# git clean -fd  # Delete untracked files and directories

# # 🔒 Authentication (for GitHub)
# git config --global credential.helper cache  # Cache credentials
# git config --global credential.helper store  # Save credentials

# # 🧰 Misc
# git show <commit>  # Show commit details
# git cherry-pick <commit>  # Apply specific commit
# git reflog  # Show all HEAD movements (great for recovery)
# git archive --format=zip HEAD > latest.zip  # Export repo as zip

# # 🧨 Delete repo (local)
# rm -rf .git  # Remove Git tracking from folder