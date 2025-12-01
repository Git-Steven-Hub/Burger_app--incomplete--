# Importo las librerías necesarias
import sys, os, warnings
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo

# Usar imports explícitos del paquete `Burger`.
# Recomendado: ejecutar con `python -m Burger.Main` desde el directorio padre.
from Burger.views import InicioView, AdminView, MenuView, PedidosView
from Burger.styles.Styles import estilos_boton
from Burger.services.Burger_System import Sistema
from Burger.services.Burger_Controller import ControladorMain

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons/icono.png")))
    
    burger_sistema = Sistema()
    burger_sistema.connect()
    
    burger_ui = InicioView()
    controlador = ControladorMain(burger_ui, burger_sistema)
    
    app.setStyleSheet(estilos_boton)
    burger_ui.show()
    
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    translator = QTranslator()
    translator.load(
        QLocale.system(),
        "qtbase",
        "_", 
        QLibraryInfo.location(QLibraryInfo.TranslationsPath),
    )
    app.installTranslator(translator)
    
    sys.exit(app.exec())