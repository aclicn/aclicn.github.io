# Responsible AI：研究中的 AI 使用與責任歸屬

文獻評述、註解書目、延伸閱讀與全文 PDF 彙整。

網站：https://aclicn.github.io/ai-responsibility/

## 文件

- [文獻評述與統整觀點](AI-research-accountability-literature-review.md)
- [註解書目](annotated-bibliography-AI-accountability-epistemics.md)
- [延伸閱讀](reading-list-AI-accountability-epistemics.md)

原始 Markdown 為內容來源；HTML 版本保留原文。網站轉換不代表另行查核文獻或原文中的查核聲明。

## PDF 全文

兩份 ZIP 的 PDF 已分別解壓，可直接在 GitHub 開啟或下載單篇檔案：

- [part1：13 篇 PDF](pdfs/part1/)
- [part2：14 篇 PDF](pdfs/part2/)

## 更新網站

編輯根目錄的 Markdown 後，重新產生 HTML，將來源與 `docs/` 一起提交：

```powershell
python -m pip install -r requirements.txt
python scripts/build_site.py
git add .
git commit -m "docs: update research materials"
git push
```

GitHub Pages 設定：`Deploy from a branch`、`main`、`/docs`。網站無需 JavaScript；PDF ZIP 保存在儲存庫，由首頁連結下載。

本機預覽：`python -m http.server 8000 --directory docs`，開啟 http://localhost:8000/ai-responsibility/。舊的首頁及文件網址會自動導向新位置。
