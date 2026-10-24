# Background File Organizer

A lightweight, portable background utility for Windows designed to automatically organize files in a specified directory by their file extensions. Built with Python and executable packaging support, it runs silently in the background while keeping your folders neat and structured.

## Features

* **Graphical Directory Picker**: Uses native Windows file dialogs (`tkinter`) to select any target directory dynamically at runtime.

* **Silent Background Execution**: Runs continuously without keeping a terminal window open, utilizing a standalone detached launcher.

* **Smart Download Safety Filter**: Automatically ignores incomplete or temporary download files (`.crdownload`, `.part`, `.tmp`) to prevent moving files currently in use.

* **Automated Reporting**: Maintains a clean log (`report.txt`) recording every file organization action. Automatically refreshes log contents upon launch.

* **Graceful Termination Mechanism**: Stops safely when a `stop.txt` file is placed in the project folder, eliminating the need to terminate processes via Task Manager.

* **Standalone Portability**: Can be compiled into a single `.exe` executable with PyInstaller, requiring no pre-installed Python environment on the host system.

## Project Structure

```
.
├── app.py           # Core logic (file grouping, moving, reporting)
├── launcher.py      # Background process launcher script
├── .gitignore       # Git exclusion configuration for build/log artifacts
└── README.md        # Documentation

```

## Installation & Setup

### Requirements

* Python 3.x (if running directly from source)

* Windows OS (supports native process detachment flags)

### Setting Up

1. Clone the repository:

   ```
   git clone https://github.com/kindratkomisha-gif/download-organizer
   cd download-organizer
   
   ```

2. (Optional) Install `PyInstaller` if you intend to compile the project into an executable:

   ```
   pip install pyinstaller
   
   ```

## Usage

### Running from Python Source

1. **Start the application in the background:**
   Run `launcher.py`:

   ```
   python launcher.py
   
   ```

   *A folder selection dialog will open. Choose the folder you want to continuously organize (e.g., Downloads).*

2. **Check Execution Logs:**
   Open `report.txt` in the root folder to view sorted file activity logs.

3. **Stop the Application Gracefully:**
   Create an empty file named `stop.txt` in the root directory. The application will detect the trigger on its next cycle, record the stop event in `report.txt`, clean up the trigger file, and exit safely.

## Compiling to Independent Executable (.exe)

To deploy the application on systems without Python installed, build a single executable using PyInstaller:

```
python -m PyInstaller --noconsole --onefile app.py

```

The resulting standalone executable will be generated inside the `dist/` directory as `app.exe`.

## License

This project is open-source and available under the [MIT License](LICENSE).