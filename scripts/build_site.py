"""Build the committed GitHub Pages site from the original Markdown documents."""
from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as etree

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from build_pdf_request import build_pdf_request

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "docs"
OUT = PAGES / "ai-responsibility"
REPO = "https://github.com/aclicn/aclicn.github.io"
DOCUMENTS = [
    ("AI-research-accountability-literature-review", ("文獻評述與統整觀點", "Research synthesis"),
     ("從研究各階段的 AI 使用出發，整理責任歸屬、理解與驗證的論點。", "The original English summary of accountability, understanding, and verification across research stages.")),
    ("annotated-bibliography-AI-accountability-epistemics", ("註解書目", "Annotated bibliography"),
     ("依主題閱讀 40 篇文獻的摘要，查看 DOI、PDF 狀態與來源限制。", "Summaries of 40 papers, grouped by theme, with DOI links, PDF status, and source limitations.")),
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


def filename(base, language):
    return base + ('-en' if language == 'en' else '')


def shell(title, content, active="", toc="", language="zh-Hant-TW"):
    en = language == 'en'
    def tr(zh, english):
        return english if en else zh
    home = filename('index', language) + '.html'
    nav = f'<a href="{home}"' + (' aria-current="page"' if not active else '') + '>' + tr('文件首頁', 'Documents') + '</a>'
    for base, labels, _ in DOCUMENTS:
        slug = filename(base, language)
        current = ' aria-current="page"' if base == active else ''
        nav += f'<a href="{slug}.html"{current}>{labels[int(en)]}</a>'
    alternate_language = 'zh-Hant-TW' if en else 'en'
    alternate = filename(active or 'index', alternate_language) + '.html'
    nav += f'<a href="{alternate}" hreflang="{alternate_language}" lang="{alternate_language}">{tr("English", "繁體中文")}</a>'
    contents = tr('本頁目錄', 'On this page')
    sidebar = f'<aside aria-label="{contents}"><details open><summary>{contents}</summary>{toc}</details></aside>' if toc else ''
    layout = 'reading-layout' if toc else 'home-layout'
    return f'''<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{tr('AI 研究責任：文獻評述與註解書目。', 'AI research accountability: synthesis and annotated bibliography.')}">
<link rel="alternate" hreflang="{alternate_language}" href="{alternate}">
<title>{escape(title)} · Responsible AI</title>
<link rel="stylesheet" href="assets/site.css">
</head>
<body id="top">
<a class="skip" href="#main">{tr('跳至主要內容', 'Skip to content')}</a>
<header><a class="brand" href="{home}">ACL <span>/ RESPONSIBLE AI</span></a><a href="{REPO}">{tr('GitHub 專案', 'GitHub repository')} ↗</a></header>
<nav class="documents" aria-label="{tr('文件導覽', 'Document navigation')}">{nav}</nav>
<div class="{layout}">{sidebar}<main id="main">{content}</main></div>
<footer><span>{tr('AI 研究責任 · 文獻與閱讀材料', 'AI research accountability · Literature and reading materials')}</span><a href="#top">{tr('回到頁首', 'Back to top')} ↑</a></footer>
</body>
</html>
'''


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    published = []
    for language in ('zh-Hant-TW', 'en'):
        en = language == 'en'
        def tr(zh, english):
            return english if en else zh
        for base, _, _ in DOCUMENTS:
            slug = filename(base, language)
            source = (ROOT / f"{slug}.md").read_text(encoding="utf-8-sig")
            # Source documents link to Markdown; web pages link to the matching HTML.
            for linked_base, _, _ in DOCUMENTS:
                for linked_language in ('zh-Hant-TW', 'en'):
                    linked = filename(linked_base, linked_language)
                    source = source.replace(f']({linked}.md)', f']({linked}.html)')
            md = markdown.Markdown(extensions=["extra", "toc", Links()], extension_configs={"toc": {"toc_depth": "2-3"}})
            body = md.convert(source)
            title = re.search(r"^# (.+)$", source, re.MULTILINE).group(1)
            toolbar = f'<div class="document-tools"><span>{tr("閱讀文件", "Reading document")}</span><a href="{REPO}/blob/main/{slug}.md">{tr("Markdown 原文", "Markdown source")} ↗</a></div>'
            (OUT / f"{slug}.html").write_text(shell(title, toolbar + '<article>' + body + '</article>', base, md.toc, language), encoding="utf-8")
            published.append(slug + '.html')
        entries = ''.join(f'<li><span class="number">0{i}</span><div><h2><a href="{filename(base, language)}.html">{labels[int(en)]} →</a></h2><p>{descriptions[int(en)]}</p></div></li>' for i, (base, labels, descriptions) in enumerate(DOCUMENTS, 1))
        downloads = f'<li><a href="pdf-request-list.html">{tr("PDF 協助取得清單（英文，可轉寄）", "PDF request list for colleagues")}</a></li>'
        downloads += f'<li><a href="{REPO}/tree/main/pdfs">{tr("全部 PDF", "All PDF files")} ({len(list((ROOT / "pdfs").rglob("*.pdf")))})</a></li>'
        downloads += ''.join(f'<li><a href="{REPO}/tree/main/pdfs/part{i}">{tr("單篇 PDF · 第", "Individual PDFs · Part")} {i}</a></li>' for i in (1, 2))
        archives = ''.join(f'<li><a href="{REPO}/raw/refs/heads/main/{path.name}">{tr("全文 PDF 彙整 · 第", "PDF archive · Part")} {i}（ZIP, {path.stat().st_size / 1024 / 1024:.1f} MB）↓</a></li>' for i, path in enumerate(sorted(ROOT.glob('pdfs-fulltext-part*.zip')), 1))
        home = f'''<section class="intro"><p class="eyebrow">{tr('研究實踐 / 責任歸屬 / 認識論', 'RESEARCH PRACTICE / ACCOUNTABILITY / EPISTEMOLOGY')}</p>
<h1>{tr('AI 在研究中的使用<br>與責任歸屬', 'AI in research<br>and accountability')}</h1>
<p class="lead">{tr('誰能為主張負責？研究者如何保有自己的判斷與理解？', 'Who can answer for a claim? How do researchers retain their own judgment and understanding?')}</p>
<p>{tr('這裡收錄文獻評述與註解書目，供研究團隊閱讀、討論與檢核。', 'A research synthesis and annotated bibliography for reading, discussion, and verification.')}</p></section>
<ol class="document-list">{entries}</ol>
<section class="downloads"><h2>{tr('全文資料', 'Full-text materials')}</h2><ul>{downloads}{archives}</ul></section>'''
        homepage = filename('index', language) + '.html'
        (OUT / homepage).write_text(shell(tr('AI 在研究中的使用與責任歸屬', 'AI in research and accountability'), home, language=language), encoding="utf-8")
        published.append(homepage)
    (PAGES / '.nojekyll').touch()
    # Keep previously published URLs working after moving the reading site.
    for page in published:
        target = 'ai-responsibility/' + ('' if page == 'index.html' else page)
        redirect = f'''<!doctype html>
<html lang="zh-Hant-TW"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="https://aclicn.github.io/{target}">
<title>AI 研究責任 · 網址已更新</title></head>
<body><p>網站已移至 <a href="{target}">AI 研究責任</a>。</p></body></html>
'''
        (PAGES / page).write_text(redirect, encoding='utf-8')
    build_pdf_request()
    print(f"Built {len(published)} document/index pages and the PDF request list in {OUT}")


if __name__ == '__main__':
    build()
