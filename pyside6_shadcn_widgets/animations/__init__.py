"""
Animations Module
~~~~~~~~~~~~~~~~~

Smooth animations for PySide6 widgets.
"""

from pyside6_shadcn_widgets.animations.fade import FadeIn, FadeOut
from pyside6_shadcn_widgets.animations.slide import (
    SlideInUp,
    SlideInDown,
    SlideInLeft,
    SlideInRight,
    SlideOutUp,
    SlideOutDown,
    SlideOutLeft,
    SlideOutRight,
)
from pyside6_shadcn_widgets.animations.scale import ScaleIn, ScaleOut

__all__ = [
    "FadeIn",
    "FadeOut",
    "SlideInUp",
    "SlideInDown",
    "SlideInLeft",
    "SlideInRight",
    "SlideOutUp",
    "SlideOutDown",
    "SlideOutLeft",
    "SlideOutRight",
    "ScaleIn",
    "ScaleOut",
]
