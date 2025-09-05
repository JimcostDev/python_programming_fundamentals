import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame

class VisorCubo(OpenGLFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animar = True
        self.inicializado = False
        self.rotacion_x = 30
        self.rotacion_y = 30
        self.rotacion_z = 0
        self.velocidad_rotacion = 0.5
        self.color_cubo = [0.6, 0.6, 0.8]  # Color azul grisáceo
        self.color_fondo = [0.0, 0.0, 0.2]  # Azul oscuro
        self.escala = 1.5  # Aumentada la escala
        
    def initgl(self):
        """Método de inicialización del contexto OpenGL"""
        glClearColor(*self.color_fondo, 1.0)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.inicializado = True

    def dibujar_cubo(self):
        """Método para dibujar el cubo con caras transparentes y líneas"""
        vertices = [
            # Frontal
            [-0.5, -0.5,  0.5], [ 0.5, -0.5,  0.5], [ 0.5,  0.5,  0.5], [-0.5,  0.5,  0.5],
            # Trasera
            [-0.5, -0.5, -0.5], [ 0.5, -0.5, -0.5], [ 0.5,  0.5, -0.5], [-0.5,  0.5, -0.5]
        ]
        
        caras = [
            [0, 1, 2, 3],  # Frontal
            [1, 5, 6, 2],  # Derecha
            [5, 4, 7, 6],  # Trasera
            [4, 0, 3, 7],  # Izquierda
            [3, 2, 6, 7],  # Superior
            [0, 1, 5, 4]   # Inferior
        ]

        # Dibujar caras con transparencia
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_QUADS)
        glColor4f(*self.color_cubo, 0.4)  # Color semi-transparente
        for cara in caras:
            for vertice in cara:
                glVertex3fv(vertices[vertice])
        glEnd()

        # Dibujar líneas
        glLineWidth(1.0)  # Ancho de línea
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glBegin(GL_QUADS)
        glColor4f(1.0, 1.0, 1.0, 0.8)  # Color blanco semi-transparente para las líneas
        for cara in caras:
            for vertice in cara:
                glVertex3fv(vertices[vertice])
        glEnd()

    def redraw(self):
        """Método principal de renderizado"""
        if not self.inicializado:
            self.initgl()
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        try:
            ancho_vista = self.winfo_width() // 2
            alto_vista = self.winfo_height() // 2
        except tk.TclError:
            return
            
        if self.animar:
            self.rotacion_y = (self.rotacion_y + self.velocidad_rotacion) % 360
            self.after(16, self.redraw)

        def configurar_vista(viewport, proyeccion_func):
            glViewport(*viewport)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            proyeccion_func()
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glScalef(self.escala, self.escala, self.escala)
            glRotatef(self.rotacion_x, 1, 0, 0)
            glRotatef(self.rotacion_y, 0, 1, 0)
            glRotatef(self.rotacion_z, 0, 0, 1)
            self.dibujar_cubo()

        # 1. Proyección Ortogonal
        configurar_vista(
            (0, alto_vista, ancho_vista, alto_vista),
            lambda: glOrtho(-2, 2, -2, 2, -10, 10)
        )
        
        # 2. Proyección Gabinete
        def proyeccion_gabinete():
            glOrtho(-2, 2, -2, 2, -10, 10)
            gabinete = [
                1.0, 0.0, -0.3536, 0.0,
                0.0, 1.0, -0.3536, 0.0,
                0.0, 0.0, 1.0, 0.0,
                0.0, 0.0, 0.0, 1.0
            ]
            glMultMatrixf(gabinete)
        
        configurar_vista(
            (ancho_vista, alto_vista, ancho_vista, alto_vista),
            proyeccion_gabinete
        )
        
        # 3. Proyección Perspectiva Simétrica
        def proyeccion_perspectiva():
            gluPerspective(60, ancho_vista/alto_vista, 0.1, 50.0)
            glTranslatef(0, 0, -3)
        
        configurar_vista(
            (0, 0, ancho_vista, alto_vista),
            proyeccion_perspectiva
        )
        
        # 4. Proyección Perspectiva Oblicua
        def proyeccion_oblicua():
            glFrustum(-1, 1, -1, 1, 2, 10)
            glTranslatef(0, 0, -5)
            oblicua = [
                1.0, 0.0, 0.3, 0.0,
                0.0, 1.0, 0.3, 0.0,
                0.0, 0.0, 1.0, 0.0,
                0.0, 0.0, 0.0, 1.0
            ]
            glMultMatrixf(oblicua)
        
        configurar_vista(
            (ancho_vista, 0, ancho_vista, alto_vista),
            proyeccion_oblicua
        )

def main():
    raiz = tk.Tk()
    raiz.title("Visualizador de Cubo 3D")
    
    # Crear el visor
    visor = VisorCubo(raiz, width=800, height=600)
    visor.pack(fill=tk.BOTH, expand=True)
    
    # Iniciar la animación
    visor.after(100, visor.redraw)
    
    raiz.mainloop()

if __name__ == "__main__":
    main()