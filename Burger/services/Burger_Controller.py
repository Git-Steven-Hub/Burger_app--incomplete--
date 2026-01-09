# ------ Importo las librerías necesarias ------ #
from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from Burger.animations.transitions import fade_slide
from Burger.widgets.close_shift import CloseShiftMessage
from Burger.widgets.auth_dialog import EnterAdmin
from Burger.widgets.datos_pedidos import DatosPedidos
from Burger.widgets.messages import Messages
from Burger.widgets.change_pass import ChangePass
import re

# ------ Creo la clase controladora (lógica) ------ #
class ControladorMain:
    # ------ Creo el init tomando las vistas y el sistema ------ #
    def __init__(self, views, sistema):
        # ------ Defino el ui y el sistema (además creo un bloqueador de animación para evitar bugs visuales) ------ #
        self.ui = views
        self.sistema = sistema
        self.animado = False
        self.turno_activo = False
        self.nombre = None
        
        self.conectar_acciones()
        
    def conectar_acciones(self):
        # ------ Defino el ui ------ #
        ui = self.ui
        self.ui.on_close = self.cerrar_aplicacion
        
        # ------ Conexiones InicioView ------ #
        ui.inicio.ir_admin.connect(self.confirmar_admin)
        ui.inicio.iniciar_sesion.connect(self.login_usuario)
        ui.inicio.nuevo_usuario.connect(self.create_user)
        ui.inicio.btn_salir.clicked.connect(ui.close)
        
        # ------ Conexiones AdminView ------ #
        ui.admin.volver_menu.connect(lambda: self.cambiar_frame(ui.admin, ui.inicio))
        
        
        # ------ Conexiones MenuView ------ #
        ui.menu.iniciar_pedido.connect(lambda: self.cambiar_frame(ui.menu, ui.pedidos))
        ui.menu.cerrar_turno.connect(self.terminar_turno)
        ui.menu.cambiar_contrasena.connect(self.change_pass)
        
        # ------ Conexiones PedidosView ------ #
        ui.pedidos.retroceder.connect(self.volver_menu)
        ui.pedidos.confirmar_pedido.connect(self.tomar_pedido)
    
    # ----- Creo la función para crear usuarios, el cual también controla si el nombre y la contraseña son válidas ----- #    
    def create_user(self, nombre, contrasena):
        if len(nombre) < 3:
            self.ui.inicio.tooltip_length()
            return
        
        if not re.match(r"^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$", nombre):
            self.ui.inicio.tooltip_letters()
            return
        
        if len(contrasena) < 4:
            self.ui.inicio.tooltip_pass_length()
            return
        
        add = self.sistema.insert_new_user(nombre, contrasena)
        
        if add:
            Messages.usuario_creado(self.ui)
            self.ui.inicio.clear()
        
        if not add:
            Messages.usuario_existente(self.ui)
        
    # ----- Creo la función que se encarga de iniciar sesión ----- #
    def login_usuario(self, nombre, contrasena):
        autenticar = self.sistema.authenticate(nombre, contrasena)
        
        if autenticar and autenticar[0] == "Empleado":
            self.nombre = nombre
            self.turno_activo = True # ----- Devuelvo True para el estado del turno ----- #
            self.ui.menu.subtitulo_label.setText(f"¡Encargado de turno {nombre.title()}!")
            self.sistema.register_entry(nombre)
            self.cambiar_frame(self.ui.inicio, self.ui.menu)
            self.ui.inicio.clear()
        
        else:
            Messages.error_usuario(self.ui)
            return
    
    # ----- Creo la función para cambiar la contraseña del usuario ----- #
    def change_pass(self):
        dialogo = ChangePass(self.sistema, self.nombre, self.ui)

        if not dialogo.exec():
            return
        
        self.sistema.change_password(self.nombre, dialogo.old_pass.text(), dialogo.new_pass.text())
        Messages.contraseña(self.ui)

    # ----- Creo la función que se encarga de confirmar al administrador ----- #
    def confirmar_admin(self):
        dialogo = EnterAdmin(self.ui)

        if dialogo.exec():
            nombre = dialogo.admin_user.text()
            contrasena = dialogo.admin_pass.text()
            autenticar = self.sistema.authenticate(nombre, contrasena)
            
            if autenticar and autenticar[0] == "admin":
                self.cambiar_frame(self.ui.inicio, self.ui.admin)
                self.ui.inicio.clear()
            
            else:
                Messages.error_usuario(self.ui)
            
    # ----- Creo la función que se encarga de cerrar la app ----- #
    def cerrar_aplicacion(self):
        if self.turno_activo:
            respuesta = Messages.turno_activo(self.ui)
            
            if respuesta == QMessageBox.No:
                return False
            
            self.sistema.registration_outside(self.nombre)
            self.turno_activo = False
            
        self.sistema.close_system()
        return True

    # ----- Creo la función que se encarga de cambiar los frames y ejecutar la animación ----- #
    def cambiar_frame(self, frame_actual, frame_siguiente):
        # ----- Si la animación ya está en curso no se ejecuta de nuevo ----- #
        if self.animado:
            return
        
        # ----- Se marca que la animación está en curso ----- #
        self.animado = True
        
        # ----- Defino el grupo, que toma el frame actual y el siguiente ----- #
        grupo = fade_slide(self.ui.stack, frame_actual, frame_siguiente)
        
        if grupo:
            grupo.finished.connect(lambda: self._animacion_finalizada())
        
    # ----- Creo la función que se encarga de finalizar la animación ----- #
    def _animacion_finalizada(self):
        self.animado = False
    
    # ----- Creo la función que se encarga devolver al menú limpiando los campos de texto ----- #
    def volver_menu(self):
        self.cambiar_frame(self.ui.pedidos, self.ui.menu)
        self.ui.pedidos.clean()
    
    # ----- Creo la función que se encarga de finalizar el turno, generando un mensaje ----- #
    def terminar_turno(self):
        confirm = CloseShiftMessage(self.ui)

        if confirm.execute():
            self.sistema.registration_outside(self.nombre)
            self.turno_activo = False
            self.cambiar_frame(self.ui.menu, self.ui.inicio)

    # ----- Creo la función que se encarga tomar los datos del pedido, comprobarlos y ejecutar el pedido ----- #
    def tomar_pedido(self):
        # ----- Tomo los datos de los campos de texto convirtiendolos en int para su uso ----- #
        cantidades = [
            int(self.ui.pedidos.combo_simple.text() or 0),
            int(self.ui.pedidos.combo_doble.text() or 0),
            int(self.ui.pedidos.combo_triple.text() or 0),
            int(self.ui.pedidos.postre_flan.text() or 0)
            ]
        
        total = cantidades[0] * 5 + cantidades[1] * 6 + cantidades[2] * 7 + cantidades[3] * 2

        if len(self.ui.pedidos.nombre_cliente.text()) < 3:
            Messages.error_nombre(self.ui)
            return
        
        if not re.match(r"^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$", self.ui.pedidos.nombre_cliente.text()):
            Messages.error_nombre(self.ui)
            return
        
        if sum(cantidades) == 0:
            Messages.error_pedido(self.ui)
            return   
        
        datos = DatosPedidos(self.ui.pedidos, total, self.ui)
        abrir = datos.exec()
        
        if not abrir:
            return 
        
        # ----- Si la opción del efectivo está seleccionado, se calcula el vuelto generando un mensaje limpiando los campos de texto ----- #
        if self.ui.pedidos.efectivo.isChecked():
            monto = datos.monto_cliente.value()
            vuelto = monto - total
            cliente = (self.ui.pedidos.nombre_cliente.text().capitalize())
            pago = "Efectivo"
            fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
            self.sistema.insert_sales(self.nombre, cliente, fecha, pago, cantidades[0], cantidades[1], cantidades[2], cantidades[3], total, vuelto)
            
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_efectivo(self.ui, cliente, vuelto)
        
        # ----- Si la opción de transferencia está seleccionado, se genera el respectivo mensaje limpiado los campos de texto ----- #
        if self.ui.pedidos.transferencia.isChecked():
            cliente = (self.ui.pedidos.nombre_cliente.text().capitalize())
            pago = "Transferencia"
            vuelto = "Sin vuelto"
            fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
            self.sistema.insert_sales(self.nombre, cliente, fecha, pago, cantidades[0], cantidades[1], cantidades[2], cantidades[3], total, vuelto)
            
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_transferencia(self.ui, cliente)