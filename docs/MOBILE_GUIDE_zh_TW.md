# AI 代理助手手機版使用指南

## 目前可用方案

### 1. 遠端存取方式

目前本應用程式提供以下方式在手機上使用：

#### A. VNC 遠端連線
1. 在電腦端設定：
   ```bash
   # macOS 內建的螢幕共享
   系統設定 > 共享 > 螢幕共享 > 開啟

   # 或安裝 VNC 伺服器
   brew install vnc-server
   ```

2. 在手機上：
   - 下載 VNC Viewer（[App Store](https://apps.apple.com/tw/app/vnc-viewer/id352019548) / [Google Play](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android)）
   - 輸入電腦 IP 位址連線
   - 使用完整桌面版功能

#### B. 網頁版介面（開發中）
- 使用手機瀏覽器存取
- 支援基本監控功能
- 預計下一版本推出

### 2. 未來手機版本計劃

我們正在開發原生手機應用程式，預計包含：

#### iOS 版本
- 預計上架 App Store
- 原生 iOS UI 設計
- 支援 iPhone 和 iPad
- 整合 iCloud 同步

#### Android 版本
- 預計上架 Google Play
- Material Design 介面
- 支援各種 Android 裝置
- Google Drive 同步支援

#### 功能規劃
1. 基礎功能
   - 系統資源監控
   - 效能分析
   - 基本設定調整

2. 進階功能
   - 遠端控制 AI 代理
   - 即時通知
   - 跨裝置同步
   - Widget 支援

3. 專業功能
   - 自訂 AI 代理腳本
   - 效能優化建議
   - 詳細分析報告
   - 自動化任務

## 臨時解決方案

在原生應用程式推出前，您可以：

### 1. 使用 VNC 方案
```bash
# 1. 在電腦上安裝並運行程式
python3 src/install.py

# 2. 開啟遠端存取
# macOS:
系統設定 > 共享 > 螢幕共享

# Linux:
sudo apt install x11vnc
x11vnc -pw YOUR_PASSWORD

# 3. 在手機上使用 VNC Viewer 連線
```

### 2. 使用網頁版（需等待下一版本）
```bash
# 未來將支援以下使用方式：
http://your-computer-ip:8080
```

## 注意事項

1. 安全考量
   - VNC 連線建議使用強密碼
   - 只在信任的網路環境使用
   - 定期更新 VNC 客戶端

2. 網路需求
   - 建議使用 Wi-Fi 連線
   - 需要穩定的網路環境
   - 頻寬建議 10Mbps 以上

3. 效能考量
   - 遠端操作可能有延遲
   - 部分功能可能受限
   - 建議重要操作在電腦上執行

## 常見問題

### Q: VNC 連線失敗怎麼辦？
A: 檢查以下幾點：
1. 確認電腦和手機在同一個網路
2. 檢查防火牆設定
3. 確認 IP 位址正確
4. 重新啟動 VNC 服務

### Q: 何時會推出原生應用程式？
A: 我們的開發時程：
1. Beta 測試版：預計 2025 Q3
2. App Store 上架：預計 2025 Q4
3. Google Play 上架：預計 2025 Q4

### Q: 手機版會支援所有功能嗎？
A: 手機版將根據裝置特性提供最適合的功能：
1. 基礎監控和設定：完整支援
2. AI 代理操作：部分支援
3. 進階分析：建議在電腦上執行

## 技術支援

如果您在使用過程中遇到問題：

1. 檢查文件：docs/GUIDE_zh_TW.md
2. 提交問題：https://github.com/glen200392/ai-agent-assistant/issues
3. 聯繫支援：support@example.com

## 未來更新

請追蹤我們的開發進度：
1. Star 我們的 GitHub 專案
2. 關注 Release 頁面
3. 訂閱更新通知

我們會持續改善使用體驗，並盡快提供原生手機應用程式。
