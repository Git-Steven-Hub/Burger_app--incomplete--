# ----- Importo las librerías necesarias ----- #
from Burger.widgets.tooltips_ui import show_tooltip as tooltip
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox

# ----- Creo la clase ChangePass ----- #
class ChangePass(QDialog):
    # ----- Tomo como referencia el sistema y el nombre del usuario ----- #
    def __init__(self, sistema, nombre, parent: QDialog = None):
        super().__init__(parent)
        
        # ----- Inicializo el sistema y el nombre del usuario ----- #
        self.sistema = sistema
        self.nombre = nombre
        
        # ----- Le añado el título y fijo el tamaño la ventana ----- #
        self.setWindowTitle("Cambiar contraseña")
        self.setFixedSize(300, 150)
        
        # ----- Creo el layout y le agrego márgenes ----- #
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # ----- Creo el input para la contraseña antigua ----- #
        self.old_pass = QLineEdit()
        self.old_pass.setPlaceholderText("Contraseña actual")
        self.old_pass.setEchoMode(QLineEdit.Password)
        
        # ----- Creo el input para la nueva contraseña ----- #
        self.new_pass = QLineEdit()
        self.new_pass.setPlaceholderText("Nueva contraseña")
        self.new_pass.setEchoMode(QLineEdit.Password)
        
        # ----- Creo los botones, les doy tamaño y hago que el botón aceptar llame a otra función ----- #
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.setFixedHeight(50)
        botones.accepted.connect(self.validar)
        botones.rejected.connect(self.reject)
        
        # ----- Añado todo al layout ----- #
        layout.addWidget(self.old_pass)
        layout.addWidget(self.new_pass)
        layout.addWidget(botones)
    
    # ----- Creo la función para validar ambas contraseñas ----- #
    def validar(self):
        # ----- Si la nueva contraseña tiene menos de 4 caracteres envía un mensaje ----- #
        if len(self.new_pass.text()) < 4:
            tooltip(self.new_pass, "La nueva contraseña debe tener 4 caracteres o más.", QPoint(-19, 8))
            return
        
        # ----- Creo la variable para autenticar ----- #
        autenticar = self.sistema.authenticate(self.nombre, self.old_pass.text())
        
        # ----- Si la autenticación en la contraseña antigua falla envía un mensaje ----- #
        if not autenticar:
            tooltip(self.old_pass, "Contraseña actual incorrecta.", QPoint(10, 10))
            return
        
        # ----- Si todo está correcto el cambio se acepta ----- #
        self.accept()