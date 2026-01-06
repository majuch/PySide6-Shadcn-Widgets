"""
Badge component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt


class Badge(QLabel):
    """
    Badge component with shadcn/ui styling.
    
    Supports multiple variants and sizes.
    
    Example:
        >>> badge = Badge("New", variant="default", size="md")
        >>> badge = Badge("Error", variant="destructive")
    """
    
    # Badge variants
    VARIANT_DEFAULT = "default"
    VARIANT_SECONDARY = "secondary"
    VARIANT_DESTRUCTIVE = "destructive"
    VARIANT_OUTLINE = "outline"
    
    # Badge sizes
    SIZE_SM = "sm"
    SIZE_MD = "md"
    SIZE_LG = "lg"
    
    def __init__(self, text: str = "", variant: str = VARIANT_DEFAULT,
                 size: str = SIZE_MD, pill: bool = False, parent: Optional[QWidget] = None):
        """
        Initialize badge component.
        
        Args:
            text: Badge text
            variant: Badge variant (default, secondary, destructive, outline)
            size: Badge size (sm, md, lg)
            pill: Whether to use pill shape (fully rounded)
            parent: Parent widget
        """
        super().__init__(text, parent)
        
        self.variant = variant
        self.size = size
        self.pill = pill
        
        # Setup badge
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self) -> None:
        """Setup badge UI."""
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles based on variant and size."""
        # Determine padding and font size based on size
        if self.size == self.SIZE_SM:
            padding_v, padding_h = 2, 8
            font_size = "11px"
            height = "18px"
        elif self.size == self.SIZE_MD:
            padding_v, padding_h = 4, 10
            font_size = "12px"
            height = "22px"
        elif self.size == self.SIZE_LG:
            padding_v, padding_h = 6, 12
            font_size = "14px"
            height = "26px"
        
        # Border radius
        border_radius = "12px" if self.pill else "6px"
        
        # Variant-specific styles
        if self.variant == self.VARIANT_DEFAULT:
            bg_color = "hsl(222.2, 47.4%, 11.2%)"
            text_color = "hsl(210, 40%, 98%)"
            border = "none"
        
        elif self.variant == self.VARIANT_SECONDARY:
            bg_color = "hsl(210, 40%, 96.1%)"
            text_color = "hsl(222.2, 47.4%, 11.2%)"
            border = "none"
        
        elif self.variant == self.VARIANT_DESTRUCTIVE:
            bg_color = "hsl(0, 84.2%, 60.2%)"
            text_color = "hsl(210, 40%, 98%)"
            border = "none"
        
        elif self.variant == self.VARIANT_OUTLINE:
            bg_color = "transparent"
            text_color = "hsl(222.2, 84%, 4.9%)"
            border = "1px solid hsl(214.3, 31.8%, 91.4%)"
        
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: {text_color};
                border: {border};
                border-radius: {border_radius};
                padding: {padding_v}px {padding_h}px;
                font-size: {font_size};
                font-weight: 500;
                min-height: {height};
            }}
        """)
