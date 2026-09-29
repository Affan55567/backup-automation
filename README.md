# Backup Automation Tool

A Python automation script that backs up client data from a source directory to a backup directory with comprehensive logging.

## Features

- 📁 **Automated Backup**: Copies entire `ClientData` directory to `ClientBackup`
- 📊 **File Counting**: Automatically counts and reports the number of files backed up
- 📝 **Logging**: Detailed logging with success and error messages
- ✅ **Error Handling**: Gracefully handles errors and logs exceptions
- 🔄 **Directory Merge**: Uses `dirs_exist_ok=True` to merge with existing backups

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Usage

### Basic Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Affan55567/backup-automation.git
   cd backup-automation
   ```

2. Ensure you have a `ClientData` folder with files to backup in the same directory as the script

3. Run the script:
   ```bash
   python automation1.py
   ```

### Expected Output

```
AUTOMATE - INFO - Backup started
AUTOMATE - INFO - Backup completed
AUTOMATE - INFO - Files backed up: 42
```

## How It Works

1. **Initialize Logger**: Sets up logging to console with formatted messages
2. **Check Source**: Verifies that `ClientData` directory exists
3. **Copy Files**: Recursively copies all files from `ClientData` to `ClientBackup`
4. **Count Files**: Traverses the backup directory and counts all files
5. **Log Results**: Reports the total number of files backed up
6. **Error Handling**: Catches and logs any exceptions that occur

## Directory Structure

```
backup-automation/
├── automation1.py       # Main automation script
├── README.md            # This file
└── ClientData/          # Source directory (create this)
    └── files...         # Your files to backup
```

## Error Cases

- **ClientData not found**: If the source directory doesn't exist, the script logs an error and continues
- **Permission issues**: Any file permission errors are caught and logged

## Improvements Made

This script demonstrates:
- ✅ Proper logging setup
- ✅ Pathlib for cross-platform file handling
- ✅ Exception handling
- ✅ Recursive directory traversal
- ✅ Professional code structure

## License

Free to use and modify for personal and commercial projects.

## Author

Created by Affan55567
