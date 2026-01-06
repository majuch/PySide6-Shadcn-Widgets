"""
Dark theme for PySide6 Shadcn Widgets.
"""

from pyside6_shadcn_widgets.themes.theme import Theme


class DarkTheme(Theme):
    """
    Dark theme with colors matching shadcn/ui dark mode.
    """
    
    def __init__(self):
        """Initialize the dark theme with shadcn/ui color values."""
        super().__init__()
        
        # Override with dark theme colors (HSL format)
        self.colors = {
            "background": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "card": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "card_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "popover": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "popover_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "primary": (210, 40, 98),  # hsl(210 40% 98%)
            "primary_foreground": (222.2, 47.4, 11.2),  # hsl(222.2 47.4% 11.2%)
            "secondary": (217.2, 32.6, 17.5),  # hsl(217.2 32.6% 17.5%)
            "secondary_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "muted": (217.2, 32.6, 17.5),  # hsl(217.2 32.6% 17.5%)
            "muted_foreground": (215, 20.2, 65.1),  # hsl(215 20.2% 65.1%)
            "accent": (217.2, 32.6, 17.5),  # hsl(217.2 32.6% 17.5%)
            "accent_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "destructive": (0, 62.8, 30.6),  # hsl(0 62.8% 30.6%)
            "destructive_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "border": (217.2, 32.6, 17.5),  # hsl(217.2 32.6% 17.5%)
            "input": (217.2, 32.6, 17.5),  # hsl(217.2 32.6% 17.5%)
            "ring": (212.7, 26.8, 83.9),  # hsl(212.7 26.8% 83.9%)
        }
