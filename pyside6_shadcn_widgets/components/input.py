"""
Input component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QLineEdit, QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal, Property
from PySide6.QtGui import QColor


class Input(QLineEdit):
    """
    Modern input component with shadcn/ui styling.
    
    Features focus animations, error states, and optional icon support.
    
    Example:
        >>> input_field = Input(placeholder="Enter your name")
        >>> input_field.set_error(True)
    """
    
    def __init__(self, placeholder: str = "", parent: Optional[QWidget] = None):
        """
        Initialize input component.
        
        Args:
            placeholder: Placeholder text
            parent: Parent widget
        """
        super().__init__(parent)
        
        self._has_error = False
        self._border_width = 1
        
        # Setup input
        self.setPlaceholderText(placeholder)
        self._setup_animations()
        self._apply_styles()
    
    def _setup_animations(self) -> None:
        """Setup focus animation for border."""
        self.border_animation = QPropertyAnimation(self, b"borderWidth")
        self.border_animation.setDuration(200)
        self.border_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles to input."""
        self.setStyleSheet("""
            QLineEdit {
                background-color: hsl(0, 0%, 100%);
                color: hsl(222.2, 84%, 4.9%);
                border: 1px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                min-height: 40px;
            }
            QLineEdit:focus {
                border: 2px solid hsl(222.2, 84%, 4.9%);
            }
            QLineEdit:disabled {
                background-color: hsl(210, 40%, 96.1%);
                color: hsl(215.4, 16.3%, 46.9%);
            }
            QLineEdit::placeholder {
                color: hsl(215.4, 16.3%, 46.9%);
            }
        """)
    
    def set_error(self, has_error: bool) -> None:
        """
        Set error state of the input.
        
        Args:
            has_error: Whether input has an error
        """
        self._has_error = has_error
        
        if has_error:
            self.setStyleSheet("""
                QLineEdit {
                    background-color: hsl(0, 0%, 100%);
                    color: hsl(222.2, 84%, 4.9%);
                    border: 2px solid hsl(0, 84.2%, 60.2%);
                    border-radius: 8px;
                    padding: 8px 16px;
                    font-size: 14px;
                    min-height: 40px;
                }
                QLineEdit:focus {
                    border: 2px solid hsl(0, 84.2%, 50%);
                }
            """)
        else:
            self._apply_styles()
    
    def has_error(self) -> bool:
        """
        Check if input has an error state.
        
        Returns:
            True if input has error, False otherwise
        """
        return self._has_error
    
    def focusInEvent(self, event) -> None:
        """Handle focus in event with animation."""
        super().focusInEvent(event)
        
        if not self._has_error:
            # Animate border width
            self.border_animation.stop()
            self.border_animation.setStartValue(self._border_width)
            self.border_animation.setEndValue(2)
            self.border_animation.start()
    
    def focusOutEvent(self, event) -> None:
        """Handle focus out event."""
        super().focusOutEvent(event)
        
        if not self._has_error:
            # Animate border back to normal
            self.border_animation.stop()
            self.border_animation.setStartValue(self._border_width)
            self.border_animation.setEndValue(1)
            self.border_animation.start()
    
    def get_border_width(self) -> int:
        """Get current border width."""
        return self._border_width
    
    def set_border_width(self, width: int) -> None:
        """
        Set border width.
        
        Args:
            width: Border width in pixels
        """
        self._border_width = width
        self.update()
    
    borderWidth = Property(int, get_border_width, set_border_width)
