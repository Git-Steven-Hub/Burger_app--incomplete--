# ----- Importo las librerías necesarias ----- #
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
        
class AdminView(QWidget):
    volver_menu = Signal()
    crear_usuario = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
        
    def _build_ui(self):
        root_layout = QVBoxLayout(self)
        
        self.frame_titulo = QFrame()
        self.frame_opciones = QFrame()
    
        self.frame_titulo.setObjectName("frame_decorado")
        self.frame_opciones.setStyleSheet("QFrame {background-color: transparent;}")
        
        root_layout.addWidget(self.frame_titulo, stretch=1)
        
        root_layout.addWidget(self.frame_opciones, stretch=3)
        self.frame_opciones.setContentsMargins(0, 20, 0, 0)
        
        # ----- Creo el título y le asigno un nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        
        # ----- Creo el subtitulo y le asigno un nombre para el estilo ----- #
        subtitulo = QLabel("¡Administrador!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo.setLayout(titulo_layout)
        
        # ----- Llamo los botones del admin ----- #
        self._setup_buttons_layout()
    
    def _setup_buttons_layout(self):
        self.opciones_layout = QVBoxLayout(self.frame_opciones)

        icons_dir = os.path.join(os.path.dirname(__file__), "../resources/icons")
        
        # ----- Creo un grupo para la parte de usuarios ----- #
        grupo_usuarios = QGroupBox("Usuarios")
        layout_usuarios = QGridLayout()
        layout_usuarios.setContentsMargins(10, 25, 10, 10)

        # ----- Creo el botón para crear usuarios, agregando su icono y su estilo  ----- #
        self.btn_crear = QPushButton("Crear usuario")
        self.btn_crear.setIcon(QIcon(os.path.join(icons_dir, "nuevo usuario.png")))
        self.btn_crear.setIconSize(QSize(23, 23))
        self.btn_crear.setObjectName("id2")
        self.btn_crear.setFixedWidth(180)
        
        # ----- Creo el botón para modificar usuarios, agregando su icono y su estilo ----- #
        self.btn_modificar = QPushButton("Modificar usuario")
        self.btn_modificar.setIcon(QIcon(os.path.join(icons_dir, "editar usuario.png")))
        self.btn_modificar.setIconSize(QSize(23, 23))
        self.btn_modificar.setObjectName("id5")
        self.btn_modificar.setFixedWidth(180)
        
        # ----- Creo el botón para eliminar usuarios, agregando su icono y su estilo ----- #
        self.btn_eliminar = QPushButton("Eliminar usuario")
        self.btn_eliminar.setIcon(QIcon(os.path.join(icons_dir, "eliminar usuario.png")))
        self.btn_eliminar.setIconSize(QSize(23, 23))
        self.btn_eliminar.setFixedWidth(180)
        
        # ----- Creo el botón para modificar al administrador, agregando su icono y su estilo ----- #
        self.btn_editar_admin = QPushButton("Modificar Admin")
        self.btn_editar_admin.setIcon(QIcon(os.path.join(icons_dir, "modificar admin.png")))
        self.btn_editar_admin.setIconSize(QSize(23, 23))
        self.btn_editar_admin.setObjectName("id5")
        self.btn_editar_admin.setFixedWidth(180)
        
        # ----- Agrego los botones para los usuarios en sus correspondientes posiciones ----- #
        layout_usuarios.addWidget(self.btn_crear, 0, 0, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.btn_modificar, 1, 0, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.btn_eliminar, 0, 1, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.btn_editar_admin, 1, 1, alignment=Qt.AlignCenter)
        layout_usuarios.setVerticalSpacing(10)
        
        # ----- Seteo el grupo de los usuarios ----- #
        grupo_usuarios.setLayout(layout_usuarios)
        
        # ----- Creo un grupo para el sistema de la app ----- #
        grupo_sistema = QGroupBox("Sistema")
        layout_sistema = QGridLayout()
        layout_sistema.setContentsMargins(10, 25, 10, 10)
        
        # ----- Creo el botón para ver los registros, agregando su icono y su estilo ----- #
        self.btn_registros = QPushButton("Ver registros")
        self.btn_registros.setIcon(QIcon(os.path.join(icons_dir, "registros.png")))
        self.btn_registros.setIconSize(QSize(23, 23))
        self.btn_registros.setObjectName("id4")
        self.btn_registros.setFixedWidth(180)
        
        # ----- Creo el botón para el respaldo de la app, agregando su icono y su estilo ----- #
        self.btn_respaldo = QPushButton("Respaldo")
        self.btn_respaldo.setIcon(QIcon(os.path.join(icons_dir, "backup.png")))
        self.btn_respaldo.setIconSize(QSize(23, 23))
        self.btn_respaldo.setObjectName("id6")
        self.btn_respaldo.setFixedWidth(180)
        
        # ----- Creo el botón para volver al login principal, agregando su icono y su estilo ----- #
        self.btn_volver = QPushButton("Volver al menú")
        self.btn_volver.setIcon(QIcon(os.path.join(icons_dir, "retroceder.png")))
        self.btn_volver.setIconSize(QSize(23, 23))
        self.btn_volver.setObjectName("id3")
        self.btn_volver.setFixedWidth(180)
        
        # ----- Agrego los botones del sistema en sus correspondientes posiciones ----- #
        layout_sistema.addWidget(self.btn_registros, 0, 0, alignment=Qt.AlignCenter)
        layout_sistema.addWidget(self.btn_respaldo, 0, 1, alignment=Qt.AlignCenter)
        layout_sistema.addWidget(self.btn_volver, 1, 0, 1, 2,alignment=Qt.AlignCenter)
        layout_sistema.setVerticalSpacing(15)
        
        # ----- Seteo el grupo para el sistema ----- #
        grupo_sistema.setLayout(layout_sistema)
        
        # ----- Agrego ambos grupos al frame del administrador ----- #
        self.opciones_layout.addWidget(grupo_usuarios)
        self.opciones_layout.addWidget(grupo_sistema)
        self.opciones_layout.addStretch()
        
        # ----- Seteo el grupo de los usuarios ----- #
        self.btn_volver.clicked.connect(lambda: self.volver_menu.emit())