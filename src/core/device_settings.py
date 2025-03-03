import os
import json
from typing import Dict, List, Any
import psutil
import platform

class DeviceSettings:
    def __init__(self):
        self.settings_file = "device_settings.json"
        self.default_settings = {
            "performance_mode": "balanced",  # balanced, performance, power_save
            "monitoring_interval": 60,  # seconds
            "log_level": "INFO",
            "max_memory_usage": 80,  # percentage
            "max_cpu_usage": 80,  # percentage
            "auto_optimize": True,
            "notification_enabled": True,
            "backup_enabled": True,
            "update_check": True
        }
        self.current_settings = self.load_settings()

    def load_settings(self) -> Dict[str, Any]:
        """Load settings from file or create with defaults"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    return {**self.default_settings, **json.load(f)}
            except Exception as e:
                print(f"Error loading settings: {e}")
                return self.default_settings.copy()
        return self.default_settings.copy()

    def save_settings(self) -> bool:
        """Save current settings to file"""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.current_settings, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False

    def get_current_settings(self) -> Dict[str, Any]:
        """Get current settings"""
        return self.current_settings

    def update_settings(self, new_settings: Dict[str, Any]) -> bool:
        """Update settings with new values"""
        self.current_settings.update(new_settings)
        return self.save_settings()

    def get_optimization_suggestions(self) -> List[Dict[str, Any]]:
        """Generate optimization suggestions based on system analysis"""
        suggestions = []
        
        # Memory optimization
        memory = psutil.virtual_memory()
        if memory.percent > self.current_settings['max_memory_usage']:
            suggestions.append({
                "type": "memory",
                "severity": "high",
                "issue": "High memory usage detected",
                "suggestion": "Consider closing unused applications or increasing virtual memory"
            })

        # CPU optimization
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > self.current_settings['max_cpu_usage']:
            suggestions.append({
                "type": "cpu",
                "severity": "high",
                "issue": "High CPU usage detected",
                "suggestion": "Check for resource-intensive processes and consider optimization"
            })

        # Disk optimization
        disk = psutil.disk_usage('/')
        if disk.percent > 90:
            suggestions.append({
                "type": "disk",
                "severity": "medium",
                "issue": "Low disk space",
                "suggestion": "Clean up unnecessary files or add more storage"
            })

        return suggestions

    def apply_optimization(self, optimization_type: str) -> bool:
        """Apply specific optimization settings"""
        if optimization_type == "performance":
            self.current_settings.update({
                "performance_mode": "performance",
                "monitoring_interval": 30,
                "max_memory_usage": 90,
                "max_cpu_usage": 90,
                "auto_optimize": True
            })
        elif optimization_type == "balanced":
            self.current_settings.update({
                "performance_mode": "balanced",
                "monitoring_interval": 60,
                "max_memory_usage": 80,
                "max_cpu_usage": 80,
                "auto_optimize": True
            })
        elif optimization_type == "power_save":
            self.current_settings.update({
                "performance_mode": "power_save",
                "monitoring_interval": 120,
                "max_memory_usage": 70,
                "max_cpu_usage": 70,
                "auto_optimize": True
            })
        else:
            return False
        
        return self.save_settings()

    def get_system_health_report(self) -> Dict[str, Any]:
        """Generate system health report"""
        return {
            "memory_usage": psutil.virtual_memory()._asdict(),
            "cpu_usage": {
                "percent": psutil.cpu_percent(interval=1),
                "cores": psutil.cpu_count(),
                "frequency": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
            },
            "disk_usage": psutil.disk_usage('/')._asdict(),
            "network": psutil.net_io_counters()._asdict(),
            "performance_mode": self.current_settings["performance_mode"],
            "optimization_status": self.get_optimization_status()
        }

    def get_optimization_status(self) -> Dict[str, Any]:
        """Get current optimization status"""
        return {
            "auto_optimize": self.current_settings["auto_optimize"],
            "current_mode": self.current_settings["performance_mode"],
            "monitoring_interval": self.current_settings["monitoring_interval"],
            "thresholds": {
                "memory": self.current_settings["max_memory_usage"],
                "cpu": self.current_settings["max_cpu_usage"]
            }
        }

    def get_compatibility_report(self) -> Dict[str, Any]:
        """Generate compatibility report for AI workloads"""
        compatibility = {
            "os_compatibility": True,
            "hardware_compatibility": True,
            "issues": []
        }

        # Check OS compatibility
        if platform.system().lower() not in ['windows', 'darwin', 'linux']:
            compatibility["os_compatibility"] = False
            compatibility["issues"].append("Unsupported operating system")

        # Check hardware compatibility
        memory_gb = psutil.virtual_memory().total / (1024**3)
        cpu_cores = psutil.cpu_count()

        if memory_gb < 8:
            compatibility["hardware_compatibility"] = False
            compatibility["issues"].append("Insufficient RAM (minimum 8GB required)")

        if cpu_cores < 4:
            compatibility["hardware_compatibility"] = False
            compatibility["issues"].append("Insufficient CPU cores (minimum 4 cores required)")

        return compatibility
