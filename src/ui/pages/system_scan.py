from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QProgressBar,
    QTextEdit,
    QScrollArea,
    QFrame
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from ..utils.styles import apply_style
from ..utils.i18n import i18n
from core.system_scanner import SystemScanner
import json

class ScanWorker(QThread):
    finished = pyqtSignal(dict)
    progress = pyqtSignal(int)
    
    def run(self):
        scanner = SystemScanner()
        self.progress.emit(20)
        result = scanner.scan_system()
        self.progress.emit(100)
        self.finished.emit(result)

class SystemScanPage(QWidget):
    def __init__(self):
        super().__init__()
        self.scanner = SystemScanner()
        self.init_ui()
        self.scan_worker = None

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        self.title_label = QLabel(i18n.t('system_scan', "System Scan"))
        self.title_label.setObjectName("page-title")
        apply_style(self.title_label, """
            QLabel#page-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.title_label)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Scan Button
        self.scan_button = QPushButton(i18n.t('start_scan', "Start Scan"))
        self.scan_button.setFixedWidth(200)
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Results Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout(self.results_widget)
        
        scroll.setWidget(self.results_widget)
        layout.addWidget(scroll)

        # Initial state
        self.progress_bar.hide()

    def start_scan(self):
        self.scan_button.setEnabled(False)
        self.progress_bar.show()
        self.progress_bar.setValue(0)
        
        # Clear previous results
        for i in reversed(range(self.results_layout.count())): 
            self.results_layout.itemAt(i).widget().setParent(None)

        # Create and start worker thread
        self.scan_worker = ScanWorker()
        self.scan_worker.finished.connect(self.handle_scan_complete)
        self.scan_worker.progress.connect(self.progress_bar.setValue)
        self.scan_worker.start()

    def handle_scan_complete(self, results):
        self.scan_button.setEnabled(True)
        self.display_results(results)

    def display_results(self, results):
        # System Info Section
        self.add_section(i18n.t('system_info', "System Information"), results["system_info"])
        
        # Hardware Info Section
        hardware = self.format_hardware_info(results["hardware_info"])
        self.add_section(i18n.t('hardware_info', "Hardware Information"), hardware)
        
        # Performance Metrics Section
        metrics = self.format_performance_metrics(results["performance_metrics"])
        self.add_section(i18n.t('performance_metrics', "Performance Metrics"), metrics)
        
        # Python Environment Section
        env_info = results["python_environment"]
        self.add_section(i18n.t('python_env', "Python Environment"), {
            i18n.t('python_path', "Python Path"): env_info["python_path"],
            i18n.t('python_version', "Python Version"): env_info["python_version"],
            i18n.t('installed_packages', "Installed Packages"): f"{len(env_info['pip_packages'])} {i18n.t('packages_installed', 'packages installed')}"
        })
        
        # Recommendations
        recommendations = self.scanner.get_hardware_recommendations()
        if recommendations:
            self.add_section(i18n.t('recommendations', "Recommendations"), {
                f"{i18n.t('recommendation', 'Recommendation')} {i+1}": rec 
                for i, rec in enumerate(recommendations)
            })
        
        # AI Agent Recommendations
        ai_recommendations = self.scanner.get_ai_agent_recommendations()
        if ai_recommendations:
            self.add_section(i18n.t('ai_recommendations', "AI Agent Recommendations"), {
                f"{i18n.t('recommendation', 'Recommendation')} {i+1}": rec 
                for i, rec in enumerate(ai_recommendations)
            })

    def add_section(self, title, data):
        # Section Title
        section_title = QLabel(title)
        section_title.setObjectName("section-title")
        apply_style(section_title, """
            QLabel#section-title {
                font-size: 18px;
                font-weight: bold;
                margin-top: 15px;
                margin-bottom: 10px;
            }
        """)
        self.results_layout.addWidget(section_title)
        
        # Section Content
        content = QTextEdit()
        content.setReadOnly(True)
        content.setMaximumHeight(200)
        
        # Format the data
        if isinstance(data, dict):
            formatted_data = json.dumps(data, indent=2)
        elif isinstance(data, list):
            formatted_data = "\n".join(f"- {item}" for item in data)
        else:
            formatted_data = str(data)
            
        content.setText(formatted_data)
        self.results_layout.addWidget(content)

    def format_hardware_info(self, info):
        return {
            i18n.t('cpu_cores', "CPU Cores"): info["cpu_cores"],
            i18n.t('cpu_freq', "CPU Frequency"): f"{info['cpu_freq']['current']:.2f}MHz" if info["cpu_freq"] else "N/A",
            i18n.t('total_memory', "Total Memory"): f"{info['total_memory'] / (1024**3):.2f}GB",
            i18n.t('available_memory', "Available Memory"): f"{info['available_memory'] / (1024**3):.2f}GB",
            i18n.t('memory_usage', "Memory Usage"): f"{info['memory_percent']}%",
            i18n.t('disk_space', "Disk Space"): f"{i18n.t('total', 'Total')}: {info['disk_total'] / (1024**3):.2f}GB, {i18n.t('used', 'Used')}: {info['disk_used'] / (1024**3):.2f}GB",
            i18n.t('disk_usage', "Disk Usage"): f"{info['disk_percent']}%"
        }

    def format_performance_metrics(self, metrics):
        return {
            i18n.t('cpu_usage_per_core', "CPU Usage (per core)"): f"{metrics['cpu_usage']}%",
            i18n.t('memory_usage', "Memory Usage"): f"{metrics['memory_usage']}%",
            i18n.t('disk_io', "Disk I/O"): metrics['disk_io'] if metrics['disk_io'] else "N/A",
            i18n.t('network_io', "Network I/O"): {
                i18n.t('bytes_sent', "Bytes Sent"): f"{metrics['network_io']['bytes_sent'] / (1024**2):.2f}MB",
                i18n.t('bytes_received', "Bytes Received"): f"{metrics['network_io']['bytes_recv'] / (1024**2):.2f}MB"
            }
        }

    def update_translations(self):
        """Update all translatable text in the page"""
        self.title_label.setText(i18n.t('system_scan', "System Scan"))
        self.scan_button.setText(i18n.t('start_scan', "Start Scan"))
