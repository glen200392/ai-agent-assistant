from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QCheckBox,
    QSpinBox,
    QScrollArea,
    QFrame,
    QGroupBox,
    QMessageBox
)
from PyQt6.QtCore import Qt, QTimer
from ..utils.styles import apply_style
from ..utils.i18n import i18n
from core.device_settings import DeviceSettings
import json

class DeviceSettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.settings_manager = DeviceSettings()
        self.monitoring_timer = QTimer()
        self.monitoring_timer.timeout.connect(self.update_system_health)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        self.title_label = QLabel(i18n.t('settings_monitoring', "Device Settings & Monitoring"))
        self.title_label.setObjectName("page-title")
        apply_style(self.title_label, """
            QLabel#page-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.title_label)

        # Settings Section
        settings_group = QGroupBox(i18n.t('performance_settings', "Performance Settings"))
        settings_layout = QVBoxLayout()

        # Performance Mode
        mode_layout = QHBoxLayout()
        self.mode_label = QLabel(i18n.t('performance_mode', "Performance Mode:"))
        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            i18n.t('balanced', "balanced"),
            i18n.t('performance', "performance"),
            i18n.t('power_save', "power_save")
        ])
        self.mode_combo.currentTextChanged.connect(self.apply_performance_mode)
        
        mode_layout.addWidget(self.mode_label)
        mode_layout.addWidget(self.mode_combo)
        mode_layout.addStretch()
        settings_layout.addLayout(mode_layout)

        # Monitoring Settings
        monitor_layout = QHBoxLayout()
        self.monitor_label = QLabel(i18n.t('monitoring_interval', "Monitoring Interval (seconds):"))
        self.interval_spin = QSpinBox()
        self.interval_spin.setRange(30, 300)
        self.interval_spin.setValue(60)
        self.interval_spin.valueChanged.connect(self.update_monitoring_interval)
        
        monitor_layout.addWidget(self.monitor_label)
        monitor_layout.addWidget(self.interval_spin)
        monitor_layout.addStretch()
        settings_layout.addLayout(monitor_layout)

        # Checkboxes for various settings
        self.auto_optimize_check = QCheckBox(i18n.t('auto_optimize', "Enable Auto-Optimization"))
        self.notifications_check = QCheckBox(i18n.t('enable_notifications', "Enable Notifications"))
        self.backup_check = QCheckBox(i18n.t('enable_backup', "Enable Automatic Backup"))
        self.updates_check = QCheckBox(i18n.t('check_updates', "Check for Updates"))
        
        settings_layout.addWidget(self.auto_optimize_check)
        settings_layout.addWidget(self.notifications_check)
        settings_layout.addWidget(self.backup_check)
        settings_layout.addWidget(self.updates_check)
        
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)

        # System Health Monitoring Section
        health_group = QGroupBox(i18n.t('system_health', "System Health"))
        health_layout = QVBoxLayout()
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        self.health_widget = QWidget()
        self.health_info_layout = QVBoxLayout(self.health_widget)
        
        scroll.setWidget(self.health_widget)
        health_layout.addWidget(scroll)
        
        health_group.setLayout(health_layout)
        layout.addWidget(health_group)

        # Action Buttons
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton(i18n.t('save_settings', "Save Settings"))
        self.save_button.clicked.connect(self.save_settings)
        
        self.scan_button = QPushButton(i18n.t('run_health_check', "Run Health Check"))
        self.scan_button.clicked.connect(self.run_health_check)
        
        self.optimize_button = QPushButton(i18n.t('optimize_system', "Optimize System"))
        self.optimize_button.clicked.connect(self.optimize_system)
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.scan_button)
        button_layout.addWidget(self.optimize_button)
        
        layout.addLayout(button_layout)

        # Load current settings
        self.load_current_settings()
        
        # Start monitoring
        self.start_monitoring()

    def load_current_settings(self):
        settings = self.settings_manager.get_current_settings()
        
        self.mode_combo.setCurrentText(settings["performance_mode"])
        self.interval_spin.setValue(settings["monitoring_interval"])
        self.auto_optimize_check.setChecked(settings["auto_optimize"])
        self.notifications_check.setChecked(settings["notification_enabled"])
        self.backup_check.setChecked(settings["backup_enabled"])
        self.updates_check.setChecked(settings["update_check"])

    def save_settings(self):
        new_settings = {
            "performance_mode": self.mode_combo.currentText(),
            "monitoring_interval": self.interval_spin.value(),
            "auto_optimize": self.auto_optimize_check.isChecked(),
            "notification_enabled": self.notifications_check.isChecked(),
            "backup_enabled": self.backup_check.isChecked(),
            "update_check": self.updates_check.isChecked()
        }
        
        if self.settings_manager.update_settings(new_settings):
            QMessageBox.information(
                self, 
                i18n.t('success', "Success"), 
                i18n.t('settings_saved', "Settings saved successfully!")
            )
        else:
            QMessageBox.warning(
                self, 
                i18n.t('error', "Error"), 
                i18n.t('save_failed', "Failed to save settings")
            )

    def apply_performance_mode(self, mode):
        if self.settings_manager.apply_optimization(mode):
            QMessageBox.information(
                self, 
                i18n.t('success', "Success"), 
                i18n.t('mode_applied', f"Applied {mode} performance mode")
            )
        else:
            QMessageBox.warning(
                self, 
                i18n.t('error', "Error"), 
                i18n.t('mode_failed', f"Failed to apply {mode} mode")
            )

    def start_monitoring(self):
        interval = self.settings_manager.get_current_settings()["monitoring_interval"]
        self.monitoring_timer.start(interval * 1000)  # Convert to milliseconds
        self.update_system_health()

    def update_monitoring_interval(self, value):
        self.monitoring_timer.setInterval(value * 1000)

    def update_system_health(self):
        # Clear previous health info
        for i in reversed(range(self.health_info_layout.count())): 
            self.health_info_layout.itemAt(i).widget().setParent(None)

        # Get current health status
        health_report = self.settings_manager.get_system_health_report()
        
        # Display memory usage
        memory_label = QLabel(
            f"{i18n.t('memory_usage', 'Memory Usage')}: {health_report['memory_usage']['percent']}%"
        )
        self.health_info_layout.addWidget(memory_label)
        
        # Display CPU usage
        cpu_label = QLabel(
            f"{i18n.t('cpu_usage', 'CPU Usage')}: {health_report['cpu_usage']['percent']}%"
        )
        self.health_info_layout.addWidget(cpu_label)
        
        # Display disk usage
        disk_label = QLabel(
            f"{i18n.t('disk_usage', 'Disk Usage')}: {health_report['disk_usage']['percent']}%"
        )
        self.health_info_layout.addWidget(disk_label)
        
        # Display performance mode
        mode_label = QLabel(
            f"{i18n.t('current_mode', 'Current Mode')}: {health_report['performance_mode']}"
        )
        self.health_info_layout.addWidget(mode_label)

    def run_health_check(self):
        # Get optimization suggestions
        suggestions = self.settings_manager.get_optimization_suggestions()
        
        if suggestions:
            message = f"{i18n.t('health_check_results', 'System Health Check Results')}:\n\n"
            for suggestion in suggestions:
                message += f"- {suggestion['issue']}\n"
                message += f"  {i18n.t('suggestion', 'Suggestion')}: {suggestion['suggestion']}\n\n"
        else:
            message = i18n.t('system_optimal', "System is running optimally!")
            
        QMessageBox.information(
            self, 
            i18n.t('health_check_results', "Health Check Results"), 
            message
        )

    def optimize_system(self):
        current_mode = self.mode_combo.currentText()
        
        # Apply optimization based on current health status
        health_report = self.settings_manager.get_system_health_report()
        
        if health_report['cpu_usage']['percent'] > 80 or health_report['memory_usage']['percent'] > 80:
            self.settings_manager.apply_optimization('performance')
            self.mode_combo.setCurrentText('performance')
        elif health_report['cpu_usage']['percent'] < 20 and health_report['memory_usage']['percent'] < 40:
            self.settings_manager.apply_optimization('power_save')
            self.mode_combo.setCurrentText('power_save')
        else:
            self.settings_manager.apply_optimization('balanced')
            self.mode_combo.setCurrentText('balanced')
            
        QMessageBox.information(
            self,
            i18n.t('optimization_complete', "Optimization Complete"),
            i18n.t('system_optimized', "System has been optimized based on current usage patterns")
        )

    def update_translations(self):
        """Update all translatable text in the page"""
        self.title_label.setText(i18n.t('settings_monitoring', "Device Settings & Monitoring"))
        self.mode_label.setText(i18n.t('performance_mode', "Performance Mode:"))
        self.monitor_label.setText(i18n.t('monitoring_interval', "Monitoring Interval (seconds):"))
        self.auto_optimize_check.setText(i18n.t('auto_optimize', "Enable Auto-Optimization"))
        self.notifications_check.setText(i18n.t('enable_notifications', "Enable Notifications"))
        self.backup_check.setText(i18n.t('enable_backup', "Enable Automatic Backup"))
        self.updates_check.setText(i18n.t('check_updates', "Check for Updates"))
        self.save_button.setText(i18n.t('save_settings', "Save Settings"))
        self.scan_button.setText(i18n.t('run_health_check', "Run Health Check"))
        self.optimize_button.setText(i18n.t('optimize_system', "Optimize System"))
        self.update_system_health()
