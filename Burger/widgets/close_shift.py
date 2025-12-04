from PySide6.QtWidgets import QMessageBox, QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt

class CloseShiftMessage(QMessageBox):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Cerrar turno")
        self.setText("¿Estás seguro que quiere cerrar el turno?")
        self.setIcon(QMessageBox.Warning)

        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        
        efecto = QGraphicsDropShadowEffect()
        efecto.setBlurRadius(0)
        efecto.setOffset(0, 0)
        efecto.setColor(Qt.black)
        
        self.setGraphicsEffect(efecto)
    
    def execute(self):
        return self.exec() == QMessageBox.Yes