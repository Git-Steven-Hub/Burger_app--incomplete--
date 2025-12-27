# ----- Importo las librerías necesarias ----- #
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

# ----- Creo la clase para el input del dinero ----- #
class DineroLineEdit(QLineEdit):
    # ----- Creo el init y defino el monto máximo que puede ingresarse ----- #
    def __init__(self, max_value = 100000, parent = None):
        super().__init__(parent)
        
        # ----- Creo los centavos/pesos y el máximo total, le seteo el el texto y su tamaño ----- #
        self.centavs = 0
        self.max_centavs = max_value * 100
        self.setAlignment(Qt.AlignRight)
        self.setText("$ 0.00")
        self.setFixedHeight(30)
    
    # ----- Creo el evento al presionar las teclas ----- #
    def keyPressEvent(self, event):
        key = event.key()
        
        if Qt.Key_0 <= key <= Qt.Key_9:
            nuevo = self.centavs * 10 + (key - Qt.Key_0)
            if nuevo <= self.max_centavs:
                self.centavs = nuevo
                self._update()
            return
        
        if key == Qt.Key_Backspace:
            self.centavs //= 10
            self._update()
            return
        
        event.ignore()
    
    # ----- Agrego un update para remplazar los puntos y comas, adémas que al valor lo divido entre 100----- #
    def _update(self):
        value = self.centavs / 100
        self.setText(f"$ {value:,.2f}".replace(",", "."))
    
    # ----- Devuelvo el valor ----- #
    def value(self):
        return self.centavs / 100