# window_close_anim.py
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QMainWindow

class WindowCloseAnimator:
    def __init__(self, window: QMainWindow):
        self.window = window

    def animate_close(self):
        self.anim = QPropertyAnimation(self.window, b"windowOpacity")
        self.anim.setDuration(220)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

        def close_now():
            self.window._closing = True
            self.window.close()

        self.anim.finished.connect(close_now)
        self.anim.start()
