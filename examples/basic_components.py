"""
Basic Components Demo

This example showcases all the components from PySide6 Shadcn Widgets.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QScrollArea, QGroupBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt

from pyside6_shadcn_widgets.components import (
    Button, Card, Input, Badge, CheckBox, Switch, Progress, Select, Dialog, Tabs
)
from pyside6_shadcn_widgets.themes import LightTheme


class BasicComponentsDemo(QMainWindow):
    """Main demo window showcasing all components."""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PySide6 Shadcn Widgets - Basic Components Demo")
        self.setMinimumSize(1000, 800)
        
        # Apply theme
        self.theme = LightTheme()
        self.theme.apply()
        
        # Setup UI
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the main UI."""
        # Central widget with scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Main container
        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setSpacing(24)
        main_layout.setContentsMargins(32, 32, 32, 32)
        
        # Title
        title = QLabel("PySide6 Shadcn Widgets")
        title.setStyleSheet("font-size: 32px; font-weight: 700; color: hsl(222.2, 84%, 4.9%);")
        main_layout.addWidget(title)
        
        subtitle = QLabel("Modern UI components inspired by shadcn/ui")
        subtitle.setStyleSheet("font-size: 16px; color: hsl(215.4, 16.3%, 46.9%);")
        main_layout.addWidget(subtitle)
        
        main_layout.addSpacing(16)
        
        # Add component sections
        main_layout.addWidget(self._create_button_section())
        main_layout.addWidget(self._create_input_section())
        main_layout.addWidget(self._create_card_section())
        main_layout.addWidget(self._create_badge_section())
        main_layout.addWidget(self._create_checkbox_switch_section())
        main_layout.addWidget(self._create_progress_section())
        main_layout.addWidget(self._create_select_section())
        main_layout.addWidget(self._create_tabs_section())
        
        main_layout.addStretch()
        
        scroll.setWidget(container)
        self.setCentralWidget(scroll)
    
    def _create_button_section(self) -> QGroupBox:
        """Create button showcase section."""
        group = QGroupBox("Buttons")
        layout = QVBoxLayout(group)
        layout.setSpacing(16)
        
        # Button variants
        variants_label = QLabel("Variants:")
        variants_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(variants_label)
        
        variants_layout = QHBoxLayout()
        variants_layout.setSpacing(12)
        
        btn_default = Button("Default", variant=Button.VARIANT_DEFAULT)
        btn_destructive = Button("Destructive", variant=Button.VARIANT_DESTRUCTIVE)
        btn_outline = Button("Outline", variant=Button.VARIANT_OUTLINE)
        btn_ghost = Button("Ghost", variant=Button.VARIANT_GHOST)
        btn_link = Button("Link", variant=Button.VARIANT_LINK)
        
        for btn in [btn_default, btn_destructive, btn_outline, btn_ghost, btn_link]:
            btn.clicked.connect(lambda checked, b=btn: print(f"Clicked: {b.text()}"))
            variants_layout.addWidget(btn)
        
        variants_layout.addStretch()
        layout.addLayout(variants_layout)
        
        # Button sizes
        sizes_label = QLabel("Sizes:")
        sizes_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(sizes_label)
        
        sizes_layout = QHBoxLayout()
        sizes_layout.setSpacing(12)
        
        btn_sm = Button("Small", size=Button.SIZE_SM)
        btn_md = Button("Medium", size=Button.SIZE_MD)
        btn_lg = Button("Large", size=Button.SIZE_LG)
        
        for btn in [btn_sm, btn_md, btn_lg]:
            sizes_layout.addWidget(btn)
        
        sizes_layout.addStretch()
        layout.addLayout(sizes_layout)
        
        return group
    
    def _create_input_section(self) -> QGroupBox:
        """Create input showcase section."""
        group = QGroupBox("Input Fields")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        # Normal input
        input1 = Input(placeholder="Enter your email...")
        layout.addWidget(input1)
        
        # Error state input
        input2 = Input(placeholder="This field has an error")
        input2.set_error(True)
        layout.addWidget(input2)
        
        # Disabled input
        input3 = Input(placeholder="Disabled input")
        input3.setDisabled(True)
        layout.addWidget(input3)
        
        return group
    
    def _create_card_section(self) -> QGroupBox:
        """Create card showcase section."""
        group = QGroupBox("Cards")
        layout = QHBoxLayout(group)
        layout.setSpacing(16)
        
        # Card 1
        card1 = Card()
        card1.set_header("Card Title")
        card1.set_content("This is a card component with header, content, and footer. Hover over it to see the elevation effect.")
        card1.set_footer("Card footer")
        layout.addWidget(card1)
        
        # Card 2
        card2 = Card()
        card2.set_header("Another Card")
        card2.set_content("Cards can contain any widget as content, not just text.")
        layout.addWidget(card2)
        
        layout.addStretch()
        
        return group
    
    def _create_badge_section(self) -> QGroupBox:
        """Create badge showcase section."""
        group = QGroupBox("Badges")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        # Badge variants
        variants_label = QLabel("Variants:")
        variants_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(variants_label)
        
        variants_layout = QHBoxLayout()
        variants_layout.setSpacing(8)
        
        badge1 = Badge("Default", variant=Badge.VARIANT_DEFAULT)
        badge2 = Badge("Secondary", variant=Badge.VARIANT_SECONDARY)
        badge3 = Badge("Destructive", variant=Badge.VARIANT_DESTRUCTIVE)
        badge4 = Badge("Outline", variant=Badge.VARIANT_OUTLINE)
        
        for badge in [badge1, badge2, badge3, badge4]:
            variants_layout.addWidget(badge)
        
        variants_layout.addStretch()
        layout.addLayout(variants_layout)
        
        # Badge sizes
        sizes_label = QLabel("Sizes:")
        sizes_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(sizes_label)
        
        sizes_layout = QHBoxLayout()
        sizes_layout.setSpacing(8)
        
        badge_sm = Badge("Small", size=Badge.SIZE_SM)
        badge_md = Badge("Medium", size=Badge.SIZE_MD)
        badge_lg = Badge("Large", size=Badge.SIZE_LG)
        
        for badge in [badge_sm, badge_md, badge_lg]:
            sizes_layout.addWidget(badge)
        
        sizes_layout.addStretch()
        layout.addLayout(sizes_layout)
        
        return group
    
    def _create_checkbox_switch_section(self) -> QGroupBox:
        """Create checkbox and switch showcase section."""
        group = QGroupBox("Checkbox & Switch")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        # Checkboxes
        checkbox_label = QLabel("Checkboxes:")
        checkbox_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(checkbox_label)
        
        checkbox1 = CheckBox("Accept terms and conditions")
        checkbox2 = CheckBox("Subscribe to newsletter")
        checkbox2.setChecked(True)
        
        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)
        
        layout.addSpacing(8)
        
        # Switches
        switch_label = QLabel("Switches:")
        switch_label.setStyleSheet("font-weight: 600;")
        layout.addWidget(switch_label)
        
        switch_layout = QHBoxLayout()
        switch_layout.setSpacing(16)
        
        switch1 = Switch()
        switch1.toggled.connect(lambda checked: print(f"Switch 1: {checked}"))
        
        switch2 = Switch()
        switch2.setChecked(True)
        switch2.toggled.connect(lambda checked: print(f"Switch 2: {checked}"))
        
        switch_layout.addWidget(QLabel("Enable notifications:"))
        switch_layout.addWidget(switch1)
        switch_layout.addSpacing(32)
        switch_layout.addWidget(QLabel("Dark mode:"))
        switch_layout.addWidget(switch2)
        switch_layout.addStretch()
        
        layout.addLayout(switch_layout)
        
        return group
    
    def _create_progress_section(self) -> QGroupBox:
        """Create progress bar showcase section."""
        group = QGroupBox("Progress Bars")
        layout = QVBoxLayout(group)
        layout.setSpacing(16)
        
        # Different progress values
        progress1 = Progress()
        progress1.setValue(25)
        layout.addWidget(QLabel("25% Progress:"))
        layout.addWidget(progress1)
        
        progress2 = Progress()
        progress2.setValue(60)
        layout.addWidget(QLabel("60% Progress:"))
        layout.addWidget(progress2)
        
        progress3 = Progress()
        progress3.setValue(90)
        layout.addWidget(QLabel("90% Progress:"))
        layout.addWidget(progress3)
        
        # Indeterminate progress
        progress4 = Progress()
        progress4.set_indeterminate(True)
        layout.addWidget(QLabel("Indeterminate (Loading):"))
        layout.addWidget(progress4)
        
        return group
    
    def _create_select_section(self) -> QGroupBox:
        """Create select/dropdown showcase section."""
        group = QGroupBox("Select / Dropdown")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        select = Select()
        select.addItems([
            "Select an option...",
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4",
            "Option 5",
        ])
        select.currentTextChanged.connect(lambda text: print(f"Selected: {text}"))
        
        layout.addWidget(select)
        
        return group
    
    def _create_tabs_section(self) -> QGroupBox:
        """Create tabs showcase section."""
        group = QGroupBox("Tabs")
        layout = QVBoxLayout(group)
        
        tabs = Tabs()
        
        # Tab 1
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel("Content for Tab 1"))
        tab1_layout.addWidget(QLabel("This is the first tab with some content."))
        tab1_layout.addStretch()
        
        # Tab 2
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel("Content for Tab 2"))
        tab2_layout.addWidget(QLabel("This is the second tab."))
        tab2_layout.addStretch()
        
        # Tab 3
        tab3 = QWidget()
        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(QLabel("Content for Tab 3"))
        tab3_layout.addWidget(QLabel("This is the third tab."))
        tab3_layout.addStretch()
        
        tabs.addTab(tab1, "General")
        tabs.addTab(tab2, "Settings")
        tabs.addTab(tab3, "Advanced")
        
        layout.addWidget(tabs)
        
        # Add dialog button
        dialog_btn = Button("Open Dialog", variant=Button.VARIANT_DEFAULT)
        dialog_btn.clicked.connect(self._show_dialog)
        layout.addWidget(dialog_btn)
        
        return group
    
    def _show_dialog(self):
        """Show a dialog example."""
        dialog = Dialog(self)
        dialog.set_header("Dialog Title")
        dialog.set_content("This is a dialog with backdrop and smooth animations. Click outside to close.")
        
        close_btn = Button("Close", variant=Button.VARIANT_OUTLINE)
        close_btn.clicked.connect(dialog.close)
        dialog.set_footer(close_btn)
        
        dialog.exec()


def main():
    """Run the demo application."""
    app = QApplication(sys.argv)
    
    window = BasicComponentsDemo()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
