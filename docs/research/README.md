# Recherchen

Ablage für ausgearbeitete Recherchen. Jede Recherche besteht aus einem
eigenständigen HTML-Dokument (Quelle, im Browser direkt lesbar, hell und dunkel)
und dem daraus erzeugten A4-PDF.

| Dokument | Thema |
| --- | --- |
| `thailand-condo-erwerb-rumaenische-gesellschaft` | Dürfen rumänische Gesellschaften in Thailand Eigentumswohnungen kaufen? Rechtsgrundlage, 49-%-Quote, Devisennachweis, Verfahren, Kosten, Vermietung, Reformstand. |

## PDF neu erzeugen

Das PDF wird aus dem HTML gerendert — die HTML-Datei ist die Quelle, das PDF
das Erzeugnis. Nach einer Änderung am HTML:

```bash
cd docs/research
python3 build_pdf.py                                        # alle HTML-Dateien
python3 build_pdf.py thailand-condo-erwerb-rumaenische-gesellschaft.html
```

Benötigt `playwright` (`pip install playwright`) und ein Chromium. In der
Cloud-Session liegt Chromium bereits unter `PLAYWRIGHT_BROWSERS_PATH`;
`build_pdf.py` sucht es dort selbst, ein `playwright install` ist nicht nötig.

Die Druckformatierung (A4, helle Palette, Randspalte für Fundstellen,
Seitenzahlen, ausgeschriebene Quellen-URLs) steckt im `@media print`-Block
am Ende des `<style>`-Bereichs der jeweiligen HTML-Datei.

## Hinweis

Die Dokumente sind Recherchen aus öffentlich zugänglichen Quellen, keine
Rechts- oder Steuerberatung. Jedes Dokument nennt seinen Stand und führt die
verwendeten Quellen auf.
