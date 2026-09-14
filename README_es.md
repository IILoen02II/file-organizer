# Organizador de Archivos

Un organizador de archivos interactivo por terminal, escrito en Python. Clasifica automáticamente los archivos de una carpeta (por ejemplo, Descargas) en subcarpetas según su tipo, con filtro por antigüedad y modo simulación.

Disponible en español e inglés.

## Características

- Organiza archivos por categoría: Imágenes, Documentos, Videos, Audio, Comprimidos, Código, Otros
- Filtro por antigüedad mínima (en días)
- Modo simulación: revisa qué haría el programa antes de mover/copiar nada de verdad
- Elegir entre mover o copiar archivos
- Menú interactivo con diseño (usando [rich](https://github.com/Textualize/rich))
- Configuración guardada automáticamente (carpeta, idioma, preferencias)
- Interfaz en español e inglés

## Requisitos

- Python 3.9 o superior

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/IILoen02II/file-organizer.git
   cd file-organizer
   ```

2. Crea y activa un entorno virtual:

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

   > **Nota (Windows/PowerShell):** si al activar el entorno virtual aparece un error relacionado con la "política de ejecución" (`execution policy`), abre PowerShell como administrador y ejecuta una vez: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Instala el proyecto como comando (recomendado con [pipx](https://pypa.github.io/pipx/)):

   ```bash
   pipx install -e .
   ```

   O, dentro del entorno virtual:

   ```bash
   pip install -e .
   ```

## Uso

Simplemente ejecuta:

```bash
organizar
```

La primera vez, el programa te pedirá:
- El idioma de la interfaz (Español / English)
- La ruta de la carpeta que quieres organizar

Estos datos quedan guardados automáticamente para la próxima vez, y se pueden cambiar luego desde el menú de Configuración.

### Menú principal

1. **Iniciar organización** — corre el organizador con la configuración actual (pide confirmación antes de ejecutar)
2. **Configuración** — permite ajustar:
   - Simular (activado/desactivado)
   - Días mínimos de antigüedad
   - Modo (mover / copiar)
   - Carpeta a organizar
3. **Salir**

## Estructura del proyecto

```
organizador-archivos/
├── organizer/
│   ├── __init__.py
│   ├── main.py           # Lógica principal y menú
│   ├── load_path.py       # Carga y guarda configuración persistente (.env)
│   └── translations.py    # Textos en español e inglés
├── pyproject.toml
├── requirements.txt
├── .env.example
└── .gitignore
```

## Desarrollo

Este proyecto usa un archivo `.env` (no incluido en el repositorio) para guardar configuración local, como la ruta de la carpeta y el idioma elegido. Se genera automáticamente la primera vez que ejecutas `organizar`, o puedes copiar la plantilla manualmente:

```bash
cp .env.example .env
```

## Licencia

MIT
