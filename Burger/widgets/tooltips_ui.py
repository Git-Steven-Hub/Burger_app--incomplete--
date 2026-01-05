from PySide6.QtWidgets import QToolTip
from PySide6.QtCore import QPoint

def show_tooltip(widget, text, offset=QPoint(4, 10), timeout=1500):
    pos = widget.mapToGlobal(widget.rect().topLeft() + offset)
    QToolTip.showText(pos, text, widget, widget.rect(), timeout)