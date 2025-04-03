#!/usr/bin/env python
"""
Setup script for "So You Think You Can Data?" Model Validation Course
This script installs all required dependencies and verifies the environment.
"""

import os
import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

def print_section(title):
    """Print a section title with formatting."""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80 + "\n")

def check_python_version():
    """Check if Python version is 3.9 or higher."""
    print_section("Checking Python Version")
    
    python_version = sys.version_info
    print(f"Detected Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 9):
        print("WARNING: This course recommends Python 3.9 or higher.")
        print("You may encounter issues with older versions.")
        return False
    
    print("✅ Python version check passed!")
    return True

def install_requirements():
    """Install required packages from requirements.txt."""
    print_section("Installing Required Packages")
    
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    
    if not os.path.exists(requirements_file):
        print(f"ERROR: Could not find {requirements_file}")
        print("Please make sure you're running this script from the course repository root.")
        return False
    
    print("Installing packages from requirements.txt...")
    print("This may take a few minutes depending on your internet connection.")
    print("Some packages might require additional system dependencies.")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Package installation failed with error code {e.returncode}")
        print("Please try installing packages manually with:")
        print(f"  pip install -r {requirements_file}")
        return False

def verify_installations():
    """Verify that all required packages are installed with correct versions."""
    print_section("Verifying Package Installations")
    
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    requirements = []
    
    # Parse requirements excluding comments and empty lines
    with open(requirements_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    
    print(f"Checking {len(requirements)} required packages...")
    
    # Check each requirement
    all_satisfied = True
    for requirement in requirements:
        try:
            pkg_resources.require(requirement)
            name = requirement.split('>=')[0] if '>=' in requirement else requirement
            version = pkg_resources.get_distribution(name).version
            print(f"✅ {name} {version} - Installed")
        except (DistributionNotFound, VersionConflict) as e:
            print(f"❌ {requirement} - Not satisfied: {str(e)}")
            all_satisfied = False
    
    if all_satisfied:
        print("\n✅ All required packages are installed with correct versions!")
    else:
        print("\n❌ Some packages are missing or have incorrect versions.")
        print("Please try running the installation step again or install them manually.")
    
    return all_satisfied

def check_jupyter():
    """Verify Jupyter notebook works properly."""
    print_section("Checking Jupyter Notebook")
    
    try:
        subprocess.check_call([sys.executable, "-m", "jupyter", "notebook", "--version"], 
                              stdout=subprocess.PIPE)
        print("✅ Jupyter notebook is properly installed!")
        
        print("\nTo start Jupyter notebook, run:")
        print("  jupyter notebook")
        print("\nThen navigate to verification-notebook.ipynb to confirm everything works.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Jupyter notebook is not installed or not working properly.")
        print("Please try installing it manually with:")
        print("  pip install jupyter notebook")
        return False

def create_directories():
    """Create necessary directories for the course."""
    print_section("Creating Course Directories")
    
    directories = ['notebooks', 'data', 'solutions', 'resources']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")
    
    print("\n✅ All necessary directories are in place!")
    return True

def main():
    """Main setup function."""
    print("\n" + "=" * 80)
    print(" So You Think You Can Data? - Model Validation Course Setup ".center(80, "="))
    print("=" * 80 + "\n")
    
    print("This script will set up your environment for the course.")
    print("It will check your Python version, install required packages,")
    print("and verify that everything is working properly.\n")
    
    # Run all setup steps
    steps = [
        check_python_version,
        install_requirements,
        verify_installations,
        create_directories,
        check_jupyter
    ]
    
    success_count = 0
    for step in steps:
        if step():
            success_count += 1
    
    # Print summary
    print_section("Setup Summary")
    print(f"Completed {success_count}/{len(steps)} setup steps successfully.")
    
    if success_count == len(steps):
        print("\n🎉 Congratulations! Your environment is fully set up for the course!")
        print("You can now open the verification notebook to confirm everything works.")
    else:
        print("\n⚠️ Setup completed with some warnings or errors.")
        print("Please address the issues mentioned above before starting the course.")
    
    print("\nIf you encounter any problems, please check the course Q&A section")
    print("or post in the discussion forum for help.")

if __name__ == "__main__":
    main()
