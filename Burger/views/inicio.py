import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class InicioView(QWidget):
    ir_admin = Signal()
    iniciar_sesion = Signal(str, str)
    nuevo_usuario = Signal(str, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        root_layout = QVBoxLayout(self)
    
        # ----- Creo los frames para cada opción ----- #
        self.frame_titulo = QFrame()
        self.frame_opciones = QFrame()
    
        self.frame_titulo.setObjectName("frame_decorado")
        self.frame_opciones.setObjectName("frame_decorado")
        
        # ----- Le agrego espacio para cada frame ----- #
        root_layout.addWidget(self.frame_titulo, stretch=1)
        root_layout.addWidget(self.frame_opciones, stretch=3)
        
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
        
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo.setLayout(titulo_layout)
        
        # ----- Creo el efecto de opacidad ----- #
        efecto = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(efecto)
        efecto.setOpacity(0.0)
        self.efecto = efecto
        
        # ----- Creo la animación ----- #
        animacion = QPropertyAnimation(efecto, b"opacity")
        animacion.setDuration(1000)
        animacion.setStartValue(0.0)
        animacion.setEndValue(1.0)
        animacion.setEasingCurve(QEasingCurve.OutCubic)
        # ----- Mantengo la referencía de la animación ----- #
        self._anim = animacion
        
        animacion.start()
        
        # ----- Llamo a los botones para rellenar opciones_section ----- #
        self._setup_buttons_layout()
        
    def _setup_buttons_layout(self):
        # ----- Usar el layout de opciones_section creado en _build_ui ----- #
        self.opciones_layout = QVBoxLayout(self.frame_opciones)
        
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