"""
Fade animations for PySide6 widgets.
"""

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QObject
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget


class FadeIn:
    """
    Fade in animation that animates opacity from 0 to 1.
    
    Example:
        >>> widget = QWidget()
        >>> animation = FadeIn(widget, duration=300)
        >>> animation.start()
    """
    
    def __init__(self, widget: QWidget, duration: int = 300, easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize fade in animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.easing = easing
        
        # Create opacity effect
        self.opacity_effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(self.opacity_effect)
        
        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the fade in animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the fade in animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """
        Get the underlying QPropertyAnimation object.
        
        Returns:
            The QPropertyAnimation instance
        """
        return self.animation


class FadeOut:
    """
    Fade out animation that animates opacity from 1 to 0.
    
    Example:
        >>> widget = QWidget()
        >>> animation = FadeOut(widget, duration=300)
        >>> animation.start()
    """
    
    def __init__(self, widget: QWidget, duration: int = 300, easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize fade out animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.easing = easing
        
        # Create or get existing opacity effect
        opacity_effect = widget.graphicsEffect()
        if opacity_effect is None or not isinstance(opacity_effect, QGraphicsOpacityEffect):
            opacity_effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(opacity_effect)
        
        self.opacity_effect = opacity_effect
        
        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the fade out animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the fade out animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """
        Get the underlying QPropertyAnimation object.
        
        Returns:
            The QPropertyAnimation instance
        """
        return self.animation
