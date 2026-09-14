# File Organizer

An interactive terminal-based file organizer written in Python. It automatically sorts files in a folder (e.g., Downloads) into subfolders by type, with an age filter and a simulation mode.

Available in English and Spanish.

## Features

- Organizes files by category: Images, Documents, Videos, Audio, Archives, Code, Other
- Minimum age filter (in days)
- Simulation mode: preview what the program would do before actually moving/copying anything
- Choose between moving or copying files
- Interactive menu with styled output (using [rich](https://github.com/Textualize/rich))
- Configuration saved automatically (folder, language, preferences)
- English and Spanish interface

## Requirements

- Python 3.9 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/organizador-archivos.git
   cd organizador-archivos
   ```

2. Create and activate a virtual environment:

   **Linux / macOS:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **Windows (CMD):**

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

   > **Note (Windows/PowerShell):** if activation fails with an "execution policy" error, open PowerShell as administrator and run once: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install the project as a command (recommended with [pipx](https://pypa.github.io/pipx/)):

   ```bash
   pipx install -e .
   ```

   Or, inside the virtual environment:

   ```bash
   pip install -e .
   ```

## Usage

Simply run:

```bash
organizar
```

The first time, the program will ask you for:
- The interface language (English / Español)
- The path to the folder you want to organize

This data is saved automatically for next time, and can be changed later from the Settings menu.

### Main menu

1. **Start organizing** — runs the organizer with the current configuration (asks for confirmation before running)
2. **Settings** — lets you adjust:
   - Simulate (on/off)
   - Minimum age in days
   - Mode (move / copy)
   - Folder to organize
3. **Exit**

## Project structure

```
organizador-archivos/
├── organizer/
│   ├── __init__.py
│   ├── main.py           # Main logic and menu
│   ├── load_path.py       # Loads and saves persistent config (.env)
│   └── translations.py    # English and Spanish text
├── pyproject.toml
├── requirements.txt
├── .env.example
└── .gitignore
```

## Development

This project uses a `.env` file (not included in the repository) to store local configuration, such as the folder path and chosen language. It's generated automatically the first time you run `organizar`, or you can copy the template manually:

```bash
cp .env.example .env
```

## License

MIT
