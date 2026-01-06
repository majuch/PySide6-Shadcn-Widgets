"""
Progress component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QProgressBar, QWidget
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property, QTimer
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QLinearGradient


class Progress(QProgressBar):
    """
    Modern progress bar with smooth value transitions.
    
    Features smooth value changes, indeterminate/loading animation, and color variants.
    
    Example:
        >>> progress = Progress()
        >>> progress.setValue(75)
        >>> progress.set_indeterminate(True)
    """
    
    # Color variants
    VARIANT_DEFAULT = "default"
    VARIANT_SUCCESS = "success"
    VARIANT_WARNING = "warning"
    VARIANT_DESTRUCTIVE = "destructive"
    
    def __init__(self, variant: str = VARIANT_DEFAULT, parent: Optional[QWidget] = None):
        """
        Initialize progress component.
        
        Args:
            variant: Color variant (default, success, warning, destructive)
            parent: Parent widget
        """
        super().__init__(parent)
        
        self.variant = variant
        self._animated_value = 0
        self._indeterminate = False
        self._indeterminate_position = 0.0
        
        # Setup progress bar
        self.setMinimum(0)
        self.setMaximum(100)
        self.setTextVisible(False)
        self.setFixedHeight(8)
        
        self._setup_animations()
        self._apply_styles()
    
    def _setup_animations(self) -> None:
        """Setup value change animation."""
        self.value_animation = QPropertyAnimation(self, b"animatedValue")
        self.value_animation.setDuration(300)
        self.value_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Indeterminate animation timer
        self.indeterminate_timer = QTimer(self)
        self.indeterminate_timer.timeout.connect(self._update_indeterminate)
        self.indeterminate_timer.setInterval(16)  # ~60 FPS
    
    def _apply_styles(self) -> None:
        """Apply QSS styles based on variant."""
        # Get color based on variant
        if self.variant == self.VARIANT_DEFAULT:
            progress_color = "hsl(222.2, 47.4%, 11.2%)"
        elif self.variant == self.VARIANT_SUCCESS:
            progress_color = "hsl(142, 71%, 45%)"
        elif self.variant == self.VARIANT_WARNING:
            progress_color = "hsl(38, 92%, 50%)"
        elif self.variant == self.VARIANT_DESTRUCTIVE:
            progress_color = "hsl(0, 84.2%, 60.2%)"
        else:
            progress_color = "hsl(222.2, 47.4%, 11.2%)"
        
        self.setStyleSheet(f"""
            QProgressBar {{
                border: none;
                border-radius: 4px;
                background-color: hsl(210, 40%, 96.1%);
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: {progress_color};
                border-radius: 4px;
            }}
        """)
    
    def setValue(self, value: int) -> None:
        """
        Set progress value with smooth animation.
        
        Args:
            value: Progress value (0-100)
        """
        if self._indeterminate:
            return
        
        # Animate to new value
        self.value_animation.stop()
        self.value_animation.setStartValue(self._animated_value)
        self.value_animation.setEndValue(value)
        self.value_animation.start()
        
        super().setValue(value)
    
    def set_indeterminate(self, indeterminate: bool) -> None:
        """
        Set indeterminate/loading state.
        
        Args:
            indeterminate: Whether to show indeterminate animation
        """
        self._indeterminate = indeterminate
        
        if indeterminate:
            self.setMinimum(0)
            self.setMaximum(0)
            self.indeterminate_timer.start()
        else:
            self.setMinimum(0)
            self.setMaximum(100)
            self.indeterminate_timer.stop()
            self._indeterminate_position = 0.0
    
    def _update_indeterminate(self) -> None:
        """Update indeterminate animation position."""
        self._indeterminate_position += 0.02
        if self._indeterminate_position > 1.0:
            self._indeterminate_position = 0.0
        self.update()
    
    def is_indeterminate(self) -> bool:
        """
        Check if progress bar is in indeterminate state.
        
        Returns:
            True if indeterminate, False otherwise
        """
        return self._indeterminate
    
    def get_animated_value(self) -> int:
        """Get current animated value."""
        return self._animated_value
    
    def set_animated_value(self, value: int) -> None:
        """
        Set animated value.
        
        Args:
            value: Animated value (0-100)
        """
        self._animated_value = value
        super().setValue(value)
    
    animatedValue = Property(int, get_animated_value, set_animated_value)
