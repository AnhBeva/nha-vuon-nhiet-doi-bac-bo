from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent

ORDER = [
    "README.md",
    "ban-do-nha-vuon-bac-bo.md",
    "giao-trinh-nha-vuon-bac-bo.md",
    "thuat-ngu-nha-vuon-bac-bo.md",
    "cong-cu-thuc-hanh.md",
]
ORDER.extend(sorted(p.name for p in ROOT.glob("Module-*.md")))


def anchor(text):
    text = text.lower()
    repl = {
        "à":"a","á":"a","ạ":"a","ả":"a","ã":"a","â":"a","ầ":"a","ấ":"a","ậ":"a","ẩ":"a","ẫ":"a","ă":"a","ằ":"a","ắ":"a","ặ":"a","ẳ":"a","ẵ":"a",
        "è":"e","é":"e","ẹ":"e","ẻ":"e","ẽ":"e","ê":"e","ề":"e","ế":"e","ệ":"e","ể":"e","ễ":"e",
        "ì":"i","í":"i","ị":"i","ỉ":"i","ĩ":"i",
        "ò":"o","ó":"o","ọ":"o","ỏ":"o","õ":"o","ô":"o","ồ":"o","ố":"o","ộ":"o","ổ":"o","ỗ":"o","ơ":"o","ờ":"o","ớ":"o","ợ":"o","ở":"o","ỡ":"o",
        "ù":"u","ú":"u","ụ":"u","ủ":"u","ũ":"u","ư":"u","ừ":"u","ứ":"u","ự":"u","ử":"u","ữ":"u",
        "ỳ":"y","ý":"y","ỵ":"y","ỷ":"y","ỹ":"y","đ":"d",
    }
    text = "".join(repl.get(ch, ch) for ch in text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def inline_md(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def parse_table(lines):
    rows = []
    for line in lines:
        cells = [inline_md(c.strip()) for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    head = rows[0]
    body = rows[2:] if len(rows) > 1 and all(set(c.strip()) <= {"-", ":"} for c in rows[1]) else rows[1:]
    html = ["<div class='table-wrap'><table><thead><tr>"]
    html.extend(f"<th>{c}</th>" for c in head)
    html.append("</tr></thead><tbody>")
    for row in body:
        html.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
    html.append("</tbody></table></div>")
    return "".join(html)


def md_to_html(markdown, section_id):
    out = []
    lines = markdown.splitlines()
    i = 0
    in_ul = False
    in_ol = False
    in_code = False
    code_lines = []
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                out.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(parse_table(table_lines))
            continue
        if not stripped:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            i += 1
            continue
        if stripped.startswith("#"):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            hid = f"{section_id}-{anchor(text)}"
            out.append(f"<h{min(level, 4)} id='{hid}'>{inline_md(text)}</h{min(level, 4)}>")
        elif stripped.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(stripped[2:])}</li>")
        elif re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(re.sub(r'^\d+\.\s+', '', stripped))}</li>")
        elif stripped == "---":
            out.append("<hr>")
        else:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1
    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")
    return "\n".join(out)


def first_heading(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Tài liệu"


def build():
    docs = []
    for name in ORDER:
        path = ROOT / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            title = first_heading(text)
            sid = anchor(name.replace(".md", ""))
            docs.append((name, title, sid, md_to_html(text, sid)))

    nav = "\n".join(f"<a href='#{sid}'>{escape(title)}</a>" for _, title, sid, _ in docs)
    articles = "\n".join(f"<article id='{sid}' class='doc'>{html}</article>" for _, _, sid, html in docs)
    module_count = len([d for d in docs if d[0].startswith("Module-")])
    html = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nền Tảng Học Thiết Kế Nhà Và Vườn Nhiệt Đới Bắc Bộ</title>
  <style>
    :root {{
      --bg: #f4f6f5;
      --paper: #ffffff;
      --text: #1f2423;
      --muted: #63706c;
      --line: #d8dfdc;
      --accent: #276749;
      --accent-2: #9a5b3d;
      --soft: #e8f0ec;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      letter-spacing: 0;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      background: rgba(255,255,255,.96);
      position: sticky;
      top: 0;
      z-index: 5;
      backdrop-filter: blur(16px);
    }}
    .top {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 18px 28px;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      align-items: center;
    }}
    h1, h2, h3, h4 {{ line-height: 1.2; letter-spacing: 0; }}
    .brand h1 {{ font-size: clamp(22px, 3vw, 38px); margin: 0 0 6px; }}
    .brand p {{ margin: 0; color: var(--muted); max-width: 860px; }}
    .stats {{ display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end; }}
    .stat {{ border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px; background: var(--soft); min-width: 100px; }}
    .stat strong {{ display: block; font-size: 20px; }}
    .layout {{
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 310px minmax(0, 1fr);
      gap: 34px;
      padding: 26px 28px 80px;
    }}
    nav {{
      position: sticky;
      top: 96px;
      align-self: start;
      max-height: calc(100vh - 120px);
      overflow: auto;
      border-right: 1px solid var(--line);
      padding-right: 18px;
    }}
    nav a {{
      display: block;
      color: var(--text);
      text-decoration: none;
      padding: 7px 8px;
      border-radius: 6px;
      font-size: 14px;
    }}
    nav a:hover {{ background: var(--soft); color: var(--accent); }}
    main {{ min-width: 0; }}
    .doc {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 54px);
      margin-bottom: 24px;
      box-shadow: 0 18px 50px rgba(29, 43, 38, .06);
    }}
    .doc h1 {{ margin-top: 0; font-size: clamp(30px, 5vw, 58px); }}
    .doc h2 {{ margin-top: 44px; padding-top: 16px; border-top: 1px solid var(--line); font-size: 28px; }}
    .doc h3 {{ margin-top: 28px; color: var(--accent); }}
    p, li {{ font-size: 16px; }}
    code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    pre {{ overflow: auto; background: #1f261f; color: #f7f1e7; padding: 16px; border-radius: 8px; }}
    .table-wrap {{ overflow-x: auto; margin: 18px 0; border: 1px solid var(--line); border-radius: 8px; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 720px; background: #fff; }}
    th, td {{ padding: 11px 12px; border-bottom: 1px solid var(--line); vertical-align: top; text-align: left; }}
    th {{ background: var(--soft); color: #173d2a; font-weight: 700; }}
    tr:last-child td {{ border-bottom: 0; }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 28px 0; }}
    @media (max-width: 900px) {{
      .top {{ grid-template-columns: 1fr; }}
      .stats {{ justify-content: flex-start; }}
      .layout {{ grid-template-columns: 1fr; padding: 18px 14px 50px; }}
      nav {{ position: static; max-height: 260px; border: 1px solid var(--line); border-radius: 8px; padding: 10px; background: var(--paper); }}
      .doc {{ padding: 22px 16px; }}
      table {{ min-width: 640px; }}
    }}
    @media print {{
      header, nav {{ display: none; }}
      .layout {{ display: block; padding: 0; }}
      .doc {{ box-shadow: none; border: 0; page-break-after: always; }}
      body {{ background: white; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="top">
      <div class="brand">
        <h1>Nền Tảng Học Thiết Kế Nhà Và Vườn Nhiệt Đới Bắc Bộ</h1>
        <p>Học toàn dự án từ ý tưởng, thiết kế, thi công, vận hành đến bảo trì 30-50 năm.</p>
      </div>
      <div class="stats">
        <div class="stat"><strong>{module_count}</strong>module</div>
        <div class="stat"><strong>8</strong>phần học</div>
        <div class="stat"><strong>30-50</strong>năm vòng đời</div>
      </div>
    </div>
  </header>
  <div class="layout">
    <nav aria-label="Mục lục">{nav}</nav>
    <main>{articles}</main>
  </div>
</body>
</html>"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Đã dựng index.html với {len(docs)} tài liệu, gồm {module_count} module.")


if __name__ == "__main__":
    build()
