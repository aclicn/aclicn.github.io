"""Build the committed GitHub Pages site from the original Markdown documents."""
from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as etree

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
REPO = "https://github.com/aclicn/aclicn.github.io"
DOCUMENTS = [
    ("AI-research-accountability-literature-review", "文獻評述與統整觀點", "從研究各階段的 AI 使用出發，整理責任歸屬、理解與驗證的論點。"),
    ("annotated-bibliography-AI-accountability-epistemics", "註解書目", "依主題閱讀文獻，對照中英文介紹、重點與來源限制。"),
    ("reading-list-AI-accountability-epistemics", "延伸閱讀", "快速瀏覽學術寫作與出版中的責任歸屬與認識論風險文獻。"),
]


class BareURL(InlineProcessor):
    def handleMatch(self, match, data):
        url = match.group(0).rstrip(".,;:")
        node = etree.Element("a", {"href": url})
        node.text = url
        return node, match.start(), match.start() + len(url)


class Links(Extension):
    def extendMarkdown(self, md):
        # ASCII URL characters stop before Chinese punctuation in bibliography entries.
        md.inlinePatterns.register(BareURL(r"https?://[A-Za-z0-9_~:/?#\[\]@!$&'()*+,;=.%\-]+", md), "bare_url", 95)


def shell(title, content, active="", toc=""):
    nav = '<a href="index.html"' + (' aria-current="page"' if not active else '') + '>文件首頁</a>'
    for slug, label, _ in DOCUMENTS:
        current = ' aria-current="page"' if slug == active else ''
        nav += f'<a href="{slug}.html"{current}>{label}</a>'
    sidebar = f'<aside aria-label="本頁目錄"><details open><summary>本頁目錄</summary>{toc}</details></aside>' if toc else ''
    layout = 'reading-layout' if toc else 'home-layout'
    return f'''<!doctype html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="AI 研究責任：文獻評述、註解書目與延伸閱讀。">
<title>{escape(title)} · Responsible AI</title>
<link rel="stylesheet" href="assets/site.css">
</head>
<body id="top">
<a class="skip" href="#main">跳至主要內容</a>
<header><a class="brand" href="index.html">ACL <span>/ RESPONSIBLE AI</span></a><a href="{REPO}">GitHub 專案 ↗</a></header>
<nav class="documents" aria-label="文件導覽">{nav}</nav>
<div class="{layout}">{sidebar}<main id="main">{content}</main></div>
<footer><span>AI 研究責任 · 文獻與閱讀材料</span><a href="#top">回到頁首 ↑</a></footer>
</body>
</html>
'''


def build():
    OUT.mkdir(exist_ok=True)
    for slug, label, _ in DOCUMENTS:
        source = (ROOT / f"{slug}.md").read_text(encoding="utf-8-sig")
        md = markdown.Markdown(extensions=["extra", "toc", Links()], extension_configs={"toc": {"toc_depth": "2-3"}})
        body = md.convert(source)
        title = re.search(r"^# (.+)$", source, re.MULTILINE).group(1)
        toolbar = f'<div class="document-tools"><span>閱讀文件</span><a href="{REPO}/blob/main/{slug}.md">Markdown 原文 ↗</a></div>'
        (OUT / f"{slug}.html").write_text(shell(title, toolbar + '<article>' + body + '</article>', slug, md.toc), encoding="utf-8")
    entries = ''.join(f'<li><span class="number">0{i}</span><div><h2><a href="{slug}.html">{label} →</a></h2><p>{description}</p></div></li>' for i, (slug, label, description) in enumerate(DOCUMENTS, 1))
    archives = ''.join(f'<li><a href="{REPO}/raw/refs/heads/main/{path.name}">全文 PDF 彙整 · 第 {i} 部分（ZIP，{path.stat().st_size / 1024 / 1024:.1f} MB）↓</a></li>' for i, path in enumerate(sorted(ROOT.glob('pdfs-fulltext-part*.zip')), 1))
    home = f'''<section class="intro"><p class="eyebrow">研究實踐 / 責任歸屬 / 認識論</p>
<h1>AI 在研究中的使用<br>與責任歸屬</h1>
<p class="lead">誰能為主張負責？研究者如何保有自己的判斷與理解？</p>
<p>這裡收錄文獻評述、註解書目與延伸閱讀，供研究團隊閱讀、討論與檢核。</p></section>
<ol class="document-list">{entries}</ol>
<section class="downloads"><h2>全文資料</h2><ul>{archives}</ul></section>'''
    (OUT / 'index.html').write_text(shell('AI 在研究中的使用與責任歸屬', home), encoding="utf-8")
    (OUT / '.nojekyll').touch()
    print(f"Built {len(DOCUMENTS) + 1} HTML pages in {OUT}")


if __name__ == '__main__':
    build()
