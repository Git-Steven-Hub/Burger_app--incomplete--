# ----- Importo las librerías necesarias ----- #
import os, ctypes
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from Burger.animations.window_close import WindowCloseAnimator
from Burger.animations.main_animation import WindowAnimator
from Burger.views import InicioView, AdminView, MenuView, PedidosView
from Burger.resources.styles.buttons_styles import estilos_boton

# ----- Creo la clase que se encarga de manejar todas las vistas ----- #
class Burger(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ----- Creo dos variables para evitar bugs con las animaciones al abrir la app por primera vez y al cerrarla ----- #
        self._first_show = True
        self._closing = False
        
        # ----- Seteo el tamaño de la app para que no sea modificable al uso ----- #
        self.setFixedSize(550, 500)      
        
        # ----- Le doy titulo a la app ----- #
        self.setWindowTitle("Burguesía")
        
        # ----- Agrego un icono a la app ----- #
        icono_app = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/icons/icono.png"))
        self.setWindowIcon(QIcon(icono_app))
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)       
        
        # ----- Index 0: InicioView ----- #
        self.inicio = InicioView()
        self.stack.addWidget(self.inicio)
        
        # ----- Index 1: AdminView ----- #
        self.admin = AdminView()
        self.stack.addWidget(self.admin)
        
        # ----- Index 2: MenuView ----- #
        self.menu = MenuView()
        self.stack.addWidget(self.menu)

        # ----- Index 3: PedidosView ----- #
        self.pedidos = PedidosView()
        self.stack.addWidget(self.pedidos)
        
        # ----- Icono en la barra de tareas ----- #
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("burguer.app.2025")
        
        # ----- Mostrar primer index ----- #
        self.stack.setCurrentIndex(0)

        # ----- Aplicar estilos globales ----- #
        self.setStyleSheet(estilos_boton)
        
        self.animator = WindowAnimator(self)
    
    # ----- Creo el evento para mostrar la ventana con animación ----- #
    def showEvent(self, event):
        super().showEvent(event)
        if self._first_show:
            self._first_show = False
            self.setWindowOpacity(0.0)
            QTimer.singleShot(0, self.animator.start)
        
    # ----- Creo el título y el subtitulo ----- #
    def closeEvent(self, event):
        if getattr(self, "_closing", False):
            event.accept()
            return

        if hasattr(self, "on_close") and not self.on_close():
            event.ignore()
            return

        event.ignore()
        self.start_close_animation()
    
    def start_close_animation(self):
        self._closing = True
        animator = WindowCloseAnimator(self)
        animator.animate_close()