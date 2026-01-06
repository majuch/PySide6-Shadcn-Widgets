"""
Theme Switcher Demo

This example demonstrates switching between light and dark themes.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QGroupBox
)
from PySide6.QtCore import Qt

from pyside6_shadcn_widgets.components import Button, Card, Input, Badge, CheckBox, Switch
from pyside6_shadcn_widgets.themes import LightTheme, DarkTheme


class ThemeSwitcherDemo(QMainWindow):
    """Main demo window for theme switching."""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PySide6 Shadcn Widgets - Theme Switcher")
        self.setMinimumSize(800, 600)
        
        # Initialize with light theme
        self.current_theme = "light"
        self.light_theme = LightTheme()
        self.dark_theme = DarkTheme()
        
        # Setup UI
        self._setup_ui()
        
        # Apply initial theme
        self.light_theme.apply()
    
    def _setup_ui(self):
        """Setup the main UI."""
        central = QWidget()
        self.setCentralWidget(central)
        
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(24)
        main_layout.setContentsMargins(32, 32, 32, 32)
        
        # Title
        title = QLabel("Theme Switcher Demo")
        title.setStyleSheet("font-size: 32px; font-weight: 700;")
        main_layout.addWidget(title)
        
        subtitle = QLabel("Toggle between light and dark themes")
        subtitle.setStyleSheet("font-size: 16px;")
        main_layout.addWidget(subtitle)
        
        main_layout.addSpacing(16)
        
        # Theme switcher
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Dark Mode:")
        theme_label.setStyleSheet("font-size: 16px; font-weight: 600;")
        theme_layout.addWidget(theme_label)
        
        self.theme_switch = Switch()
        self.theme_switch.toggled.connect(self._toggle_theme)
        theme_layout.addWidget(self.theme_switch)
        
        theme_layout.addStretch()
        main_layout.addLayout(theme_layout)
        
        main_layout.addSpacing(16)
        
        # Sample components
        main_layout.addWidget(self._create_sample_components())
        
        main_layout.addStretch()
    
    def _create_sample_components(self) -> QGroupBox:
        """Create sample components to show theme."""
        group = QGroupBox("Sample Components")
        layout = QVBoxLayout(group)
        layout.setSpacing(16)
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        btn1 = Button("Default Button")
        btn2 = Button("Outline Button", variant=Button.VARIANT_OUTLINE)
        btn3 = Button("Ghost Button", variant=Button.VARIANT_GHOST)
        
        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)
        btn_layout.addStretch()
        
        layout.addLayout(btn_layout)
        
        # Input
        input_field = Input(placeholder="Type something...")
        layout.addWidget(input_field)
        
        # Card
        card = Card()
        card.set_header("Sample Card")
        card.set_content("This card will change appearance based on the selected theme.")
        layout.addWidget(card)
        
        # Badges
        badge_layout = QHBoxLayout()
        badge_layout.setSpacing(8)
        
        badge1 = Badge("Default")
        badge2 = Badge("Secondary", variant=Badge.VARIANT_SECONDARY)
        badge3 = Badge("Outline", variant=Badge.VARIANT_OUTLINE)
        
        badge_layout.addWidget(badge1)
        badge_layout.addWidget(badge2)
        badge_layout.addWidget(badge3)
        badge_layout.addStretch()
        
        layout.addLayout(badge_layout)
        
        # Checkbox
        checkbox = CheckBox("Sample checkbox")
        layout.addWidget(checkbox)
        
        return group
    
    def _toggle_theme(self, dark_mode: bool):
        """
        Toggle between light and dark themes.
        
        Args:
            dark_mode: True for dark theme, False for light theme
        """
        if dark_mode:
            self.dark_theme.apply()
            self.current_theme = "dark"
            print("Switched to dark theme")
        else:
            self.light_theme.apply()
            self.current_theme = "light"
            print("Switched to light theme")


def main():
    """Run the demo application."""
    app = QApplication(sys.argv)
    
    window = ThemeSwitcherDemo()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
