# ----- Importo las librerías necesarias ----- #
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Burger.widgets.background import BackgroundFrame
        
class PedidosView(QWidget):
    retroceder = Signal()
    confirmar_pedido = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        # ----- Creo el layout vertical ----- #
        root_layout = QVBoxLayout(self)
        
        # ----- Creo los frames para cada opción ----- #
        self.frame_titulo = QFrame()
        self.frame_opciones = QFrame()
        
        self.frame_titulo = BackgroundFrame()
        self.frame_titulo.setObjectName("frame_titulo")
        self.frame_opciones.setObjectName("frame_decorado")
        
        # ----- Les agrego espacio a cada frame ----- #
        root_layout.addWidget(self.frame_titulo, stretch=1)
        root_layout.addWidget(self.frame_opciones, stretch=3)
        
        # ----- Creo el título y le asigno un nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        
        # ----- Creo el subtitulo y le asigno un nombre para el estilo ----- #
        subtitulo = QLabel("¡PEDIDOS!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        
        # ----- Añado todo al layout ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo.setLayout(titulo_layout)
        
        # ----- Llamo a los botones ----- #
        self._setup_buttons_layout()
        
    def _setup_buttons_layout(self):
        # ----- Seteo el layout del frame del inicio ----- #
        self.frame_opciones_layout = QVBoxLayout(self.frame_opciones)

        # ----- Validador para los pedidos ----- #
        self.validador = QIntValidator(0, 100)

        # ----- Campo para el nombre ----- #
        self.nombre_cliente = QLineEdit()
        self.nombre_cliente.setPlaceholderText("Nombre")
        
        # ----- Campos para los pedidos ----- #
        self.combo_simple = QLineEdit()
        self.combo_doble = QLineEdit()
        self.combo_triple = QLineEdit()
        self.postre_flan = QLineEdit()
        
        # ----- Guardo los campos de los pedidos en una tupla y hago iteración para agregarles el validador y su placeholder ----- #
        self.inputs = [self.combo_simple, self.combo_doble, self.combo_triple, self.postre_flan]
        for i in self.inputs:
            i.setValidator(self.validador)
            i.setPlaceholderText("Cantidad")

        # ----- Creo el label del cliente y le agrego su estilo ----- #
        texto_nombre = QLabel("Nombre del cliente")
        texto_nombre.setObjectName("label_cliente")

        # ----- Creo el label del pago y le agrego su estilo ----- #
        texto_pago = QLabel("Forma de pago")
        texto_pago.setObjectName("label_pago")

        # ----- Creo el label del pago y le agrego su estilo ----- #
        texto_combo_simple = QLabel("Cantidad de combo Simple 🍔 (Costo $5):")
        texto_combo_doble = QLabel("Cantidad de combo Doble 🍔 (Costo $6):")
        texto_combo_triple = QLabel("Cantidad de combo Triple 🍔 (Costo $7):")
        texto_postre = QLabel("Cantidad de postre Flan 🍮 (Costo $2):")
        
        # ----- Agrego los labels en una tupla y les agrego un estilo ----- #
        textos = [texto_combo_simple, texto_combo_doble, texto_combo_triple, texto_postre]
        for i in textos:
            i.setObjectName("labels_pedidos")

        # ----- Creo la casilla para el pago en efectivo ----- #
        self.efectivo = QRadioButton("Efectivo")
        self.efectivo.setFixedSize(80, 30)
        
        # ----- Creo la casilla para el pago en transferencia ----- #
        self.transferencia = QRadioButton("Transferencia")
        self.transferencia.setFixedSize(100, 30)
        self.efectivo.setChecked(True)

        # ----- Creo el espacio para las formas de pago ----- #
        pago_layout = QHBoxLayout()
        pago_layout.setSpacing(10)
        pago_layout.addWidget(self.efectivo)
        pago_layout.addWidget(self.transferencia)
        pago_layout.addStretch()

        # ----- Creo el espacio para los pedidos ----- #
        grid = QGridLayout()
        grid.setVerticalSpacing(15)
        grid.setHorizontalSpacing(10)

        # ----- Agrego cada texto con su respectivo QLineEdit ----- #
        grid.addWidget(texto_nombre, 0, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.nombre_cliente, 0, 1)
        # ----- Separación ----- #
        grid.addWidget(texto_pago, 1, 0, alignment=Qt.AlignCenter | Qt.AlignTop)
        grid.addLayout(pago_layout, 1, 1)
        # ----- Separación ----- #
        grid.addWidget(texto_combo_simple, 2, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_simple, 2, 1)
        # ----- Separación ----- #
        grid.addWidget(texto_combo_doble, 3, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_doble, 3, 1)
        # ----- Separación ----- #
        grid.addWidget(texto_combo_triple, 4, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_triple, 4, 1)
        # ----- Separación ----- #
        grid.addWidget(texto_postre, 5, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.postre_flan, 5, 1)

        # ----- Creo el botón para volver al menu ----- #
        self.btn_atras = QPushButton("Retroceder")
        boton_atras_icon = os.path.dirname(__file__)
        self.btn_atras.setIcon(QIcon(os.path.join(boton_atras_icon, "icons/retroceder.png")))
        self.btn_atras.setIconSize(QSize(25, 25))
        
        # ----- Creo el botón para confirmar el pedido ----- #
        self.btn_confirmar = QPushButton("Confirmar")
        boton_confirmar_icon = os.path.dirname(__file__)
        self.btn_confirmar.setIcon(QIcon(os.path.join(boton_confirmar_icon, "icons/aceptar.png")))
        self.btn_confirmar.setIconSize(QSize(25, 25))
        self.btn_confirmar.setObjectName("id1")

        # ----- Les doy espacio verticalos a los botones y los agrego ----- #
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_atras)
        botones_layout.addWidget(self.btn_confirmar)

        # ----- Agrego todo al layout principal ----- #
        self.frame_opciones_layout.addLayout(grid)
        self.frame_opciones_layout.addSpacing(20)
        self.frame_opciones_layout.addLayout(botones_layout)
        self.frame_opciones_layout.addStretch()

        # ----- Vista para apretar "Enter" y que salte al siguiento campo de texto ----- #
        self.nombre_cliente.returnPressed.connect(lambda: self.combo_simple.setFocus())
        self.combo_simple.returnPressed.connect(lambda: self.combo_doble.setFocus())
        self.combo_doble.returnPressed.connect(lambda: self.combo_triple.setFocus())
        self.combo_triple.returnPressed.connect(lambda: self.postre_flan.setFocus())
        self.postre_flan.returnPressed.connect(self.btn_confirmar.click)

        # conectar botones a las señales públicas
        self.btn_atras.clicked.connect(self.retroceder.emit)
        self.btn_confirmar.clicked.connect(self.confirmar_pedido.emit)