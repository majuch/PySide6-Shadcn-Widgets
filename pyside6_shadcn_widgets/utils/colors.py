"""
Color utilities for converting between HSL, RGB, and HEX color formats.
"""

import colorsys
from typing import Tuple


def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """
    Convert HSL color values to RGB.
    
    Args:
        h: Hue (0-360 degrees)
        s: Saturation (0-100 percent)
        l: Lightness (0-100 percent)
        
    Returns:
        Tuple of (r, g, b) values in range 0-255
        
    Example:
        >>> hsl_to_rgb(222.2, 84, 4.9)
        (2, 7, 23)
    """
    # Normalize values
    h_normalized = h / 360.0
    s_normalized = s / 100.0
    l_normalized = l / 100.0
    
    # Convert using colorsys
    r, g, b = colorsys.hls_to_rgb(h_normalized, l_normalized, s_normalized)
    
    # Convert to 0-255 range
    return (int(r * 255), int(g * 255), int(b * 255))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to hexadecimal color string.
    
    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        
    Returns:
        Hexadecimal color string (e.g., "#ff5733")
        
    Example:
        >>> rgb_to_hex(255, 87, 51)
        "#ff5733"
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert hexadecimal color string to RGB values.
    
    Args:
        hex_color: Hexadecimal color string (e.g., "#ff5733" or "ff5733")
        
    Returns:
        Tuple of (r, g, b) values in range 0-255
        
    Example:
        >>> hex_to_rgb("#ff5733")
        (255, 87, 51)
    """
    # Remove '#' if present
    hex_color = hex_color.lstrip('#')
    
    # Convert to RGB
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def hsl_to_hex(h: float, s: float, l: float) -> str:
    """
    Convert HSL color values directly to hexadecimal color string.
    
    Args:
        h: Hue (0-360 degrees)
        s: Saturation (0-100 percent)
        l: Lightness (0-100 percent)
        
    Returns:
        Hexadecimal color string (e.g., "#020717")
        
    Example:
        >>> hsl_to_hex(222.2, 84, 4.9)
        "#020717"
    """
    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)


def adjust_lightness(h: float, s: float, l: float, amount: float) -> Tuple[float, float, float]:
    """
    Adjust the lightness of an HSL color.
    
    Args:
        h: Hue (0-360 degrees)
        s: Saturation (0-100 percent)
        l: Lightness (0-100 percent)
        amount: Amount to adjust lightness (-100 to 100)
        
    Returns:
        Tuple of adjusted (h, s, l) values
        
    Example:
        >>> adjust_lightness(222.2, 84, 4.9, 10)
        (222.2, 84, 14.9)
    """
    new_l = max(0, min(100, l + amount))
    return (h, s, new_l)


def adjust_alpha(hex_color: str, alpha: float) -> str:
    """
    Convert a hex color to RGBA format with specified alpha.
    
    Args:
        hex_color: Hexadecimal color string
        alpha: Alpha value (0.0 to 1.0)
        
    Returns:
        RGBA color string (e.g., "rgba(255, 87, 51, 0.5)")
        
    Example:
        >>> adjust_alpha("#ff5733", 0.5)
        "rgba(255, 87, 51, 0.5)"
    """
    r, g, b = hex_to_rgb(hex_color)
    return f"rgba({r}, {g}, {b}, {alpha})"
