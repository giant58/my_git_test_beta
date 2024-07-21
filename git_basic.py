# -*- coding: utf-8 -*-

'''
執行: (在windows的search列打) git bash
		○ git --version    # 顯示目前安裝git版本
	• 開始讓某個資料夾有版本控制功能
		○ cd <該資料夾目錄>     # 可以直接拖拉該資料夾到bash視窗
		○ git init    # 開始版本控制
	• 設定個人資訊(追蹤用，不必和git帳號一致)
		○ git config --global user.name "xxx"   # 姓名
		○ git config --global user.email "xxx@gmail.com"  # email
		○ git config --list  # 顯示設定; (最後按'q'結束)
	• 基本指令
        ○ git status   # 檢查目前目錄是否有更動
		○ git add .   # 將目錄內所有檔案加到index (等候一次性更新 commit)
		○ git commit -m "remark"   # 更新到local資料庫(加上remark易讀)
        ○ git log   # 更新歷史
        ○ git clone 數據庫網址  #
        ○ git git push origin master  #
'''