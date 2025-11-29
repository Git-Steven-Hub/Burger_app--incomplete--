# Importo las librerías necesarias
import sys, os, warnings
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Burger_UI import Burger
from Burger_System import Sistema
from Burger_Controller import ControladorMain

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons/icono.png")))
    
    burger_sistema = Sistema()
    burger_sistema.connect()
    
    burger_ui = Burger()
    controlador = ControladorMain(burger_ui, burger_sistema)
    
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