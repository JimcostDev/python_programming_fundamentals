# ¿Qué es un entorno virtual?

Tiene una máquina de desarrollo. En esa máquina, es posible que tenga una versión de Python instalada o una versión de una biblioteca que quiera usar. **¿Qué ocurre cuando mueve el programa a una máquina que tiene instalada una versión diferente de Python o versiones diferentes de las bibliotecas de las que depende?**

Una cosa que no quiere hacer es asumir que el programa funcionará y que solo puede instalar la última versión de las bibliotecas de las que depende. Si lo hace, podría acabar destruyendo la capacidad de los demás programas para funcionar en la máquina de destino. La solución es encontrar una manera de que la aplicación funcione de forma aislada.

**La solución de Python para estos problemas es un entorno virtual**. Un entorno virtual es una copia independiente de todo lo necesario para ejecutar el programa. Esto incluye el intérprete de Python y todas las bibliotecas que necesita el programa. Mediante un entorno virtual, puede asegurarse de que el programa tendrá acceso a las versiones y los recursos correctos para ejecutarse correctamente.

El flujo de trabajo básico tiene este aspecto:

* Cree un entorno virtual que no afecte al resto de la máquina.
* Entre en el entorno virtual, donde debe especificar la versión de Python y las bibliotecas que necesita.
* Desarrolle el programa.

## Para crear el entorno virtual ejecutar el comando:
```bash
 python -m venv env
```

## Active el entorno virtual:

```bash
 # Windows
source env/Scripts/activate

# Linux, WSL or macOS
source env/bin/activate
```

## Desactivar entorno virtual:

```bash
 deactivate
```
link: https://docs.microsoft.com/es-mx/learn/modules/python-create-manage-projects/2-set-up-project