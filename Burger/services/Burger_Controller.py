# ------ Importo las librerías necesarias ------ #
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Burger.views import InicioView, AdminView, MenuView, PedidosView
from Burger.animations.transitions import fade_slide
from Burger.widgets.close_shift import CloseShiftMessage
import re
  
class ControladorMain:
    def __init__(self, views, sistema):
        self.ui = views
        self.sistema = sistema
        
        self.conectar_acciones()
        
    def conectar_acciones(self):
        ui = self.ui
        
        # ------ Conexiones InicioView ------ #
        ui.inicio.ir_admin.connect(lambda: self.cambiar_frame(ui.inicio, ui.admin))
        ui.inicio.iniciar_sesion.connect(self.login_usuario)
        ui.inicio.btn_salir.clicked.connect(self.cerrar_aplicacion)
        
        # ------ Conexiones AdminView ------ #
        ui.admin.volver_menu.connect(lambda: self.cambiar_frame(ui.admin, ui.inicio))
        
        
        # ------ Conexiones MenuView ------ #
        ui.menu.iniciar_pedido.connect(lambda: self.cambiar_frame(ui.menu, ui.pedidos))
        ui.menu.cerrar_turno.connect(self.terminar_turno)
        
        # ------ Conexiones PedidosView ------ #
        ui.pedidos.retroceder.connect(lambda: self.cambiar_frame(ui.pedidos, ui.menu))
    
    def login_usuario(self, usuario, contrasena):
        self.cambiar_frame(self.ui.inicio, self.ui.menu)
        
        
    def cerrar_aplicacion(self):
        try:
            self.sistema.apagar_sistema()
        except:
            pass
        self.ui.close()
    
    def cambiar_frame(self, frame_actual, frame_siguiente):
        self.animaciones = fade_slide(self.ui.stack, frame_actual, frame_siguiente)
        
    def terminar_turno(self):
        confirm = CloseShiftMessage(self.ui)
        if confirm.execute():
            self.cambiar_frame(self.ui.menu, self.ui.inicio)
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