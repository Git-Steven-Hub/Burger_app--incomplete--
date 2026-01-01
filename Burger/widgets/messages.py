from PySide6.QtWidgets import QMessageBox

class Messages:
    def usuario_existente(parent):
        QMessageBox.warning(parent, "Error", "El usuario ya existe.")
    
    def usuario_creado(parent):
        QMessageBox.information(parent, "Usuario creado", "El usuario se creó correctamente.")
    
    def admin_error(parent):
        QMessageBox.warning(parent, "Error", "Usuario o contraseña erróneas.")
    
    def error_nombre(parent):
        QMessageBox.warning(parent, "Error", "Nombre no válido.")
        
    def error_pedido(parent):
        QMessageBox.warning(parent, "Error", "El pedido no puede estar vacío.")
        
    def pedido_finalizado_transferencia(parent, nombre):
        QMessageBox.information(parent, "Pedido realizado", f"¡El pedido de {nombre} se confirmó con éxito.")
        
    def pedido_finalizado_efectivo(parent, nombre, vuelto=None):
        texto = f"¡El pedido de {nombre} se confirmó con éxito!"
        if vuelto is not None:
            texto += f"\nEl vuelto es de ${vuelto:.2f}"
        
        QMessageBox.information(parent, "Pedido realizado", texto)