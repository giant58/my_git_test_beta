# -*- coding: utf-8 -*-

'''
指令: (在windows的search列打) git bash
		○ git --version    # 顯示目前安裝git版本
	• 開始讓某個資料夾有版本控制功能
		○ cd <該資料夾目錄>     # 可以直接拖拉該資料夾到bash視窗
		○ git init    # 開始版本控制
	• 設定個人資訊(追蹤用，不必和git帳號一致)
		○ git config --global user.name "xxx"   # 姓名
		○ git config --global user.email "xxx@gmail.com"  # email
	• 基本指令
        ○ git status   # 檢查目前目錄是否有更動
		○ git add .   # 將目錄內所有檔案加到index (等候一次性更新 commit)
		○ git commit -m "message"   # 更新到local資料庫(加上message易讀)
        ○ git log   # 更新歷史 (用sourcetree看比較方便)
    • 和GitHub連結
		○ 先登入GitHub，然後點"New repository"
			§ 命名repositiory，然後點"Create repository"
            § 依push existing repository頁面說明輸入相對指定，將local目錄連結到遠端GitHub
		○ git remote add 遠端名稱 遠端網址   # 設定remote repository
			§ git remote    # 檢查現在有哪些remote repository
            § git remote -v   #檢查現在有哪些remote repository與其網址
        ○ git push -u 遠端名稱 本地名稱  #將local repository同步到remote repository
            § -u 是第一次push遠端名稱後要成為另一個branch以方便未來繼續push(就不需要再帶 -u的參數了)，未來push相同遠端名稱就不需要再帶 -u

其他指令:
	• git config --global alias.ci commit   # 將git commit … 縮短成 git ci …
	• git config --list  # 顯示設定; (最後按'q'結束)
        (在c:/user/ca_su底下有個gitconfig的檔案，就有所有被設定過的git參數)
'''
