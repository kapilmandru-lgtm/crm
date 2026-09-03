#!/usr/bin/env python3
"""Rendert die HTML-Rechercheberichte in diesem Ordner als A4-PDF.

Aufruf:
    python3 build_pdf.py                 # alle *.html im Ordner
    python3 build_pdf.py bericht.html    # gezielt eine Datei

Voraussetzungen: playwright (pip install playwright) und ein Chromium.
Im Container liegt Chromium unter PLAYWRIGHT_BROWSERS_PATH und wird
automatisch gefunden; ein "playwright install" ist nicht noetig.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent


def chromium_path() -> str | None:
    """Vorhandenes Chromium suchen, statt eines herunterzuladen.

    Playwright erwartet die Browser-Revision, die zu seiner eigenen Version
    passt. Im Container liegt oft eine aeltere; dann laesst sich der Browser
    ueber executable_path trotzdem verwenden.
    """
    root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for pattern in ("chromium-*/chrome-linux/chrome",
                    "chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell"):
        found = sorted(root.glob(pattern))
        if found:
            return str(found[-1])
    return None  # Playwright entscheidet selbst

# Kopf- und Fusszeile rendern in einem eigenen Kontext ohne das Seiten-CSS,
# deshalb sind Schriftgroesse und Rand hier ausgeschrieben.
HEADER = """
<div style="width:100%;padding:0 15mm;font-family:Helvetica,Arial,sans-serif;
            font-size:7pt;color:#8A948D;display:flex;justify-content:space-between;">
  <span>Thail&auml;ndisches Wohnungseigentum f&uuml;r rum&auml;nische Gesellschaften</span>
  <span>Rechtsrecherche</span>
</div>
"""

FOOTER = """
<div style="width:100%;padding:0 15mm;font-family:Helvetica,Arial,sans-serif;
            font-size:7pt;color:#8A948D;display:flex;justify-content:space-between;">
  <span>Keine Rechtsberatung &middot; Stand 3. September 2026</span>
  <span>Seite <span class="pageNumber"></span> von <span class="totalPages"></span></span>
</div>
"""


def render(html: Path, pdf: Path) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium_path())
        page = browser.new_context(color_scheme="light").new_page()
        page.goto(html.as_uri(), wait_until="networkidle")
        # Webfonts muessen geladen sein, sonst druckt Chromium den Fallback.
        page.evaluate("() => document.fonts.ready")
        page.pdf(
            path=str(pdf),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=HEADER,
            footer_template=FOOTER,
            margin={"top": "18mm", "bottom": "16mm", "left": "15mm", "right": "15mm"},
        )
        browser.close()


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv] or sorted(HERE.glob("*.html"))
    if not targets:
        print("Keine HTML-Datei gefunden.", file=sys.stderr)
        return 1
    for html in targets:
        html = html if html.is_absolute() else HERE / html
        pdf = html.with_suffix(".pdf")
        render(html, pdf)
        print(f"{html.name} -> {pdf.name}  ({pdf.stat().st_size:,} Bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
