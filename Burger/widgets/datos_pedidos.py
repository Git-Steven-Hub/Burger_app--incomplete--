from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox, QDialogButtonBox, QHBoxLayout, QDoubleSpinBox, QSizePolicy
from PySide6.QtCore import Qt, QEvent

class DatosPedidos(QDialog):
    def __init__(self, pedidos_view, total, parent: QDialog = None):
        super().__init__(parent)
        
        self.datos = pedidos_view
        self.total = total
        
        self.setWindowTitle("Confirmar pedido")
        self.setMinimumSize(420, 250)
        self.adjustSize()
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        
        forma_pago = ("Efectivo" if self.datos.efectivo.isChecked() else "Transferencia")
        
        texto_general = QLabel("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        

        
        resumen = QLabel(f"""
                         <b>Cliente:</b> {self.datos.nombre_cliente.text().capitalize()}<br><br>
                         <b>Pedido:</b><br>
                         • Cantidad combo simple: {self.datos.combo_simple.text() or "0"}<br>
                         • Cantidad combo doble: {self.datos.combo_doble.text() or "0"}<br>
                         • Cantidad combo triple: {self.datos.combo_triple.text() or "0"}<br>
                         • Cantidad postre: {self.datos.postre_flan.text() or "0"}<br><br>
                         <b>Forma de pago:</b> {forma_pago}<br>
                         <b>Total:</b> ${self.total:.2f}<br>
                        """)

        texto_general.setAlignment(Qt.AlignCenter)
        texto_general.setWordWrap(True)
        resumen.setAlignment(Qt.AlignCenter)
        resumen.setWordWrap(True)
        resumen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(texto_general)
        layout.addWidget(resumen)
        
        if forma_pago == "Efectivo":
            self.setMinimumSize(400, 325)
            layout_monto = QHBoxLayout()
            layout_monto.setSpacing(5)
            
            texto_monto = QLabel("<b>Monto del cliente:</b>")
            
            self.monto_cliente = QDoubleSpinBox()
            self.monto_cliente.setRange(0, 99999.99)
            self.monto_cliente.setDecimals(2)
            self.monto_cliente.setPrefix("$ ")
            self.monto_cliente.setButtonSymbols(QDoubleSpinBox.NoButtons)
            self.monto_cliente.lineEdit().installEventFilter(self)
            self.monto_cliente.setFixedWidth(180)
            self.monto_cliente.setFixedHeight(30)
            
            layout_monto.addStretch()
            layout_monto.addWidget(texto_monto, alignment=Qt.AlignVCenter)
            layout_monto.addWidget(self.monto_cliente, alignment=Qt.AlignVCenter)
            
            layout.addLayout(layout_monto)
            
        layout.addStretch()
        layout.addWidget(botones)
    
    def eventFilter(self, obj, event):
        if obj == self.monto_cliente.lineEdit() and event.type() == QEvent.FocusIn:
            obj.selectAll()
            return False
        return super().eventFilter(obj, event)
    
    def error_nombre(self):
        QMessageBox.warning(self, "Error", "Nombre no válido.")
        
    def error_pedido(self):
        QMessageBox.warning(self, "Error", "El pedido no puede estar vacío.")
        
    def error_monto(self):
        QMessageBox.warning(self, "Error", "Monto insuficiente.")