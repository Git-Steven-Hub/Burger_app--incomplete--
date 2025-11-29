# Importo las librerías necesarias
import os, sys, warnings, re, ctypes
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Styles import *
from Burger_System import Sistema


class Burger(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ----- Seteo el tamaño de la app para que no sea modificable al uso ----- #
        self.setFixedSize(550, 500)
        
        # ----- Le doy titulo a la app ----- #
        self.setWindowTitle("Burguesía")
        
        # ----- Agrego un icono a la app ----- #
        icono_app = os.path.dirname(__file__)
        self.setWindowIcon(QIcon(os.path.join(icono_app, "icons/icono.png")))
        
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)       
        
        # ----- Index 0 ----- #
        self.inicio = self.setup_inicio()
        self.stack.addWidget(self.inicio)
        
        # ----- Index 1 ----- #
        self.admin = self.setup_admin()
        self.stack.addWidget(self.admin)
        
        # ----- Index 2 ----- #
        self.menu = self.setup_menu()
        self.stack.addWidget(self.menu)

        # ----- Index 3 ----- #
        self.pedidos = self.setup_pedidos()
        self.stack.addWidget(self.pedidos)
        
        # ----- Esto es para que la app tenga icono en la barra de tareas, depués se lo saco ----- #
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("burguer.app.2025")
        
        # ----- Muestro el primer index ----- #
        self.stack.setCurrentIndex(0)

        # ----- Les agrego los estilos ----- #
        self.setStyleSheet(estilos_boton)
        
    def setup_inicio(self):
        # ----- Creo el widget principal ----- #
        self.frame = QWidget()
        root_layout = QVBoxLayout(self.frame)
        
        # ----- Creo los frames para cada opción ----- #
        self.frame_bienvenida = QFrame()
        self.frame_inicio = QFrame()
    
        # ----- Le agrego espacio para cada frame ----- #
        root_layout.addWidget(self.frame_bienvenida, stretch=1)
        root_layout.addWidget(self.frame_inicio, stretch=3)
        
        # ----- Añado el título y le asigno su nombre para el estilo ----- #
        titulo = QLabel("¡BIENVENIDO NUEVAMENTE!\n🍔 LA BURGUESIA 🍔")
        titulo.setObjectName("bienvenida")
        titulo.setAlignment(Qt.AlignCenter)
        QSpacerItem(20, 40)
        
        # ----- Añado el subtitulo y le agrego su estilo ----- #
        subtitulo = QLabel("¡Las mejores burguers!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        # ----- Añado el título y el subtitulo ----- #
        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(titulo)
        self.titulo_layout.addWidget(subtitulo)
        self.frame_bienvenida.setLayout(self.titulo_layout)
        
        # ----- Creo el efecto de opacidad ----- #
        self.efecto = QGraphicsOpacityEffect(self.frame)
        self.frame.setGraphicsEffect(self.efecto)
        self.efecto.setOpacity(0.0)
        
        # ----- Creo la animación ----- #
        self.animacion = QPropertyAnimation(self.efecto, b"opacity")
        self.animacion.setDuration(700)
        self.animacion.setStartValue(0.0)
        self.animacion.setEndValue(1.0)
        self.animacion.setEasingCurve(QEasingCurve.OutCubic)
        
        # ----- Comienzo la animación ----- #
        self.animacion.start()
        
        # ----- Llamo a los botones mostrando el frame ----- #
        self.botones_inicio()
        
        return self.frame
    
    def botones_inicio(self):
        # ----- Seteo el layout del frame del inicio ----- #
        self.frame_inicio_layout = QVBoxLayout(self.frame_inicio)
        
        # ----- Creo el botón de inicio y le asigno nombre ----- #
        self.sesion = QPushButton("Iniciar sesión")
        sesion_icon = os.path.dirname(__file__)
        self.sesion.setIcon(QIcon(os.path.join(sesion_icon, "icons/login.png")))
        self.sesion.setIconSize(QSize(25, 25))
        self.sesion.setObjectName("id1")
        self.sesion.setFixedWidth(380)
        
        # ----- Creo el botón de usuario nuevo y le asigno nombre----- #
        self.usuario_nuevo = QPushButton("Nuevo usuario")
        nuevo_usuario_icon = os.path.dirname(__file__)
        self.usuario_nuevo.setIcon(QIcon(os.path.join(nuevo_usuario_icon, "icons/nuevo usuario.png")))
        self.usuario_nuevo.setIconSize(QSize(25, 25))
        self.usuario_nuevo.setObjectName("id2")
        self.usuario_nuevo.setFixedWidth(380)
        
        # ----- Creo el botón para el administrador ----- #
        self.administrador = QPushButton("Administrador")
        admin_icon = os.path.dirname(__file__)
        self.administrador.setIcon(QIcon(os.path.join(admin_icon, "icons/admin.png")))
        self.administrador.setIconSize(QSize(25, 25))
        self.administrador.setObjectName("boton_admin")
        # ----- Creo el botón de salir y le asigno nombre ----- #
        self.salir = QPushButton("Salir")
        salir_icon = os.path.dirname(__file__)
        self.salir.setIcon(QIcon(os.path.join(salir_icon, "icons/cerrar app.png")))
        self.salir.setIconSize(QSize(25, 25))
        self.salir.setObjectName("id3")
        
        # ----- Creo los QLineEdit para el inicio de sesión ----- #
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.contraseña = QLineEdit()
        self.contraseña.setPlaceholderText("Contraseña")
        self.contraseña.setEchoMode(QLineEdit.Password)
        
        # ----- Creo los QLineEdit para el nuevo usuario ----- #
        self.nuevo_usuario = QLineEdit()
        self.nuevo_usuario.setPlaceholderText("Crear usuario")
        self.nueva_contraseña = QLineEdit()
        self.nueva_contraseña.setPlaceholderText("Crear contraseña")
        
        # ----- Creo el layout para las columnas ----- #
        columnas = QGridLayout()
        columnas.setVerticalSpacing(10)

        # ----- Creo un layout para los botones de "Modificar usuario" y "Salir" ----- #
        columnas2 = QHBoxLayout()
        columnas2.setSpacing(40)
        columnas2.setAlignment(Qt.AlignCenter)

        # ----- Agrego los botones al layout ----- #
        columnas2.addWidget(self.administrador)
        columnas2.addWidget(self.salir)
        
        # ----- Pongo cada botón dándole tamaño con su respectivo QlineEdit en sus columnas ----- #
        columnas.addWidget(self.sesion, 0, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.usuario, 1, 1, alignment=Qt.AlignCenter)
        self.usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.contraseña, 2, 1, alignment=Qt.AlignCenter)
        self.contraseña.setFixedWidth(350)
        self.contraseña.setContentsMargins(0, 0, 0, 5)
        # ----- Separación ----- #
        columnas.addWidget(self.usuario_nuevo, 3, 1, alignment=Qt.AlignCenter)
        columnas.addWidget(self.nuevo_usuario, 4, 1, alignment=Qt.AlignCenter)
        self.nuevo_usuario.setFixedWidth(350)
        # ----- Separación ----- #
        columnas.addWidget(self.nueva_contraseña, 5, 1, alignment=Qt.AlignCenter)
        self.nueva_contraseña.setFixedWidth(350)
        self.nueva_contraseña.setContentsMargins(0, 0, 0, 5)
        
        # ----- Agrego los botones al frame ----- #
        columnas.addLayout(columnas2, 7, 0, 1, 3)
        self.frame_inicio_layout.addLayout(columnas)
        self.frame_inicio_layout.addStretch()
        
        # self.usuario.returnPressed.connect(lambda: self.stack.setCurrentIndex(1)) esto sirve para usar tecla enter en vez del botón
        # self.contraseña.returnPressed.connect(lambda: self.stack.setCurrentIndex(1))
        
    def confirmacion_nuevo_usuario(self):
        pass
          
    def confirmacion_admin(self):
        # ----- Creo la ventana de la confirmación ----- #
        confirmacion = QDialog(self)
        
        # ----- Le doy nombre a la ventana ----- #
        confirmacion.setWindowTitle("Acceso administrador")
        
        # ----- Seteo su tamaño ----- #
        confirmacion.setFixedSize(300, 150)
        
        # ----- Creo el boxvertical ----- #
        layout = QVBoxLayout(confirmacion)
        
        # ----- Le agrego los margenes ----- #
        layout.setContentsMargins(15, 15, 15, 15)
        
        # ----- Creo el LineEdit para que el admin ponga su usuario ----- #
        admin = QLineEdit()
        admin.setPlaceholderText("Usuario")
        
        # ----- Creo el LineEdit para la contraseña del admin ocultando lo escrito ----- #
        admin_pass = QLineEdit()
        admin_pass.setPlaceholderText("Contraseña")
        admin_pass.setEchoMode(QLineEdit.Password)

        # ----- Seteo los botones para aceptar y cancelar la confirmación ----- #
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(confirmacion.accept)
        botones.rejected.connect(confirmacion.reject)
        
        # ----- Agregro todo al layout ----- #
        layout.addWidget(admin)
        layout.addWidget(admin_pass)
        layout.addWidget(botones)
        
        # ----- Creo la acción que rechaza si está mal la contraseña o el usuario ----- #
        if confirmacion.exec() == QDialog.Accepted:
            if admin.text() == "admin" and admin_pass.text() == "admin123":
                self.ir_frame(self.stack.currentWidget(), self.admin)
            else:
                QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
        
    def setup_admin(self):
        # ----- Creo el widget principal ----- #
        frame = QWidget()
        root_layout = QVBoxLayout(frame)

        # ----- Creo el widget principal ----- #
        self.frame_titulo_admin = QFrame()
        self.frame_opciones_admin = QFrame()
        
        # ----- Le agrego espacio para cada frame ----- #
        root_layout.addWidget(self.frame_titulo_admin, stretch=1)
        root_layout.addWidget(self.frame_opciones_admin, stretch=3)
        self.frame_opciones_admin.setStyleSheet("QFrame { background-color: transparent; }")
        
        # ----- Añado el título y le asigno su nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        
        # ----- Añado el subtitulo y le asigno su nombre para el estilo ----- #
        subtitulo = QLabel("¡Administrador!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        # ----- Añado todo al layout ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo_admin.setLayout(titulo_layout)
        
        # ----- Llamo los botones del admin mostrando el frame ----- #
        self.botones_admin()
        
        return frame

    def botones_admin(self):
        self.frame_botones_administrador = QVBoxLayout(self.frame_opciones_admin)

        grupo_usuarios = QGroupBox("Usuarios")
        layout_usuarios = QGridLayout()
        layout_usuarios.setContentsMargins(10, 25, 10, 10)

        
        self.crear = QPushButton("Crear usuario")
        crear_icon = os.path.dirname(__file__)
        self.crear.setIcon(QIcon(os.path.join(crear_icon, "icons/nuevo usuario.png")))
        self.crear.setIconSize(QSize(23, 23))
        self.crear.setObjectName("id2")
        self.crear.setFixedWidth(180)
        
        self.modificar = QPushButton("Modificar usuario")
        modificar_icon = os.path.dirname(__file__)
        self.modificar.setIcon(QIcon(os.path.join(modificar_icon, "icons/editar usuario.png")))
        self.modificar.setIconSize(QSize(23, 23))
        self.modificar.setObjectName("id5")
        self.modificar.setFixedWidth(180)
        
        self.eliminar = QPushButton("Eliminar usuario")
        eliminar_icon = os.path.dirname(__file__)
        self.eliminar.setIcon(QIcon(os.path.join(eliminar_icon, "icons/eliminar usuario.png")))
        self.eliminar.setIconSize(QSize(23, 23))
        self.eliminar.setFixedWidth(180)
        
        self.editar_admin = QPushButton("Modificar Admin")
        editar_admin_icon = os.path.dirname(__file__)
        self.editar_admin.setIcon(QIcon(os.path.join(editar_admin_icon, "icons/modificar admin.png")))
        self.editar_admin.setIconSize(QSize(23, 23))
        self.editar_admin.setObjectName("id5")
        self.editar_admin.setFixedWidth(180)
        
        layout_usuarios.addWidget(self.crear, 0, 0, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.modificar, 1, 0, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.eliminar, 0, 1, alignment=Qt.AlignCenter)
        layout_usuarios.addWidget(self.editar_admin, 1, 1, alignment=Qt.AlignCenter)
        layout_usuarios.setVerticalSpacing(10)
        
        grupo_usuarios.setLayout(layout_usuarios)
        
        grupo_sistema = QGroupBox("Sistema")
        layout_sistema = QGridLayout()
        layout_sistema.setContentsMargins(10, 25, 10, 10)
        
        self.registros = QPushButton("Ver registros")
        registros_icon = os.path.dirname(__file__)
        self.registros.setIcon(QIcon(os.path.join(registros_icon, "icons/registros.png")))
        self.registros.setIconSize(QSize(23, 23))
        self.registros.setObjectName("id4")
        self.registros.setFixedWidth(180)
        
        self.respaldo = QPushButton("Respaldo")
        respaldo_icon = os.path.dirname(__file__)
        self.respaldo.setIcon(QIcon(os.path.join(respaldo_icon, "icons/backup.png")))
        self.respaldo.setIconSize(QSize(23, 23))
        self.respaldo.setObjectName("id6")
        self.respaldo.setFixedWidth(180)
        
        self.volver = QPushButton("Volver al menú")
        volver_icon = os.path.dirname(__file__)
        self.volver.setIcon(QIcon(os.path.join(volver_icon, "icons/retroceder.png")))
        self.volver.setIconSize(QSize(23, 23))
        self.volver.setObjectName("id3")
        self.volver.setFixedWidth(180)
        
    
        layout_sistema.addWidget(self.registros, 0, 0, alignment=Qt.AlignCenter)
        layout_sistema.addWidget(self.respaldo, 0, 1, alignment=Qt.AlignCenter)
        layout_sistema.addWidget(self.volver, 1, 0, 1, 2,alignment=Qt.AlignCenter)
        layout_sistema.setVerticalSpacing(15)
        
        grupo_sistema.setLayout(layout_sistema)
        
        self.frame_botones_administrador.addWidget(grupo_usuarios)
        self.frame_botones_administrador.addWidget(grupo_sistema)
        self.frame_botones_administrador.addStretch()
        
        self.volver.clicked.connect(lambda: self.ir_frame(self.stack.currentWidget(), self.inicio))
        
    def ir_frame(self, frame_actual, frame_siguiente):
        # ----- Guardo la geometría original -----
        geo = self.stack.geometry()
        ancho = geo.width()

        # --- CCreo efectos nuevos ---
        eff_out = QGraphicsOpacityEffect()
        eff_in = QGraphicsOpacityEffect()

        frame_actual.setGraphicsEffect(eff_out)
        frame_siguiente.setGraphicsEffect(eff_in)

        eff_out.setOpacity(1)
        eff_in.setOpacity(0)

        # --- Animación fade out ---
        fade_out = QPropertyAnimation(eff_out, b"opacity")
        fade_out.setDuration(350)
        fade_out.setStartValue(1)
        fade_out.setEndValue(0)

        # --- Animación fade in ---
        fade_in = QPropertyAnimation(eff_in, b"opacity")
        fade_in.setDuration(350)
        fade_in.setStartValue(0)
        fade_in.setEndValue(1)

        # --- Slide out ---
        slide_out = QPropertyAnimation(frame_actual, b"geometry")
        slide_out.setDuration(350)
        slide_out.setStartValue(geo)
        slide_out.setEndValue(QRect(-ancho, geo.y(), ancho, geo.height()))

        # --- Slide in ---
        slide_in = QPropertyAnimation(frame_siguiente, b"geometry")
        slide_in.setDuration(350)
        slide_in.setStartValue(QRect(ancho, geo.y(), ancho, geo.height()))
        slide_in.setEndValue(geo)

        # --- Seteo los grupos ---
        group_out = QParallelAnimationGroup()
        group_out.addAnimation(fade_out)
        group_out.addAnimation(slide_out)

        group_in = QParallelAnimationGroup()
        group_in.addAnimation(fade_in)
        group_in.addAnimation(slide_in)

        # --- Función para evitar errores ---
        def cambiar_frame():
            self.stack.setCurrentWidget(frame_siguiente)
            
            # ----- Aseguro que el efecto siga existiendo ----- #
            frame_siguiente.setGraphicsEffect(eff_in)
            group_in.start()

        group_out.finished.connect(cambiar_frame)

        # ----- Guardo las referncias para evitar futuros problemas ----- #
        self.animaciones = [eff_out, eff_in, fade_out, fade_in, group_out, group_in]

        group_out.start()
    
    def setup_menu(self):
        # ----- Creo el widget principal ----- #
        frame = QWidget()
        root_layout = QVBoxLayout(frame)
        
        # ----- Creo el widget principal ----- #
        self.frame_titulo_menu = QFrame()
        self.frame_opciones_menu = QFrame()
        
        # ----- Creo el widget principal ----- #
        root_layout.addWidget(self.frame_titulo_menu, stretch=1)
        root_layout.addWidget(self.frame_opciones_menu, stretch=3)
        
        # ----- Añado el título y le asigno su nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        
        # ----- Añado el subtitulo y le asigno su nombre para el estilo ----- #
        subtitulo = QLabel("¡Menu encargados!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setContentsMargins(0, 0, 0, 10)
        
        # ----- Añado todo al layout ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo_menu.setLayout(titulo_layout)
        
        # ----- Llamo a los botones mostrando el frame ----- #
        self.botones_menu()
        
        return frame
        
    def botones_menu(self):
        self.frame_botones_menu = QVBoxLayout(self.frame_opciones_menu)
        
        self.iniciar_pedido = QPushButton("Iniciar pedido")
        pedido_icon = os.path.dirname(__file__)
        self.iniciar_pedido.setIcon(QIcon(os.path.join(pedido_icon, "icons/combo.png")))
        self.iniciar_pedido.setIconSize(QSize(25, 25))    
        self.iniciar_pedido.setObjectName("id1")
        self.iniciar_pedido.setFixedWidth(380)
        
        self.estado_turno = QPushButton("Ver resumen del día")
        resumen_icon = os.path.dirname(__file__)
        self.estado_turno.setIcon(QIcon(os.path.join(resumen_icon, "icons/resumen.png")))
        self.estado_turno.setIconSize(QSize(25, 25))        
        self.estado_turno.setObjectName("id4")
        self.estado_turno.setFixedWidth(380)
        
        self.historial_turno = QPushButton("Ver tu historial de turnos")
        turnos_icon = os.path.dirname(__file__)
        self.historial_turno.setIcon(QIcon(os.path.join(turnos_icon, "icons/turnos.png")))
        self.historial_turno.setIconSize(QSize(25, 25))
        self.historial_turno.setFixedWidth(380)
        
        self.cambiar_contraseña = QPushButton("Cambiar contraseña")
        cambiar_contraseña_icon = os.path.dirname(__file__)
        self.cambiar_contraseña.setIcon(QIcon(os.path.join(cambiar_contraseña_icon, "icons/password.png")))
        self.cambiar_contraseña.setIconSize(QSize(25, 25))
        self.cambiar_contraseña.setObjectName("id5")
        self.cambiar_contraseña.setFixedWidth(380)
        
        self.terminar_turno = QPushButton("Cerrar turno")
        terminar_turno_icon = os.path.dirname(__file__)
        self.terminar_turno.setIcon(QIcon(os.path.join(terminar_turno_icon, "icons/salir.png")))
        self.terminar_turno.setIconSize(QSize(25, 25))
        self.terminar_turno.setObjectName("id3")
        self.terminar_turno.setFixedWidth(380)

        columnas = QGridLayout()
        
        columnas.addWidget(self.iniciar_pedido, 0, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.estado_turno, 1, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.historial_turno, 2, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.cambiar_contraseña, 3, 0, alignment=Qt.AlignCenter)
        columnas.addWidget(self.terminar_turno, 4, 0, alignment=Qt.AlignCenter)
        
        self.frame_botones_menu.addLayout(columnas)
        
    def acciones_menu(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Cerrar turno")
        mensaje.setText("¿Estás seguro que quiere cerrar el turno?")
        mensaje.setIcon(QMessageBox.Warning)
        
        mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mensaje.setDefaultButton(QMessageBox.No)
        
        efecto = QGraphicsDropShadowEffect()
        efecto.setBlurRadius(0)
        efecto.setOffset(0, 0)
        efecto.setColor(Qt.black)
        
        mensaje.setGraphicsEffect(efecto)
        
        if mensaje.exec() == QMessageBox.Yes:
            self.ir_frame(self.stack.currentWidget(), self.inicio)
        
    def setup_pedidos(self):
        # ----- Creo el layout vertical ----- #
        frame = QWidget()
        root_layout = QVBoxLayout(frame)
        
        # ----- Creo los frames para cada opción ----- #
        self.frame_titulo = QFrame()
        self.frame_opciones = QFrame()
        
        # ----- Les agrego espacio a cada frame ----- #
        root_layout.addWidget(self.frame_titulo, stretch=1)
        root_layout.addWidget(self.frame_opciones, stretch=3)
        
        # ----- Creo el título y le asigno un nombre para el estilo ----- #
        titulo = QLabel("🍔LA BURGUESIA🍔")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        subtitulo = QLabel("¡PEDIDOS!")
        subtitulo.setObjectName("subtitulo")
        subtitulo.setAlignment(Qt.AlignCenter)
        
        # ----- Agrego el titulo ----- #
        titulo_layout = QVBoxLayout()
        titulo_layout.addWidget(titulo)
        titulo_layout.addWidget(subtitulo)
        self.frame_titulo.setLayout(titulo_layout)
        
        self.botones_pedidos()
        
        return frame
        
    def botones_pedidos(self):
        # ----- Layout principal del frame_opciones ----- #
        self.frame_opciones_layout = QVBoxLayout(self.frame_opciones)

        # ----- Validador para cantidades ----- #
        self.validador = QIntValidator(0, 100)

        # ----- Campos de entrada ----- #
        self.nombre_cliente = QLineEdit()
        self.nombre_cliente.setPlaceholderText("Nombre")
        
        self.combo_simple = QLineEdit()
        self.combo_doble = QLineEdit()
        self.combo_triple = QLineEdit()
        self.postre_flan = QLineEdit()
        
        self.inputs = [self.combo_simple, self.combo_doble, self.combo_triple, self.postre_flan]
        for i in self.inputs:
            i.setValidator(self.validador)
            i.setPlaceholderText("Cantidad")

        # ----- Labels ----- #
        texto_nombre = QLabel("Nombre del cliente")
        texto_nombre.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        texto_pago = QLabel("Forma de pago")
        texto_pago.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        texto_simple = QLabel("Cantidad de combo Simple 🍔 (Costo $5):")
        texto_doble = QLabel("Cantidad de combo Doble 🍔 (Costo $6):")
        texto_triple = QLabel("Cantidad de combo Triple 🍔 (Costo $7):")
        texto_postre = QLabel("Cantidad de postre Flan 🍮 (Costo $2):")
        textos = [texto_simple, texto_doble, texto_triple, texto_postre]
        for i in textos:
            i.setStyleSheet("font-weight: bold; font-size: 14px;")

        # ----- Forma de pago ----- #
        self.efectivo = QRadioButton("Efectivo")
        self.efectivo.setFixedSize(80, 30)
        self.transferencia = QRadioButton("Transferencia")
        self.transferencia.setFixedSize(100, 30)
        self.efectivo.setChecked(True)
     
        pago_layout = QHBoxLayout()
        pago_layout.setSpacing(10)
        pago_layout.addWidget(self.efectivo)
        pago_layout.addWidget(self.transferencia)
        pago_layout.addStretch()  # Para que no quede demasiado pegado

        # ----- QGridLayout para el formulario ----- #
        grid = QGridLayout()
        grid.setVerticalSpacing(15)
        grid.setHorizontalSpacing(10)

        # Agregamos cada label y campo
        grid.addWidget(texto_nombre, 0, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.nombre_cliente, 0, 1)

        grid.addWidget(texto_pago, 1, 0, alignment=Qt.AlignCenter | Qt.AlignTop)
        grid.addLayout(pago_layout, 1, 1)

        grid.addWidget(texto_simple, 2, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_simple, 2, 1)

        grid.addWidget(texto_doble, 3, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_doble, 3, 1)

        grid.addWidget(texto_triple, 4, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.combo_triple, 4, 1)

        grid.addWidget(texto_postre, 5, 0, alignment=Qt.AlignRight)
        grid.addWidget(self.postre_flan, 5, 1)

        # ----- Botones ----- #
        self.boton_atras = QPushButton("Retroceder")
        boton_atras_icon = os.path.dirname(__file__)
        self.boton_atras.setIcon(QIcon(os.path.join(boton_atras_icon, "icons/retroceder.png")))
        self.boton_atras.setIconSize(QSize(25, 25))
        
        self.boton_confirmar = QPushButton("Confirmar")
        boton_confirmar_icon = os.path.dirname(__file__)
        self.boton_confirmar.setIcon(QIcon(os.path.join(boton_confirmar_icon, "icons/aceptar.png")))
        self.boton_confirmar.setIconSize(QSize(25, 25))
        self.boton_confirmar.setObjectName("id1")

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_atras)
        botones_layout.addWidget(self.boton_confirmar)

        # ----- Agregamos todo al layout principal ----- #
        self.frame_opciones_layout.addLayout(grid)
        self.frame_opciones_layout.addSpacing(20)
        self.frame_opciones_layout.addLayout(botones_layout)
        self.frame_opciones_layout.addStretch()

        # ----- Focus ----- #
        self.nombre_cliente.returnPressed.connect(lambda: self.combo_simple.setFocus())
        self.combo_simple.returnPressed.connect(lambda: self.combo_doble.setFocus())
        self.combo_doble.returnPressed.connect(lambda: self.combo_triple.setFocus())
        self.combo_triple.returnPressed.connect(lambda: self.postre_flan.setFocus())
        self.postre_flan.returnPressed.connect(self.boton_confirmar.click)
        
    def limpiar_campos(self):
        self.nombre_cliente.clear()
        self.combo_simple.clear()
        self.combo_doble.clear()
        self.combo_triple.clear()
        self.postre_flan.clear() 
        self.efectivo.setChecked(True)
    
    def setup_resumen(self, total):
        dialog = QDialog(self)
        dialog.setWindowTitle("Confirmar el pedido")
        dialog.setFixedSize(350, 300)
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(15, 15, 15, 15)
        
        datos = {
            "Cliente" : self.nombre_cliente.text().capitalize(),
            "Combo1" : self.combo_simple.text(),
            "Combo2" : self.combo_doble.text(),
            "Combo3" : self.combo_triple.text(),
            "Postre" : self.postre_flan.text(),
            "Pago" : "Efectivo." if self.efectivo.isChecked() else "Transferencia."
        }
        
        self.monto_cliente = QLineEdit()
        self.monto_cliente.setPlaceholderText("Monto del pago")
        self.monto_cliente.setValidator(QDoubleValidator(0.0, 99999.0, 2))
        self.monto_cliente.setFixedWidth(120)
        
        resumen = QLabel(f"""
                        <b>Cliente:</b> {self.nombre_cliente}<br><br>
                        <b>Pedido:</b><br>
                        • Combo Simple: {self.combo_simple}<br>
                        • Combo Doble: {self.combo_doble}<br>
                        • Combo Triple: {self.combo_triple}<br>
                        • Flan: {self.postre_flan}<br>
                        <b>Pago:</b> {datos["Pago"]}<br>
                        <b>Total:</b> ${total}<br>
                         """)
        
        
        
        resultado = self.sistema.tomar_pedido(datos)
        
        if not resultado["Bien"]:
            QMessageBox.warning(self, "Error", resultado["Error"])
            return

    def cobro_pedido(self):
        datos = {
            "cliente" : self.nombre_cliente.text().capitalize(),
            "combo1" : self.combo_simple.text(),
            "combo2" : self.combo_doble.text(),
            "combo3" : self.combo_triple.text(),
            "postre" : self.postre_flan.text(),
            "pago" : "Efectivo" if self.efectivo.isChecked() else "Transferencia",
            "total" : {self.total},
        }
        pedido_resumen = f""" Pedido de {datos["cliente"]}:<br>
        - Cantidad de combo simple: {datos['combo1']}<br>
        - Cantidad de combo doble: {datos['combo2']}<br>
        - Cantidad de combo triple: {datos['combo3']}<br>
        - Cantidad de postre flan: {datos['postre']}<br>
        - Forma de pago: {datos['pago']}<br>
        - Total a pagar: {self.total}</br>
        """
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Resúmen pedido")
        mensaje.setText("<b>¿El pedido está correcto? Después no se podrá modificar.</b>")
        mensaje.setTextFormat(Qt.RichText)
        mensaje.setInformativeText(pedido_resumen)
        mensaje.setIcon(QMessageBox.Question)
        mensaje.setObjectName("mensaje_confirmacion")
        
        mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mensaje.setDefaultButton(QMessageBox.No)
        
        efecto = QGraphicsDropShadowEffect()
        efecto.setBlurRadius(20)
        efecto.setOffset(3, 3)
        efecto.setColor(Qt.black)
        
        mensaje.setGraphicsEffect(efecto)
        
        if mensaje.exec() == QMessageBox.Yes:
            self.cobro_pedido()
            self.limpiar_campos()
        
        
        
        mensaje = QDialog(self)
        mensaje.setWindowTitle("Cobro")
        mensaje.setFixedSize(400, 400)
        
        validador = QIntValidator(0, 9999999)
        
        layout = QVBoxLayout(mensaje)
        layout.setContentsMargins(15, 15, 15, 15)
        texto_monto = QLabel(f"Total: {self.total}")
        texto_cobro = QLabel("Monto entregado: ")
        monto_entregado = QLineEdit()
        
        monto_entregado.setValidator(validador)