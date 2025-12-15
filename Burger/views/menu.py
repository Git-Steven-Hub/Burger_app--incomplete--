# ----- Importo las librerías necesarias ----- #
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QLineEdit, QGridLayout, QHBoxLayout, QSpacerItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize, Signal
from Burger.widgets.background import BackgroundFrame
from Burger.widgets.effects import apply_shadow_label

class MenuView(QWidget):
    iniciar_pedido = Signal()
    cerrar_turno = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        # ----- Creo el widget principal ----- #
        root_layout = QVBoxLayout(self)
        
        # ----- Creo el widget principal ----- #
        self.frame_titulo = QFrame()
        self.frame_opciones= QFrame()
        
        self.frame_titulo = BackgroundFrame()
        self.frame_titulo.setObjectName("frame_titulo")
        self.frame_opciones.setObjectName("frame_decorado")
        
        # ----- Creo el widget principal ----- #
        root_layout.addWidget(self.frame_titulo, stretch=1)
        root_layout.addWidget(self.frame_opciones, stretch=3)
        
        # ----- Creo el título y le asigno un nombre para el estilo ----- #
        self.titulo_label = QLabel("¡MENU ENCARGADOS!\nLA BURGUESIA")
        self.titulo_label.setObjectName("titulo")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        
        # ----- Creo el subtitulo y le asigno un nombre para el estilo ----- #
        self.subtitulo_label = QLabel("¡nombre!")
        self.subtitulo_label.setObjectName("subtitulo")
        self.subtitulo_label.setAlignment(Qt.AlignCenter)
        self.subtitulo_label.setContentsMargins(0, 0, 0, 5)
        
        # ----- Añado todo al layout ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(self.titulo_label)
        titulo_layout.addWidget(self.subtitulo_label)
        self.frame_titulo.setLayout(titulo_layout)
        
        # ----- Llamo a los botones ----- #
        self._setup_buttons_layout()
    
    def showEvent(self, event):
        super().showEvent(event)
        if not hasattr(self, "shadows") or self.shadows is None:
            self.shadows = apply_shadow_label([self.titulo_label, self.subtitulo_label])
        
    def _setup_buttons_layout(self):
        # ----- Seteo el layout del frame del inicio ----- #
        self.frame_botones = QVBoxLayout(self.frame_opciones)

        # ------ Creo el apartado que se encarga de encontrar todos los iconos ------ #
        icons_dir = os.path.join(os.path.dirname(__file__), "../resources/icons")

        # ----- Creo el botón para iniciar el pedido, colocando su icono y estilo ----- #
        self.btn_iniciar_pedido = QPushButton("Iniciar pedido")
        self.btn_iniciar_pedido.setIcon(QIcon(os.path.join(icons_dir, "combo.png")))
        self.btn_iniciar_pedido.setIconSize(QSize(25, 25))    
        self.btn_iniciar_pedido.setObjectName("id1")
        self.btn_iniciar_pedido.setFixedWidth(380)
        
        # ----- Creo el botón para ver el resumen del día, colocando su icono y estilo----- #
        self.btn_estado_turno = QPushButton("Ver resumen del día")
        self.btn_estado_turno.setIcon(QIcon(os.path.join(icons_dir, "resumen.png")))
        self.btn_estado_turno.setIconSize(QSize(25, 25))        
        self.btn_estado_turno.setObjectName("id4")
        self.btn_estado_turno.setFixedWidth(380)
        
        # ----- Creo el botón para ver el historial completo, colocando su icono y estilo ----- #
        self.btn_historial_turno = QPushButton("Ver tu historial de turnos")
        self.btn_historial_turno.setIcon(QIcon(os.path.join(icons_dir, "turnos.png")))
        self.btn_historial_turno.setIconSize(QSize(25, 25))
        self.btn_historial_turno.setFixedWidth(380)
        
        # ----- Creo el botón para cambiar la propia contraseña, colocando su icono y estilo ----- #
        self.btn_cambiar_contrasena = QPushButton("Cambiar contraseña")
        self.btn_cambiar_contrasena.setIcon(QIcon(os.path.join(icons_dir, "password.png")))
        self.btn_cambiar_contrasena.setIconSize(QSize(25, 25))
        self.btn_cambiar_contrasena.setObjectName("id5")
        self.btn_cambiar_contrasena.setFixedWidth(380)
        
        # ----- Creo el botón para cerrar el turno, colocando su icono y estilo ----- #
        self.btn_terminar_turno = QPushButton("Cerrar turno")
        self.btn_terminar_turno.setIcon(QIcon(os.path.join(icons_dir, "salir.png")))
        self.btn_terminar_turno.setIconSize(QSize(25, 25))
        self.btn_terminar_turno.setObjectName("id3")
        self.btn_terminar_turno.setFixedWidth(380)

        # ----- Creo el layout para las columnas ----- #
        columnas = QGridLayout()
        
        # ----- Agrego los botones en su posición correspondiente ----- #
        columnas.addWidget(self.btn_iniciar_pedido, 0, 0, alignment=Qt.AlignCenter)
        # ----- Separación ----- #
        columnas.addWidget(self.btn_estado_turno, 1, 0, alignment=Qt.AlignCenter)
        # ----- Separación ----- #
        columnas.addWidget(self.btn_historial_turno, 2, 0, alignment=Qt.AlignCenter)
        # ----- Separación ----- #
        columnas.addWidget(self.btn_cambiar_contrasena, 3, 0, alignment=Qt.AlignCenter)
        # ----- Separación ----- #
        columnas.addWidget(self.btn_terminar_turno, 4, 0, alignment=Qt.AlignCenter)
        
        # ----- Agrego todo al layout principal ---- #
        self.frame_botones.addLayout(columnas)

        # conectar la señal pública a la acción del botón
        self.btn_terminar_turno.clicked.connect(self.cerrar_turno.emit)
        self.btn_iniciar_pedido.clicked.connect(self.iniciar_pedido.emit)