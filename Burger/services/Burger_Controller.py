from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Burger_UI import *
from Burger_System import *
import re

class ControladorMain:
    def __init__(self, ui, sistema):
        self.ui = ui
        self.sistema = sistema
        
        self.conectar_acciones()
        
    def conectar_acciones(self):
        vista = self.ui
        #------ login ------#
        vista.salir.clicked.connect(self.cerrar_aplicacion)
        vista.sesion.clicked.connect(lambda: self.cambiar_frame(vista.stack.currentWidget(), vista.menu))
        
        # vista.usuario_nuevo.clicked.connect()
        
        vista.administrador.clicked.connect(vista.confirmacion_admin)
        #------ admin ------#
        vista.volver.clicked.connect(lambda: self.cambiar_frame(vista.stack.currentWidget(), vista.inicio))
        #------ encargados ------#
        vista.iniciar_pedido.clicked.connect(lambda: self.cambiar_frame(vista.stack.currentWidget(), vista.pedidos))
        vista.terminar_turno.clicked.connect(vista.acciones_menu)
        #------ pedidos ------#
        vista.boton_atras.clicked.connect(lambda: (self.cambiar_frame(vista.stack.currentWidget(), vista.menu), 
                                                   vista.limpiar_campos() if hasattr(vista, "limpiar_campos") else None
                                                ))
        vista.boton_confirmar.clicked.connect(vista.setup_resumen)
        vista.boton_confirmar.clicked.connect(self.tomar_pedido)
        
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
        
        
        
    def cerrar_aplicacion(self):
        try:
            self.sistema.apagar_sistema()
        except:
            pass
        self.ui.close()
    
    def cambiar_frame(self, frame_actual, frame_siguiente):
        self.ui.ir_frame(frame_actual, frame_siguiente)