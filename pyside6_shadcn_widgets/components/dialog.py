"""
Dialog/Modal component for PySide6 Shadcn Widgets.
"""

from typing import Optional
from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, Signal
from PySide6.QtWidgets import QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class Dialog(QDialog):
    """
    Modern dialog/modal with backdrop and smooth animations.
    
    Features fade and scale entrance animations, backdrop click to close,
    and header, content, footer sections.
    
    Example:
        >>> dialog = Dialog()
        >>> dialog.set_header("Dialog Title")
        >>> dialog.set_content(QLabel("Dialog content"))
        >>> dialog.set_footer(QPushButton("Close"))
        >>> dialog.exec()
    """
    
    closed = Signal()
    
    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize dialog component.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        
        # Setup dialog
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self._setup_ui()
        self._setup_animations()
    
    def _setup_ui(self) -> None:
        """Setup dialog UI structure."""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Backdrop
        self.backdrop = QFrame(self)
        self.backdrop.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 0.5);
            }
        """)
        self.backdrop.mousePressEvent = lambda e: self.close()
        
        # Content container
        self.content_container = QFrame(self)
        self.content_container.setStyleSheet("""
            QFrame {
                background-color: hsl(0, 0%, 100%);
                border-radius: 12px;
            }
        """)
        self.content_container.setMinimumWidth(400)
        self.content_container.setMaximumWidth(600)
        
        # Add shadow to content container
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(24)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 8)
        self.content_container.setGraphicsEffect(shadow)
        
        # Content layout
        content_layout = QVBoxLayout(self.content_container)
        content_layout.setContentsMargins(24, 24, 24, 24)
        content_layout.setSpacing(16)
        
        # Header section
        self.header_widget = QWidget()
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_widget.setStyleSheet("""
            QLabel {
                color: hsl(222.2, 84%, 4.9%);
                font-size: 18px;
                font-weight: 600;
            }
        """)
        self.header_widget.hide()
        
        # Content section
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_widget.setStyleSheet("""
            QLabel {
                color: hsl(222.2, 84%, 4.9%);
                font-size: 14px;
            }
        """)
        
        # Footer section
        self.footer_widget = QWidget()
        self.footer_layout = QHBoxLayout(self.footer_widget)
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_widget.hide()
        
        # Add sections
        content_layout.addWidget(self.header_widget)
        content_layout.addWidget(self.content_widget)
        content_layout.addWidget(self.footer_widget)
        
        # Layout for centering content container
        center_layout = QVBoxLayout()
        center_layout.addStretch()
        center_layout.addWidget(self.content_container, alignment=Qt.AlignmentFlag.AlignCenter)
        center_layout.addStretch()
        
        main_layout.addLayout(center_layout)
    
    def _setup_animations(self) -> None:
        """Setup entrance and exit animations."""
        # Backdrop fade animation
        self.backdrop_effect = QGraphicsOpacityEffect(self.backdrop)
        self.backdrop.setGraphicsEffect(self.backdrop_effect)
        
        self.backdrop_animation = QPropertyAnimation(self.backdrop_effect, b"opacity")
        self.backdrop_animation.setDuration(300)
        self.backdrop_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Content scale animation
        self.content_effect = QGraphicsOpacityEffect(self.content_container)
        self.content_container.setGraphicsEffect(self.content_effect)
        
        self.content_fade = QPropertyAnimation(self.content_effect, b"opacity")
        self.content_fade.setDuration(300)
        self.content_fade.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Combined animation group
        self.entrance_group = QParallelAnimationGroup()
        self.entrance_group.addAnimation(self.backdrop_animation)
        self.entrance_group.addAnimation(self.content_fade)
    
    def showEvent(self, event) -> None:
        """Handle show event with entrance animation."""
        super().showEvent(event)
        
        # Resize backdrop to fill parent
        if self.parent():
            self.backdrop.setGeometry(self.rect())
        
        # Animate entrance
        self.backdrop_animation.setStartValue(0.0)
        self.backdrop_animation.setEndValue(1.0)
        
        self.content_fade.setStartValue(0.0)
        self.content_fade.setEndValue(1.0)
        
        self.entrance_group.start()
    
    def closeEvent(self, event) -> None:
        """Handle close event."""
        self.closed.emit()
        super().closeEvent(event)
    
    def set_header(self, widget_or_text) -> None:
        """
        Set dialog header content.
        
        Args:
            widget_or_text: QWidget or string for header
        """
        # Clear existing header
        while self.header_layout.count():
            item = self.header_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new header
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            self.header_layout.addWidget(label)
        else:
            self.header_layout.addWidget(widget_or_text)
        
        self.header_widget.show()
    
    def set_content(self, widget_or_text) -> None:
        """
        Set dialog content.
        
        Args:
            widget_or_text: QWidget or string for content
        """
        # Clear existing content
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new content
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            label.setWordWrap(True)
            self.content_layout.addWidget(label)
        else:
            self.content_layout.addWidget(widget_or_text)
    
    def set_footer(self, widget_or_text) -> None:
        """
        Set dialog footer content.
        
        Args:
            widget_or_text: QWidget or string for footer
        """
        # Clear existing footer
        while self.footer_layout.count():
            item = self.footer_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new footer
        if isinstance(widget_or_text, str):
            label = QLabel(widget_or_text)
            self.footer_layout.addWidget(label)
        else:
            self.footer_layout.addWidget(widget_or_text)
        
        self.footer_widget.show()
    
    def resizeEvent(self, event) -> None:
        """Handle resize event to adjust backdrop."""
        super().resizeEvent(event)
        self.backdrop.setGeometry(self.rect())
