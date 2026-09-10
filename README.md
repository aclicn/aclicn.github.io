# Responsible AI：研究中的 AI 使用與責任歸屬

文獻評述、註解書目與全文 PDF 彙整。中文與英文各自提供 Markdown 及 HTML。

網站：https://aclicn.github.io/ai-responsibility/

## 文件

| 文件 | 繁體中文 | English |
| --- | --- | --- |
| 文獻評述 | [Markdown](AI-research-accountability-literature-review.md) · [HTML](https://aclicn.github.io/ai-responsibility/AI-research-accountability-literature-review.html) | [Markdown](AI-research-accountability-literature-review-en.md) · [HTML](https://aclicn.github.io/ai-responsibility/AI-research-accountability-literature-review-en.html) |
| 註解書目 | [Markdown](annotated-bibliography-AI-accountability-epistemics.md) · [HTML](https://aclicn.github.io/ai-responsibility/annotated-bibliography-AI-accountability-epistemics.html) | [Markdown](annotated-bibliography-AI-accountability-epistemics-en.md) · [HTML](https://aclicn.github.io/ai-responsibility/annotated-bibliography-AI-accountability-epistemics-en.html) |

文獻評述只保留統整觀點；英文版保留原稿較精簡的英文摘要。逐篇摘要集中在獨立註解書目，兩種語言各保留 40 篇文章及 DOI、PDF 狀態。

原始 Markdown 為內容來源；HTML 版本保留原文。網站轉換不代表另行查核文獻或原文中的查核聲明。

## PDF 全文

兩份 ZIP 的 PDF 已分別解壓，可直接在 GitHub 開啟或下載單篇檔案：

- [part1：13 篇 PDF](pdfs/part1/)
- [part2：14 篇 PDF](pdfs/part2/)

[PDF 協助取得清單（英文 HTML，可轉寄）](docs/ai-responsibility/pdf-request-list.html)：列出尚未取得的 12 篇文獻，附完整書目與 DOI；另列 1 篇原紀錄已取得但目前未收錄的檔案。HTML 內含樣式，可直接作為附件寄給同事；執行網站建置時會依英文註解書目的狀態重新產生。

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
