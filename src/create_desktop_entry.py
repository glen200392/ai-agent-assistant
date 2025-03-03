#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def create_desktop_entry():
    # Get the absolute path to the main script
    main_script = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))
    python_path = sys.executable
    
    # Desktop entry content
    entry_content = f"""[Desktop Entry]
Name=AI Agent Assistant
Name[zh_TW]=AI 代理助手
Comment=System Analysis and AI Agent Management Tool
Comment[zh_TW]=系統分析與 AI 代理管理工具
Exec={python_path} {main_script}
Icon={os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets/icon.png'))}
Terminal=false
Type=Application
Categories=Development;System;
Keywords=AI;System;Monitor;Agent;
"""

    # Create desktop entry file
    home = str(Path.home())
    applications_dir = os.path.join(home, '.local/share/applications')
    os.makedirs(applications_dir, exist_ok=True)
    
    desktop_file = os.path.join(applications_dir, 'ai-agent-assistant.desktop')
    
    with open(desktop_file, 'w') as f:
        f.write(entry_content)
    
    # Make the desktop entry executable
    os.chmod(desktop_file, 0o755)
    
    print("Desktop entry created successfully!")
    print(f"Location: {desktop_file}")

if __name__ == "__main__":
    create_desktop_entry()
