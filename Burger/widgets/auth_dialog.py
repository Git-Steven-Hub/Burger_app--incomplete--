from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QMessageBox

# ----- Creo la ventana para entrar al administrador----- #
class EnterAdmin(QDialog):
    def __init__(self, parent: QDialog = None):
        super().__init__(parent)
       
        # ----- Le doy nombre a la ventana ----- #
        self.setWindowTitle("Acceso administrador")
        
        # ----- Seteo su tamaño ----- #
        self.setFixedSize(300, 150)
        
        # ----- Creo el boxvertical ----- #
        layout = QVBoxLayout(self)
        
        # ----- Le agrego los margenes ----- #
        layout.setContentsMargins(15, 15, 15, 15)
        
        # ----- Creo el LineEdit para que el admin ponga su usuario ----- #
        self.admin_user = QLineEdit()
        self.admin_user.setPlaceholderText("Usuario")
        
        # ----- Creo el LineEdit para la contraseña del admin ocultando lo escrito ----- #
        self.admin_pass = QLineEdit()
        self.admin_pass.setPlaceholderText("Contraseña")
        self.admin_pass.setEchoMode(QLineEdit.Password)

        # ----- Seteo los botones para aceptar y cancelar la confirmación ----- #
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.setFixedHeight(50)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        
        # ----- Agregro todo al layout ----- #
        layout.addWidget(self.admin_user)
        layout.addWidget(self.admin_pass)
        layout.addWidget(botones)
    
    def out(self):
        QMessageBox.warning(self, "Error", "Usuario o contraseña erróneas.")