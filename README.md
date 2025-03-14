# Linter

## Usage

- Run the script with `python3 Main.py` and enter either a **GitHub repository URL** or a **local folder path**.
- The script will **clone** the repository into the specified download folder *(default: `~/Downloads/`)*.
- The script will **analyze** the content and print a summary of its findings in the terminal.
- A **Report.txt** will be generated for further inspection.
- Upon completion, the script returns an **exit code**:

| Exit Code | Meaning |
|-----------|----------------|
| `1` | Errors were found. |
| `0` | No errors detected. |

### Example Valid Paths
| Type               | Example |
|------------------|--------------------------------|
| **Full URL** | `https://github.com/JulianLundh/Linter` |
| **Short URL** | `github.com/JulianLundh/Linter` |
| **Absolute Path** | `~/Downloads/JulianLundh/Linter` |
| **Full Path** | `/Users/julian/Downloads/JulianLundh/Linter` |

## Requirements
To run this software, you need:

- Python 3
- pip (Python package manager)
- Git
- GitPython
- Trufflehog
- Gitignore Parser

## Installation Instructions

### 1: Install Python & pip
If Python is not installed, install it with:

**Ubuntu/Debian:**
```sh
sudo apt update && sudo apt install python3-pip -y
```

### 2: Install Git
```sh
sudo apt install git -y
```

### 3: Install Required Python Packages
```sh
pip install gitpython trufflehog gitignore_parser
```

## Configuration

- The **`config.json`** file allows you to specify which errors are permitted.
- It also lets you select the **download directory** where repositories will be cloned.
- If a specific issue is allowed, it will still be reported, but the script will return **exit code 0** instead of `1`.

## FAQ
- If running from a shared folder (e.g., macOS Parallels), move the file to a local Linux directory before executing.
