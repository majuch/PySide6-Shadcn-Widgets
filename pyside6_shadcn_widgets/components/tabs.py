"""
Tabs component for PySide6 Shadcn Widgets.
"""

from typing import Optional, List
from PySide6.QtWidgets import QTabWidget, QWidget, QTabBar, QStylePainter, QStyleOptionTab, QStyle
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property, QRect, Signal
from PySide6.QtGui import QPainter, QColor, QPen


class Tabs(QTabWidget):
    """
    Modern tabs component with animated indicator.
    
    Features smooth content transition and sliding indicator between tabs.
    
    Example:
        >>> tabs = Tabs()
        >>> tabs.addTab(QWidget(), "Tab 1")
        >>> tabs.addTab(QWidget(), "Tab 2")
        >>> tabs.addTab(QWidget(), "Tab 3")
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize tabs component.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        
        self._indicator_position = 0
        self._indicator_width = 0
        
        # Setup tabs
        self._setup_ui()
        self._setup_animations()
        self._apply_styles()
        
        # Connect signals
        self.currentChanged.connect(self._on_tab_changed)
    
    def _setup_ui(self) -> None:
        """Setup tabs UI."""
        # Use custom tab bar
        self.setTabBar(QTabBar(self))
        self.tabBar().setExpanding(False)
        self.tabBar().setDrawBase(False)
    
    def _setup_animations(self) -> None:
        """Setup tab change animation."""
        self.indicator_animation = QPropertyAnimation(self, b"indicatorPosition")
        self.indicator_animation.setDuration(250)
        self.indicator_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        self.width_animation = QPropertyAnimation(self, b"indicatorWidth")
        self.width_animation.setDuration(250)
        self.width_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles to tabs."""
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 8px;
                background-color: hsl(0, 0%, 100%);
                padding: 16px;
                top: -1px;
            }
            QTabWidget::tab-bar {
                alignment: left;
            }
            QTabBar::tab {
                background-color: transparent;
                color: hsl(215.4, 16.3%, 46.9%);
                padding: 12px 16px;
                font-size: 14px;
                font-weight: 500;
                border: none;
                border-bottom: 2px solid transparent;
                margin-right: 8px;
            }
            QTabBar::tab:hover {
                color: hsl(222.2, 84%, 4.9%);
            }
            QTabBar::tab:selected {
                color: hsl(222.2, 84%, 4.9%);
            }
        """)
    
    def _on_tab_changed(self, index: int) -> None:
        """
        Handle tab change to animate indicator.
        
        Args:
            index: New tab index
        """
        if index < 0:
            return
        
        # Get tab bar
        tab_bar = self.tabBar()
        
        # Calculate new indicator position and width
        tab_rect = tab_bar.tabRect(index)
        new_position = tab_rect.x()
        new_width = tab_rect.width()
        
        # Animate indicator
        self.indicator_animation.stop()
        self.indicator_animation.setStartValue(self._indicator_position)
        self.indicator_animation.setEndValue(new_position)
        self.indicator_animation.start()
        
        self.width_animation.stop()
        self.width_animation.setStartValue(self._indicator_width)
        self.width_animation.setEndValue(new_width)
        self.width_animation.start()
    
    def showEvent(self, event) -> None:
        """Handle show event to initialize indicator."""
        super().showEvent(event)
        
        # Initialize indicator position
        if self.count() > 0:
            tab_bar = self.tabBar()
            tab_rect = tab_bar.tabRect(self.currentIndex())
            self._indicator_position = tab_rect.x()
            self._indicator_width = tab_rect.width()
    
    def paintEvent(self, event) -> None:
        """Custom paint event to draw indicator."""
        super().paintEvent(event)
        
        # Draw animated indicator under active tab
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Get tab bar geometry
        tab_bar = self.tabBar()
        tab_bar_height = tab_bar.height()
        
        # Draw indicator
        indicator_color = QColor(2, 12, 27)  # hsl(222.2, 47.4%, 11.2%)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(indicator_color)
        
        indicator_rect = QRect(
            int(self._indicator_position),
            tab_bar_height - 3,
            int(self._indicator_width),
            3
        )
        painter.drawRoundedRect(indicator_rect, 2, 2)
    
    def get_indicator_position(self) -> float:
        """Get current indicator position."""
        return self._indicator_position
    
    def set_indicator_position(self, position: float) -> None:
        """
        Set indicator position.
        
        Args:
            position: X position of indicator
        """
        self._indicator_position = position
        self.update()
    
    indicatorPosition = Property(float, get_indicator_position, set_indicator_position)
    
    def get_indicator_width(self) -> float:
        """Get current indicator width."""
        return self._indicator_width
    
    def set_indicator_width(self, width: float) -> None:
        """
        Set indicator width.
        
        Args:
            width: Width of indicator
        """
        self._indicator_width = width
        self.update()
    
    indicatorWidth = Property(float, get_indicator_width, set_indicator_width)
