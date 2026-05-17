from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent

ORDER = [
    "README.md",
    "ban-do-nha-vuon-bac-bo.md",
    "giao-trinh-nha-vuon-bac-bo.md",
    "hinh-anh-truc-quan.md",
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


def parse_image(line, next_line=None):
    match = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
    if not match:
        return None
    alt, src = match.groups()
    caption = None
    if next_line:
        cap = re.match(r"^\*Caption:\s*(.*?)\*\s*$", next_line.strip())
        if cap:
            caption = cap.group(1)
    html = [
        "<figure class='learning-figure'>",
        f"<img src='{escape(src)}' alt='{escape(alt)}' loading='lazy'>",
    ]
    if caption:
        html.append(f"<figcaption>{inline_md(caption)}</figcaption>")
    html.append("</figure>")
    return "".join(html), bool(caption)


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
        parsed_image = parse_image(stripped, lines[i + 1] if i + 1 < len(lines) else None)
        if parsed_image:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            image_html, used_caption = parsed_image
            out.append(image_html)
            i += 2 if used_caption else 1
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
      --lumi-green: #008B51;
      --lumi-green-deep: #006B3F;
      --lumi-mint: #E6F4EE;
      --lumi-pale: #F3FAF6;
      --text: #1F2933;
      --muted: #4B5563;
      --line: #DDE5E1;
      --surface: #FFFFFF;
      --code: #13251D;
      --warn: #8A5B16;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, var(--lumi-pale) 0, #f8faf9 360px, #eef3f1 100%);
      color: var(--text);
      line-height: 1.68;
      letter-spacing: 0;
    }}
    a {{ color: var(--lumi-green-deep); }}
    .site-header {{
      border-bottom: 1px solid var(--line);
      background: rgba(255,255,255,.97);
      position: sticky;
      top: 0;
      z-index: 10;
      backdrop-filter: blur(18px);
    }}
    .top {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 14px 28px;
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: 22px;
      align-items: center;
    }}
    .brand-logo {{
      display: block;
      height: 42px;
      width: auto;
      object-fit: contain;
    }}
    .brand-title {{
      min-width: 0;
      border-left: 1px solid var(--line);
      padding-left: 20px;
    }}
    .brand-kicker {{
      color: var(--lumi-green-deep);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      margin: 0 0 3px;
    }}
    .brand-title h1 {{
      font-size: clamp(18px, 2.2vw, 30px);
      margin: 0;
      line-height: 1.2;
      letter-spacing: 0;
    }}
    .brand-title p {{ margin: 4px 0 0; color: var(--muted); max-width: 780px; font-size: 14px; }}
    .stats {{ display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }}
    .stat {{
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 7px 11px;
      background: var(--surface);
      min-width: 92px;
      color: var(--muted);
      font-size: 12px;
    }}
    .stat strong {{ display: block; color: var(--lumi-green); font-size: 20px; line-height: 1.05; }}
    .hero {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 34px 28px 8px;
    }}
    .hero-panel {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-left: 6px solid var(--lumi-green);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 42px);
      display: grid;
      grid-template-columns: minmax(0, 1fr) 320px;
      gap: 28px;
      box-shadow: 0 18px 50px rgba(31, 41, 51, .06);
    }}
    .hero h2 {{
      margin: 0 0 10px;
      max-width: 980px;
      font-size: clamp(30px, 5vw, 62px);
      line-height: 1.04;
      letter-spacing: 0;
    }}
    .hero p {{ color: var(--muted); margin: 0; max-width: 850px; font-size: 17px; }}
    .hero-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 20px;
    }}
    .hero-tags span {{
      border: 1px solid var(--line);
      background: var(--lumi-mint);
      color: var(--lumi-green-deep);
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 13px;
      font-weight: 700;
    }}
    .hero-note {{
      background: var(--lumi-pale);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      align-self: start;
    }}
    .hero-note strong {{ color: var(--lumi-green-deep); display: block; margin-bottom: 8px; }}
    .hero-note p {{ font-size: 14px; }}
    .layout {{
      max-width: 1480px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 330px minmax(0, 1fr);
      gap: 28px;
      padding: 24px 28px 80px;
    }}
    nav {{
      position: sticky;
      top: 92px;
      align-self: start;
      max-height: calc(100vh - 112px);
      overflow: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      background: rgba(255,255,255,.94);
      box-shadow: 0 12px 30px rgba(31, 41, 51, .04);
    }}
    .nav-title {{
      margin: 0 0 10px;
      color: var(--lumi-green-deep);
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
    }}
    nav a {{
      display: block;
      color: var(--text);
      text-decoration: none;
      padding: 8px 9px;
      border-radius: 6px;
      font-size: 14px;
      line-height: 1.35;
      border-left: 3px solid transparent;
    }}
    nav a:hover {{
      background: var(--lumi-mint);
      color: var(--lumi-green-deep);
      border-left-color: var(--lumi-green);
    }}
    main {{ min-width: 0; }}
    .doc {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 54px);
      margin-bottom: 24px;
      box-shadow: 0 18px 50px rgba(31, 41, 51, .06);
    }}
    h1, h2, h3, h4 {{ line-height: 1.2; letter-spacing: 0; }}
    .doc h1 {{
      margin-top: 0;
      font-size: clamp(30px, 4.6vw, 54px);
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
    }}
    .doc h2 {{
      margin-top: 44px;
      padding-top: 18px;
      border-top: 1px solid var(--line);
      font-size: 28px;
    }}
    .doc h3 {{ margin-top: 28px; color: var(--lumi-green-deep); }}
    .doc h4 {{ color: var(--muted); }}
    p, li {{ font-size: 16px; }}
    .doc p strong:first-child {{ color: var(--lumi-green-deep); }}
    .learning-figure {{
      margin: 24px 0;
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      background: var(--surface);
      box-shadow: 0 12px 32px rgba(31, 41, 51, .06);
    }}
    .learning-figure img {{
      display: block;
      width: 100%;
      height: auto;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      background: var(--lumi-pale);
    }}
    .learning-figure figcaption {{
      padding: 12px 14px;
      border-top: 1px solid var(--line);
      background: var(--lumi-pale);
      color: var(--muted);
      font-size: 14px;
    }}
    code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    code {{ background: var(--lumi-mint); color: var(--lumi-green-deep); border-radius: 4px; padding: 1px 5px; }}
    pre {{
      overflow: auto;
      background: var(--code);
      color: #F3FAF6;
      padding: 16px;
      border-radius: 8px;
      border-left: 4px solid var(--lumi-green);
    }}
    pre code {{ background: transparent; color: inherit; padding: 0; }}
    .table-wrap {{
      overflow-x: auto;
      margin: 18px 0;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
    }}
    table {{ width: 100%; border-collapse: collapse; min-width: 760px; background: var(--surface); }}
    th, td {{ padding: 12px 13px; border-bottom: 1px solid var(--line); vertical-align: top; text-align: left; }}
    th {{
      background: var(--lumi-mint);
      color: var(--lumi-green-deep);
      font-weight: 700;
      position: sticky;
      top: 0;
      z-index: 1;
    }}
    tr:nth-child(even) td {{ background: #FAFCFB; }}
    tr:last-child td {{ border-bottom: 0; }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 28px 0; }}
    @media (max-width: 980px) {{
      .top {{ grid-template-columns: 1fr; gap: 12px; }}
      .brand-logo {{ height: 36px; }}
      .brand-title {{ border-left: 0; padding-left: 0; }}
      .stats {{ justify-content: flex-start; }}
      .hero {{ padding: 20px 14px 4px; }}
      .hero-panel {{ grid-template-columns: 1fr; }}
      .layout {{ grid-template-columns: 1fr; padding: 18px 14px 50px; }}
      nav {{ position: static; max-height: 320px; }}
      .doc {{ padding: 22px 16px; }}
      table {{ min-width: 680px; }}
    }}
    @media print {{
      .site-header, nav, .hero {{ display: none; }}
      .layout {{ display: block; padding: 0; }}
      .doc {{ box-shadow: none; border: 0; page-break-after: always; }}
      body {{ background: white; }}
      table {{ min-width: 0; }}
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="top">
      <a href="#readme" aria-label="Lumi">
        <img class="brand-logo" src="assets/lumi-logo-2022.png" alt="Lumi">
      </a>
      <div class="brand-title">
        <p class="brand-kicker">Nền tảng học tập ứng dụng</p>
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
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-panel">
      <div>
        <h2 id="hero-title">Học để ra quyết định tốt hơn cho một ngôi nhà sống lâu.</h2>
        <p>Website này đặt toàn bộ bản đồ kiến thức, giáo trình, thuật ngữ, công cụ thực hành và 72 module vào một môi trường học tĩnh, sáng, kỹ thuật và dễ tra cứu.</p>
        <div class="hero-tags">
          <span>Khí hậu Bắc Bộ</span>
          <span>Nhà vườn nhiệt đới</span>
          <span>Thiết kế vòng đời</span>
          <span>Vận hành 30-50 năm</span>
        </div>
      </div>
      <aside class="hero-note">
        <strong>Lumi learning interface</strong>
        <p>Nội dung học hiện ngay bên dưới. Dùng mục lục để chuyển nhanh giữa bản đồ, giáo trình, glossary, công cụ và từng module.</p>
      </aside>
    </div>
  </section>
  <div class="layout">
    <nav aria-label="Mục lục"><p class="nav-title">Mục lục học tập</p>{nav}</nav>
    <main>{articles}</main>
  </div>
</body>
</html>"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Đã dựng index.html với {len(docs)} tài liệu, gồm {module_count} module.")


if __name__ == "__main__":
    build()
