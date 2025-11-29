import os
from PySide6.QtCore import QLocale, QPoint, QRect, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon, QPalette, QRegion
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QSizePolicy, QWidget

class InicioView(QWidget):
    ir_admin = Signal()
    iniciar_sesion = Signal(str, str)
    nuevo_usuario = Signal(str, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        # ----- Creo el widget principal ----- #
        self.frame = QWidget()
        root_layout = QVBoxLayout(self)
        
        # ----- Creo los frames para cada opción ----- #
        self.frame_bienvenida = QFrame()
        self.frame_inicio = QFrame()
    
        # ----- Le agrego espacio para cada frame ----- #
        root_layout.addWidget(self.frame_bienvenida, stretch=1)
        root_layout.addWidget(self.frame_inicio, stretch=3)
        
        # ----- Añado el título y le asigno su nombre para el estilo ----- #
        titulo = QLabel("¡BIENVENIDO NUEVAMENTE!\n🍔 LA BURGUESIA 🍔")
        titulo.setObjectName("bienvenida")
        titulo.setAlignment(Qt.AlignCenter)
        QSpacerItem(20, 40)
        
        # ----- Añado el subtitulo y le agrego su estilo ----- #
        subtitulo = QLabel("¡Las mejores burguers!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        # ----- Añado el título y el subtitulo ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_bienvenida.setLayout(titulo_layout)
        
        # ----- Creo el efecto de opacidad ----- #
        efecto = QGraphicsOpacityEffect(self.frame)
        frame.setGraphicsEffect(self.efecto)
        efecto.setOpacity(0.0)
        
        # ----- Creo la animación ----- #
        animacion = QPropertyAnimation(self.efecto, b"opacity")
        animacion.setDuration(700)
        animacion.setStartValue(0.0)
        animacion.setEndValue(1.0)
        animacion.setEasingCurve(QEasingCurve.OutCubic)
        animacion.start()
        
        # ----- Mantengo la referencía de la animación ----- #
        self._anim = animacion
        
        # ----- Llamo a los botones mostrando el frame ----- #
        self._setup_buttones_layout()
        
    def _setup_buttons_layout(self):
                # ----- Seteo el layout del frame del inicio ----- #
        self.frame_inicio_layout = QVBoxLayout(self.frame_inicio)
        
        # ----- Creo el botón de inicio y le asigno nombre ----- #
        self.sesion = QPushButton("Iniciar sesión")
        sesion_icon = os.path.dirname(__file__)
        self.sesion.setIcon(QIcon(os.path.join(sesion_icon, "resources/icons/login.png")))
        self.sesion.setIconSize(QSize(25, 25))
        self.sesion.setObjectName("id1")
        self.sesion.setFixedWidth(380)
        
        # ----- Creo el botón de usuario nuevo y le asigno nombre----- #
        self.usuario_nuevo = QPushButton("Nuevo usuario")
        nuevo_usuario_icon = os.path.dirname(__file__)
        self.usuario_nuevo.setIcon(QIcon(os.path.join(nuevo_usuario_icon, "resources/icons/nuevo usuario.png")))
        self.usuario_nuevo.setIconSize(QSize(25, 25))
        self.usuario_nuevo.setObjectName("id2")
        self.usuario_nuevo.setFixedWidth(380)
        
        # ----- Creo el botón para el administrador ----- #
        self.administrador = QPushButton("Administrador")
        admin_icon = os.path.dirname(__file__)
        self.administrador.setIcon(QIcon(os.path.join(admin_icon, "resources/icons/admin.png")))
        self.administrador.setIconSize(QSize(25, 25))
        self.administrador.setObjectName("boton_admin")
        # ----- Creo el botón de salir y le asigno nombre ----- #
        self.salir = QPushButton("Salir")
        salir_icon = os.path.dirname(__file__)
        self.salir.setIcon(QIcon(os.path.join(salir_icon, "resources/icons/cerrar app.png")))
        self.salir.setIconSize(QSize(25, 25))
        self.salir.setObjectName("id3")
        
        # ----- Creo los QLineEdit para el inicio de sesión ----- #
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.contraseña = QLineEdit()
        self.contraseña.setPlaceholderText("Contraseña")
        self.contraseña.setEchoMode(QLineEdit.Password)
        
        # ----- Creo los QLineEdit para el nuevo usuario ----- #
        self.nuevo_usuario = QLineEdit()
        self.nuevo_usuario.setPlaceholderText("Crear usuario")
        self.nueva_contraseña = QLineEdit()
        self.nueva_contraseña.setPlaceholderText("Crear contraseña")
        
        # ----- Creo el layout para las columnas ----- #
        columnas = QGridLayout()
        columnas.setVerticalSpacing(10)

        # ----- Creo un layout para los botones de "Modificar usuario" y "Salir" ----- #
        columnas2 = QHBoxLayout()
        columnas2.setSpacing(40)
        columnas2.setAlignment(Qt.AlignCenter)

        # ----- Agrego los botones al layout ----- #
        columnas2.addWidget(self.administrador)
        columnas2.addWidget(self.salir)
        
        # ----- Pongo cada botón dándole tamaño con su respectivo QlineEdit en sus columnas ----- #
        columnas.addWidget(self.sesion, 0, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.usuario, 1, 1, alignment=Qt.AlignCenter)
        self.usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.contraseña, 2, 1, alignment=Qt.AlignCenter)
        self.contraseña.setFixedWidth(350)
        self.contraseña.setContentsMargins(0, 0, 0, 5)
        # ----- Separación ----- #
        columnas.addWidget(self.usuario_nuevo, 3, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.nuevo_usuario, 4, 1, alignment=Qt.AlignCenter)
        self.nuevo_usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.nueva_contraseña, 5, 1, alignment=Qt.AlignCenter)
        self.nueva_contraseña.setFixedWidth(350)
        self.nueva_contraseña.setContentsMargins(0, 0, 0, 5)
        
        # ----- Agrego los botones al frame ----- #
        columnas.addLayout(columnas2, 7, 0, 1, 3)
        self.frame_inicio_layout.addLayout(columnas)
        self.frame_inicio_layout.addStretch()