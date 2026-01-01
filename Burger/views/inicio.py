# ------ Importo las librerías necesarias ------ #
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QLineEdit, QGridLayout, QHBoxLayout, QSpacerItem, QToolTip
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize, Signal, QPoint
from Burger.widgets.background import BackgroundFrame
from Burger.widgets.effects import apply_shadow_label

# ------ Creo al clase para poder ser stackeada ------ #
class InicioView(QWidget):
    ir_admin = Signal()
    iniciar_sesion = Signal(str, str)
    nuevo_usuario = Signal(str, str)
    
    # ------ Creo el init ------ #
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    # ------ Creo el UI en el mismo widget ------ #
    def _build_ui(self):
        # ------ Creo la raíz ------ #
        root_layout = QVBoxLayout(self)
    
        # ----- Creo los frames para cada opción ----- #
        self.frame_titulo = QFrame()
        self.frame_opciones = QFrame()

        # ------ Le agrego el fondo al título y seteo sus nombres para su estilo ------ #
        self.frame_titulo = BackgroundFrame()
        self.frame_titulo.setObjectName("frame_titulo")
        self.frame_opciones.setObjectName("frame_decorado")
        
        # ----- Le agrego espacio para cada frame ----- #
        root_layout.addWidget(self.frame_titulo, stretch=1)
        root_layout.addWidget(self.frame_opciones, stretch=3)
        
        # ----- Creo el título y le asigno su nombre para el estilo ----- #
        self.titulo_label = QLabel("¡BIENVENIDO NUEVAMENTE!\n LA BURGUESIA ")
        self.titulo_label.setObjectName("titulo")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        QSpacerItem(20, 40)
        
        # ----- Creo el subtitulo y le agrego su estilo ----- #
        self.subtitulo_label = QLabel("¡Las mejores burguers!")
        self.subtitulo_label.setObjectName("subtitulo")
        self.subtitulo_label.setAlignment(Qt.AlignCenter)
        self.subtitulo_label.setContentsMargins(0, 0, 0, 5)
        
        # ------ Añado el título, el subtitulo y lo seteo ------ #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(self.titulo_label)
        titulo_layout.addWidget(self.subtitulo_label)
        self.frame_titulo.setLayout(titulo_layout)
        
        # ----- Llamo a los botones para rellenar opciones_section ----- #
        self._setup_buttons_layout()
    
    # ------ Creo el evento para que se vean las sombras del título y del subtitulo ------ #
    def showEvent(self, event):
        super().showEvent(event)
        if not hasattr(self, "shadows") or self.shadows is None:
            self.shadows = apply_shadow_label([self.titulo_label, self.subtitulo_label])
        
    # ------ Creo el apartado de los botones ------ #
    def _setup_buttons_layout(self):
        # ----- Uso el layout de las opciones ----- #
        self.opciones_layout = QVBoxLayout(self.frame_opciones)
        
        # ------ Creo el apartado que se encarga de encontrar todos los iconos ------ #
        icons_dir = os.path.join(os.path.dirname(__file__), "../resources/icons")
        
        # ----- Creo el botón de inicio y le asigno nombre ----- #
        self.btn_sesion = QPushButton("Iniciar sesión")
        self.btn_sesion.setIcon(QIcon(os.path.join(icons_dir, "login.png")))
        self.btn_sesion.setIconSize(QSize(25, 25))
        self.btn_sesion.setObjectName("id1")
        self.btn_sesion.setFixedWidth(380)
        
        # ----- Creo el botón de usuario nuevo y le asigno nombre----- #
        self.btn_usuario_nuevo = QPushButton("Nuevo usuario")
        self.btn_usuario_nuevo.setIcon(QIcon(os.path.join(icons_dir, "nuevo usuario.png")))
        self.btn_usuario_nuevo.setIconSize(QSize(25, 25))
        self.btn_usuario_nuevo.setObjectName("id2")
        self.btn_usuario_nuevo.setFixedWidth(380)
        
        # ----- Creo el botón para el administrador ----- #
        self.btn_administrador = QPushButton("Administrador")
        self.btn_administrador.setIcon(QIcon(os.path.join(icons_dir, "admin.png")))
        self.btn_administrador.setIconSize(QSize(25, 25))
        self.btn_administrador.setObjectName("boton_admin")
        
        # ----- Creo el botón de salir y le asigno nombre ----- #
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.setIcon(QIcon(os.path.join(icons_dir, "cerrar app.png")))
        self.btn_salir.setIconSize(QSize(25, 25))
        self.btn_salir.setObjectName("id3")
        
        # ----- Creo los QLineEdit para el inicio de sesión ----- #
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.contrasena = QLineEdit()
        self.contrasena.setPlaceholderText("Contraseña")
        self.contrasena.setEchoMode(QLineEdit.Password)
        
        # ----- Creo los QLineEdit para el nuevo usuario ----- #
        self.line_nuevo_usuario = QLineEdit()
        self.line_nuevo_usuario.setPlaceholderText("Crear usuario")
        self.nueva_contrasena = QLineEdit()
        self.nueva_contrasena.setPlaceholderText("Crear contraseña")
        
        # ----- Creo el layout para las columnas ----- #
        columnas = QGridLayout()
        columnas.setVerticalSpacing(10)

        # ----- Creo un layout para los botones de "Modificar usuario" y "Salir" ----- #
        columnas2 = QHBoxLayout()
        columnas2.setSpacing(40)
        columnas2.setAlignment(Qt.AlignCenter)

        # ----- Agrego los botones al layout ----- #
        columnas2.addWidget(self.btn_administrador)
        columnas2.addWidget(self.btn_salir)
        
        # ----- Pongo cada botón dándole tamaño con su respectivo QlineEdit en sus columnas ----- #
        columnas.addWidget(self.btn_sesion, 0, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.usuario, 1, 1, alignment=Qt.AlignCenter)
        self.usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.contrasena, 2, 1, alignment=Qt.AlignCenter)
        self.contrasena.setFixedWidth(350)
        self.contrasena.setContentsMargins(0, 0, 0, 5)
        # ----- Separación ----- #
        columnas.addWidget(self.btn_usuario_nuevo, 3, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.line_nuevo_usuario, 4, 1, alignment=Qt.AlignCenter)
        self.line_nuevo_usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.nueva_contrasena, 5, 1, alignment=Qt.AlignCenter)
        self.nueva_contrasena.setFixedWidth(350)
        self.nueva_contrasena.setContentsMargins(0, 0, 0, 5)
        
        # ----- Agrego los botones al frame ----- #
        columnas.addLayout(columnas2, 7, 0, 1, 3)
        self.opciones_layout.addLayout(columnas)
        self.opciones_layout.addStretch()
        
        # ----- Conecto los botones a sus respectivas señales ----- #
        self.btn_administrador.clicked.connect(self.ir_admin)
        self.btn_sesion.clicked.connect(lambda: self.iniciar_sesion.emit(self.usuario.text(), self.contrasena.text()))
        self.btn_usuario_nuevo.clicked.connect(lambda: self.nuevo_usuario.emit(self.line_nuevo_usuario.text(), self.nueva_contrasena.text()))
        
    def clear(self):
        self.usuario.clear()
        self.contrasena.clear()
        self.line_nuevo_usuario.clear()
        self.nueva_contrasena.clear()
        
    def tooltip_length(self):
        pos = self.line_nuevo_usuario.mapToGlobal(self.line_nuevo_usuario.rect().topLeft() + QPoint(4, 10))
        
        QToolTip.showText(pos, "El nombre debe tener al menos 3 caracteres.", self.line_nuevo_usuario, self.line_nuevo_usuario.rect(), 1500)
        
    def tooltip_letters(self):
        pos = self.line_nuevo_usuario.mapToGlobal(self.line_nuevo_usuario.rect().topLeft() + QPoint(4, 10))
        
        QToolTip.showText(pos, "Solo se admiten letras.", self.line_nuevo_usuario, self.line_nuevo_usuario.rect(), 1500)