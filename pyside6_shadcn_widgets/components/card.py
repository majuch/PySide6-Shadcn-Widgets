"""
Card component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QColor


class Card(QFrame):
    """
    Card component with header, content, and footer sections.
    
    Features hover elevation effect and shadcn/ui styling.
    
    Example:
        >>> card = Card()
        >>> card.set_header("Card Title")
        >>> card.set_content(QLabel("Card content goes here"))
        >>> card.set_footer(QLabel("Card footer"))
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize card component.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        
        self._elevation = 2
        
        # Setup UI
        self._setup_ui()
        self._setup_animations()
        self._apply_styles()
    
    def _setup_ui(self) -> None:
        """Setup card UI structure."""
        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(12)
        
        # Header section
        self.header_widget = QWidget()
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_widget.hide()
        
        # Content section
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Footer section
        self.footer_widget = QWidget()
        self.footer_layout = QVBoxLayout(self.footer_widget)
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_widget.hide()
        
        # Add sections to main layout
        self.main_layout.addWidget(self.header_widget)
        self.main_layout.addWidget(self.content_widget)
        self.main_layout.addWidget(self.footer_widget)
        
        # Add shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(12)
        self.shadow.setColor(QColor(0, 0, 0, 20))
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)
    
    def _setup_animations(self) -> None:
        """Setup hover animation for elevation effect."""
        self.elevation_animation = QPropertyAnimation(self, b"elevation")
        self.elevation_animation.setDuration(200)
        self.elevation_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles to card."""
        self.setStyleSheet("""
            QFrame {
                background-color: hsl(0, 0%, 100%);
                border: 1px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 12px;
            }
        """)
        
        # Style for header
        self.header_widget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QLabel {
                color: hsl(222.2, 84%, 4.9%);
                font-size: 18px;
                font-weight: 600;
            }
        """)
        
        # Style for content
        self.content_widget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QLabel {
                color: hsl(222.2, 84%, 4.9%);
                font-size: 14px;
            }
        """)
        
        # Style for footer
        self.footer_widget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QLabel {
                color: hsl(215.4, 16.3%, 46.9%);
                font-size: 13px;
            }
        """)
    
    def set_header(self, widget_or_text) -> None:
        """
        Set card header content.
        
        Args:
            widget_or_text: QWidget or string for header
        """
        # Clear existing header
        while self.header_layout.count():
            item = self.header_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new header
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            self.header_layout.addWidget(label)
        else:
            self.header_layout.addWidget(widget_or_text)
        
        self.header_widget.show()
    
    def set_content(self, widget_or_text) -> None:
        """
        Set card content.
        
        Args:
            widget_or_text: QWidget or string for content
        """
        # Clear existing content
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new content
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            label.setWordWrap(True)
            self.content_layout.addWidget(label)
        else:
            self.content_layout.addWidget(widget_or_text)
    
    def set_footer(self, widget_or_text) -> None:
        """
        Set card footer content.
        
        Args:
            widget_or_text: QWidget or string for footer
        """
        # Clear existing footer
        while self.footer_layout.count():
            item = self.footer_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new footer
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            self.footer_layout.addWidget(label)
        else:
            self.footer_layout.addWidget(widget_or_text)
        
        self.footer_widget.show()
    
    def enterEvent(self, event) -> None:
        """Handle mouse enter for hover elevation effect."""
        super().enterEvent(event)
        
        # Increase elevation on hover
        self.elevation_animation.stop()
        self.elevation_animation.setStartValue(self._elevation)
        self.elevation_animation.setEndValue(8)
        self.elevation_animation.start()
    
    def leaveEvent(self, event) -> None:
        """Handle mouse leave."""
        super().leaveEvent(event)
        
        # Decrease elevation
        self.elevation_animation.stop()
        self.elevation_animation.setStartValue(self._elevation)
        self.elevation_animation.setEndValue(2)
        self.elevation_animation.start()
    
    def get_elevation(self) -> float:
        """Get current elevation value."""
        return self._elevation
    
    def set_elevation(self, elevation: float) -> None:
        """
        Set elevation value and update shadow.
        
        Args:
            elevation: Elevation value (affects shadow blur and offset)
        """
        self._elevation = elevation
        
        # Update shadow based on elevation
        blur_radius = 8 + elevation
        offset_y = 1 + elevation / 4
        opacity = 15 + elevation * 2
        
        self.shadow.setBlurRadius(blur_radius)
        self.shadow.setOffset(0, offset_y)
        self.shadow.setColor(QColor(0, 0, 0, int(opacity)))
    
    elevation = Property(float, get_elevation, set_elevation)
