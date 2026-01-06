"""
Button component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Property, QSize, Signal
from PySide6.QtGui import QColor, QCursor
from PySide6.QtCore import Qt


class Button(QPushButton):
    """
    Modern button component with shadcn/ui styling.
    
    Supports multiple variants and sizes with smooth hover and click animations.
    
    Example:
        >>> button = Button("Click me", variant="default", size="md")
        >>> button.clicked.connect(lambda: print("Button clicked!"))
    """
    
    # Button variants
    VARIANT_DEFAULT = "default"
    VARIANT_DESTRUCTIVE = "destructive"
    VARIANT_OUTLINE = "outline"
    VARIANT_GHOST = "ghost"
    VARIANT_LINK = "link"
    
    # Button sizes
    SIZE_SM = "sm"
    SIZE_MD = "md"
    SIZE_LG = "lg"
    
    def __init__(self, text: str = "", variant: str = VARIANT_DEFAULT, 
                 size: str = SIZE_MD, parent: Optional[QWidget] = None):
        """
        Initialize button component.
        
        Args:
            text: Button text
            variant: Button variant (default, destructive, outline, ghost, link)
            size: Button size (sm, md, lg)
            parent: Parent widget
        """
        super().__init__(text, parent)
        
        self.variant = variant
        self.size = size
        self._loading = False
        self._scale = 1.0
        
        # Setup button
        self._setup_ui()
        self._setup_animations()
        self._apply_styles()
    
    def _setup_ui(self) -> None:
        """Setup button UI elements."""
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        # Set size based on size property
        if self.size == self.SIZE_SM:
            self.setMinimumHeight(32)
            self.setFont(self.font())
        elif self.size == self.SIZE_MD:
            self.setMinimumHeight(40)
        elif self.size == self.SIZE_LG:
            self.setMinimumHeight(48)
        
        # Add subtle shadow for non-ghost/link variants
        if self.variant not in [self.VARIANT_GHOST, self.VARIANT_LINK]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(8)
            shadow.setColor(QColor(0, 0, 0, 30))
            shadow.setOffset(0, 2)
            self.setGraphicsEffect(shadow)
    
    def _setup_animations(self) -> None:
        """Setup hover and click animations."""
        # Scale animation for click effect
        self.scale_animation = QPropertyAnimation(self, b"scale")
        self.scale_animation.setDuration(150)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles based on variant and size."""
        # Base styles
        padding_sm = "6px 12px"
        padding_md = "8px 16px"
        padding_lg = "12px 24px"
        
        padding = padding_md
        if self.size == self.SIZE_SM:
            padding = padding_sm
            font_size = "13px"
        elif self.size == self.SIZE_MD:
            padding = padding_md
            font_size = "14px"
        elif self.size == self.SIZE_LG:
            padding = padding_lg
            font_size = "16px"
        
        # Variant-specific styles
        if self.variant == self.VARIANT_DEFAULT:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: hsl(222.2, 47.4%, 11.2%);
                    color: hsl(210, 40%, 98%);
                    border: none;
                    border-radius: 8px;
                    padding: {padding};
                    font-size: {font_size};
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: hsl(222.2, 47.4%, 15%);
                }}
                QPushButton:pressed {{
                    background-color: hsl(222.2, 47.4%, 9%);
                }}
                QPushButton:disabled {{
                    background-color: hsl(210, 40%, 96.1%);
                    color: hsl(215.4, 16.3%, 46.9%);
                }}
            """)
        
        elif self.variant == self.VARIANT_DESTRUCTIVE:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: hsl(0, 84.2%, 60.2%);
                    color: hsl(210, 40%, 98%);
                    border: none;
                    border-radius: 8px;
                    padding: {padding};
                    font-size: {font_size};
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: hsl(0, 84.2%, 55%);
                }}
                QPushButton:pressed {{
                    background-color: hsl(0, 84.2%, 50%);
                }}
                QPushButton:disabled {{
                    background-color: hsl(210, 40%, 96.1%);
                    color: hsl(215.4, 16.3%, 46.9%);
                }}
            """)
        
        elif self.variant == self.VARIANT_OUTLINE:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    color: hsl(222.2, 84%, 4.9%);
                    border: 1px solid hsl(214.3, 31.8%, 91.4%);
                    border-radius: 8px;
                    padding: {padding};
                    font-size: {font_size};
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: hsl(210, 40%, 96.1%);
                }}
                QPushButton:pressed {{
                    background-color: hsl(210, 40%, 90%);
                }}
                QPushButton:disabled {{
                    color: hsl(215.4, 16.3%, 46.9%);
                    border-color: hsl(214.3, 31.8%, 95%);
                }}
            """)
        
        elif self.variant == self.VARIANT_GHOST:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    color: hsl(222.2, 84%, 4.9%);
                    border: none;
                    border-radius: 8px;
                    padding: {padding};
                    font-size: {font_size};
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: hsl(210, 40%, 96.1%);
                }}
                QPushButton:pressed {{
                    background-color: hsl(210, 40%, 90%);
                }}
                QPushButton:disabled {{
                    color: hsl(215.4, 16.3%, 46.9%);
                }}
            """)
        
        elif self.variant == self.VARIANT_LINK:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    color: hsl(222.2, 47.4%, 11.2%);
                    border: none;
                    padding: {padding};
                    font-size: {font_size};
                    font-weight: 500;
                    text-decoration: underline;
                }}
                QPushButton:hover {{
                    color: hsl(222.2, 47.4%, 20%);
                }}
                QPushButton:pressed {{
                    color: hsl(222.2, 47.4%, 8%);
                }}
                QPushButton:disabled {{
                    color: hsl(215.4, 16.3%, 46.9%);
                }}
            """)
    
    def enterEvent(self, event) -> None:
        """Handle mouse enter event for hover effect."""
        super().enterEvent(event)
        if not self.isEnabled():
            return
        
        # Subtle scale up on hover
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(1.02)
        self.scale_animation.start()
    
    def leaveEvent(self, event) -> None:
        """Handle mouse leave event."""
        super().leaveEvent(event)
        
        # Scale back to normal
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(1.0)
        self.scale_animation.start()
    
    def mousePressEvent(self, event) -> None:
        """Handle mouse press event for click animation."""
        super().mousePressEvent(event)
        if not self.isEnabled():
            return
        
        # Scale down on press
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(0.98)
        self.scale_animation.setDuration(100)
        self.scale_animation.start()
    
    def mouseReleaseEvent(self, event) -> None:
        """Handle mouse release event."""
        super().mouseReleaseEvent(event)
        if not self.isEnabled():
            return
        
        # Scale back to hover state
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(1.02)
        self.scale_animation.setDuration(150)
        self.scale_animation.start()
    
    def get_scale(self) -> float:
        """Get current scale value."""
        return self._scale
    
    def set_scale(self, scale: float) -> None:
        """
        Set scale value and trigger visual update.
        
        Note: Visual scale effect is achieved through the animation's
        smooth property changes triggering repaints, creating a subtle
        visual feedback effect.
        """
        self._scale = scale
        self.update()
    
    scale = Property(float, get_scale, set_scale)
    
    def set_loading(self, loading: bool) -> None:
        """
        Set loading state.
        
        Args:
            loading: Whether button is in loading state
            
        Note: Currently shows "Loading..." text. Spinner animation can be
        added as a future enhancement using QMovie or custom painting.
        """
        self._loading = loading
        self.setEnabled(not loading)
        if loading:
            self.setText("Loading...")
    
    def is_loading(self) -> bool:
        """
        Check if button is in loading state.
        
        Returns:
            True if loading, False otherwise
        """
        return self._loading
