# GitHub 同步指南

## 快速開始

### 1. 設定 GitHub 驗證

```bash
# 設定 Git 使用者資訊
git config --global user.name "你的GitHub使用者名稱"
git config --global user.email "你的GitHub信箱"

# 設定 SSH 金鑰（建議使用）
ssh-keygen -t ed25519 -C "你的GitHub信箱"
cat ~/.ssh/id_ed25519.pub
# 將輸出的內容複製到 GitHub > Settings > SSH Keys
```

### 2. 自動同步設定

在專案目錄下建立自動同步腳本：

```bash
# 建立同步腳本
cat > sync_github.sh << 'EOF'
#!/bin/bash

# 確保在正確的目錄
cd "$(dirname "$0")"

# 檢查是否有未提交的更改
if [[ $(git status --porcelain) ]]; then
    echo "發現更改，準備同步..."
    
    # 添加所有更改
    git add .
    
    # 提交更改
    echo "請輸入更新說明（直接按 Enter 使用預設說明）："
    read commit_message
    if [ -z "$commit_message" ]; then
        commit_message="自動同步更新 $(date '+%Y-%m-%d %H:%M:%S')"
    fi
    git commit -m "$commit_message"
    
    # 推送到 GitHub
    git push
    
    echo "同步完成！"
else
    echo "沒有需要同步的更改"
fi
EOF

# 設定執行權限
chmod +x sync_github.sh
```

### 3. 使用方式

#### A. 使用同步腳本
```bash
# 執行同步腳本
./sync_github.sh
```

#### B. 手動同步
```bash
# 查看更改
git status

# 加入更改
git add .

# 提交更改
git commit -m "更新說明"

# 推送到 GitHub
git push
```

## 自動同步設定

### 1. 使用 cron 定時同步（Linux/macOS）

```bash
# 編輯 crontab
crontab -e

# 加入以下行（每小時同步一次）
0 * * * * cd /path/to/your/project && ./sync_github.sh >> sync.log 2>&1
```

### 2. 使用 GitHub Desktop（圖形介面）

1. 下載並安裝 [GitHub Desktop](https://desktop.github.com/)
2. 登入你的 GitHub 帳號
3. 加入現有專案
4. 定期點擊 "Sync" 按鈕

## 同步衝突處理

### 1. 避免衝突
```bash
# 開始工作前先更新
git pull

# 定期同步
git push
```

### 2. 解決衝突
```bash
# 如果發生衝突
git pull
# 手動解決衝突文件
git add .
git commit -m "解決衝突"
git push
```

## 分支管理

### 1. 建立功能分支
```bash
# 建立並切換到新分支
git checkout -b feature-name

# 完成後合併回主分支
git checkout main
git merge feature-name
```

### 2. 同步特定分支
```bash
# 推送特定分支
git push origin feature-name

# 拉取特定分支
git pull origin feature-name
```

## 版本標記

```bash
# 建立新版本標記
git tag -a v1.0.0 -m "版本 1.0.0"

# 推送標記
git push --tags
```

## 進階技巧

### 1. 設定 Git 忽略檔案
```bash
# 編輯 .gitignore
nano .gitignore

# 常用忽略項目
__pycache__/
*.pyc
.env
.vscode/
```

### 2. 檢視歷史記錄
```bash
# 查看提交歷史
git log

# 查看特定檔案的歷史
git log -p filename
```

### 3. 還原更改
```bash
# 還原單個檔案
git checkout -- filename

# 還原全部更改
git reset --hard HEAD
```

## 常見問題

### Q: 如何處理 "拒絕推送" 錯誤？
```bash
# 先更新本地版本
git pull
# 解決衝突後再推送
git push
```

### Q: 如何取消最後一次提交？
```bash
# 取消提交但保留更改
git reset --soft HEAD^

# 完全取消提交及更改
git reset --hard HEAD^
```

### Q: 如何查看遠端倉庫狀態？
```bash
# 查看遠端倉庫資訊
git remote -v

# 查看分支狀態
git branch -a
```

## 建議工作流程

1. 開始工作前：
   ```bash
   git pull
   ```

2. 工作過程中：
   - 定期執行 `./sync_github.sh`
   - 或使用 GitHub Desktop 同步

3. 完成工作後：
   ```bash
   git add .
   git commit -m "完成工作描述"
   git push
   ```

## 安全建議

1. 不要提交敏感資訊
2. 使用 SSH 金鑰而非密碼
3. 定期更改 GitHub 密碼
4. 啟用兩步驗證

這樣設定後，您就可以：
- 透過腳本快速同步
- 定時自動同步
- 使用圖形介面管理
- 安全地協同工作
