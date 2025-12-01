"""Paquete de servicios para la app Burger.

Contiene lógica de acceso a datos y controladores.
"""

from .Burger_Controller import ControladorMain
from .Burger_System import Sistema

__all__ = ["Burger_System", "Burger_Controller"]
