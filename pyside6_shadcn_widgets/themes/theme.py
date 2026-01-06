"""
Base Theme class for PySide6 Shadcn Widgets.
"""

from typing import Dict, Optional
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from pyside6_shadcn_widgets.utils.colors import hsl_to_hex


class Theme:
    """
    Base theme class that defines the color palette and styling for widgets.
    
    This class provides methods to convert HSL color values (as used in shadcn/ui)
    to Qt-compatible formats and apply themes to applications.
    """
    
    def __init__(self):
        """Initialize the theme with default color values."""
        self.colors: Dict[str, tuple] = {
            # Format: (h, s, l) - HSL values
            "background": (0, 0, 100),
            "foreground": (222.2, 84, 4.9),
            "card": (0, 0, 100),
            "card_foreground": (222.2, 84, 4.9),
            "popover": (0, 0, 100),
            "popover_foreground": (222.2, 84, 4.9),
            "primary": (222.2, 47.4, 11.2),
            "primary_foreground": (210, 40, 98),
            "secondary": (210, 40, 96.1),
            "secondary_foreground": (222.2, 47.4, 11.2),
            "muted": (210, 40, 96.1),
            "muted_foreground": (215.4, 16.3, 46.9),
            "accent": (210, 40, 96.1),
            "accent_foreground": (222.2, 47.4, 11.2),
            "destructive": (0, 84.2, 60.2),
            "destructive_foreground": (210, 40, 98),
            "border": (214.3, 31.8, 91.4),
            "input": (214.3, 31.8, 91.4),
            "ring": (222.2, 84, 4.9),
        }
        
        # Border radius values (in pixels)
        self.radius = {
            "sm": 6,
            "md": 8,
            "lg": 12,
        }
        
        # Spacing values (multiples of 4px base unit)
        self.spacing = {
            "xs": 4,
            "sm": 8,
            "md": 16,
            "lg": 24,
            "xl": 32,
        }
    
    def get_color(self, name: str) -> str:
        """
        Get a color value as a hexadecimal string.
        
        Args:
            name: Name of the color from the theme palette
            
        Returns:
            Hexadecimal color string (e.g., "#ffffff")
        """
        if name in self.colors:
            h, s, l = self.colors[name]
            return hsl_to_hex(h, s, l)
        return "#000000"  # Default fallback
    
    def get_qcolor(self, name: str) -> QColor:
        """
        Get a color value as a QColor object.
        
        Args:
            name: Name of the color from the theme palette
            
        Returns:
            QColor object
        """
        hex_color = self.get_color(name)
        return QColor(hex_color)
    
    def get_stylesheet(self) -> str:
        """
        Generate a complete QSS stylesheet for the theme.
        
        Returns:
            QSS stylesheet string
        """
        return f"""
            QWidget {{
                background-color: {self.get_color('background')};
                color: {self.get_color('foreground')};
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                font-size: 14px;
            }}
            
            QPushButton {{
                border: 1px solid {self.get_color('border')};
                border-radius: {self.radius['md']}px;
                padding: {self.spacing['sm']}px {self.spacing['md']}px;
                background-color: {self.get_color('primary')};
                color: {self.get_color('primary_foreground')};
            }}
            
            QPushButton:hover {{
                opacity: 0.9;
            }}
            
            QPushButton:pressed {{
                opacity: 0.8;
            }}
            
            QPushButton:disabled {{
                opacity: 0.5;
            }}
            
            QLineEdit {{
                border: 1px solid {self.get_color('input')};
                border-radius: {self.radius['md']}px;
                padding: {self.spacing['sm']}px {self.spacing['md']}px;
                background-color: {self.get_color('background')};
                color: {self.get_color('foreground')};
            }}
            
            QLineEdit:focus {{
                border: 2px solid {self.get_color('ring')};
            }}
            
            QCheckBox {{
                spacing: {self.spacing['sm']}px;
                color: {self.get_color('foreground')};
            }}
            
            QCheckBox::indicator {{
                width: 16px;
                height: 16px;
                border: 1px solid {self.get_color('border')};
                border-radius: 4px;
                background-color: {self.get_color('background')};
            }}
            
            QCheckBox::indicator:checked {{
                background-color: {self.get_color('primary')};
                border-color: {self.get_color('primary')};
            }}
            
            QTabWidget::pane {{
                border: 1px solid {self.get_color('border')};
                border-radius: {self.radius['md']}px;
                background-color: {self.get_color('card')};
            }}
            
            QTabBar::tab {{
                background-color: transparent;
                color: {self.get_color('muted_foreground')};
                padding: {self.spacing['sm']}px {self.spacing['md']}px;
                border-bottom: 2px solid transparent;
            }}
            
            QTabBar::tab:selected {{
                color: {self.get_color('foreground')};
                border-bottom: 2px solid {self.get_color('primary')};
            }}
            
            QTabBar::tab:hover {{
                color: {self.get_color('foreground')};
            }}
            
            QProgressBar {{
                border: none;
                border-radius: {self.radius['lg']}px;
                background-color: {self.get_color('secondary')};
                text-align: center;
                height: 8px;
            }}
            
            QProgressBar::chunk {{
                background-color: {self.get_color('primary')};
                border-radius: {self.radius['lg']}px;
            }}
        """
    
    def apply(self, app: Optional[QApplication] = None) -> None:
        """
        Apply the theme to a QApplication.
        
        Args:
            app: QApplication instance. If None, uses QApplication.instance()
        """
        if app is None:
            app = QApplication.instance()
        
        if app:
            app.setStyleSheet(self.get_stylesheet())
            
            # Set palette colors
            palette = QPalette()
            palette.setColor(QPalette.ColorRole.Window, self.get_qcolor('background'))
            palette.setColor(QPalette.ColorRole.WindowText, self.get_qcolor('foreground'))
            palette.setColor(QPalette.ColorRole.Base, self.get_qcolor('background'))
            palette.setColor(QPalette.ColorRole.AlternateBase, self.get_qcolor('secondary'))
            palette.setColor(QPalette.ColorRole.Text, self.get_qcolor('foreground'))
            palette.setColor(QPalette.ColorRole.Button, self.get_qcolor('primary'))
            palette.setColor(QPalette.ColorRole.ButtonText, self.get_qcolor('primary_foreground'))
            palette.setColor(QPalette.ColorRole.Highlight, self.get_qcolor('primary'))
            palette.setColor(QPalette.ColorRole.HighlightedText, self.get_qcolor('primary_foreground'))
            
            app.setPalette(palette)
