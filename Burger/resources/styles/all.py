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
        #titulo {
            font-family: Ink Free;
            font-size: 28px;
            font-weight: bold;
            color: black;
            padding: 12px 18px;
            border-radius: 16px;
            background-color: rgba(255, 255, 255, 0.65);
            border: 2px solid rgba(0, 0, 0, 0.12);
        }
        #subtitulo {
            font-size: 18px;
            font-family: Poppins;
            color: black;
            padding: 6px 12px;
            border-radius: 12px;
            background-color: rgba(255, 255, 255, 0.45);
            border: 1px solid rgba(0, 0, 0, 0.10);
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
"""