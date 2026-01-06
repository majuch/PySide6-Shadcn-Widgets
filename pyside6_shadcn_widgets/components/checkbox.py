"""
CheckBox component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QCheckBox, QWidget
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QPainter, QColor, QPen, QPainterPath
from PySide6.QtCore import QRect, QPoint


class CheckBox(QCheckBox):
    """
    Custom checkbox with modern styling and check animation.
    
    Features smooth check mark animation and indeterminate state support.
    
    Example:
        >>> checkbox = CheckBox("Accept terms")
        >>> checkbox.setChecked(True)
    """
    
    def __init__(self, text: str = "", parent: Optional[QWidget] = None):
        """
        Initialize checkbox component.
        
        Args:
            text: Checkbox label text
            parent: Parent widget
        """
        super().__init__(text, parent)
        
        self._check_progress = 0.0
        
        # Setup checkbox
        self._setup_animations()
        self._apply_styles()
    
    def _setup_animations(self) -> None:
        """Setup check animation."""
        self.check_animation = QPropertyAnimation(self, b"checkProgress")
        self.check_animation.setDuration(200)
        self.check_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles to checkbox."""
        self.setStyleSheet("""
            QCheckBox {
                color: hsl(222.2, 84%, 4.9%);
                spacing: 8px;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 4px;
                background-color: hsl(0, 0%, 100%);
            }
            QCheckBox::indicator:hover {
                border-color: hsl(222.2, 84%, 4.9%);
            }
            QCheckBox::indicator:checked {
                background-color: hsl(222.2, 47.4%, 11.2%);
                border-color: hsl(222.2, 47.4%, 11.2%);
            }
            QCheckBox::indicator:indeterminate {
                background-color: hsl(222.2, 47.4%, 11.2%);
                border-color: hsl(222.2, 47.4%, 11.2%);
            }
            QCheckBox::indicator:disabled {
                background-color: hsl(210, 40%, 96.1%);
                border-color: hsl(214.3, 31.8%, 95%);
            }
        """)
    
    def nextCheckState(self) -> None:
        """Handle check state change with animation."""
        super().nextCheckState()
        
        if self.isChecked():
            # Animate check in
            self.check_animation.stop()
            self.check_animation.setStartValue(0.0)
            self.check_animation.setEndValue(1.0)
            self.check_animation.start()
        else:
            # Animate check out
            self.check_animation.stop()
            self.check_animation.setStartValue(1.0)
            self.check_animation.setEndValue(0.0)
            self.check_animation.start()
    
    def get_check_progress(self) -> float:
        """Get current check animation progress."""
        return self._check_progress
    
    def set_check_progress(self, progress: float) -> None:
        """
        Set check animation progress.
        
        Args:
            progress: Progress value (0.0 to 1.0)
        """
        self._check_progress = progress
        self.update()
    
    checkProgress = Property(float, get_check_progress, set_check_progress)
