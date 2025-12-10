import os
from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QPainter, QPixmap, QPainterPath, QPen
from PySide6.QtCore import Qt

class BackgroundFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background_path = os.path.join(os.path.dirname(__file__), "../resources/wallpapers/background.jpg")
        self.pixmap = QPixmap(self.background_path)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        rect = self.rect()
        
        path = QPainterPath()
        path.addRoundedRect(rect, 30, 30)
        painter.setClipPath(path)
        
        painter.drawTiledPixmap(rect, self.pixmap)
        
        painter.setPen(QPen(Qt.black, 3.5))
        painter.drawPath(path)