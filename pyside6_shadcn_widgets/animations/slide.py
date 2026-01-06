"""
Slide animations for PySide6 widgets.
"""

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtWidgets import QWidget


class SlideInUp:
    """Slide in from bottom animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50, 
                 easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize slide in up animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(QPoint(self.original_pos.x(), self.original_pos.y() + distance))
        self.animation.setEndValue(self.original_pos)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide in up animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideInDown:
    """Slide in from top animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize slide in down animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(QPoint(self.original_pos.x(), self.original_pos.y() - distance))
        self.animation.setEndValue(self.original_pos)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide in down animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideInLeft:
    """Slide in from right animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize slide in left animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(QPoint(self.original_pos.x() + distance, self.original_pos.y()))
        self.animation.setEndValue(self.original_pos)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide in left animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideInRight:
    """Slide in from left animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic):
        """
        Initialize slide in right animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(QPoint(self.original_pos.x() - distance, self.original_pos.y()))
        self.animation.setEndValue(self.original_pos)
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide in right animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideOutUp:
    """Slide out to top animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize slide out up animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(self.original_pos)
        self.animation.setEndValue(QPoint(self.original_pos.x(), self.original_pos.y() - distance))
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide out up animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideOutDown:
    """Slide out to bottom animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize slide out down animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(self.original_pos)
        self.animation.setEndValue(QPoint(self.original_pos.x(), self.original_pos.y() + distance))
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide out down animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideOutLeft:
    """Slide out to left animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize slide out left animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(self.original_pos)
        self.animation.setEndValue(QPoint(self.original_pos.x() - distance, self.original_pos.y()))
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide out left animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation


class SlideOutRight:
    """Slide out to right animation."""
    
    def __init__(self, widget: QWidget, duration: int = 300, distance: int = 50,
                 easing: QEasingCurve.Type = QEasingCurve.Type.InCubic):
        """
        Initialize slide out right animation.
        
        Args:
            widget: The widget to animate
            duration: Animation duration in milliseconds
            distance: Distance to slide in pixels
            easing: Easing curve type for the animation
        """
        self.widget = widget
        self.duration = duration
        self.distance = distance
        self.easing = easing
        
        # Store original position
        self.original_pos = widget.pos()
        
        # Create animation
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(self.original_pos)
        self.animation.setEndValue(QPoint(self.original_pos.x() + distance, self.original_pos.y()))
        self.animation.setEasingCurve(easing)
    
    def start(self) -> None:
        """Start the slide out right animation."""
        self.animation.start()
    
    def stop(self) -> None:
        """Stop the animation."""
        self.animation.stop()
    
    def get_animation(self) -> QPropertyAnimation:
        """Get the underlying QPropertyAnimation object."""
        return self.animation
