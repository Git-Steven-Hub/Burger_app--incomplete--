from Burger.resources.styles.all import general

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
            padding-top: 6px;
            padding-bottom: 10px;
            background-color: gray;
            border: 1px solid rgba(255,255,255,0.35);
        }
        QPushButton:pressed {
            background-color: darkgray;
            padding-top: 10px;
            padding-bottom: 6px;
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
        QMessageBox QPushButton {
            background-color: mediumseagreen;
            border: 2px solid forestgreen;
            border-radius: 4px;
            padding: 6px 12px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color: seagreen;
            border-color: seagreen;
            padding-top: 4px;
            padding-bottom: 8px;
        }
        QMessageBox QPushButton:pressed {
            background-color: darkgreen;
            padding-top: 8px;
            padding-bottom: 4px;
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