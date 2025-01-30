# Guía para Instalar Python

## Instalar Python en Windows

1. **Descargar el instalador**  
   - Ve a [la página oficial de Python](https://www.python.org/downloads/).
   - Descarga la última versión de Python para Windows (archivo `.exe`).

2. **Ejecutar el instalador**  
   - Abre el archivo `.exe` descargado.
   - Marca la casilla **"Add Python to PATH"** (muy importante).
   - Haz clic en **"Install Now"** y espera a que termine.

3. **Verificar la instalación**  
   - Abre la terminal (tecla **Win + R**, escribe `cmd` y presiona Enter).
   - Escribe `python --version` y presiona Enter.
   - Si ves algo como `Python 3.x.x`, la instalación fue exitosa.

> ## Nota: 
> #### Linux
> En la mayoría de las distribuciones de Linux modernas, Python suele estar preinstalado:
> - **Ubuntu/Debian**: Python 3.x está preinstalado.
> - **Fedora**: Python 3.x está preinstalado.
> - **CentOS/RHEL**: Python 3.x disponible, pero en algunas versiones, Python 2 puede ser la opción por defecto.
>
> #### macOS
> Python 2.x estaba preinstalado en versiones anteriores a macOS 12 (Monterey). En macOS 12 y versiones posteriores, Python 3.x es el predeterminado, aunque puede que necesites instalarlo manualmente en versiones más antiguas.
---

## Instalar Python en macOS

1. **Usar el instalador oficial**  
   - Ve a [la página de descargas de Python](https://www.python.org/downloads/).
   - Descarga el archivo `.pkg` para macOS y ábrelo.
   - Sigue los pasos del instalador.

2. **Usar Homebrew (opcional, recomendado)**  
   - Abre la terminal y ejecuta:  
     ```sh
     brew install python
     ```

3. **Verificar la instalación**  
   - En la terminal, escribe:  
     ```sh
     python3 --version
     ```
   - Si aparece `Python 3.x.x`, todo está bien.

---

## Instalar Python en Linux (Ubuntu/Debian)

1. **Actualizar el sistema**  
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```

2. **Instalar Python**  
   ```sh
   sudo apt install python3 python3-pip -y
   ```

3. **Verificar la instalación**  
   ```sh
   python3 --version
   ```
