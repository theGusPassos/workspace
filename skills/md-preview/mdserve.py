#!/usr/bin/env python3
"""Serve a directory; .md files are rendered client-side with marked + GitHub CSS."""
import html, json, os, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8765

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>body{{margin:0;background:#fff}}@media(prefers-color-scheme:dark){{body{{background:#0d1117}}}}
.markdown-body{{max-width:900px;margin:0 auto;padding:32px 16px}} nav{{font:14px sans-serif;margin-bottom:16px}}</style>
</head><body><article class="markdown-body"><nav><a href="/">index</a> · {title}</nav><div id="c"></div></article>
<script>
const src = {src};
document.getElementById('c').innerHTML = marked.parse(src);
document.querySelectorAll('code.language-mermaid').forEach(el => {{
  const d = document.createElement('div'); d.className = 'mermaid'; d.textContent = el.textContent;
  el.parentElement.replaceWith(d);
}});
mermaid.initialize({{startOnLoad:false, theme: matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'default'}});
mermaid.run();
</script></body></html>"""


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/":
            return self.index()
        full = os.path.normpath(os.path.join(ROOT, path.lstrip("/")))
        if full.startswith(ROOT) and full.endswith(".md") and os.path.isfile(full):
            with open(full, encoding="utf-8") as f:
                text = f.read()
            # json.dumps + escape "</" so the markdown can't close the <script> tag
            body = PAGE.format(title=html.escape(path), src=json.dumps(text).replace("</", "<\\/"))
            return self.send(body)
        return super().do_GET()

    def index(self):
        files = []
        for d, dirs, fs in os.walk(ROOT):
            dirs[:] = [x for x in dirs if not x.startswith(".") and x != "node_modules"]
            files += [os.path.relpath(os.path.join(d, f), ROOT) for f in fs if f.endswith(".md")]
        md = "# Markdown files\n\n" + "\n".join(f"- [{f}](/{f})" for f in sorted(files))
        self.send(PAGE.format(title="index", src=json.dumps(md)))

    def send(self, body):
        b = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)


print(f"http://localhost:{PORT}/  ->  {ROOT}", flush=True)
ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
