# Git Merge Conflicts Workshop

A simple Python calculator application designed to teach git merge conflict resolution in 30 minutes.

## Prerequisites

- Git installed
- Python 3.6+ installed
- Basic understanding of git commands (commit, branch, merge)

## Workshop Setup

### Step 1: Initial Setup

1. Clone this repository (if working from remote):
   ```bash
   git clone <repository-url>
   cd SE-merge-conflict-workshop
   ```

2. Verify the initial state:
   ```bash
   git log --oneline
   git branch
   ```

### Step 2: Create Conflicting Branches

Run the setup script to create branches with conflicts:
```bash
python setup_workshop.py
```

This script will:
- Create a `feature-power` branch that adds a power operation
- Create a `feature-modulo` branch that adds a modulo operation
- Both branches modify the same sections of code, creating merge conflicts

### Step 3: Experience the Conflict

1. Switch to the `feature-power` branch:
   ```bash
   git checkout feature-power
   ```
   Review the changes made in this branch.

2. Switch back to `main`:
   ```bash
   git checkout main
   ```

3. Merge `feature-power`:
   ```bash
   git merge feature-power
   ```
   This should merge successfully.

4. Now try to merge `feature-modulo`:
   ```bash
   git merge feature-modulo
   ```
   **This will create merge conflicts!**

### Step 4: Resolve the Conflicts

1. Open `calculator.py` in your editor. You'll see conflict markers:
   ```
   <<<<<<< HEAD
   (code from feature-power)
   =======
   (code from feature-modulo)
   >>>>>>> feature-modulo
   ```

2. Resolve the conflicts by:
   - Keeping both features (power and modulo)
   - Removing the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Ensuring the code is correct and complete

3. Stage the resolved file:
   ```bash
   git add calculator.py
   ```

4. Complete the merge:
   ```bash
   git commit
   ```
   (Git will open an editor with a default merge commit message)

### Step 5: Verify the Resolution

1. Test the calculator:
   ```bash
   python calculator.py
   ```

2. Verify all operations work:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Power (^)
   - Modulo (%)

## Learning Objectives

After completing this workshop, you should understand:

1. How merge conflicts occur
2. How to identify conflict markers in files
3. How to resolve conflicts manually
4. How to complete a merge after resolving conflicts
5. Best practices for avoiding conflicts

## Troubleshooting

### Reset to Start Over

If you want to start fresh:
```bash
git checkout main
git branch -D feature-power feature-modulo
python setup_workshop.py
```

### View Conflict Details

To see what's conflicting:
```bash
git status
git diff
```

## Additional Exercises

1. Create your own feature branch and merge it
2. Practice resolving conflicts with different strategies
3. Try using `git merge --abort` to cancel a merge
4. Experiment with `git rebase` instead of merge

## Notes for Instructors

- This workshop is designed to be completed in 30 minutes
- The conflicts are intentionally simple and easy to resolve
- Students should understand both features need to be kept
- Emphasize the importance of testing after resolving conflicts
