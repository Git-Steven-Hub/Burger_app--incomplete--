# Sistema de la app
# Importo las librerías necesarias
import os
import sqlite3
from datetime import datetime

# Creo la clase principal
class Sistema:
    def __init__(self):
        bbdd_directorio = os.path.dirname(os.path.abspath(__file__))
        self.ruta_db = os.path.join(bbdd_directorio, "burgerdata.db")
        
    def connect(self):
        self.connection = sqlite3.connect(self.ruta_db)
        self.cursor = self.connection.cursor()
        self.create()
        self.admin_creation()
        
    # Creo ambas tablas de ventas y registros
    def create(self):
        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS Ventas (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Encargado TEXT(50),
                    Cliente TEXT(50),
                    Fecha TEXT(50),
                    "Forma de pago" TEXT(50),
                    "Combo S" INTEGER,
                    "Combo D" INTEGER,
                    "Combo T" INTEGER,
                    Postre INTEGER,
                    Total REAL,
                    Vuelto REAL
                    )
                ''')
        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS Registros (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Encargado TEXT(50),
                    Fecha TEXT(50),
                    "Entrada/Salida" TEXT(50),
                    Caja REAL
                )
                ''')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usuarios (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,  
                    Nombre TEXT (50),
                    Contraseña TEXT (50),
                    Rol TEXT (20)
                )
                ''')
        self.connection.commit()
    
    def admin_creation(self):
        self.cursor.execute("SELECT 1 FROM Usuarios WHERE Rol=?", ("admin",))
        
        if not self.cursor.fetchone():
            self.cursor.execute("INSERT INTO Usuarios (Nombre, Contraseña, Rol) VALUES (?, ?, ?)", ("admin", "admin123", "admin"))

            self.connection.commit()

    def insert_new_user(self, nombre, contrasena):
        self.cursor.execute("SELECT 1 FROM Usuarios WHERE Nombre=?", (nombre,))
        
        if self.cursor.fetchone():
            return False
        
        self.cursor.execute("INSERT INTO Usuarios (Nombre, Contraseña, Rol) VALUES (?, ?, ?)", (nombre, contrasena, "Empleado"))
        self.connection.commit()  
        
        return True
          
    def authenticate(self, nombre, contrasena):
        self.cursor.execute("SELECT Rol FROM Usuarios WHERE Nombre=? AND Contraseña=?", (nombre, contrasena))
        return self.cursor.fetchone()
    

        
    # def insert_sales(self):
    #     self.cursor.executemany("INSERT INTO Ventas (ID, Encargado, Cliente, Fecha, Combo_S, Combo_D, Combo_T, Postre, Total) VALUES(NULL,?,?,?,?,?,?,?,?)", [(self.encargado, self.cliente, self.fecha, self.combo1, self.combo2, self.combo3, self.postre, self.total)])
    #     self.connection.commit()
        
    # def insert_register_in(self):
    #     fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    #     self.cursor.executemany("INSERT INTO Registros (ID, Encargado, Fecha, Evento, Caja) VALUES (NULL,?,?,?,?)", [(self.encargado, fecha, "IN", "0")])
    #     self.connection.commit()
    
    # def insert_register_out(self):
    #     fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    #     self.cursor.executemany("INSERT INTO Registros (ID, Encargado, Fecha, Evento, Caja) VALUES (NULL,?,?,?,?)", [(self.encargado, fecha, "OUT", self.ingresos)])
    #     self.connection.commit()
    
    # Creo el menú principal
    def menu(self):  
        pass
    # Creo el método para ingresar un nuevo pedido
    def pedido(self):
        pass
        
        # Creo el método para el cambio de turno
    # def cambio_turno(self):
    #     # Sumo todas las ventas del turno y las registro en el archivo de ventas
    #     self.ingresos = sum(self.variable)
    #     self.insert_register_out()
    #     self.connection.commit()
    #     # Llamo al método constructor para iniciar un nuevo turno
    #     self.__init__()
    
        # Creo el método para apagar el sistema
    def close_system(self):
        # Sumo todas las ventas del turno y las registro en el archivo de ventas
        # self.insert_register_out()
        if hasattr(self, "connection"):
            self.connection.commit()
            self.connection.close()
            


"""
🔐 Extra importante (muy recomendado)

No guardes contraseñas en texto plano.

Cuando avances un poco más:

Usá hashlib o bcrypt

Guardá hashes, no contraseñas reales

Ejemplo simple (más adelante):

import hashlib
hash = hashlib.sha256(password.encode()).hexdigest()

📌 ¿Cuándo sí tendría sentido una tabla Admin aparte?

Solo si:

Los admins tienen muchísimos campos propios

O permisos complejos independientes

Para tu app actual → NO hace falta

"""