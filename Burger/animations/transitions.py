# ------ Importo las librerías necesarias ------ #
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QParallelAnimationGroup
from PySide6.QtWidgets import QStackedWidget, QWidget


def fade_slide(stack: QStackedWidget, old_widget: QWidget, new_widget: QWidget, duration=500, direction="left"):
    
    if old_widget == new_widget:
        return

    # ----- Posiciones -----
    stack_rect = stack.geometry()
    old_geometry = old_widget.geometry()
    new_widget.setGeometry(stack_rect)
    new_widget.show()

    # ----- Solo animamos geometría (slide) -----
    if direction == "left":
        start_new = QRect(stack_rect.width(), stack_rect.y(), stack_rect.width(), stack_rect.height())
        end_new = stack_rect
        end_old = QRect(-stack_rect.width(), stack_rect.y(), stack_rect.width(), stack_rect.height())
    else:
        start_new = QRect(-stack_rect.width(), stack_rect.y(), stack_rect.width(), stack_rect.height())
        end_new = stack_rect
        end_old = QRect(stack_rect.width(), stack_rect.y(), stack_rect.width(), stack_rect.height())

    new_anim = QPropertyAnimation(new_widget, b"geometry")
    new_anim.setStartValue(start_new)
    new_anim.setEndValue(end_new)
    new_anim.setDuration(duration)
    new_anim.setEasingCurve(QEasingCurve.InOutCubic)

    old_anim = QPropertyAnimation(old_widget, b"geometry")
    old_anim.setStartValue(old_geometry)
    old_anim.setEndValue(end_old)
    old_anim.setDuration(duration)
    old_anim.setEasingCurve(QEasingCurve.InOutCubic)

    # ----- Grupo paralelo -----
    group = QParallelAnimationGroup()
    group.addAnimation(new_anim)
    group.addAnimation(old_anim)

    # ----- Limpiar al terminar -----
    def on_finished():
        stack.setCurrentWidget(new_widget)
        old_widget.hide()
        old_widget.setGeometry(old_geometry)

    group.finished.connect(on_finished)

    # ----- Guardar referencia para evitar garbage collector -----
    stack._anim_group = group
    group.start()

    return group
