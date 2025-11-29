# ----- Importo las librerías necesarias ----- #
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MenuView(QWidget):
    iniciar_pedido = Signal()
    cerrar_turno = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        # ----- Creo el widget principal ----- #
        frame = QWidget()
        root_layout = QVBoxLayout(frame)
        
        # ----- Creo el widget principal ----- #
        self.frame_titulo_menu = QFrame()
        self.frame_opciones_menu = QFrame()
        
        # ----- Creo el widget principal ----- #
        root_layout.addWidget(self.frame_titulo_menu, stretch=1)
        root_layout.addWidget(self.frame_opciones_menu, stretch=3)
        
        # ----- Creo el título y le asigno un nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        
        # ----- Creo el subtitulo y le asigno un nombre para el estilo ----- #
        subtitulo = QLabel("¡Menu encargados!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        # ----- Añado todo al layout ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo_menu.setLayout(titulo_layout)
        
        # ----- Llamo a los botones ----- #
        self._setup_buttons_layout()
        
    def _setup_buttons_layout(self):
        # ----- Seteo el layout del frame del inicio ----- #
        self.frame_botones_menu = QVBoxLayout(self.frame_opciones_menu)
        
        self.iniciar_pedido = QPushButton("Iniciar pedido")
        pedido_icon = os.path.dirname(__file__)
        self.iniciar_pedido.setIcon(QIcon(os.path.join(pedido_icon, "icons/combo.png")))
        self.iniciar_pedido.setIconSize(QSize(25, 25))    
        self.iniciar_pedido.setObjectName("id1")
        self.iniciar_pedido.setFixedWidth(380)
        
        self.estado_turno = QPushButton("Ver resumen del día")
        resumen_icon = os.path.dirname(__file__)
        self.estado_turno.setIcon(QIcon(os.path.join(resumen_icon, "icons/resumen.png")))
        self.estado_turno.setIconSize(QSize(25, 25))        
        self.estado_turno.setObjectName("id4")
        self.estado_turno.setFixedWidth(380)
        
        self.historial_turno = QPushButton("Ver tu historial de turnos")
        turnos_icon = os.path.dirname(__file__)
        self.historial_turno.setIcon(QIcon(os.path.join(turnos_icon, "icons/turnos.png")))
        self.historial_turno.setIconSize(QSize(25, 25))
        self.historial_turno.setFixedWidth(380)
        
        self.cambiar_contraseña = QPushButton("Cambiar contraseña")
        cambiar_contraseña_icon = os.path.dirname(__file__)
        self.cambiar_contraseña.setIcon(QIcon(os.path.join(cambiar_contraseña_icon, "icons/password.png")))
        self.cambiar_contraseña.setIconSize(QSize(25, 25))
        self.cambiar_contraseña.setObjectName("id5")
        self.cambiar_contraseña.setFixedWidth(380)
        
        self.terminar_turno = QPushButton("Cerrar turno")
        terminar_turno_icon = os.path.dirname(__file__)
        self.terminar_turno.setIcon(QIcon(os.path.join(terminar_turno_icon, "icons/salir.png")))
        self.terminar_turno.setIconSize(QSize(25, 25))
        self.terminar_turno.setObjectName("id3")
        self.terminar_turno.setFixedWidth(380)

        columnas = QGridLayout()
        
        columnas.addWidget(self.iniciar_pedido, 0, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.estado_turno, 1, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.historial_turno, 2, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.cambiar_contraseña, 3, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.terminar_turno, 4, 0, alignment=Qt.AlignCenter)
        
        self.frame_botones_menu.addLayout(columnas)