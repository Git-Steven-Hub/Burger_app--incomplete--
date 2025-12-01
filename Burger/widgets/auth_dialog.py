        # ----- Creo la ventana de la confirmación ----- #
        confirmacion = QDialog(self)
        
        # ----- Le doy nombre a la ventana ----- #
        confirmacion.setWindowTitle("Acceso administrador")
        
        # ----- Seteo su tamaño ----- #
        confirmacion.setFixedSize(300, 150)
        
        # ----- Creo el boxvertical ----- #
        layout = QVBoxLayout(confirmacion)
        
        # ----- Le agrego los margenes ----- #
        layout.setContentsMargins(15, 15, 15, 15)
        
        # ----- Creo el LineEdit para que el admin ponga su usuario ----- #
        admin = QLineEdit()
        admin.setPlaceholderText("Usuario")
        
        # ----- Creo el LineEdit para la contraseña del admin ocultando lo escrito ----- #
        admin_pass = QLineEdit()
        admin_pass.setPlaceholderText("Contraseña")
        admin_pass.setEchoMode(QLineEdit.Password)

        # ----- Seteo los botones para aceptar y cancelar la confirmación ----- #
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(confirmacion.accept)
        botones.rejected.connect(confirmacion.reject)
        
        # ----- Agregro todo al layout ----- #
        layout.addWidget(admin)
        layout.addWidget(admin_pass)
        layout.addWidget(botones)
        
        # ----- Creo la acción que rechaza si está mal la contraseña o el usuario ----- #
        if confirmacion.exec() == QDialog.Accepted:
            if admin.text() == "admin" and admin_pass.text() == "admin123":
                self.ir_frame(self.stack.currentWidget(), self.admin)
            else:
                QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")