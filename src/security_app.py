"""
Launcher for Security+ Study App. Keeps a small entrypoint that initializes the DB
and starts the GUI. The main GUI lives in `gui.py` and core logic in `app_core.py`.
"""
import sys
from pathlib import Path
from app_core import init_db, resolve_asset_path
from gui import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

def main():
    init_db()
    app = QApplication(sys.argv)
    icon_path = resolve_asset_path("app_icon.png")
    if not icon_path:
        icon_path = resolve_asset_path("app_icon.ico")
    if icon_path:
        app.setWindowIcon(QIcon(str(icon_path)))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
