# Documentación: Visualizador de Cubo 3D con OpenGL en Tkinter

Este código crea una aplicación de visualización de un cubo 3D que se renderiza en cuatro tipos de proyecciones (ortogonal, gabinete, perspectiva simétrica y perspectiva oblicua) en una ventana de Tkinter usando `pyopengltk` y `OpenGL`. La rotación del cubo se anima para mostrar las proyecciones en tiempo real.

---

## Clases y Funciones

### 1. `VisorCubo` (Clase principal de visualización)

Esta clase hereda de `OpenGLFrame` y es responsable de inicializar OpenGL, definir y dibujar el cubo, y configurar las vistas en diferentes proyecciones. Se define como el contenedor principal para el cubo y permite la animación.

#### Constructor: `__init__(self, *args, **kwargs)`

**Propósito:** Inicializa las variables clave de configuración de la visualización.

- **Variables clave:**
  - `self.animar`: Activa/desactiva la animación.
  - `self.inicializado`: Marca si OpenGL se ha inicializado (`False` al principio).
  - `self.rotacion_x`, `self.rotacion_y`, `self.rotacion_z`: Definen los ángulos de rotación en cada eje (X, Y, Z).
  - `self.velocidad_rotacion`: Define la velocidad de rotación en el eje Y.
  - `self.color_cubo`: Color del cubo en formato RGB (se define un color azul grisáceo).
  - `self.color_fondo`: Color de fondo de la ventana OpenGL (azul oscuro).
  - `self.escala`: Escala del cubo para aumentar su tamaño visual.

---

### 2. `initgl(self)`

**Propósito:** Configura los parámetros de inicialización de OpenGL.

- **Acciones clave:**
  - `glClearColor`: Define el color de fondo de la ventana usando `self.color_fondo`.
  - `glEnable(GL_DEPTH_TEST)`: Habilita el test de profundidad para ocultar superficies traseras.
  - `glShadeModel(GL_SMOOTH)`: Activa el modelo de sombreado suave.
  - `glEnable(GL_BLEND)` y `glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)`: Configura la transparencia para las superficies y bordes del cubo.
  - `self.inicializado`: Establece la bandera a `True` una vez inicializado el contexto OpenGL.

---

### 3. `dibujar_cubo(self)`

**Propósito:** Dibuja el cubo con sus caras y líneas de borde. Cada cara del cubo es semitransparente y se representan líneas de borde visibles.

- **Variables clave:**
  - `vertices`: Lista de coordenadas de los vértices del cubo.
  - `caras`: Define los grupos de vértices que forman cada cara del cubo.

- **Acciones clave:**
  - Dibuja cada cara como un `GL_QUADS` con transparencia (`glColor4f(*self.color_cubo, 0.4)`).
  - Usa `glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)` para rellenar las caras y luego cambia a `GL_LINE` para dibujar los bordes con un ancho de línea (`glLineWidth(1.0)`).

---

### 4. `redraw(self)`

**Propósito:** Función principal de renderizado. Define el ciclo de animación del cubo y configura cada una de las vistas.

- **Variables clave y acciones:**
  - `ancho_vista` y `alto_vista`: Determinan la mitad de la ventana, para dividirla en cuatro partes.
  - `self.rotacion_y`: Incrementa el ángulo de rotación en el eje Y para animar el cubo.
  - `configurar_vista(viewport, proyeccion_func)`: Función auxiliar interna que establece cada tipo de vista según los parámetros y proyección definidos.

- **Sub-funciones de proyección:**
  1. **Proyección Ortogonal:** Muestra el cubo sin perspectiva, útil para visualizar dimensiones sin deformación.
     - `glOrtho(-2, 2, -2, 2, -10, 10)`: Define una proyección ortogonal.
  
  2. **Proyección Gabinete:** Proyección axonométrica que incluye una ligera perspectiva de 45°.
     - `glMultMatrixf(gabinete)`: Multiplica la matriz de proyección ortogonal para simular una inclinación.
  
  3. **Proyección Perspectiva Simétrica:** Proyección con perspectiva, común para simular profundidad.
     - `gluPerspective(60, ancho_vista/alto_vista, 0.1, 50.0)`: Establece una perspectiva simétrica.
     - `glTranslatef(0, 0, -3)`: Traslada la vista para centrarse en el cubo.
  
  4. **Proyección Perspectiva Oblicua:** Proyección con ángulo para un efecto tridimensional pronunciado.
     - `glFrustum(-1, 1, -1, 1, 2, 10)`: Configura una proyección en forma de frustum.
     - `glMultMatrixf(oblicua)`: Inclina la matriz de proyección para un efecto oblicuo.

---

### 5. `main()`

**Propósito:** Inicializa la ventana de Tkinter y ejecuta el ciclo principal.

- **Acciones clave:**
  - `raiz = tk.Tk()`: Crea la ventana principal de la aplicación.
  - `visor = VisorCubo(raiz, width=800, height=600)`: Crea una instancia de `VisorCubo` y define el tamaño de la ventana.
  - `visor.after(100, visor.redraw)`: Programa el inicio de la animación del cubo.
  - `raiz.mainloop()`: Inicia el ciclo de eventos de Tkinter.

---

### Notas de Modificación

Si deseas ajustar o personalizar el visualizador, aquí hay algunas sugerencias:

1. **Color del cubo y fondo:** Modifica `self.color_cubo` y `self.color_fondo` en el constructor `__init__`.
2. **Velocidad de rotación:** Cambia `self.velocidad_rotacion` para aumentar o disminuir la velocidad de animación del cubo.
3. **Tamaño del cubo:** Modifica `self.escala` para cambiar el tamaño del cubo sin afectar la escala general de las proyecciones.
4. **Tipos de Proyección:** Si necesitas otra perspectiva o un ángulo diferente, ajusta las matrices en cada función de proyección dentro de `configurar_vista`.

