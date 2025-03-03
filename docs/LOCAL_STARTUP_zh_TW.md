# 本機啟動指南

## 方法一：快速安裝啟動

1. 安裝程式：
```bash
# 進入專案目錄
cd ai-agent-assistant

# 執行安裝腳本
python3 src/install.py
```

2. 啟動方式：
   - 在應用程式選單中點擊 "AI 代理助手"
   - 或使用 Spotlight (⌘ + Space) 搜尋 "AI 代理助手"

## 方法二：直接執行（開發模式）

1. 建立虛擬環境：
```bash
# 建立虛擬環境
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate  # Linux/macOS
# 或
.\venv\Scripts\activate   # Windows
```

2. 安裝依賴：
```bash
# 安裝所需套件
pip install -r requirements.txt
```

3. 啟動程式：
```bash
# 直接執行主程式
python3 src/main.py
```

## 方法三：命令列啟動

如果已經安裝完成，可以直接使用命令：
```bash
ai-agent-assistant
```

## 常見問題

### Q: 找不到應用程式圖示？
```bash
# 重新執行安裝腳本
python3 src/install.py
```

### Q: 虛擬環境啟動失敗？
```bash
# 刪除現有虛擬環境
rm -rf venv

# 重新建立
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Q: 相依套件安裝失敗？
```bash
# 更新 pip
python3 -m pip install --upgrade pip

# 單獨安裝必要套件
pip install PyQt6
pip install psutil
pip install requests
```

### Q: 程式無法啟動？
檢查以下幾點：
1. Python 版本是否 >= 3.8
2. 是否已安裝所有依賴
3. 檢查錯誤訊息

## 開發模式啟動

如果要進行開發或除錯：

1. 啟用除錯模式：
```bash
# 設定環境變數
export DEBUG=1

# 啟動程式
python3 src/main.py
```

2. 查看詳細日誌：
```bash
tail -f ~/.local/share/ai-agent-assistant/app.log
```

## 設定檔位置

- 應用程式：`~/.local/share/ai-agent-assistant/`
- 設定檔：`~/.config/ai-agent-assistant/settings.json`
- 日誌檔：`~/.local/share/ai-agent-assistant/app.log`
- 使用者資料：`~/Documents/AI-Agent-Assistant/`

## 更新程式

1. 從 GitHub 更新：
```bash
# 進入專案目錄
cd ai-agent-assistant

# 拉取最新版本
git pull

# 重新安裝
python3 src/install.py
```

2. 或重新安裝：
```bash
# 移除舊版
rm -rf ~/.local/share/ai-agent-assistant

# 重新克隆專案
git clone https://github.com/glen200392/ai-agent-assistant.git
cd ai-agent-assistant

# 安裝新版
python3 src/install.py
```

## 效能優化建議

1. 使用系統 Python 而非自編譯版本
2. 確保記憶體至少 4GB 可用
3. 使用 SSD 存儲
4. 保持系統更新

## 多使用者環境

1. 每個使用者獨立安裝：
```bash
python3 src/install.py --user
```

2. 系統級安裝（需要 root 權限）：
```bash
sudo python3 src/install.py --system
```

## 技術支援

如果遇到問題：
1. 查看錯誤日誌
2. 檢查系統需求
3. 提交 GitHub Issue
4. 聯繫技術支援
