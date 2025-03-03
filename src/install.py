#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def install_application():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create installation directory
    home = str(Path.home())
    install_dir = os.path.join(home, '.local/share/ai-agent-assistant')
    os.makedirs(install_dir, exist_ok=True)
    
    # Copy application files
    print("Copying application files...")
    for item in ['main.py', 'core', 'ui', 'assets']:
        src = os.path.join(current_dir, item)
        dst = os.path.join(install_dir, item)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
        else:
            shutil.copytree(src, dst, dirs_exist_ok=True)

    # Create virtual environment
    print("Creating virtual environment...")
    os.system(f'python3 -m venv {install_dir}/venv')
    
    # Install dependencies
    print("Installing dependencies...")
    pip_path = os.path.join(install_dir, 'venv/bin/pip')
    requirements_path = os.path.join(os.path.dirname(current_dir), 'requirements.txt')
    os.system(f'{pip_path} install PyQt6>=6.4.0 psutil>=5.9.0 requests>=2.28.0 python-dotenv>=0.19.0 SQLAlchemy>=1.4.0 PyYAML>=6.0 rich>=12.0.0')
    
    # Create desktop entry
    print("Creating desktop entry...")
    entry_content = f"""[Desktop Entry]
Name=AI Agent Assistant
Name[zh_TW]=AI 代理助手
Comment=System Analysis and AI Agent Management Tool
Comment[zh_TW]=系統分析與 AI 代理管理工具
Exec={install_dir}/venv/bin/python3 {install_dir}/main.py
Icon={install_dir}/assets/icon.png
Terminal=false
Type=Application
Categories=Development;System;
Keywords=AI;System;Monitor;Agent;
"""
    
    applications_dir = os.path.join(home, '.local/share/applications')
    os.makedirs(applications_dir, exist_ok=True)
    
    desktop_file = os.path.join(applications_dir, 'ai-agent-assistant.desktop')
    with open(desktop_file, 'w') as f:
        f.write(entry_content)
    
    os.chmod(desktop_file, 0o755)
    
    print("\nInstallation completed!")
    print(f"Application installed to: {install_dir}")
    print("You can now launch the application from your desktop environment.")

if __name__ == "__main__":
    if os.geteuid() == 0:  # Don't run as root
        print("Please do not run this script with sudo. It should be run as a normal user.")
        sys.exit(1)
    
    install_application()
