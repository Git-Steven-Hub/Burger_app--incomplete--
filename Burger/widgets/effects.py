from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

class ShadowedLabel:
    def __init__(self, blur_radius=15, offset=(2, 2), color=(0, 0, 0, 180)):
        self.blur_radius = blur_radius
        self.offset = offset
        self.color = QColor(*color)
        
    def apply(self, widget: QLabel):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(self.blur_radius)
        shadow.setOffset(*self.offset)
        shadow.setColor(self.color)
        widget.setGraphicsEffect(shadow)
        self.shadow = shadow

def remove_shadow(widget: QLabel):
    widget.setGraphicsEffect(None)

def apply_shadow_label(labels, blur_radius=15, offset=(2, 2), color=(0, 0, 0, 180)):
    shadows = []
    for label in labels:
        s = ShadowedLabel(blur_radius, offset, color)
        s.apply(label)
        shadows.append(s)
    return shadows
