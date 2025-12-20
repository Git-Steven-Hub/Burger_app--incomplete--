from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox, QDialogButtonBox, QHBoxLayout, QDoubleSpinBox, QSizePolicy, QFrame
from PySide6.QtCore import Qt, QEvent

class DatosPedidos(QDialog):
    def __init__(self, pedidos_view, total, parent: QDialog = None):
        super().__init__(parent)
        
        self.datos = pedidos_view
        self.total = total
        self.vuelto = 0
        
        self.setWindowTitle("Confirmar pedido")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        
        self.botones = botones
        self.nombre = self.datos.nombre_cliente.text().capitalize()
        
        forma_pago = ("Efectivo" if self.datos.efectivo.isChecked() else "Transferencia")
        
        carta_presentacion = QFrame()
        carta_presentacion.setObjectName("carta_resumen")
        carta_presentacion.setMinimumHeight(220)
        
        carta_presentacion_layout = QVBoxLayout(carta_presentacion)
        carta_presentacion_layout.setContentsMargins(20, 15, 20, 15)
        carta_presentacion_layout.setSpacing(10)
        
        
        texto_general = QLabel("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        texto_general.setObjectName("titulo_dialogo")
        
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
        resumen.setObjectName("resumen_pedido")
        
        carta_presentacion_layout.addWidget(resumen)
        texto_general.setAlignment(Qt.AlignCenter)
        texto_general.setWordWrap(True)
        resumen.setAlignment(Qt.AlignCenter)
        resumen.setWordWrap(True)
        resumen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(texto_general)
        layout.addWidget(carta_presentacion)
        
        if forma_pago == "Efectivo":
            layout_monto = QHBoxLayout()
            layout_monto.setSpacing(5)
            
            texto_monto = QLabel("<b>Monto del cliente:</b>")
            texto_monto.setObjectName("texto_monto_cliente")
            texto_monto.setContentsMargins(10, 5, 10, 5)
            
            self.monto_cliente = QDoubleSpinBox()
            self.monto_cliente.setRange(0, 99999.99)
            self.monto_cliente.setDecimals(2)
            self.monto_cliente.setPrefix("$ ")
            self.monto_cliente.valueChanged.connect(self.validar_monto)
            self.monto_cliente.lineEdit().textEdited.connect(self.validar_monto)
            self.validar_monto()
            self.monto_cliente.setButtonSymbols(QDoubleSpinBox.NoButtons)
            self.monto_cliente.setKeyboardTracking(False)
            self.monto_cliente.installEventFilter(self)
            self.monto_cliente.setFixedWidth(180)
            self.monto_cliente.setFixedHeight(30)
            
            layout_monto.addWidget(texto_monto, alignment=Qt.AlignVCenter)
            layout_monto.addWidget(self.monto_cliente, alignment=Qt.AlignVCenter)
            layout.addLayout(layout_monto)
        
        layout.addWidget(botones)
        layout.setContentsMargins(25, 5, 25, 5)
        self.adjustSize()
        self.setMinimumWidth(350)
        self.setFixedHeight(self.sizeHint().height())
    
    def eventFilter(self, obj, event):
        if obj is self.monto_cliente and event.type() == QEvent.FocusIn:
            self.monto_cliente.lineEdit().selectAll()
            return False
        return super().eventFilter(obj, event)
        
    def validar_monto(self):
        boton_ok = self.botones.button(QDialogButtonBox.Ok)

        texto = self.monto_cliente.text()
        texto = texto.replace("$", "").replace(",", ".").strip()

        try:
            valor = float(texto)
        except ValueError:
            valor = 0.0

        boton_ok.setEnabled(valor >= self.total)