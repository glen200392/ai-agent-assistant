from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QHBoxLayout, 
    QPushButton,
    QStackedWidget,
    QLabel,
    QComboBox
)
from PyQt6.QtCore import Qt, QLocale
from .pages.system_scan import SystemScanPage
from .pages.agent_design import AgentDesignPage
from .pages.device_settings import DeviceSettingsPage
from .utils.i18n import i18n

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(i18n.t('window_title', "AI Agent Assistant"))
        self.setMinimumSize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Create stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        
        # Create pages
        self.system_scan_page = SystemScanPage()
        self.agent_design_page = AgentDesignPage()
        self.device_settings_page = DeviceSettingsPage()
        
        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.system_scan_page)
        self.stacked_widget.addWidget(self.agent_design_page)
        self.stacked_widget.addWidget(self.device_settings_page)
        
        # Create navigation buttons
        self.nav_layout = QVBoxLayout()
        self.scan_button = QPushButton(i18n.t('system_scan', "System Scan"))
        self.agent_button = QPushButton(i18n.t('agent_design', "Agent Design"))
        self.settings_button = QPushButton(i18n.t('device_settings', "Device Settings"))
        
        # Language selector
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["English", "繁體中文"])
        self.lang_combo.currentTextChanged.connect(self.change_language)
        
        self.nav_layout.addWidget(self.lang_combo)
        self.nav_layout.addWidget(self.scan_button)
        self.nav_layout.addWidget(self.agent_button)
        self.nav_layout.addWidget(self.settings_button)
        
        # Connect buttons to page changes
        self.scan_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.system_scan_page))
        self.agent_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.agent_design_page))
        self.settings_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.device_settings_page))
        
        # Create main layout with navigation and pages
        main_layout = QHBoxLayout()
        nav_widget = QWidget()
        nav_widget.setLayout(self.nav_layout)
        nav_widget.setMaximumWidth(200)
        
        main_layout.addWidget(nav_widget)
        main_layout.addWidget(self.stacked_widget)
        
        self.layout.addLayout(main_layout)

    def change_language(self, language: str):
        """Change the application language"""
        if language == "English":
            i18n.set_locale("en_US")
        elif language == "繁體中文":
            i18n.set_locale("zh_TW")
            
        # Update UI text
        self.setWindowTitle(i18n.t('window_title', "AI Agent Assistant"))
        self.scan_button.setText(i18n.t('system_scan', "System Scan"))
        self.agent_button.setText(i18n.t('agent_design', "Agent Design"))
        self.settings_button.setText(i18n.t('device_settings', "Device Settings"))
        
        # Update pages
        self.system_scan_page.update_translations()
        self.agent_design_page.update_translations()
        self.device_settings_page.update_translations()
