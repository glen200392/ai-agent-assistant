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
