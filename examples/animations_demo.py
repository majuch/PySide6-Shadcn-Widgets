"""
Animations Demo

This example demonstrates all the animation types available in PySide6 Shadcn Widgets.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QGroupBox
)
from PySide6.QtCore import Qt

from pyside6_shadcn_widgets.components import Button, Card
from pyside6_shadcn_widgets.animations import (
    FadeIn, FadeOut, SlideInUp, SlideInDown, SlideInLeft, SlideInRight,
    SlideOutUp, SlideOutDown, SlideOutLeft, SlideOutRight, ScaleIn, ScaleOut
)
from pyside6_shadcn_widgets.themes import LightTheme


class AnimationsDemo(QMainWindow):
    """Main demo window showcasing all animations."""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PySide6 Shadcn Widgets - Animations Demo")
        self.setMinimumSize(900, 700)
        
        # Apply theme
        self.theme = LightTheme()
        self.theme.apply()
        
        # Setup UI
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the main UI."""
        central = QWidget()
        self.setCentralWidget(central)
        
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(24)
        main_layout.setContentsMargins(32, 32, 32, 32)
        
        # Title
        title = QLabel("Animations Demo")
        title.setStyleSheet("font-size: 32px; font-weight: 700; color: hsl(222.2, 84%, 4.9%);")
        main_layout.addWidget(title)
        
        subtitle = QLabel("Click buttons to see different animation effects")
        subtitle.setStyleSheet("font-size: 16px; color: hsl(215.4, 16.3%, 46.9%);")
        main_layout.addWidget(subtitle)
        
        main_layout.addSpacing(16)
        
        # Animation target
        self.animation_target = Card()
        self.animation_target.set_header("Animation Target")
        self.animation_target.set_content("Watch this card animate when you click the buttons below!")
        self.animation_target.setFixedSize(400, 200)
        
        target_container = QHBoxLayout()
        target_container.addStretch()
        target_container.addWidget(self.animation_target)
        target_container.addStretch()
        main_layout.addLayout(target_container)
        
        main_layout.addSpacing(24)
        
        # Fade animations
        main_layout.addWidget(self._create_fade_section())
        
        # Slide animations
        main_layout.addWidget(self._create_slide_section())
        
        # Scale animations
        main_layout.addWidget(self._create_scale_section())
        
        main_layout.addStretch()
    
    def _create_fade_section(self) -> QGroupBox:
        """Create fade animation controls."""
        group = QGroupBox("Fade Animations")
        layout = QHBoxLayout(group)
        layout.setSpacing(12)
        
        fade_in_btn = Button("Fade In")
        fade_in_btn.clicked.connect(self._play_fade_in)
        layout.addWidget(fade_in_btn)
        
        fade_out_btn = Button("Fade Out")
        fade_out_btn.clicked.connect(self._play_fade_out)
        layout.addWidget(fade_out_btn)
        
        layout.addStretch()
        
        return group
    
    def _create_slide_section(self) -> QGroupBox:
        """Create slide animation controls."""
        group = QGroupBox("Slide Animations")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        # Slide In
        slide_in_layout = QHBoxLayout()
        slide_in_label = QLabel("Slide In:")
        slide_in_label.setStyleSheet("font-weight: 600;")
        slide_in_layout.addWidget(slide_in_label)
        
        slide_in_up = Button("From Bottom", size=Button.SIZE_SM)
        slide_in_up.clicked.connect(self._play_slide_in_up)
        slide_in_layout.addWidget(slide_in_up)
        
        slide_in_down = Button("From Top", size=Button.SIZE_SM)
        slide_in_down.clicked.connect(self._play_slide_in_down)
        slide_in_layout.addWidget(slide_in_down)
        
        slide_in_left = Button("From Right", size=Button.SIZE_SM)
        slide_in_left.clicked.connect(self._play_slide_in_left)
        slide_in_layout.addWidget(slide_in_left)
        
        slide_in_right = Button("From Left", size=Button.SIZE_SM)
        slide_in_right.clicked.connect(self._play_slide_in_right)
        slide_in_layout.addWidget(slide_in_right)
        
        slide_in_layout.addStretch()
        layout.addLayout(slide_in_layout)
        
        # Slide Out
        slide_out_layout = QHBoxLayout()
        slide_out_label = QLabel("Slide Out:")
        slide_out_label.setStyleSheet("font-weight: 600;")
        slide_out_layout.addWidget(slide_out_label)
        
        slide_out_up = Button("To Top", size=Button.SIZE_SM)
        slide_out_up.clicked.connect(self._play_slide_out_up)
        slide_out_layout.addWidget(slide_out_up)
        
        slide_out_down = Button("To Bottom", size=Button.SIZE_SM)
        slide_out_down.clicked.connect(self._play_slide_out_down)
        slide_out_layout.addWidget(slide_out_down)
        
        slide_out_left = Button("To Left", size=Button.SIZE_SM)
        slide_out_left.clicked.connect(self._play_slide_out_left)
        slide_out_layout.addWidget(slide_out_left)
        
        slide_out_right = Button("To Right", size=Button.SIZE_SM)
        slide_out_right.clicked.connect(self._play_slide_out_right)
        slide_out_layout.addWidget(slide_out_right)
        
        slide_out_layout.addStretch()
        layout.addLayout(slide_out_layout)
        
        return group
    
    def _create_scale_section(self) -> QGroupBox:
        """Create scale animation controls."""
        group = QGroupBox("Scale Animations")
        layout = QHBoxLayout(group)
        layout.setSpacing(12)
        
        scale_in_btn = Button("Scale In")
        scale_in_btn.clicked.connect(self._play_scale_in)
        layout.addWidget(scale_in_btn)
        
        scale_out_btn = Button("Scale Out")
        scale_out_btn.clicked.connect(self._play_scale_out)
        layout.addWidget(scale_out_btn)
        
        layout.addStretch()
        
        return group
    
    # Animation methods
    def _play_fade_in(self):
        """Play fade in animation."""
        animation = FadeIn(self.animation_target, duration=500)
        animation.start()
    
    def _play_fade_out(self):
        """Play fade out animation."""
        animation = FadeOut(self.animation_target, duration=500)
        animation.start()
    
    def _play_slide_in_up(self):
        """Play slide in from bottom animation."""
        animation = SlideInUp(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_in_down(self):
        """Play slide in from top animation."""
        animation = SlideInDown(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_in_left(self):
        """Play slide in from right animation."""
        animation = SlideInLeft(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_in_right(self):
        """Play slide in from left animation."""
        animation = SlideInRight(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_out_up(self):
        """Play slide out to top animation."""
        animation = SlideOutUp(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_out_down(self):
        """Play slide out to bottom animation."""
        animation = SlideOutDown(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_out_left(self):
        """Play slide out to left animation."""
        animation = SlideOutLeft(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_slide_out_right(self):
        """Play slide out to right animation."""
        animation = SlideOutRight(self.animation_target, duration=500, distance=100)
        animation.start()
    
    def _play_scale_in(self):
        """Play scale in animation."""
        animation = ScaleIn(self.animation_target, duration=500)
        animation.start()
    
    def _play_scale_out(self):
        """Play scale out animation."""
        animation = ScaleOut(self.animation_target, duration=500)
        animation.start()


def main():
    """Run the demo application."""
    app = QApplication(sys.argv)
    
    window = AnimationsDemo()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
