# ------ Importo las librerías necesarias ------ #
from Burger.views import InicioView, AdminView, MenuView, PedidosView
from Burger.animations.transitions import fade_slide
from Burger.widgets.close_shift import CloseShiftMessage
from Burger.widgets.auth_dialog import EnterAdmin
from Burger.widgets.datos_pedidos import DatosPedidos
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
        ui.pedidos.retroceder.connect(lambda: self.cambiar_frame(ui.pedidos, ui.menu))
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
        
    def terminar_turno(self):
        confirm = CloseShiftMessage(self.ui)
        if confirm.execute():
            self.cambiar_frame(self.ui.menu, self.ui.inicio)
            
    def tomar_pedido(self):
        pedido = PedidosView(self.ui.pedidos)
        datos_de_pedido = DatosPedidos(self.ui.pedidos, self.ui)
        
        if len(pedido.nombre_cliente.text()) < 3:
            datos_de_pedido.error_nombre()
        

        
        datos_de_pedido.exec()

        
        
""""      
    def tomar_pedido(self, datos):
        if len(datos["Cliente"]) < 3:
            return {"Error" : "El nombre del cliente no es válido."}
        
        if not re.match(r"^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$", datos["Cliente"]):
            return {"Bien" : False, "Error" : "El nombre contiene carácteres invalidos."}
        
        cantidad = {
            "Simple" : datos["Combo1"],
            "Doble" : datos["Combo2"],
            "Triple" : datos["Combo3"],
            "Postre" : datos["Postre"]}
        
        if sum(cantidad.values()) == 0:
            return {"Bien" : False, "Error" : "El pedido no puede estar vacío."}

        precios = {
            "Simple" : 5,
            "Doble" : 6,
            "Triple" : 7,
            "Postre" : 2
        }
        
        total = sum(cantidad[c] * precios[c] for c in cantidad)
        self.total = total
        
        resultado = self.tomar_pedido(datos)
        if resultado["Bien"]:
            self.ui.setup_resumen(self.total)
        
"""        