from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QParallelAnimationGroup
from PySide6.QtWidgets import QGraphicsOpacityEffect

def fade_slide(stack, frame_actual, frame_siguiente, duration=350):
    # ----- Guardo la geometría original -----
    geo = stack.geometry()
    ancho = geo.width()
    # --- Creo efectos nuevos ---
    eff_out = QGraphicsOpacityEffect()
    eff_in = QGraphicsOpacityEffect()
    frame_actual.setGraphicsEffect(eff_out)
    frame_siguiente.setGraphicsEffect(eff_in)
    eff_out.setOpacity(1)
    eff_in.setOpacity(0)
    # --- Animación fade out ---
    fade_out = QPropertyAnimation(eff_out, b"opacity")
    fade_out.setDuration(duration)
    fade_out.setStartValue(1)
    fade_out.setEndValue(0)
    # --- Animación fade in ---
    fade_in = QPropertyAnimation(eff_in, b"opacity")
    fade_in.setDuration(duration)
    fade_in.setStartValue(0)
    fade_in.setEndValue(1)
    # --- Slide out ---
    slide_out = QPropertyAnimation(frame_actual, b"geometry")
    slide_out.setDuration(duration)
    slide_out.setStartValue(geo)
    slide_out.setEndValue(QRect(-ancho, geo.y(), ancho, geo.height()))
    slide_out.setEasingCurve(QEasingCurve.OutCubic)
    # --- Slide in ---
    slide_in = QPropertyAnimation(frame_siguiente, b"geometry")
    slide_in.setDuration(duration)
    slide_in.setStartValue(QRect(ancho, geo.y(), ancho, geo.height()))
    slide_in.setEndValue(geo)
    slide_in.setEasingCurve(QEasingCurve.OutCubic)
    # --- Seteo los grupos ---
    group_out = QParallelAnimationGroup()
    group_out.addAnimation(fade_out)
    group_out.addAnimation(slide_out)
    group_in = QParallelAnimationGroup()
    group_in.addAnimation(fade_in)
    group_in.addAnimation(slide_in)
    # --- Función para evitar errores ---
    def cambiar_frame():
        stack.setCurrentWidget(frame_siguiente)
        
        # ----- Aseguro que el efecto siga existiendo ----- #
        frame_siguiente.setGraphicsEffect(eff_in)
        group_in.start()
    group_out.finished.connect(cambiar_frame)
    # ----- Guardo las referncias para evitar futuros problemas ----- #
    animaciones = [eff_out, eff_in, fade_out, fade_in, group_out, group_in]
    group_out.start()
    
    return animaciones