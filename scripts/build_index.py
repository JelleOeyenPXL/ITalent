# -*- coding: utf-8 -*-
"""
Optioneel: extraheert platte tekst uit het Word-portfolio (.docx).
De live site gebruikt `includes/report-sections.html` + `assemble_index.py`.
"""
import html
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT.parent / "Template_portfolio_I-Talent_2526 (1).docx"


def load_text_from_docx(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"Geen .docx gevonden: {path}")
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    parts: list[str] = []
    for t in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
        if t.text:
            parts.append(t.text)
        if t.tail:
            parts.append(t.tail)
    return "".join(parts)


def esc(s: str) -> str:
    return html.escape(s)


def split_sections(text: str) -> dict[str, str]:
    """Ruwe splits op vaste titels uit het sjabloon."""
    # Verwijder TOC-blok aan het begin (tot echte voorstelling)
    if "Mijn naam is Jelle Oeyen" in text:
        i = text.index("Mijn naam is Jelle Oeyen")
        text = text[i:]

    out: dict[str, str] = {}

    m_overzicht = re.search(r"Overzicht activiteiten", text)
    m_selectie = re.search(r"Selectie van activiteiten", text)
    m_eind = re.search(r"Eindreflectie", text)

    if not m_overzicht or not m_selectie or not m_eind:
        raise SystemExit("Kon sectiegrenzen niet vinden.")

    out["voorstelling"] = text[: m_overzicht.start()].strip()
    out["overzicht"] = text[m_overzicht.end() : m_selectie.start()].strip()
    # Overzicht begint met instructiezin; laat staan
    out["selectie"] = text[m_selectie.end() : m_eind.start()].strip()
    # Selectie start met instructie + eerste activiteit titel
    out["eindreflectie"] = text[m_eind.end() :].strip()
    return out


def main() -> None:
    text = load_text_from_docx(DOCX)
    sec = split_sections(text)

    out_path = ROOT / "scripts" / "_generated_fragments.html"
    parts_out: list[str] = []

    # Voorstelling staat in assemble_index.py (netjes opgemaakt); hier alleen 2–4.
    parts_out.append('    <section id="overzicht" class="section section--report">')
    parts_out.append('      <header class="report-header">')
    parts_out.append('        <p class="eyebrow eyebrow--calm">2 · Overzicht activiteiten</p>')
    parts_out.append(
        '        <h2 class="report-title">Gestructureerd overzicht</h2>'
    )
    parts_out.append(
        '        <p class="report-lead">Overzicht zoals in je Word-template: domeinen en korte beschrijvingen.</p>'
    )
    parts_out.append("      </header>")
    parts_out.append(
        '      <article class="report-chapter report-chapter--wide"><pre class="report-pre">'
        + esc(sec["overzicht"])
        + "</pre></article>"
    )
    parts_out.append("    </section>")

    parts_out.append('    <section id="selectie" class="section section--report">')
    parts_out.append('      <header class="report-header">')
    parts_out.append(
        '        <p class="eyebrow eyebrow--calm">3 · Selectie van activiteiten</p>'
    )
    parts_out.append(
        '        <h2 class="report-title">Diepgang &amp; reflectie</h2>'
    )
    parts_out.append(
        '        <p class="report-lead">Geselecteerde activiteiten met kern en reflectie (inhoud uit je Word-bestand).</p>'
    )
    parts_out.append("      </header>")
    parts_out.append(
        '      <article class="report-chapter report-chapter--wide"><pre class="report-pre">'
        + esc(sec["selectie"])
        + "</pre></article>"
    )
    parts_out.append("    </section>")

    parts_out.append('    <section id="eindreflectie" class="section section--report">')
    parts_out.append('      <header class="report-header">')
    parts_out.append(
        '        <p class="eyebrow eyebrow--calm">4 · Eindreflectie</p>'
    )
    parts_out.append('        <h2 class="report-title">Eindreflectie &amp; X-Factor</h2>')
    parts_out.append("      </header>")
    parts_out.append(
        '      <article class="report-chapter report-chapter--wide"><pre class="report-pre">'
        + esc(sec["eindreflectie"])
        + "</pre></article>"
    )
    parts_out.append("    </section>")

    out_path.write_text("\n".join(parts_out), encoding="utf-8")
    print("Wrote", out_path, "lines", len(parts_out))


if __name__ == "__main__":
    main()
