from typing import Dict, Any
from PyQt6.QtCore import QObject, QTranslator, QLocale

class I18n:
    _instance = None
    _translations = {
        'zh_TW': {
            'window_title': 'AI 代理助手',
            'system_scan': '系統掃描',
            'agent_design': '代理設計',
            'device_settings': '裝置設定',
            'start_scan': '開始掃描',
            'hardware_info': '硬體資訊',
            'performance_metrics': '效能指標',
            'recommendations': '建議事項',
            'settings': '設定',
            'performance_mode': '效能模式',
            'balanced': '平衡',
            'performance': '高效能',
            'power_save': '省電',
            'monitoring_interval': '監控間隔',
            'auto_optimize': '自動最佳化',
            'enable_notifications': '啟用通知',
            'enable_backup': '啟用備份',
            'check_updates': '檢查更新',
            'save_settings': '儲存設定',
            'run_health_check': '執行健康檢查',
            'optimize_system': '最佳化系統',
            'memory_usage': '記憶體使用量',
            'cpu_usage': 'CPU 使用量',
            'disk_usage': '磁碟使用量',
            'select_template': '選擇範本',
            'generate_agent': '生成代理',
            'validate_system': '驗證系統',
            'description': '描述',
            'requirements': '需求',
            'features': '功能',
            'success': '成功',
            'error': '錯誤',
            'warning': '警告',
            'info': '資訊',
            'settings_saved': '設定已儲存',
            'save_failed': '儲存失敗',
            'system_optimal': '系統運作正常！',
            'insufficient_memory': '記憶體不足',
            'insufficient_cpu': 'CPU 不足',
            'high_disk_usage': '磁碟空間不足',
            'optimization_complete': '最佳化完成',
            'agent_generated': '代理已生成',
            'generation_failed': '代理生成失敗',
            'validation_passed': '系統符合需求',
            'validation_failed': '系統不符合需求'
        }
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(I18n, cls).__new__(cls)
            cls._instance._locale = 'en_US'
        return cls._instance

    def set_locale(self, locale: str) -> None:
        """Set the current locale"""
        if locale in self._translations or locale == 'en_US':
            self._locale = locale

    def get_locale(self) -> str:
        """Get the current locale"""
        return self._locale

    def t(self, key: str, default: str = None) -> str:
        """Translate a key to the current locale"""
        if self._locale == 'en_US':
            return default or key
            
        translations = self._translations.get(self._locale, {})
        return translations.get(key, default or key)

    def get_qt_translator(self) -> QTranslator:
        """Get Qt translator for the current locale"""
        translator = QTranslator()
        if self._locale != 'en_US':
            # Load Qt's own translations for standard widgets
            translator.load(QLocale(self._locale), "qtbase", "_",
                          ":/translations")
        return translator

i18n = I18n()  # Singleton instance
