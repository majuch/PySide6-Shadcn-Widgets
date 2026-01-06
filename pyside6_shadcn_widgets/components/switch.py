"""
Switch/Toggle component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QCheckBox, QWidget
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property, QRectF, QPointF, Signal
from PySide6.QtGui import QPainter, QColor, QPen, QBrush


class Switch(QCheckBox):
    """
    Modern switch/toggle component with smooth sliding animation.
    
    Features smooth toggle animation and color transitions.
    
    Example:
        >>> switch = Switch()
        >>> switch.setChecked(True)
        >>> switch.toggled.connect(lambda checked: print(f"Switch: {checked}"))
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize switch component.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        
        self._switch_position = 0.0  # 0.0 = off, 1.0 = on
        self._track_color = QColor(214, 227, 235)  # hsl(214.3, 31.8%, 91.4%)
        self._thumb_color = QColor(255, 255, 255)
        
        # Dimensions
        self.track_width = 44
        self.track_height = 24
        self.thumb_diameter = 20
        self.thumb_margin = 2
        
        # Setup switch
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._setup_animations()
        
        # Set fixed size
        self.setFixedSize(self.track_width, self.track_height)
    
    def _setup_animations(self) -> None:
        """Setup toggle animation."""
        self.position_animation = QPropertyAnimation(self, b"switchPosition")
        self.position_animation.setDuration(200)
        self.position_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
    
    def paintEvent(self, event) -> None:
        """Custom paint event to draw the switch."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw track
        track_rect = QRectF(0, 0, self.track_width, self.track_height)
        track_color = QColor(2, 12, 27) if self.isChecked() else QColor(214, 227, 235)
        
        # Animate track color
        if self._switch_position > 0:
            # Interpolate between off and on colors
            off_color = QColor(214, 227, 235)
            on_color = QColor(2, 12, 27)
            
            r = int(off_color.red() + (on_color.red() - off_color.red()) * self._switch_position)
            g = int(off_color.green() + (on_color.green() - off_color.green()) * self._switch_position)
            b = int(off_color.blue() + (on_color.blue() - off_color.blue()) * self._switch_position)
            
            track_color = QColor(r, g, b)
        
        painter.setBrush(QBrush(track_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(track_rect, self.track_height / 2, self.track_height / 2)
        
        # Draw thumb
        thumb_x = self.thumb_margin + (self.track_width - self.thumb_diameter - 2 * self.thumb_margin) * self._switch_position
        thumb_y = self.thumb_margin
        thumb_rect = QRectF(thumb_x, thumb_y, self.thumb_diameter, self.thumb_diameter)
        
        painter.setBrush(QBrush(self._thumb_color))
        painter.drawEllipse(thumb_rect)
    
    def mouseReleaseEvent(self, event) -> None:
        """Handle mouse release to toggle state."""
        super().mouseReleaseEvent(event)
        
        # Animate to new position
        if self.isChecked():
            self.position_animation.setStartValue(self._switch_position)
            self.position_animation.setEndValue(1.0)
        else:
            self.position_animation.setStartValue(self._switch_position)
            self.position_animation.setEndValue(0.0)
        
        self.position_animation.start()
    
    def setChecked(self, checked: bool) -> None:
        """
        Set checked state with animation.
        
        Args:
            checked: Whether switch is checked
        """
        super().setChecked(checked)
        
        # Animate to new position
        if checked:
            self.position_animation.setStartValue(self._switch_position)
            self.position_animation.setEndValue(1.0)
        else:
            self.position_animation.setStartValue(self._switch_position)
            self.position_animation.setEndValue(0.0)
        
        self.position_animation.start()
    
    def get_switch_position(self) -> float:
        """Get current switch position."""
        return self._switch_position
    
    def set_switch_position(self, position: float) -> None:
        """
        Set switch position.
        
        Args:
            position: Position value (0.0 to 1.0)
        """
        self._switch_position = position
        self.update()
    
    switchPosition = Property(float, get_switch_position, set_switch_position)
