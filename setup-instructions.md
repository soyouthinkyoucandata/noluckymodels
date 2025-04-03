# Detailed Setup Instructions

This document provides detailed instructions for setting up your environment for the "So You Think You Can Data?" Model Validation Course.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Operating System Specific Instructions](#operating-system-specific-instructions)
3. [Installation Options](#installation-options)
4. [Troubleshooting Common Issues](#troubleshooting-common-issues)
5. [Manual Package Installation](#manual-package-installation)

## Prerequisites

Before proceeding with the setup, ensure you have the following:

- A computer with at least 4GB of RAM (8GB recommended)
- At least 2GB of free disk space
- Internet connection for downloading packages
- Basic familiarity with the command line

## Operating System Specific Instructions

### Windows

1. **Install Python 3.9+**:
   - Download the installer from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - Choose the option to install pip

2. **Verify Installation**:
   - Open Command Prompt and type:
   ```
   python --version
   pip --version
   ```

3. **Install Git** (optional but recommended):
   - Download from [git-scm.com](https://git-scm.com/download/win)
   
### macOS

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.9+**:
   ```bash
   brew install python@3.9
   ```

3. **Verify Installation**:
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux (Ubuntu/Debian)

1. **Update package lists**:
   ```bash
   sudo apt update
   ```

2. **Install Python 3.9+ and development tools**:
   ```bash
   sudo apt install python3.9 python3.9-dev python3-pip python3-venv
   ```

3. **Install additional dependencies for specific packages**:
   ```bash
   sudo apt install build-essential libssl-dev libffi-dev tk-dev
   ```

4. **Verify Installation**:
   ```bash
   python3.9 --version
   pip3 --version
   ```

## Installation Options

### Option 1: Automated Setup with setup.py (Recommended)

1. Clone or download the course repository:
   ```bash
   git clone https://github.com/soyouthinkyoucandata/noluckymodels.git
   cd noluckymodels
   ```

2. Run the setup script:
   ```bash
   # On Windows
   python setup.py
   
   # On macOS/Linux
   python3 setup.py
   ```

3. Follow the on-screen instructions.

### Option 2: Setup with pip

1. Clone or download the repository:
   ```bash
   git clone https://github.com/soyouthinkyoucandata/noluckymodels.git
   cd noluckymodels
   ```

2. Install the required packages:
   ```bash
   # On Windows
   pip install -r requirements.txt
   
   # On macOS/Linux
   pip3 install -r requirements.txt
   ```

### Option 3: Setup with conda

1. If you don't have conda installed, download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Clone or download the repository:
   ```bash
   git clone https://github.com/soyouthinkyoucandata/noluckymodels.git
   cd noluckymodels
   ```

3. Create and activate the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate mlvalidation
   ```

## Troubleshooting Common Issues

### Python Version Issues

**Issue**: Setup script shows warning about Python version.
**Solution**: Install Python 3.9 or higher from [python.org](https://www.python.org/downloads/).

### Package Installation Failures

**Issue**: Error when installing packages with pip.
**Solution**: 
1. Try updating pip:
   ```bash
   python -m pip install --upgrade pip
   ```

2. Install packages one by one to identify the problematic package:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

### Prophet Installation Issues

**Issue**: Prophet fails to install, especially on Windows.
**Solution**: Prophet requires additional compilers on Windows. Try:

1. Install Microsoft C++ Build Tools with the "Desktop development with C++" workload.
2. Try installing Prophet separately: `pip install prophet`
3. If it still fails, Prophet is not critical for most of the course - you can skip it.

### Jupyter Notebook Not Starting

**Issue**: `jupyter notebook` command not found or fails to start.
**Solution**:
1. Make sure Jupyter is installed:
   ```bash
   pip install jupyter notebook
   ```
   
2. Try running with the full path:
   ```bash
   python -m jupyter notebook
   ```

## Manual Package Installation

If you're experiencing issues with the automatic setup, here's how to install each package manually:

```bash
# Core packages
pip install numpy==1.22.0
pip install pandas==1.4.0
pip install scikit-learn==1.0.2

# Visualization
pip install matplotlib==3.5.1
pip install seaborn==0.11.2
pip install plotly==5.5.0

# Statistics
pip install scipy==1.7.3
pip install statsmodels==0.13.1

# Network analysis
pip install networkx==2.6.3

# Jupyter
pip install jupyter==1.0.0
pip install notebook==6.4.8

# Time series (optional)
pip install prophet==1.0.1
```

## Verification

After setting up your environment, run the verification notebook to ensure everything is working correctly:

```bash
jupyter notebook verification-notebook.ipynb
```

If all cells run without errors, your environment is ready for the course!
