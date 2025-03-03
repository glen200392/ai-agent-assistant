import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QLocale
from ui.main_window import MainWindow
from ui.utils.i18n import i18n

def main():
    app = QApplication(sys.argv)
    
    # Set locale based on system language
    system_locale = QLocale.system().name()
    if system_locale == "zh_TW":
        i18n.set_locale("zh_TW")
    
    # Install translator
    translator = i18n.get_qt_translator()
    app.installTranslator(translator)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
