from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
import time
import shutil

from organizer.translations import TRANSLATIONS
from organizer.load_path import downloads_path, save_downloads_path, language, save_language

console = Console()

def t(key):
    return TRANSLATIONS[language][key]

def organize_folders(folder_path, simulate=True, min_days=30, mode="move"):
    folder = Path(folder_path)

    categories = {
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Comprimidos": [".zip", ".rar"],
        "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
    }

    for file in folder.iterdir():
        if file.is_file():
            modification_time = datetime.fromtimestamp(file.stat().st_mtime)
            age_in_days = (datetime.now() - modification_time).days

            if age_in_days < min_days:
                continue

            extension = file.suffix.lower()
            category_found = "Otros"

            for category, extensions in categories.items():
                if extension in extensions:
                    category_found = category
                    break

            destination_folder = folder / category_found

            if simulate:
                console.print(f"[yellow][SIMULATION][/yellow] Would {mode}: {file.name} ({age_in_days} days) -> {category_found}")
            else:
                destination_folder.mkdir(exist_ok=True)

                if mode == "copy":
                    shutil.copy(file, destination_folder)
                else:
                    shutil.move(file, destination_folder)

                console.print(f"[green]{mode.capitalize()}d[/green] {file.name} to {destination_folder}")

def ask_for_downloads_path():
    while True:
        path = Prompt.ask(t('ask_folder'))
        if Path(path).is_dir():
            save_downloads_path(path)
            console.print(f"[green]{t('folder_saved')}:[/green] {path}")
            return path
        else:
            console.print(f"[bold red]{t('folder_invalid')}[/bold red]")

def show_main_menu():
    console.clear()
    console.print(Panel(f"[bold cyan]{t('menu_title')}[/bold cyan]", expand=False))
    console.print(f"[green]1.[/green] {t('menu_option_start')}")
    console.print(f"[green]2.[/green] {t('menu_option_config')}")
    console.print(f"[green]3.[/green] {t('menu_option_exit')}")
    return Prompt.ask(t('choose_option'), choices=["1", "2", "3"])

def ask_for_language():
    console.print("Choose language / Elige idioma:")
    console.print("1. Español")
    console.print("2. English")
    choice = Prompt.ask("...", choices=["1", "2"])
    lang = "es" if choice == "1" else "en"
    save_language(lang)
    return lang

def show_config_menu(config):
    global downloads_path
    temp_config = config.copy()

    while True:
        console.clear()
        console.print(Panel(f"[bold cyan]{t('config_title')}[/bold cyan]", expand=False))
        console.print(f"[green]1.[/green] {t('config_simulate')}: [yellow]{temp_config['simulate']}[/yellow]")
        console.print(f"[green]2.[/green] {t('config_min_days')}: [yellow]{temp_config['min_days']}[/yellow]")
        console.print(f"[green]3.[/green] {t('config_mode')}: [yellow]{temp_config['mode']}[/yellow]")
        console.print(f"[green]4.[/green] {t('config_folder')}: [yellow]{downloads_path}[/yellow]")
        console.print(f"[green]5.[/green] {t('config_save')}")
        console.print(f"[green]6.[/green] {t('config_cancel')}")

        choice = Prompt.ask(t('choose_option'), choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            temp_config["simulate"] = not temp_config["simulate"]
        elif choice == "2":
            temp_config["min_days"] = IntPrompt.ask(t('new_min_days'))
        elif choice == "3":
            temp_config["mode"] = Prompt.ask(t('config_mode'), choices=["move", "copy"])
        elif choice == "4":
            downloads_path = ask_for_downloads_path()
        elif choice == "5":
            console.print(f"[bold green]{t('config_saved')}[/bold green]")
            time.sleep(2)
            return temp_config
        elif choice == "6":
            console.print(f"[bold red]{t('config_cancelled')}[/bold red]")
            time.sleep(2)
            return config

def confirm_and_run(config, folder_path):
    console.print(Panel(f"[bold cyan]{t('confirm_title')}[/bold cyan]", expand=False))
    console.print(f"{t('config_folder')}: [yellow]{folder_path}[/yellow]")
    console.print(f"{t('config_simulate')}: [yellow]{config['simulate']}[/yellow]")
    console.print(f"{t('config_min_days')}: [yellow]{config['min_days']}[/yellow]")
    console.print(f"{t('config_mode')}: [yellow]{config['mode']}[/yellow]")

    if Confirm.ask(t('confirm_question')):
        organize_folders(
            folder_path,
            simulate=config["simulate"],
            min_days=config["min_days"],
            mode=config["mode"]
        )
    else:
        console.print(f"[yellow]{t('operation_cancelled')}[/yellow]")


def main_menu():

    global downloads_path, language

    if language is None:
        language = ask_for_language()

    config = {"simulate": True, "min_days": 30, "mode": "move"}

    if downloads_path is None:
        console.clear()
        console.print("[bold cyan]CONFIGURACIÓN INICIAL[/bold cyan]")
        console.print("[yellow]No se encontró la ruta de Descargas.[/yellow]")
        downloads_path = ask_for_downloads_path()

    while True:
        choice = show_main_menu()

        if choice == "1":
            confirm_and_run(config, downloads_path)
        elif choice == "2":
            config = show_config_menu(config)
        elif choice == "3":
            console.print(f"[bold cyan]{t('goodbye')}[/bold cyan]")
            break


if __name__ == "__main__":
    main_menu()