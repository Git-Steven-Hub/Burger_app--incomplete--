from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox, QLineEdit, QDialogButtonBox, QHBoxLayout
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import Qt

class DatosPedidos(QDialog):
    def __init__(self, pedidos_view, parent: QDialog = None):
        super().__init__(parent)
        
        self.datos = pedidos_view
        
        self.setWindowTitle("Confirmar pedido")
        self.setFixedSize(420, 250)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        botones.set
        
        forma_pago = ("Efectivo" if self.datos.efectivo.isChecked() else "Transferencia")
        
        texto_general = QLabel("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        
        resumen = QLabel(f"""
                         <b>Cliente:</b> {self.datos.nombre_cliente.text().capitalize()}<br><br>
                         <b>Pedido:</b><br>
                         • Cantidad combo simple: {self.datos.combo_simple.text()}<br>
                         • Cantidad combo doble: {self.datos.combo_doble.text()}<br>
                         • Cantidad combo triple: {self.datos.combo_triple.text()}<br>
                         • Cantidad postre: {self.datos.postre_flan.text()}<br><br>
                         <b>Forma de pago:</b> {forma_pago}<br>
                         <b>Total:</b> ${123}<br>
                        """)

        texto_general.setAlignment(Qt.AlignCenter)
        texto_general.setWordWrap(True)
        resumen.setAlignment(Qt.AlignCenter)
        resumen.setWordWrap(True)
        layout.addWidget(texto_general)
        layout.addWidget(resumen)
        
        if forma_pago == "Efectivo":
            self.setFixedSize(400, 325)
            layout_monto = QHBoxLayout()
            layout_monto.setSpacing(5)
            
            texto_monto = QLabel("<b>Monto del cliente:</b>")
            self.monto_cliente = QLineEdit()
            self.monto_cliente.setPlaceholderText("Monto del cliente")
            self.monto_cliente.setValidator(QDoubleValidator(0.0, 99999.0, 2))
            self.monto_cliente.setFixedWidth(180)
            
            layout_monto.addStretch()
            layout_monto.addWidget(texto_monto)
            layout_monto.addWidget(self.monto_cliente)
            
            layout.addLayout(layout_monto)
            
        layout.addStretch()
        layout.addWidget(botones)
        
    def error_nombre(self):
        QMessageBox.warning(self, "Error", "Nombre no válido.")
"""          
        resultado = self.sistema.tomar_pedido(datos)
        
        if not resultado["Bien"]:
            QMessageBox.warning(self, "Error", resultado["Error"])
            return
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Resúmen pedido")
        mensaje.setText("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        mensaje.setTextFormat(Qt.RichText)
        mensaje.setInformativeText(pedido_resumen)
        mensaje.setIcon(QMessageBox.Question)
        mensaje.setObjectName("mensaje_confirmacion")
        
        mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mensaje.setDefaultButton(QMessageBox.No)
        
        efecto = QGraphicsDropShadowEffect()
        efecto.setBlurRadius(20)
        efecto.setOffset(3, 3)
        efecto.setColor(Qt.black)
        
        mensaje.setGraphicsEffect(efecto)
        
        if mensaje.exec() == QMessageBox.Yes:
            self.cobro_pedido()
            self.limpiar_campos()
        
        
        
        mensaje = QDialog(self)
        mensaje.setWindowTitle("Cobro")
        mensaje.setFixedSize(400, 400)
        
        validador = QIntValidator(0, 9999999)
        
        layout = QVBoxLayout(mensaje)
        layout.setContentsMargins(15, 15, 15, 15)
        texto_monto = QLabel(f"Total: {self.total}")
        texto_cobro = QLabel("Monto entregado: ")
        monto_entregado = QLineEdit()
        
        monto_entregado.setValidator(validador)
        
"""