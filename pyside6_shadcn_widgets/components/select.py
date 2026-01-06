"""
Select/Dropdown component for PySide6 Shadcn Widgets.
"""

from typing import Optional, List
from PySide6.QtWidgets import QComboBox, QWidget, QListView, QStyledItemDelegate
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Signal
from PySide6.QtGui import QCursor


class Select(QComboBox):
    """
    Custom styled dropdown matching shadcn/ui design.
    
    Features smooth dropdown animation and modern styling.
    
    Example:
        >>> select = Select()
        >>> select.addItems(["Option 1", "Option 2", "Option 3"])
        >>> select.currentTextChanged.connect(lambda text: print(f"Selected: {text}"))
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize select component.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        
        # Setup select
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self) -> None:
        """Setup select UI elements."""
        # Set minimum height
        self.setMinimumHeight(40)
        
        # Setup list view for dropdown
        list_view = QListView(self)
        list_view.setStyleSheet("""
            QListView {
                background-color: hsl(0, 0%, 100%);
                border: 1px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 8px;
                padding: 4px;
                outline: none;
            }
            QListView::item {
                padding: 8px 12px;
                border-radius: 6px;
                color: hsl(222.2, 84%, 4.9%);
            }
            QListView::item:hover {
                background-color: hsl(210, 40%, 96.1%);
            }
            QListView::item:selected {
                background-color: hsl(210, 40%, 96.1%);
                color: hsl(222.2, 84%, 4.9%);
            }
        """)
        self.setView(list_view)
    
    def _apply_styles(self) -> None:
        """Apply QSS styles to select."""
        self.setStyleSheet("""
            QComboBox {
                background-color: hsl(0, 0%, 100%);
                color: hsl(222.2, 84%, 4.9%);
                border: 1px solid hsl(214.3, 31.8%, 91.4%);
                border-radius: 8px;
                padding: 8px 16px;
                padding-right: 32px;
                font-size: 14px;
                min-height: 40px;
            }
            QComboBox:hover {
                border-color: hsl(222.2, 84%, 4.9%);
            }
            QComboBox:focus {
                border: 2px solid hsl(222.2, 84%, 4.9%);
            }
            QComboBox::drop-down {
                border: none;
                width: 32px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid hsl(222.2, 84%, 4.9%);
                margin-right: 8px;
            }
            QComboBox:disabled {
                background-color: hsl(210, 40%, 96.1%);
                color: hsl(215.4, 16.3%, 46.9%);
            }
        """)
    
    def showPopup(self) -> None:
        """Override to add smooth popup animation."""
        super().showPopup()
        
        # Get popup widget
        popup = self.view().parentWidget()
        if popup:
            # Set initial position slightly higher
            pos = popup.pos()
            popup.move(pos.x(), pos.y() - 10)
            
            # Animate to final position
            animation = QPropertyAnimation(popup, b"pos")
            animation.setDuration(200)
            animation.setStartValue(popup.pos())
            animation.setEndValue(pos)
            animation.setEasingCurve(QEasingCurve.Type.OutCubic)
            animation.start()
