# ------ Importo las librerías necesarias ------ #
from Burger.services.Burger_System import Sistema
from Burger.animations.transitions import fade_slide
from Burger.widgets.close_shift import CloseShiftMessage
from Burger.widgets.auth_dialog import EnterAdmin
from Burger.widgets.datos_pedidos import DatosPedidos
from Burger.widgets.messages import Messages
import re

# ------ Creo la clase controladora (lógica) ------ #
class ControladorMain:
    # ------ Creo el init tomando las vistas y el sistema ------ #
    def __init__(self, views):
        # ------ Defino el ui y el sistema (además creo un bloqueador de animación para evitar bugs visuales) ------ #
        self.ui = views
        self.sistema = Sistema()
        self.sistema.connect()
        self.animado = False
        
        # ------ Llamo a las acciones ------ #
        self.conectar_acciones()
        
    def conectar_acciones(self):
        # ------ Defino el ui ------ #
        ui = self.ui
        
        # ------ Conexiones InicioView ------ #
        ui.inicio.ir_admin.connect(self.confirmar_admin)
        ui.inicio.iniciar_sesion.connect(self.login_usuario)
        ui.inicio.nuevo_usuario.connect(self.create_user)
        ui.inicio.btn_salir.clicked.connect(self.cerrar_aplicacion)
        
        # ------ Conexiones AdminView ------ #
        ui.admin.volver_menu.connect(lambda: self.cambiar_frame(ui.admin, ui.inicio))
        
        
        # ------ Conexiones MenuView ------ #
        ui.menu.iniciar_pedido.connect(lambda: self.cambiar_frame(ui.menu, ui.pedidos))
        ui.menu.cerrar_turno.connect(self.terminar_turno)
        
        # ------ Conexiones PedidosView ------ #
        ui.pedidos.retroceder.connect(self.volver_menu)
        ui.pedidos.confirmar_pedido.connect(self.tomar_pedido)
    
    # ----- Creo la función para crear usuarios, el cual también controla si el nombre y la contraseña son válidas ----- #    
    def create_user(self, nombre, contrasena):
        # ----- Si el largo del nombre es menor a 3 se generá el tooltip ----- #
        if len(nombre) < 3:
            self.ui.inicio.tooltip_length()
            return
        
        # ----- Si el nombre contiene caracteres no permitidos se genera el tooltip ----- #
        if not re.match(r"^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$", nombre):
            self.ui.inicio.tooltip_letters()
            return
        
        # ----- Si el largo de la contraseña es menor a 4 se genera el tooltip ----- #
        if len(contrasena) < 4:
            self.ui.inicio.tooltip_pass_length()
            return
        
        # ----- Creo la variable que se encarga de crear el usuario ----- #
        add = self.sistema.insert_new_user(nombre, contrasena)
        
        # ----- Si el usuario se crea correctamente, el campo de texto se limpia y envía el mensaje ----- #
        if add:
            Messages.usuario_creado(self.ui)
            self.ui.inicio.clear()
        
        # ----- Si el usuario ya existe envía el respectivo mensaje ----- #
        if not add:
            Messages.usuario_existente(self.ui)
        
    # ----- Creo la función que se encarga de iniciar sesión ----- #
    def login_usuario(self, nombre, contrasena):
        
        # ----- Creo la variable que se encarga de autenticar el usuario ----- #
        autenticar = self.sistema.authenticate(nombre, contrasena)
        
        # ----- Si el usuario se comprueba correctamente se cambia el frame ----- #
        if autenticar and autenticar[0] == "Empleado":
            nombre = nombre.capitalize()
            self.ui.menu.subtitulo_label.setText(f"¡Encargado de turno {nombre}!")
            self.cambiar_frame(self.ui.inicio, self.ui.menu)
            self.ui.inicio.clear()
        
        # ----- Si el usuario no se comprueba corrrectamente genera el mensaje ----- #
        else:
            Messages.error_usuario(self.ui)
            return
    
    # ----- Creo la función que se encarga de confirmar al administrador ----- #
    def confirmar_admin(self):
        dialogo = EnterAdmin(self.ui)

        # ----- El diálogo se ejecuta y se obtienen los datos de los campos de texto ----- #
        if dialogo.exec():
            nombre = dialogo.admin_user.text()
            contrasena = dialogo.admin_pass.text()
            
            # ----- Creo la variable que se encarnga de autenticar al admin ----- #
            autenticar = self.sistema.authenticate(nombre, contrasena)
            
            # ----- Si se comprueba que es el admin cambia el frame ----- #
            if autenticar and autenticar[0] == "admin":
                self.cambiar_frame(self.ui.inicio, self.ui.admin)
                self.ui.inicio.clear()
            
            # ----- Si no se comprueba genera el mensaje ----- #
            else:
                Messages.error_usuario(self.ui)
            
    # ----- Creo la función que se encarga de cerrar la app ----- #
    def cerrar_aplicacion(self):
        try:
            self.sistema.close_system()
            
        except Exception as e:
            print(e)
            
        self.ui.close()

    # ----- Creo la función que se encarga de cambiar los frames y ejecutar la animación ----- #
    def cambiar_frame(self, frame_actual, frame_siguiente):
        # ----- Si la animación ya está en curso no se ejecuta de nuevo ----- #
        if self.animado:
            return
        
        # ----- Se marca que la animación está en curso ----- #
        self.animado = True
        
        # ----- Defino el grupo, que toma el frame actual y el siguiente ----- #
        grupo = fade_slide(self.ui.stack, frame_actual, frame_siguiente)
        
        # ----- Si el grupo se crea correctamente, se conecta la señal de finalización ----- #
        if grupo:
            grupo.finished.connect(lambda: self._animacion_finalizada())
        
    # ----- Creo la función que se encarga de finalizar la animación ----- #
    def _animacion_finalizada(self):
        self.animado = False
    
    # ----- Creo la función que se encarga devolver al menú limpiado los campos de texto de pedidos ----- #
    def volver_menu(self):
        self.cambiar_frame(self.ui.pedidos, self.ui.menu)
        self.ui.pedidos.clean()
    
    # ----- Creo la función que se encarga de finalizar el turno, generando un mensaje ----- #
    def terminar_turno(self):
        confirm = CloseShiftMessage(self.ui)
        
        # ----- Si se confirma el cierre del turno, vuelve al frame del inicio ----- #
        if confirm.execute():
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
        
        # ----- Creo el total de todo el pedido ----- #
        total = cantidades[0] * 5 + cantidades[1] * 6 + cantidades[2] * 7 + cantidades[3] * 2
        
        # ----- Si el nombre del cliente es inválido genera un mensaje ----- #
        if len(self.ui.pedidos.nombre_cliente.text()) < 3:
            Messages.error_nombre(self.ui)
            return
        
        # ----- Si el nombre del cliente contiene caracteres no válidos genera un mensaje ----- #
        if not re.match(r"^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$", self.ui.pedidos.nombre_cliente.text()):
            Messages.error_nombre(self.ui)
            return
        
        # ----- Si al sumar las cantidades el resultado es 0, se genera un mensaje ----- #
        if sum(cantidades) == 0:
            Messages.error_pedido(self.ui)
            return   
        
        # ----- Defino los datos del pedido y lo ejecuto ----- #
        datos = DatosPedidos(self.ui.pedidos, total, self.ui)
        abrir = datos.exec()
        
        # ----- Si no se ejecuta el diálogo de los datos del pedido se cancela el proceso ----- #
        if not abrir:
            return 
        
        # ----- Si la opción del efectivo está seleccionado, se calcula el vuelto generando un mensaje limpiando los campos de texto ----- #
        if self.ui.pedidos.efectivo.isChecked():
            monto = datos.monto_cliente.value()
            vuelto = monto - total
            nombre = (self.ui.pedidos.nombre_cliente.text().capitalize())
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_efectivo(self.ui, nombre, vuelto)
        
        # ----- Si la opción de transferencia está seleccionado, se genera el respectivo mensaje limpiado los campos de texto ----- #
        if self.ui.pedidos.transferencia.isChecked():
            nombre = (self.ui.pedidos.nombre_cliente.text().capitalize())
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_transferencia(self.ui, nombre)