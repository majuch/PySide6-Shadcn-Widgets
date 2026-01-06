"""
Light theme for PySide6 Shadcn Widgets.
"""

from pyside6_shadcn_widgets.themes.theme import Theme


class LightTheme(Theme):
    """
    Light theme with colors matching shadcn/ui light mode.
    """
    
    def __init__(self):
        """Initialize the light theme with shadcn/ui color values."""
        super().__init__()
        
        # Override with light theme colors (HSL format)
        self.colors = {
            "background": (0, 0, 100),  # hsl(0 0% 100%)
            "foreground": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "card": (0, 0, 100),  # hsl(0 0% 100%)
            "card_foreground": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "popover": (0, 0, 100),  # hsl(0 0% 100%)
            "popover_foreground": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
            "primary": (222.2, 47.4, 11.2),  # hsl(222.2 47.4% 11.2%)
            "primary_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "secondary": (210, 40, 96.1),  # hsl(210 40% 96.1%)
            "secondary_foreground": (222.2, 47.4, 11.2),  # hsl(222.2 47.4% 11.2%)
            "muted": (210, 40, 96.1),  # hsl(210 40% 96.1%)
            "muted_foreground": (215.4, 16.3, 46.9),  # hsl(215.4 16.3% 46.9%)
            "accent": (210, 40, 96.1),  # hsl(210 40% 96.1%)
            "accent_foreground": (222.2, 47.4, 11.2),  # hsl(222.2 47.4% 11.2%)
            "destructive": (0, 84.2, 60.2),  # hsl(0 84.2% 60.2%)
            "destructive_foreground": (210, 40, 98),  # hsl(210 40% 98%)
            "border": (214.3, 31.8, 91.4),  # hsl(214.3 31.8% 91.4%)
            "input": (214.3, 31.8, 91.4),  # hsl(214.3 31.8% 91.4%)
            "ring": (222.2, 84, 4.9),  # hsl(222.2 84% 4.9%)
        }
