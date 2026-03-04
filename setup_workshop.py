"""
Setup script for the Git Merge Conflicts Workshop.
This script creates branches with intentional conflicts for learning purposes.
"""

import subprocess
import sys
import os


def run_git_command(command):
    """Run a git command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running: {command}")
        print(f"Error: {e.stderr}")
        return None


def check_git_repo():
    """Check if we're in a git repository."""
    result = run_git_command("git rev-parse --git-dir")
    if result is None:
        print("Error: Not in a git repository!")
        print("Please run: git init")
        sys.exit(1)


def create_initial_commit():
    """Create initial commit if needed."""
    status = run_git_command("git status --porcelain")
    if status:
        print("Creating initial commit...")
        run_git_command("git add .")
        run_git_command('git commit -m "Initial commit: Basic calculator"')
        print("Initial commit created.")
    else:
        commits = run_git_command("git log --oneline")
        if not commits:
            print("No commits found. Creating initial commit...")
            run_git_command("git add .")
            run_git_command('git commit -m "Initial commit: Basic calculator"')
            print("Initial commit created.")


def create_feature_power():
    """Create feature-power branch with power operation."""
    print("\nCreating feature-power branch...")
    
    # Switch to main first
    run_git_command("git checkout main")
    
    # Create and switch to feature-power branch
    run_git_command("git checkout -b feature-power")
    
    # Read the current calculator.py
    with open("calculator.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add power function after divide function
    power_function = '''def power(a, b):
    """Raise a to the power of b."""
    return a ** b


'''
    
    # Insert power function after divide function
    content = content.replace(
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n",
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n" + power_function
    )
    
    # Add power operator to main function
    content = content.replace(
        '    print("Operations: +, -, *, /")',
        '    print("Operations: +, -, *, /, ^")'
    )
    
    content = content.replace(
        '        operator = input("Enter operator (+, -, *, /): ")',
        '        operator = input("Enter operator (+, -, *, /, ^): ")'
    )
    
    # Add power case in the if-elif chain
    content = content.replace(
        '        elif operator == "/":\n            result = divide(num1, num2)\n        else:',
        '        elif operator == "/":\n            result = divide(num1, num2)\n        elif operator == "^":\n            result = power(num1, num2)\n        else:'
    )
    
    # Write the modified content
    with open("calculator.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Commit the changes
    run_git_command('git add calculator.py')
    run_git_command('git commit -m "Add power operation (^)"')
    
    print("feature-power branch created with power operation.")


def create_feature_modulo():
    """Create feature-modulo branch with modulo operation."""
    print("\nCreating feature-modulo branch...")
    
    # Switch to main first
    run_git_command("git checkout main")
    
    # Create and switch to feature-modulo branch
    run_git_command("git checkout -b feature-modulo")
    
    # Read the current calculator.py
    with open("calculator.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add modulo function after divide function
    modulo_function = '''def modulo(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a % b


'''
    
    # Insert modulo function after divide function
    content = content.replace(
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n",
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n" + modulo_function
    )
    
    # Add modulo operator to main function
    content = content.replace(
        '    print("Operations: +, -, *, /")',
        '    print("Operations: +, -, *, /, %")'
    )
    
    content = content.replace(
        '        operator = input("Enter operator (+, -, *, /): ")',
        '        operator = input("Enter operator (+, -, *, /, %): ")'
    )
    
    # Add modulo case in the if-elif chain
    content = content.replace(
        '        elif operator == "/":\n            result = divide(num1, num2)\n        else:',
        '        elif operator == "/":\n            result = divide(num1, num2)\n        elif operator == "%":\n            result = modulo(num1, num2)\n        else:'
    )
    
    # Write the modified content
    with open("calculator.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Commit the changes
    run_git_command('git add calculator.py')
    run_git_command('git commit -m "Add modulo operation (%)"')
    
    print("feature-modulo branch created with modulo operation.")


def create_main_browser():
    """Create main-browser branch as exact copy of main."""
    print("\nCreating main-browser branch...")
    
    # Switch to main first
    run_git_command("git checkout main")
    
    # Create and switch to main-browser branch
    run_git_command("git checkout -b main-browser")
    
    # No changes needed, it's an exact copy
    print("main-browser branch created (exact copy of main).")


def create_feature_power_browser():
    """Create feature-power-browser branch with power operation for browser demo."""
    print("\nCreating feature-power-browser branch...")
    
    # Switch to main-browser first
    run_git_command("git checkout main-browser")
    
    # Create and switch to feature-power-browser branch
    run_git_command("git checkout -b feature-power-browser")
    
    # Read the current calculator.py
    with open("calculator.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add power function after divide function
    power_function = '''def power(a, b):
    """Raise a to the power of b."""
    return a ** b


'''
    
    # Insert power function after divide function
    content = content.replace(
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n",
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n" + power_function
    )
    
    # Add power operator to main function
    content = content.replace(
        '    print("Operations: +, -, *, /")',
        '    print("Operations: +, -, *, /, ^")'
    )
    
    content = content.replace(
        '        operator = input("Enter operator (+, -, *, /): ")',
        '        operator = input("Enter operator (+, -, *, /, ^): ")'
    )
    
    # Add power case in the if-elif chain
    content = content.replace(
        '        elif operator == "/":\n            result = divide(num1, num2)\n        else:',
        '        elif operator == "/":\n            result = divide(num1, num2)\n        elif operator == "^":\n            result = power(num1, num2)\n        else:'
    )
    
    # Write the modified content
    with open("calculator.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Commit the changes
    run_git_command('git add calculator.py')
    run_git_command('git commit -m "Add power operation (^)"')
    
    print("feature-power-browser branch created with power operation.")


def create_feature_modulo_browser():
    """Create feature-modulo-browser branch with modulo operation for browser demo."""
    print("\nCreating feature-modulo-browser branch...")
    
    # Switch to main-browser first
    run_git_command("git checkout main-browser")
    
    # Create and switch to feature-modulo-browser branch
    run_git_command("git checkout -b feature-modulo-browser")
    
    # Read the current calculator.py
    with open("calculator.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add modulo function after divide function
    modulo_function = '''def modulo(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a % b


'''
    
    # Insert modulo function after divide function
    content = content.replace(
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n",
        "def divide(a, b):\n    \"\"\"Divide a by b.\"\"\"\n    if b == 0:\n        raise ValueError(\"Cannot divide by zero!\")\n    return a / b\n\n" + modulo_function
    )
    
    # Add modulo operator to main function
    content = content.replace(
        '    print("Operations: +, -, *, /")',
        '    print("Operations: +, -, *, /, %")'
    )
    
    content = content.replace(
        '        operator = input("Enter operator (+, -, *, /): ")',
        '        operator = input("Enter operator (+, -, *, /, %): ")'
    )
    
    # Add modulo case in the if-elif chain
    content = content.replace(
        '        elif operator == "/":\n            result = divide(num1, num2)\n        else:',
        '        elif operator == "/":\n            result = divide(num1, num2)\n        elif operator == "%":\n            result = modulo(num1, num2)\n        else:'
    )
    
    # Write the modified content
    with open("calculator.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Commit the changes
    run_git_command('git add calculator.py')
    run_git_command('git commit -m "Add modulo operation (%)"')
    
    print("feature-modulo-browser branch created with modulo operation.")


def main():
    """Main setup function."""
    print("=" * 60)
    print("Git Merge Conflicts Workshop Setup")
    print("=" * 60)
    
    # Check if we're in a git repo
    check_git_repo()
    
    # Create initial commit if needed
    create_initial_commit()
    
    # Check if branches already exist
    branches = run_git_command("git branch")
    existing_branches = ["feature-power", "feature-modulo", "main-browser", 
                        "feature-power-browser", "feature-modulo-browser"]
    has_existing = any(branch in branches for branch in existing_branches)
    
    if has_existing:
        response = input("\nBranches already exist. Delete and recreate? (y/n): ")
        if response.lower() == 'y':
            run_git_command("git checkout main")
            # Delete all existing branches
            for branch in existing_branches:
                run_git_command(f"git branch -D {branch} 2>nul || git branch -D {branch}")
        else:
            print("Setup cancelled.")
            sys.exit(0)
    
    # Create feature branches for command-line demo
    create_feature_power()
    create_feature_modulo()
    
    # Create browser-specific branches
    create_main_browser()
    create_feature_power_browser()
    create_feature_modulo_browser()
    
    # Return to main branch
    run_git_command("git checkout main")
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print("\nCommand-line demo branches:")
    print("1. git checkout feature-power    # Review the power feature")
    print("2. git checkout main")
    print("3. git merge feature-power       # Merge power (no conflict)")
    print("4. git merge feature-modulo      # Merge modulo (CONFLICT!)")
    print("\nBrowser demo branches (for GitHub web interface):")
    print("- main-browser (exact copy of main)")
    print("- feature-power-browser (power operation)")
    print("- feature-modulo-browser (modulo operation)")
    print("\nFollow the README.md for detailed instructions.")


if __name__ == "__main__":
    main()
