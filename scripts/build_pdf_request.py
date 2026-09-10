"""Create a self-contained HTML list that can be attached to a PDF request."""
from datetime import date
from pathlib import Path
import re

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/ai-responsibility/pdf-request-list.html'


def build_pdf_request():
    source = (ROOT / 'annotated-bibliography-AI-accountability-epistemics-en.md').read_text(encoding='utf-8')
    entries = source.split('## Consolidated references', 1)[0].splitlines()
    missing, unlocated = [], []
    seen = set()
    local_authors = {p.name.split('_')[0].replace(' ', '').lower() for p in (ROOT / 'pdfs').rglob('*.pdf')}
    for line in entries:
        if not line.startswith(('❌ ', '⚠️ ')):
            continue
        citation = line.split(' ', 1)[1]
        doi = re.search(r'\[DOI: ([^\]]+)\]', citation)
        if not doi:
            raise ValueError(f'Missing DOI: {citation}')
        if doi[1].lower() in seen:
            continue
        seen.add(doi[1].lower())
        author = citation.split(',')[0].replace(' ', '').lower()
        if author in local_authors:
            raise ValueError(f'PDF now exists for {author}; update its bibliography status before rebuilding.')
        (missing if line.startswith('❌') else unlocated).append(citation)
    missing.sort(key=str.casefold)
    unlocated.sort(key=str.casefold)

    def reference_list(citations):
        return '<ol class="references">' + ''.join('<li>' + markdown.markdown(citation) + '</li>' for citation in citations) + '</ol>'

    optional = ''
    if unlocated:
        optional = f'''<section aria-labelledby="additional"><h2 id="additional">Additional file to locate ({len(unlocated)})</h2>
<p>This item was previously recorded as obtained, but its PDF is absent from the current project folders and archives. It is separate from the {len(missing)} references above and is not recorded as a failed download. A replacement copy or a working public PDF link would be helpful.</p>
{reference_list(unlocated)}</section>'''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Full-text PDF request list for a literature review on AI research accountability.">
<title>Full-text PDF request · AI research accountability</title>
<style>
:root {{ color-scheme: light; --ink: #242824; --muted: #596159; --line: #d8ddd5; --accent: #975020; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 2.5rem 1.25rem; color: var(--ink); background: #f7f7f3; font: 17px/1.7 system-ui, -apple-system, "Segoe UI", sans-serif; }}
main {{ max-width: 900px; margin: auto; padding: 2.5rem 3rem; background: white; border: 1px solid var(--line); }}
.eyebrow {{ color: var(--accent); font-size: .8rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }}
h1 {{ font: 700 clamp(1.9rem, 5vw, 2.7rem)/1.2 Georgia, serif; margin: .5rem 0 1rem; }}
h2 {{ font-size: 1.3rem; line-height: 1.4; margin-top: 2.5rem; }}
.meta, footer {{ color: var(--muted); font-size: .85rem; }}
.request {{ border-left: 3px solid var(--accent); padding-left: 1.25rem; margin: 1.75rem 0; }}
.references {{ padding-left: 1.75rem; }}
.references > li {{ padding: .75rem 0 .75rem .5rem; border-bottom: 1px solid var(--line); break-inside: avoid; }}
.references p {{ margin: .25rem 0; overflow-wrap: anywhere; }}
.references li::marker {{ color: var(--accent); font-weight: 700; }}
a {{ color: #235d50; overflow-wrap: anywhere; text-underline-offset: .2em; }}
a:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 3px; }}
footer {{ border-top: 1px solid var(--line); padding-top: 1rem; margin-top: 2rem; }}
@media (max-width: 600px) {{ body {{ padding: .75rem; }} main {{ padding: 1.25rem; }} }}
@media print {{ @page {{ margin: 18mm; }} body, main {{ background: white; padding: 0; border: 0; font-size: 10.5pt; }} h2 {{ break-after: avoid; }} a {{ color: inherit; }} }}
</style>
</head>
<body><main>
<header><p class="eyebrow">AI research accountability · Library request</p>
<h1>Full-text PDFs requested</h1>
<p class="meta">Prepared {date.today().isoformat()} · {len(missing)} references not yet obtained</p></header>
<div class="request"><p>Dear colleagues,</p>
<p>Could you help us obtain full-text PDFs of the references below through your institution's library access? They are needed for a literature review on AI use, accountability, and epistemic risks in research. If you cannot obtain a PDF, a library permalink or a link to an accessible author manuscript would also be helpful. Thank you for your help.</p></div>
<section aria-labelledby="requested"><h2 id="requested">References not yet downloaded ({len(missing)})</h2>
<p>Each reference includes a DOI link. The correction associated with Gerlich (2025) is also linked.</p>
{reference_list(missing)}</section>
{optional}
<footer><p>Source: the project's <a href="https://aclicn.github.io/ai-responsibility/annotated-bibliography-AI-accountability-epistemics-en.html">annotated bibliography</a>. Citations and existing acquisition records were extracted from that document; bibliographic details have not been independently reverified for this request. “Not yet downloaded” describes our collection, not whether an article is paywalled or available through a particular institution.</p>
<p>This HTML file is self-contained and can be forwarded as an attachment or printed.</p></footer>
</main></body></html>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding='utf-8', newline='\n')
    print(f'Built PDF request list: {len(missing)} missing references, {len(unlocated)} separately noted file(s).')


if __name__ == '__main__':
    build_pdf_request()
