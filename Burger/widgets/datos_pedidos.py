# ----- Importo las librerías necesarias ----- #
from Burger.widgets.tooltips_ui import show_tooltip as tooltip
from Burger.widgets.input_dinero import DineroLineEdit
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QHBoxLayout, QSizePolicy, QFrame, QToolTip
from PySide6.QtCore import Qt, QPoint

# ----- Creo la ventana para los datos del pedido ----- #
class DatosPedidos(QDialog):
    # ----- Tomo como referencia la vista PedidosView y el total de ControladorMain ----- #
    def __init__(self, pedidos_view, total, parent: QDialog = None):
        super().__init__(parent)
        
        # ----- Creo las variables para cada sección ----- #
        self.datos = pedidos_view
        self.total = total
        self.vuelto = 0
        
        # ----- Le pongo nombre a la ventana ----- #
        self.setWindowTitle("Confirmar pedido")

        # ----- Creo el layout, agregando espacio y margenes ----- #
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        # ----- Creo los botones para la ventana ----- #
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        
        # ----- Guardo la referencia de los botones y del nombre ----- #
        self.botones = botones
        self.nombre = self.datos.nombre_cliente.text().capitalize()
        
        # ----- Creo la variable para ver cual opción está marcada ----- #
        forma_pago = ("Efectivo" if self.datos.efectivo.isChecked() else "Transferencia")
        
        # ----- Creo un frame para agregarle los datos, le pongo su nombre de estilo y tamaño ----- #
        carta_presentacion = QFrame()
        carta_presentacion.setObjectName("carta_resumen")
        carta_presentacion.setMinimumHeight(220)
        
        # ----- Creo el layout para añadir el fame, añadiendo margenes y espacio ----- #
        carta_presentacion_layout = QVBoxLayout(carta_presentacion)
        carta_presentacion_layout.setContentsMargins(20, 15, 20, 15)
        carta_presentacion_layout.setSpacing(10)
        
        # ----- Creo el titulo del texto ----- #
        texto_general = QLabel("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        texto_general.setObjectName("titulo_dialogo")
        
        # ----- Creo el resúmen del pedido, tomando los datos y añadiendo algo de HTML ----- #
        resumen = QLabel(f"""
            <div>
                <span style="font-size: 18px; font-weight: 600;">
                    Cliente
                </span><br>
                {self.nombre}
            <hr style="
                border: none;
                border-top: 1px solid rgba(31, 61, 53, 0.15);
                margin: 1px 1;
            ">
                <span style="font-size: 18px; font-weight: 600;">
                    Pedido
                </span><br>
                • Cantidad combo simple: <b>{self.datos.combo_simple.text() or "0"}</b><br>
                • Cantidad combo doble: <b>{self.datos.combo_doble.text() or "0"}</b><br>
                • Cantidad combo triple: <b>{self.datos.combo_triple.text() or "0"}</b><br>
                • Postre: <b>{self.datos.postre_flan.text() or "0"}</b>
            <hr style="
                border: none;
                border-top: 1px solid rgba(31, 61, 53, 0.15);
                margin: 2px 2;
            ">
                <span style="font-size: 18px; font-weight: 600;">
                    Pago
                </span><br>
                {forma_pago}<br><br>
                
                <span style:"font-size: 20px; font-weight: 700; border-radius: 10px; padding: 8px 12px;">
                    <b>Total:</b> ${self.total:.2f}
                </span>
            </div>
            """)
        # ----- Agrego el resúmen al layout ----- #
        carta_presentacion_layout.addWidget(resumen)
        
        # ----- Alineo el título y le habilito los saltos de línea ----- #
        texto_general.setAlignment(Qt.AlignCenter)
        texto_general.setWordWrap(True)
        
        # ----- Alineo el resúmen y le habilito los saltos de línea,. además que le habilito la opción que se expanda en horizontal ----- #
        resumen.setAlignment(Qt.AlignCenter)
        resumen.setWordWrap(True)
        resumen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        # ----- Agrego el titulo y el resúmen al layout ----- #
        layout.addWidget(texto_general)
        layout.addWidget(carta_presentacion)
        
        # ----- Si la opción "Efectivo" está marcada, se crea el layout del monto del cliente ----- #
        if forma_pago == "Efectivo":
            layout_monto = QHBoxLayout()
            layout_monto.setSpacing(5)
            
            texto_monto = QLabel("<b>Monto del cliente:</b>")
            texto_monto.setObjectName("texto_monto_cliente")
            texto_monto.setContentsMargins(10, 5, 10, 5)
            
            # ----- Importo el input del dinero y conecto el monto a la validación del dinero ----- #
            self.monto_cliente = DineroLineEdit()
            self.monto_cliente.textChanged.connect(self.validar_monto)
            self.validar_monto()

            # ----- Agrego el titulo y el resúmen al layout ----- #
            layout_monto.addWidget(texto_monto, alignment=Qt.AlignVCenter)
            layout_monto.addWidget(self.monto_cliente, alignment=Qt.AlignVCenter)
            layout.addLayout(layout_monto)
        
        # ----- Agrego los botones al layout principal, le agrego margenes y ajusto el tamaño de la ventana ----- #
        layout.addWidget(botones)
        layout.setContentsMargins(25, 5, 25, 5)
        self.adjustSize()
        self.setMinimumWidth(350)
        self.setFixedHeight(self.sizeHint().height())
    
    # ----- Creo una validación para el monto del cliente ----- #
    def validar_monto(self):
        # ----- El botón de aceptar solamente va a estar disponible cuando el monto del cliente supere el total ----- #
        boton_ok = self.botones.button(QDialogButtonBox.Ok)
        boton_ok.setEnabled(self.monto_cliente.value() >= self.total)
        
        # ----- Creo el limite máximo para el monto ----- #
        monto_max = 100000
        
        # ----- Si el monto del cliente llega al limite envía un aviso ----- #
        if self.monto_cliente.value() == monto_max:
            tooltip(self.monto_cliente, "Máximo alcanzado.", offset=QPoint(-6, 8))