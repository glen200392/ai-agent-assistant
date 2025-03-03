import os
import sys
import psutil
import platform
from datetime import datetime

class SystemScanner:
    def scan_system(self):
        """Perform a comprehensive system scan"""
        return {
            "system_info": self._get_system_info(),
            "hardware_info": self._get_hardware_info(),
            "performance_metrics": self._get_performance_metrics(),
            "installed_software": self._get_installed_software(),
            "python_environment": self._get_python_environment()
        }
    
    def _get_system_info(self):
        """Get basic system information"""
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "hostname": platform.node(),
            "processor": platform.processor(),
            "python_version": sys.version,
            "timezone": datetime.now().astimezone().tzname()
        }
    
    def _get_hardware_info(self):
        """Get hardware specifications"""
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            "cpu_cores": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            "total_memory": memory.total,
            "available_memory": memory.available,
            "memory_percent": memory.percent,
            "disk_total": disk.total,
            "disk_used": disk.used,
            "disk_free": disk.free,
            "disk_percent": disk.percent
        }
    
    def _get_performance_metrics(self):
        """Get current system performance metrics"""
        return {
            "cpu_usage": psutil.cpu_percent(interval=1, percpu=True),
            "memory_usage": psutil.virtual_memory().percent,
            "disk_io": psutil.disk_io_counters()._asdict() if psutil.disk_io_counters() else None,
            "network_io": psutil.net_io_counters()._asdict()
        }
    
    def _get_installed_software(self):
        """Get list of installed AI/ML related packages"""
        try:
            import pkg_resources
            packages = [
                {"name": pkg.key, "version": pkg.version}
                for pkg in pkg_resources.working_set
            ]
            return packages
        except Exception as e:
            return {"error": str(e)}
    
    def _get_python_environment(self):
        """Get Python environment details"""
        return {
            "python_path": sys.executable,
            "python_version": platform.python_version(),
            "pip_packages": self._get_installed_software()
        }

    def get_hardware_recommendations(self):
        """Generate hardware recommendations based on scan results"""
        system_info = self.scan_system()
        recommendations = []

        # CPU recommendations
        cpu_usage = sum(system_info["performance_metrics"]["cpu_usage"]) / len(system_info["performance_metrics"]["cpu_usage"])
        if cpu_usage > 80:
            recommendations.append("High CPU usage detected. Consider upgrading CPU or optimizing workload.")
        
        # Memory recommendations
        memory_info = system_info["hardware_info"]
        if memory_info["memory_percent"] > 80:
            recommendations.append("High memory usage. Consider increasing RAM.")
        
        # Disk recommendations
        if memory_info["disk_percent"] > 80:
            recommendations.append("Low disk space. Consider freeing up space or adding storage.")

        return recommendations

    def get_ai_agent_recommendations(self):
        """Generate AI agent recommendations based on system capabilities"""
        system_info = self.scan_system()
        recommendations = []

        # Basic recommendations based on hardware
        memory_gb = system_info["hardware_info"]["total_memory"] / (1024 ** 3)
        cpu_cores = system_info["hardware_info"]["cpu_cores"]

        if memory_gb < 8:
            recommendations.append("Limited RAM detected. Consider lightweight models or cloud-based solutions.")
        elif memory_gb >= 16:
            recommendations.append("Sufficient RAM for most local AI models.")

        if cpu_cores < 4:
            recommendations.append("Limited CPU cores. Consider optimizing for inference only.")
        elif cpu_cores >= 8:
            recommendations.append("Good CPU capacity for running multiple AI agents.")

        return recommendations
