general = """
        QWidget {
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 mediumaquamarine,
                stop:1 paleturquoise);
        }
        #frame_titulo{
            border-radius: 30px;
        }
        #frame_decorado {
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:0, y2:1,
            stop:0 #fff8e6,
            stop:1 #ffffff
            );
        border-radius: 20px;
            border: 1.5px solid black;
        }
        QLabel {
            background-color: transparent;
            color: black;
            font-family: Poppins;
            font-size: 16px;
        }
        #label_cliente {
            font-size: 20px; 
            font-weight: bold;
        }
        #label_pago {
            font-size: 20px; 
            font-weight: bold;
        }
        #labels_pedidos {
            font-weight: bold; 
            font-size: 14px;
        }
        #bienvenida {
            background-color: transparent;
            color: white;
            font-family: Poppins, Vedana, Arial;
            font-size: 32px;
            font-weight: 900;
        }
        #titulo {
            font-family: Ink Free, Cascadia Mono;
            font-size: 50px;
            font-weight: bold;
            padding: 8px 8px;
        }
        #subtitulo {
            font-size: 18px;
            font-family: Poppins;
            color: #555;
        }
        #encargado {
            font-size: 14px;
            font-style: italic;
            color: dimgray;
            background-color: #dcdcdc;
            border-radius: 6px;
            padding: 4px 8px;   
        }
        QLineEdit {
            border: 1.5px solid mediumaquamarine;
            border-radius: 6px;
            padding: 6px 8px;
            min-height: 20px;
            font-size: 14px;
            color: black;
            background-color: honeydew;
        }
        QLineEdit:focus {
            border: 2px solid darkgreen;
            background-color: #eaffea;
            color: black;
        }
        QLineEdit::placeholder {
            color: gray;
            font-style: italic;
        }
        QGroupBox {
            QFrame {
                background-color: transparent;
                }
            font-weight: bold;
            font-size: 12px;
            border: 2px solid black;
            border-radius: 8px;
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:0, y2:1,
                stop:0 #fff8e6,
                stop:1 #ffffff
            );
            color: black;
            }
        QGroupBox:title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }
"""
estilos_boton = general + """
        QPushButton {
            background-color: dimgray;
            border: 2px solid gray;
            color: white;
            border-radius: 10px;
            padding: 8px;
            font-family: Poppins;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: gray;
            border: 2px;
        }
        QPushButton:pressed {
            background-color: darkgray;
        }
        #id1 {
            background-color: mediumseagreen;
            border: 2px solid forestgreen;
        }
        #id1:hover {
            background-color: seagreen;
            border-color: seagreen;
        }
        #id1:pressed {
            background-color: darkgreen;
        }
        #id2 {
            background-color: dodgerblue;
            border: 2px solid royalblue;
        }
        #id2:hover {
            background-color: royalblue;
            border-color: royalblue;
        }
        #id2:pressed {
            background-color: midnightblue;
        }
        #id3 {
            background-color: indianred;
            border: 2px solid crimson;
        }
        #id3:hover {
            background-color: crimson;
            border-color: crimson;
        }
        #id3:pressed {
            background-color: darkred;
        }
        #id4 {
            background-color: mediumpurple;
            border: 2px solid darkorchid;
        }
        #id4:hover {
            background-color: darkorchid;
            border-color: darkorchid;
        }
        #id4:pressed {
            background-color: indigo;
        }
        #id5 {
            background-color: coral;
            border: 2px solid darkorange;
        }
        #id5:hover {
            background-color: darkorange;
            border-color: darkorange;
        }
        #id5:pressed {
            background-color: orangered;
        }
        #id6 {
            background-color: #EDD513;
            border: 2px solid #D9C211;
        }
        #id6:hover {
            background-color: #D9C211;
            border-color: #D9C211;
        }
        #id6:pressed {
            background-color: #BDAB0F;
        }
        
        #boton_admin {
            background-color: teal;
            border: 2px solid lightseagreen;
        }
        #boton_admin:hover {
            background-color: darkcyan;
            border-color: darkcyan;
        }
        #boton_admin:pressed {
            background-color: #004d4d;
        }
        QMessageBox {
            background-color: mediumaquamarine;
            border-radius: 12px;
        }
        QMessageBox * {
            background-color: transparent;
        }
        QMessageBox QLabel#qt_msgbox_label {
            font-weight: bold;
            font-size: 18px;
        }
        QMessageBox QLabel {
            color: black;
            font-size: 16px;
            font-family: Poppins;
        }

        QMessageBox QPushButton {
            background-color: mediumseagreen;
            border: 2px solid forestgreen;
            border-radius: 8px;
            padding: 6px 12px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color: seagreen;
        }
        QMessageBox QPushButton:pressed {
            background-color: darkgreen;
        }
        QRadioButton {
            font-size: 14px;
            color: black;
            background: transparent;
        }
        QRadioButton::indicator {
            width: 11px;
            height: 11px;
            border-radius: 7px;
            border: 2px solid mediumaquamarine;
            background: mintcream;
        }
        QRadioButton::indicator:hover {
            border: 2px solid darkgreen;
        }
        QRadioButton::indicator:checked {
            background: mediumseagreen;
            border: 2px solid forestgreen;
        }
"""
#Candara
#Cascadia Mono
#Ink Free