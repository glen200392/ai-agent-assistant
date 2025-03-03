# GitHub 上傳指南

## 1. 建立 GitHub 帳號

如果還沒有 GitHub 帳號，請先至 [GitHub](https://github.com) 註冊。

## 2. 建立新的 Repository

1. 登入 GitHub 後，點擊右上角的 "+" 按鈕，選擇 "New repository"
2. 填寫 Repository 資訊：
   - Repository name: `ai-agent-assistant`
   - Description: `AI 代理助手 - 系統分析與 AI 代理管理工具`
   - 選擇 "Public"
   - 勾選 "Add a README file"
   - 選擇 "MIT License"
3. 點擊 "Create repository"

## 3. 在本地設定 Git

```bash
# 進入專案目錄
cd /Users/tsunglunho/Desktop/cline\ project

# 初始化 Git 倉庫
git init

# 設定 Git 使用者資訊（如果還沒設定過）
git config --global user.name "你的 GitHub 使用者名稱"
git config --global user.email "你的 GitHub 信箱"
```

## 4. 加入檔案到 Git

```bash
# 加入所有檔案
git add .

# 建立第一個 commit
git commit -m "Initial commit: 建立專案基礎架構"
```

## 5. 設定遠端倉庫並上傳

```bash
# 設定遠端倉庫（將 'yourusername' 替換為你的 GitHub 使用者名稱）
git remote add origin https://github.com/yourusername/ai-agent-assistant.git

# 上傳至 GitHub
git push -u origin main
```

## 6. 使用 GitHub Desktop（選項）

如果不熟悉命令列操作，也可以使用 GitHub Desktop：

1. 下載並安裝 [GitHub Desktop](https://desktop.github.com/)
2. 登入你的 GitHub 帳號
3. 點擊 "File" -> "Add Local Repository"
4. 選擇專案目錄
5. 填寫 commit 訊息後點擊 "Publish repository"

## 7. 驗證上傳

1. 前往你的 GitHub 頁面 `https://github.com/yourusername/ai-agent-assistant`
2. 確認所有檔案都已正確上傳
3. 檢查 README.md 是否正確顯示

## 8. 設定 GitHub Pages（可選）

如果要建立專案網站：

1. 前往 repository 的 "Settings"
2. 點擊左側選單的 "Pages"
3. 在 "Source" 選擇 "main" 分支
4. 點擊 "Save"

## 9. 後續更新

每次修改後上傳：

```bash
# 查看修改的檔案
git status

# 加入修改的檔案
git add .

# 建立 commit
git commit -m "更新內容說明"

# 上傳至 GitHub
git push
```

## 10. 協作設定

1. 前往 repository 的 "Settings" -> "Manage access"
2. 點擊 "Add people" 可以邀請其他開發者
3. 設定分支保護規則：
   - 前往 "Settings" -> "Branches"
   - 點擊 "Add rule"
   - 設定主分支的保護規則

## 注意事項

1. 確保 `.gitignore` 已正確設定，避免上傳不必要的檔案
2. 不要上傳敏感資訊（密碼、API 金鑰等）
3. 保持 commit 訊息清晰明確
4. 定期更新本地倉庫：`git pull`

## 常見問題

### Q: 如果上傳失敗怎麼辦？
A: 檢查以下幾點：
1. 確認網路連線
2. 確認 Git 設定正確
3. 確認 GitHub 帳號權限
4. 嘗試使用 SSH 金鑰認證

### Q: 如何處理衝突？
A: 當發生衝突時：
1. 先 `git pull` 取得最新版本
2. 解決衝突檔案
3. 重新 commit 並 push

### Q: 如何回復之前的版本？
A: 使用以下指令：
```bash
# 查看提交歷史
git log

# 回復到特定版本
git reset --hard [commit_hash]
