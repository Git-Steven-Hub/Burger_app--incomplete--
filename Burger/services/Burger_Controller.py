# ------ Importo las librerías necesarias ------ #
from Burger.views import InicioView, AdminView, MenuView, PedidosView
from Burger.animations.transitions import fade_slide
from Burger.widgets.close_shift import CloseShiftMessage
from Burger.widgets.auth_dialog import EnterAdmin
from Burger.widgets.datos_pedidos import DatosPedidos
from Burger.widgets.messages import Messages
import re

# ------ Creo la clase controladora (lógica) ------ #
class ControladorMain:
    # ------ Creo el init tomando las vistas y el sistema ------ #
    def __init__(self, views, sistema):
        # ------ Defino el ui y el sistema (además creo un bloqueador de animación para evitar bugs visuales) ------ #
        self.ui = views
        self.sistema = sistema
        self.animado = False
        
        # ------ Llamo a las acciones ------ #
        self.conectar_acciones()
        
    def conectar_acciones(self):
        ui = self.ui
        
        # ------ Conexiones InicioView ------ #
        ui.inicio.ir_admin.connect(self.confirmar_admin)
        ui.inicio.iniciar_sesion.connect(self.login_usuario)
        ui.inicio.btn_salir.clicked.connect(self.cerrar_aplicacion)
        
        # ------ Conexiones AdminView ------ #
        ui.admin.volver_menu.connect(lambda: self.cambiar_frame(ui.admin, ui.inicio))
        
        
        # ------ Conexiones MenuView ------ #
        ui.menu.iniciar_pedido.connect(lambda: self.cambiar_frame(ui.menu, ui.pedidos))
        ui.menu.cerrar_turno.connect(self.terminar_turno)
        
        # ------ Conexiones PedidosView ------ #
        ui.pedidos.retroceder.connect(self.volver_menu)
        ui.pedidos.confirmar_pedido.connect(self.tomar_pedido)
    
    def login_usuario(self, usuario, contrasena):
        self.cambiar_frame(self.ui.inicio, self.ui.menu)
        
    def confirmar_admin(self):
        dialogo = EnterAdmin(self.ui)

        if dialogo.exec():
            if dialogo.admin_user.text() == "admin" and dialogo.admin_pass.text() == "admin123":
                self.cambiar_frame(self.ui.inicio, self.ui.admin)
            else:
                dialogo.out()
    
    def cerrar_aplicacion(self):
        try:
            self.sistema.apagar_sistema()
        except:
            pass
        self.ui.close()
    
    def cambiar_frame(self, frame_actual, frame_siguiente):
        if self.animado:
            return
        
        self.animado = True
        
        grupo = fade_slide(self.ui.stack, frame_actual, frame_siguiente)
        
        if grupo:
            grupo.finished.connect(lambda: self._animacion_finalizada())
            
    def _animacion_finalizada(self):
        self.animado = False
    
    def volver_menu(self):
        self.cambiar_frame(self.ui.pedidos, self.ui.menu)
        self.ui.pedidos.clean()
        
    def terminar_turno(self):
        confirm = CloseShiftMessage(self.ui)
        if confirm.execute():
            self.cambiar_frame(self.ui.menu, self.ui.inicio)
            
    def tomar_pedido(self):
        
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
            
        if self.ui.pedidos.efectivo.isChecked():
            monto = datos.monto_cliente.value()
            vuelto = monto - total
            nombre = (self.ui.pedidos.nombre_cliente.text().capitalize())
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_efectivo(self.ui, nombre, vuelto)
        
        if self.ui.pedidos.transferencia.isChecked():
            nombre = (self.ui.pedidos.nombre_cliente.text().capitalize())
            self.ui.pedidos.clean()
            Messages.pedido_finalizado_transferencia(self.ui, nombre)