from dotenv import load_dotenv, set_key
from pathlib import Path
import os

ENV_FILE = ".env"

load_dotenv()

def get_downloads_path():
    path = os.getenv("DOWNLOADS_PATH")

    if path is None or not Path(path).is_dir():
        return None 

    return path

downloads_path = get_downloads_path()

def save_downloads_path(new_path):
    set_key(ENV_FILE, "DOWNLOADS_PATH", new_path)
    os.environ["DOWNLOADS_PATH"] = new_path  

def get_language():
    lang = os.getenv("APP_LANGUAGE")
    if lang not in ("es", "en"):
        return None
    return lang

language = get_language()

def save_language(new_lang):
    set_key(ENV_FILE, "APP_LANGUAGE", new_lang)
    os.environ["APP_LANGUAGE"] = new_lang