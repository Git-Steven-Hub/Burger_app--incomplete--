from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QParallelAnimationGroup

class WindowAnimator:
    def __init__(self, target_window):
        self.target = target_window

        # Fade
        self.fade = QPropertyAnimation(self.target, b"windowOpacity")
        self.fade.setDuration(1000)
        self.fade.setStartValue(0.0)
        self.fade.setEndValue(1.0)
        self.fade.setEasingCurve(QEasingCurve.OutCubic)

        # Movimiento suave (pos)
        self.start_pos = self.target.pos() + QPoint(0, 90)  # 30 px abajo
        self.move = QPropertyAnimation(self.target, b"pos")
        self.move.setDuration(1000)
        self.move.setStartValue(self.start_pos)
        self.move.setEndValue(self.target.pos())
        self.move.setEasingCurve(QEasingCurve.OutCubic)

        # Grupo
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.fade)
        self.anim_group.addAnimation(self.move)

    def start(self):
        current_pos = self.target.pos()
        start_pos = current_pos + QPoint(0, 90)

        self.move.setStartValue(start_pos)
        self.move.setEndValue(current_pos)
        self.anim_group.start()