# PySide6-Shadcn-Widgets

A modern, production-ready UI library for PySide6 that replicates the beautiful components and smooth animations from [shadcn/ui](https://ui.shadcn.com/).

## ✨ Features

- 🎨 **10+ Modern Components** - Button, Card, Input, Select, Dialog, Tabs, Badge, CheckBox, Switch, Progress
- 🎬 **Smooth Animations** - Fade, Slide, and Scale animations with customizable easing curves
- 🌗 **Theme System** - Built-in light and dark themes with easy customization
- 💅 **shadcn/ui Styling** - Matches the aesthetic of shadcn/ui with HSL color system
- 🔧 **Type Hints** - Full type annotations for better IDE support
- 📚 **Well Documented** - Comprehensive docstrings and examples
- ⚡ **60fps Animations** - Smooth animations using QPropertyAnimation
- ♿ **Accessible** - Proper focus indicators and keyboard navigation

## 📦 Installation

```bash
pip install pyside6-shadcn-widgets
```

Or install from source:

```bash
git clone https://github.com/majuch/PySide6-Shadcn-Widgets.git
cd PySide6-Shadcn-Widgets
pip install -e .
```

## 🚀 Quick Start

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from pyside6_shadcn_widgets.components import Button, Card, Input
from pyside6_shadcn_widgets.themes import LightTheme

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Apply theme
        theme = LightTheme()
        theme.apply()
        
        # Create UI
        central = QWidget()
        layout = QVBoxLayout(central)
        
        # Add components
        card = Card()
        card.set_header("Welcome")
        card.set_content("This is a modern card component!")
        
        button = Button("Click me!", variant=Button.VARIANT_DEFAULT)
        button.clicked.connect(lambda: print("Button clicked!"))
        
        input_field = Input(placeholder="Enter your name...")
        
        layout.addWidget(card)
        layout.addWidget(button)
        layout.addWidget(input_field)
        
        self.setCentralWidget(central)

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())
```

## 📖 Components

### Button

Modern button with multiple variants and sizes, featuring smooth hover and click animations.

**Variants:** `default`, `destructive`, `outline`, `ghost`, `link`  
**Sizes:** `sm`, `md`, `lg`

```python
from pyside6_shadcn_widgets.components import Button

# Create buttons with different variants
btn_default = Button("Default", variant=Button.VARIANT_DEFAULT)
btn_destructive = Button("Delete", variant=Button.VARIANT_DESTRUCTIVE)
btn_outline = Button("Outline", variant=Button.VARIANT_OUTLINE)
btn_ghost = Button("Ghost", variant=Button.VARIANT_GHOST)

# Different sizes
btn_small = Button("Small", size=Button.SIZE_SM)
btn_large = Button("Large", size=Button.SIZE_LG)

# Connect to signals
btn_default.clicked.connect(lambda: print("Clicked!"))
```

### Card

Container component with header, content, and footer sections, featuring hover elevation effect.

```python
from pyside6_shadcn_widgets.components import Card

card = Card()
card.set_header("Card Title")
card.set_content("Your card content goes here")
card.set_footer("Card footer")
```

### Input

Modern input field with focus animations, error states, and placeholder styling.

```python
from pyside6_shadcn_widgets.components import Input

input_field = Input(placeholder="Enter email...")

# Set error state
input_field.set_error(True)

# Check if has error
if input_field.has_error():
    print("Input has an error!")
```

### Badge

Small label component with multiple variants and sizes.

**Variants:** `default`, `secondary`, `destructive`, `outline`  
**Sizes:** `sm`, `md`, `lg`

```python
from pyside6_shadcn_widgets.components import Badge

badge = Badge("New", variant=Badge.VARIANT_DEFAULT)
badge_secondary = Badge("Beta", variant=Badge.VARIANT_SECONDARY)
badge_pill = Badge("v1.0", pill=True)
```

### CheckBox

Custom checkbox with smooth check animation and modern styling.

```python
from pyside6_shadcn_widgets.components import CheckBox

checkbox = CheckBox("Accept terms and conditions")
checkbox.setChecked(True)
```

### Switch

Toggle switch with smooth sliding animation and color transitions.

```python
from pyside6_shadcn_widgets.components import Switch

switch = Switch()
switch.setChecked(True)
switch.toggled.connect(lambda checked: print(f"Switch: {checked}"))
```

### Progress

Progress bar with smooth value transitions and indeterminate/loading state.

**Variants:** `default`, `success`, `warning`, `destructive`

```python
from pyside6_shadcn_widgets.components import Progress

progress = Progress()
progress.setValue(75)

# Indeterminate state
progress_loading = Progress()
progress_loading.set_indeterminate(True)
```

### Select

Custom styled dropdown with smooth animations and keyboard navigation.

```python
from pyside6_shadcn_widgets.components import Select

select = Select()
select.addItems(["Option 1", "Option 2", "Option 3"])
select.currentTextChanged.connect(lambda text: print(f"Selected: {text}"))
```

### Dialog

Modal dialog with backdrop, fade and scale animations, and support for header/content/footer.

```python
from pyside6_shadcn_widgets.components import Dialog, Button

dialog = Dialog()
dialog.set_header("Confirm Action")
dialog.set_content("Are you sure you want to continue?")

close_btn = Button("Close")
close_btn.clicked.connect(dialog.close)
dialog.set_footer(close_btn)

dialog.exec()
```

### Tabs

Tab component with animated sliding indicator and smooth content transitions.

```python
from pyside6_shadcn_widgets.components import Tabs
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

tabs = Tabs()

tab1 = QWidget()
layout1 = QVBoxLayout(tab1)
layout1.addWidget(QLabel("Tab 1 Content"))

tab2 = QWidget()
layout2 = QVBoxLayout(tab2)
layout2.addWidget(QLabel("Tab 2 Content"))

tabs.addTab(tab1, "General")
tabs.addTab(tab2, "Advanced")
```

## 🎬 Animations

All animations use PySide6's QPropertyAnimation with smooth easing curves.

### Fade Animations

```python
from pyside6_shadcn_widgets.animations import FadeIn, FadeOut

# Fade in
fade_in = FadeIn(widget, duration=300)
fade_in.start()

# Fade out
fade_out = FadeOut(widget, duration=300)
fade_out.start()
```

### Slide Animations

```python
from pyside6_shadcn_widgets.animations import (
    SlideInUp, SlideInDown, SlideInLeft, SlideInRight,
    SlideOutUp, SlideOutDown, SlideOutLeft, SlideOutRight
)

# Slide in from bottom
slide_in = SlideInUp(widget, duration=300, distance=50)
slide_in.start()

# Slide out to top
slide_out = SlideOutUp(widget, duration=300, distance=50)
slide_out.start()
```

### Scale Animations

```python
from pyside6_shadcn_widgets.animations import ScaleIn, ScaleOut

# Scale in (95% to 100%)
scale_in = ScaleIn(widget, duration=300)
scale_in.start()

# Scale out (100% to 95%)
scale_out = ScaleOut(widget, duration=300)
scale_out.start()
```

## 🌗 Themes

Built-in light and dark themes with HSL color system matching shadcn/ui.

### Using Built-in Themes

```python
from pyside6_shadcn_widgets.themes import LightTheme, DarkTheme

# Apply light theme
light_theme = LightTheme()
light_theme.apply()

# Apply dark theme
dark_theme = DarkTheme()
dark_theme.apply()
```

### Custom Theme

```python
from pyside6_shadcn_widgets.themes import Theme

class CustomTheme(Theme):
    def __init__(self):
        super().__init__()
        # Override colors (HSL format)
        self.colors = {
            "background": (0, 0, 100),
            "foreground": (222.2, 84, 4.9),
            "primary": (200, 70, 50),  # Custom primary color
            # ... other colors
        }

# Apply custom theme
custom_theme = CustomTheme()
custom_theme.apply()
```

### Theme Switching

```python
from pyside6_shadcn_widgets.components import Switch
from pyside6_shadcn_widgets.themes import LightTheme, DarkTheme

light_theme = LightTheme()
dark_theme = DarkTheme()

switch = Switch()
switch.toggled.connect(lambda dark: dark_theme.apply() if dark else light_theme.apply())
```

## 🛠️ Utilities

### Color Conversion

```python
from pyside6_shadcn_widgets.utils.colors import hsl_to_rgb, rgb_to_hex, hsl_to_hex

# Convert HSL to RGB
r, g, b = hsl_to_rgb(222.2, 84, 4.9)

# Convert RGB to hex
hex_color = rgb_to_hex(255, 100, 50)

# Convert HSL directly to hex
hex_color = hsl_to_hex(222.2, 84, 4.9)

# Adjust lightness
new_hsl = adjust_lightness(222.2, 84, 4.9, amount=10)
```

## 📋 Examples

Check out the `examples/` directory for complete working examples:

- **basic_components.py** - Showcase of all components
- **animations_demo.py** - Interactive animation demonstrations
- **theme_switcher.py** - Light/dark theme switching demo

Run an example:

```bash
python examples/basic_components.py
```

## 🎨 Design Philosophy

This library follows the design principles of shadcn/ui:

- **Consistent spacing**: 4px base unit (multiples of 4)
- **Border radius**: 6px (small), 8px (medium), 12px (large)
- **Subtle shadows**: Using QGraphicsDropShadowEffect
- **HSL color system**: Easy color manipulation
- **Smooth animations**: 60fps with proper easing curves
- **Accessibility**: Focus indicators and keyboard navigation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [shadcn/ui](https://ui.shadcn.com/) by [@shadcn](https://twitter.com/shadcn)
- Built with [PySide6](https://doc.qt.io/qtforpython/)

## 📧 Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

Made with ❤️ by the PySide6-Shadcn-Widgets community
