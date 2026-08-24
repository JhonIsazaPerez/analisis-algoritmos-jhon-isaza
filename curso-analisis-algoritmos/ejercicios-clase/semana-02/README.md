# Semana 02

## Entorno virtual

Comandos usados para crear y activar el entorno virtual (desde la raíz del repositorio):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Reproducir el entorno

Para que otra persona reproduzca el mismo entorno:

1. Clonar el repositorio y ubicarse en la raíz.
2. Crear el entorno virtual: `python -m venv .venv`.
3. Activarlo: `.venv\Scripts\Activate.ps1` (Windows/PowerShell) o `source .venv/bin/activate` (Linux/macOS).
4. Instalar las dependencias exactas: `pip install -r requirements.txt`.
