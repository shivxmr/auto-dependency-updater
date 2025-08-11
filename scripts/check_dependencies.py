import subprocess
import sys
from pathlib import Path

def check_for_outdated_packages():
    """Checks for outdated pip packages and returns a dictionary of updates."""
    print("Checking for outdated packages...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated"],
            capture_output=True,
            text=True,
            check=True,
        )
        
        lines = result.stdout.strip().split('\n')[2:]  # Skip header lines
        if not lines:
            print("All packages are up to date.")
            return {}
            
        updates = {}
        for line in lines:
            parts = line.split()
            package = parts[0]
            latest_version = parts[2]
            updates[package] = latest_version
            
        print(f"Found outdated packages: {list(updates.keys())}")
        return updates

    except subprocess.CalledProcessError as e:
        print(f"Error checking for outdated packages: {e.stderr}")
        return {}

def update_requirements_file(updates):
    """Updates the requirements.txt file with the latest package versions."""
    requirements_path = Path("requirements.txt")
    if not requirements_path.is_file():
        print("requirements.txt not found.")
        return

    print("Updating requirements.txt...")
    lines = requirements_path.read_text().splitlines()
    new_lines = []
    for line in lines:
        package_name = line.split("==")[0]
        if package_name in updates:
            new_lines.append(f"{package_name}=={updates[package_name]}")
        else:
            new_lines.append(line)
            
    requirements_path.write_text("\n".join(new_lines) + "\n")
    print("requirements.txt updated successfully.")

import os

def main():
    """Main function to check and update dependencies."""
    updates = check_for_outdated_packages()
    if updates:
        update_requirements_file(updates)
        if "GITHUB_OUTPUT" in os.environ:
            update_list_md = "\\n".join([f"- `{k}` to `{v}`" for k, v in updates.items()])
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write(f"updates={update_list_md}")

if __name__ == "__main__":
    main()
