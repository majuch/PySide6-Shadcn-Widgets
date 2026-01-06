"""
Scale animations for PySide6 widgets.
"""

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, Property, QObject
from PySide6.QtWidgets import QWidget


class ScaleAnimationHelper(QObject):
    """Helper class to enable scale animations on QWidget."""
    
    def __init__(self, widget: QWidget):
        """
        Initialize scale animation helper.
        
        Args:
            widget: The widget to animate
        """
        super().__init__(widget)
        self.widget = widget
        self._scale = 1.0
        self._original_geometry = widget.geometry()
    
    def get_scale(self) -> float:
        """Get the current scale value."""
        return self._scale
    
    def set_scale(self, scale: float) -> None:
        """
        Set the scale value and update widget geometry.
        
        Args:
            scale: Scale factor (1.0 = 100%)
        """
        self._scale = scale
        
        # Calculate new geometry based on scale
        original_width = self._original_geometry.width()
        original_height = self._original_geometry.height()
        original_x = self._original_geometry.x()
        original_y = self._original_geometry.y()
        
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        
        # Center the scaled widget
        new_x = original_x + (original_width - new_width) // 2
        new_y = original_y + (original_height - new_height) // 2
        
        self.widget.setGeometry(new_x, new_y, new_width, new_height)
    
    scale = Property(float, get_scale, set_scale)


class ScaleIn:
    """
    Scale in animation that animates from 95% to 100% size.
    Often combined with fade in for modal effects.
    
    Example:
        >>> widget = QWidget()
        >>> animation = ScaleIn(widget, duration=300)
        >>> animation.start()
    """
    
    def __init__(self, widget: QWidget, duration: int = 300, 
                 start_scale: float = 0.95, end_scale: float = 1.0,
                 easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize scale in animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            start_scale: Starting scale factor (default 0.95 = 95%)
            end_scale: Ending scale factor (default 1.0 = 100%)
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.start_scale = start_scale
        self.end_scale = end_scale
        self.easing = easing
        
        # Create scale helper
        self.scale_helper = ScaleAnimationHelper(widget)
        
        # Create animation
        self.animation = QPropertyAnimation(self.scale_helper, b"scale")
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_scale)
        self.animation.setEndValue(end_scale)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the scale in animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the scale in animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """
        Get the underlying QPropertyAnimation object.
        
        Returns:
            The QPropertyAnimation instance
        """
        return self.animation


class ScaleOut:
    """
    Scale out animation that animates from 100% to 95% size.
    Often combined with fade out for modal effects.
    
    Example:
        >>> widget = QWidget()
        >>> animation = ScaleOut(widget, duration=300)
        >>> animation.start()
    """
    
    def __init__(self, widget: QWidget, duration: int = 300,
                 start_scale: float = 1.0, end_scale: float = 0.95,
                 easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize scale out animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            start_scale: Starting scale factor (default 1.0 = 100%)
            end_scale: Ending scale factor (default 0.95 = 95%)
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.start_scale = start_scale
        self.end_scale = end_scale
        self.easing = easing
        
        # Create scale helper
        self.scale_helper = ScaleAnimationHelper(widget)
        
        # Create animation
        self.animation = QPropertyAnimation(self.scale_helper, b"scale")
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_scale)
        self.animation.setEndValue(end_scale)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the scale out animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the scale out animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """
        Get the underlying QPropertyAnimation object.
        
        Returns:
            The QPropertyAnimation instance
        """
        return self.animation
