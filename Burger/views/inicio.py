# ------ Importo las librerías necesarias ------ #
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QLineEdit, QGridLayout, QHBoxLayout, QSpacerItem
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize, Signal
from Burger.widgets.tooltips_ui import show_tooltip as tooltip
from Burger.widgets.background import BackgroundFrame
from Burger.widgets.effects import apply_shadow_label

class InicioView(QWidget):
    ir_admin = Signal()
    iniciar_sesion = Signal(str, str)
    nuevo_usuario = Signal(str, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
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
        
        # ----- Creo el título y el subtitulo ----- #
        self.titulo_label = QLabel("¡BIENVENIDO NUEVAMENTE!\n LA BURGUESIA")
        self.titulo_label.setObjectName("titulo")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        QSpacerItem(20, 40)
        
        self.subtitulo_label = QLabel("¡Las mejores burguers!")
        self.subtitulo_label.setObjectName("subtitulo")
        self.subtitulo_label.setAlignment(Qt.AlignCenter)
        self.subtitulo_label.setContentsMargins(0, 0, 0, 5)
        
        # ------ Añado el título, el subtitulo y lo seteo ------ #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(self.titulo_label)
        titulo_layout.addWidget(self.subtitulo_label)
        self.frame_titulo.setLayout(titulo_layout)

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
        self.icons_dir = os.path.join(os.path.dirname(__file__), "../resources/icons")
        
        # ----- Creo el botón de inicio y le asigno nombre ----- #
        self.btn_sesion = QPushButton("Iniciar sesión")
        self.btn_sesion.setIcon(QIcon(os.path.join(self.icons_dir, "login.png")))
        self.btn_sesion.setIconSize(QSize(25, 25))
        self.btn_sesion.setObjectName("id1")
        self.btn_sesion.setFixedWidth(380)
        
        # ----- Creo el botón de usuario nuevo y le asigno nombre----- #
        self.btn_usuario_nuevo = QPushButton("Nuevo usuario")
        self.btn_usuario_nuevo.setIcon(QIcon(os.path.join(self.icons_dir, "nuevo usuario.png")))
        self.btn_usuario_nuevo.setIconSize(QSize(25, 25))
        self.btn_usuario_nuevo.setObjectName("id2")
        self.btn_usuario_nuevo.setFixedWidth(380)
        
        # ----- Creo el botón para el administrador ----- #
        self.btn_administrador = QPushButton("Administrador")
        self.btn_administrador.setIcon(QIcon(os.path.join(self.icons_dir, "admin.png")))
        self.btn_administrador.setIconSize(QSize(25, 25))
        self.btn_administrador.setObjectName("boton_admin")
        
        # ----- Creo el botón de salir y le asigno nombre ----- #
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.setIcon(QIcon(os.path.join(self.icons_dir, "cerrar app.png")))
        self.btn_salir.setIconSize(QSize(25, 25))
        self.btn_salir.setObjectName("id3")
        
        # ----- Creo los QLineEdit para el inicio de sesión ----- #
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.contrasena = QLineEdit()
        self.contrasena.setPlaceholderText("Contraseña")
        self.contrasena.setEchoMode(QLineEdit.Password)
        
        # ----- Creo el botón para ver la contraseña ----- #
        self.ver_contrasena = QAction(QIcon(os.path.join(self.icons_dir, "eye closed icon.png")), "", self.contrasena)
        self.ver_contrasena.setCheckable(True)
        
        # ----- Agrego el botón de ver la contraseña ----- #
        self.contrasena.addAction(self.ver_contrasena, QLineEdit.TrailingPosition)

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
        columnas.addWidget(self.contrasena, 2, 1, alignment=Qt.AlignCenter)
        self.contrasena.setFixedWidth(350)
        self.contrasena.setContentsMargins(0, 0, 0, 5)
        columnas.addWidget(self.btn_usuario_nuevo, 3, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.line_nuevo_usuario, 4, 1, alignment=Qt.AlignCenter)
        self.line_nuevo_usuario.setFixedWidth(350)
        columnas.addWidget(self.nueva_contrasena, 5, 1, alignment=Qt.AlignCenter)
        self.nueva_contrasena.setFixedWidth(350)
        self.nueva_contrasena.setContentsMargins(0, 0, 0, 0)
        
        # ----- Agrego los botones al frame ----- #
        columnas.addLayout(columnas2, 7, 0, 1, 3)
        self.opciones_layout.addLayout(columnas)
        self.opciones_layout.addStretch()
        
        # ------ Manejo de eventos con teclado para mejor experiencia ------ #
        self.usuario.returnPressed.connect(lambda: self.contrasena.setFocus())
        self.contrasena.returnPressed.connect(self.btn_sesion.click)
        self.line_nuevo_usuario.returnPressed.connect(lambda: self.nueva_contrasena.setFocus())
        self.nueva_contrasena.returnPressed.connect(self.btn_usuario_nuevo.click)
        
        # ------ Manejo de foco para mejor experiencia ------ #
        self.btn_sesion.setFocusPolicy(Qt.NoFocus)
        self.btn_usuario_nuevo.setFocusPolicy(Qt.NoFocus)
        self.btn_administrador.setFocusPolicy(Qt.NoFocus)
        self.btn_salir.setFocusPolicy(Qt.NoFocus)

        # ----- Conecto los botones a sus respectivas señales ----- #
        self.btn_administrador.clicked.connect(self.ir_admin)
        self.btn_sesion.clicked.connect(lambda: self.iniciar_sesion.emit(self.usuario.text(), self.contrasena.text()))
        self.btn_usuario_nuevo.clicked.connect(lambda: self.nuevo_usuario.emit(self.line_nuevo_usuario.text(), self.nueva_contrasena.text()))
        self.ver_contrasena.toggled.connect(self.toggle_password)

    # ----- Creo la función para limpiar los campos de texto ----- #
    def clear(self):
        self.usuario.clear()
        self.contrasena.clear()
        self.line_nuevo_usuario.clear()
        self.nueva_contrasena.clear()
    
    # ----- Creo la función para mostrar y ocultar la contraseña ----- #
    def toggle_password(self, visible):
        if visible:
            self.contrasena.setEchoMode(QLineEdit.Normal)
            self.ver_contrasena.setIcon(QIcon(os.path.join(self.icons_dir, "eye open icon.png")))
        
        else:
            self.contrasena.setEchoMode(QLineEdit.Password)
            self.ver_contrasena.setIcon(QIcon(os.path.join(self.icons_dir, "eye closed icon.png")))

     # ----- Creo los tooltips para el nombre de usuario y para la contraseña ----- #
    def tooltip_length(self):
        tooltip(self.line_nuevo_usuario, "El nombre de usuario debe tener al menos 3 caracteres.")
        
    def tooltip_letters(self):
        tooltip(self.line_nuevo_usuario, "Solo se admiten letras.")
        
    def tooltip_pass_length(self):
        tooltip(self.nueva_contrasena, "La contraseña debe tener al menos 4 caracteres.")