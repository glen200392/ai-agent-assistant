# AI 代理助手使用指南

## 安裝說明

### 桌面版本安裝

1. 從以下位置下載最新版本：
   ```
   git clone https://github.com/yourusername/ai-agent-assistant.git
   cd ai-agent-assistant
   ```

2. 運行安裝腳本：
   ```bash
   python3 src/install.py
   ```

3. 安裝完成後，您可以：
   - 在應用程式選單中找到 "AI 代理助手" 圖示
   - 通過 Spotlight (⌘ + Space) 搜尋 "AI 代理助手"
   - 在 Launchpad 中找到應用程式圖示

### 設定與配置檔案位置

- 應用程式安裝位置：`~/.local/share/ai-agent-assistant/`
- 配置文件：`~/.config/ai-agent-assistant/settings.json`
- 掃描報告與代理檔案：`~/Documents/AI-Agent-Assistant/`

## 基本功能使用

### 系統掃描

1. 點擊左側導航欄的「系統掃描」
2. 點擊「開始掃描」按鈕
3. 等待掃描完成，查看：
   - 硬體資訊
   - 效能指標
   - 系統建議

### AI 代理設計

1. 選擇代理範本
2. 驗證系統相容性
3. 生成客製化代理
4. 查看部署清單

### 裝置設定

1. 選擇效能模式：
   - 平衡模式
   - 高效能模式
   - 省電模式
2. 調整監控間隔
3. 設定自動最佳化選項

## 跨裝置同步

### 備份配置

1. 在「裝置設定」中啟用自動備份
2. 備份檔案將保存在：`~/Documents/AI-Agent-Assistant/backups/`

### 匯出設定

1. 前往「裝置設定」頁面
2. 點擊「匯出設定」
3. 選擇要匯出的項目：
   - 系統設定
   - AI 代理配置
   - 掃描報告

### 匯入設定

1. 前往「裝置設定」頁面
2. 點擊「匯入設定」
3. 選擇備份檔案
4. 確認要還原的項目

## 行動裝置使用說明

目前本應用程式主要支援桌面環境，可通過以下方式在行動裝置上使用：

### 遠端存取方案

1. 使用 VNC 或遠端桌面：
   - 在桌面端安裝 VNC 伺服器
   - 在手機上安裝 VNC 客戶端
   - 通過 VNC 連接使用完整功能

2. 網頁介面（開發中）：
   - 啟用網頁介面功能
   - 通過瀏覽器存取
   - 支援基本監控功能

### 未來計劃

- 開發原生 iOS/Android 應用程式
- 提供 App Store/Google Play 下載
- 支援完整的行動端功能
- 實現即時同步功能

## 常見問題

### Q: 找不到桌面圖示？
A: 嘗試以下步驟：
1. 重新執行安裝腳本
2. 檢查 `~/.local/share/applications/` 目錄
3. 更新應用程式資料庫：`update-desktop-database ~/.local/share/applications/`

### Q: 如何更新應用程式？
A: 執行以下命令：
```bash
cd ai-agent-assistant
git pull
python3 src/install.py
```

### Q: 如何解除安裝？
A: 執行以下命令：
```bash
rm -rf ~/.local/share/ai-agent-assistant
rm ~/.local/share/applications/ai-agent-assistant.desktop
```

## 技術支援

- 問題回報：https://github.com/yourusername/ai-agent-assistant/issues
- 文件網站：https://ai-agent-assistant.readthedocs.io/
- 電子郵件：support@example.com

## 版本資訊

目前版本：0.1.0
- 支援繁體中文介面
- 基本系統監控功能
- AI 代理設計工具
- 桌面環境整合
