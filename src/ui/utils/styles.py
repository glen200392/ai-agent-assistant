from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt

def apply_style(widget: QWidget, style: str):
    """Apply custom CSS style to a widget"""
    widget.setStyleSheet(style)

def apply_theme(widgets: list[QWidget], theme: str = "light"):
    """Apply a theme to multiple widgets"""
    if theme == "dark":
        theme_styles = {
            "background": "#2D2D2D",
            "text": "#FFFFFF",
            "border": "#3D3D3D",
            "button": "#404040",
            "button_hover": "#505050",
            "button_pressed": "#606060"
        }
    else:  # light theme
        theme_styles = {
            "background": "#FFFFFF",
            "text": "#000000",
            "border": "#E0E0E0",
            "button": "#F0F0F0",
            "button_hover": "#E5E5E5",
            "button_pressed": "#D0D0D0"
        }

    base_styles = f"""
        QWidget {{
            background-color: {theme_styles["background"]};
            color: {theme_styles["text"]};
        }}
        
        QPushButton {{
            background-color: {theme_styles["button"]};
            border: 1px solid {theme_styles["border"]};
            padding: 5px 15px;
            border-radius: 4px;
        }}
        
        QPushButton:hover {{
            background-color: {theme_styles["button_hover"]};
        }}
        
        QPushButton:pressed {{
            background-color: {theme_styles["button_pressed"]};
        }}
        
        QLineEdit, QTextEdit, QComboBox {{
            border: 1px solid {theme_styles["border"]};
            padding: 5px;
            border-radius: 4px;
        }}
        
        QProgressBar {{
            text-align: center;
            border: 1px solid {theme_styles["border"]};
            border-radius: 4px;
        }}
        
        QProgressBar::chunk {{
            background-color: #007AFF;
        }}
        
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border: 1px solid {theme_styles["border"]};
            border-radius: 3px;
        }}
        
        QCheckBox::indicator:checked {{
            background-color: #007AFF;
            border-color: #007AFF;
        }}
    """

    for widget in widgets:
        widget.setStyleSheet(base_styles)

# Common style constants
TITLE_STYLE = """
    font-size: 24px;
    font-weight: bold;
    margin: 10px 0;
"""

SECTION_TITLE_STYLE = """
    font-size: 18px;
    font-weight: bold;
    margin: 8px 0;
"""

LABEL_STYLE = """
    font-size: 14px;
    margin: 5px 0;
"""

BUTTON_STYLE = """
    padding: 8px 16px;
    font-size: 14px;
    font-weight: bold;
    border-radius: 4px;
    background-color: #007AFF;
    color: white;
    border: none;
"""

BUTTON_PRIMARY_STYLE = BUTTON_STYLE + """
    background-color: #007AFF;
"""

BUTTON_SECONDARY_STYLE = BUTTON_STYLE + """
    background-color: #5856D6;
"""

BUTTON_SUCCESS_STYLE = BUTTON_STYLE + """
    background-color: #34C759;
"""

BUTTON_WARNING_STYLE = BUTTON_STYLE + """
    background-color: #FF9500;
"""

BUTTON_DANGER_STYLE = BUTTON_STYLE + """
    background-color: #FF3B30;
"""

INPUT_STYLE = """
    padding: 6px 12px;
    font-size: 14px;
    border: 1px solid #E5E5EA;
    border-radius: 4px;
    background-color: white;
"""

def get_theme_colors(theme: str = "light") -> dict:
    """Get color palette for the specified theme"""
    if theme == "dark":
        return {
            "background": "#2D2D2D",
            "surface": "#3D3D3D",
            "primary": "#007AFF",
            "secondary": "#5856D6",
            "success": "#34C759",
            "warning": "#FF9500",
            "danger": "#FF3B30",
            "text": "#FFFFFF",
            "text_secondary": "#EBEBF5",
            "border": "#3D3D3D"
        }
    else:
        return {
            "background": "#FFFFFF",
            "surface": "#F2F2F7",
            "primary": "#007AFF",
            "secondary": "#5856D6",
            "success": "#34C759",
            "warning": "#FF9500",
            "danger": "#FF3B30",
            "text": "#000000",
            "text_secondary": "#3C3C43",
            "border": "#E5E5EA"
        }
