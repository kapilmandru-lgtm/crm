# Requirement-Vorlage (SAP EWM)

Eine Datei je Requirement. Dateiname: `REQ-<Bereich>-<lfd. Nr.>-<Kurztitel>.md`
(Beispiel: `REQ-OUT-014-Wellenkommissionierung.md`).

---

## Kopfdaten

| Feld | Wert |
|---|---|
| Requirement-ID | |
| Titel | |
| Quelle (Confluence/Jira-ID + Link) | |
| Abrufdatum / Seitenversion | |
| Prozessbereich | Inbound / Outbound / Interne Prozesse / Inventur / Produktionsversorgung / Stammdaten / Schnittstellen / Berechtigungen |
| Lagernummer / Standort | |
| Autor fachlich | |
| Status | Entwurf / In Abstimmung / Freigegeben / Zurückgestellt |
| Priorität | Muss / Soll / Kann |
| Release / Sprint | |

## 1. Fachliche Anforderung

Was soll fachlich erreicht werden? (Ergebnis, nicht Lösung.)

## 2. Ist-Prozess (As-Is)

Heutiger Ablauf inkl. Vorsystem (z. B. WM/LE, Fremdsystem), Mengengerüst,
Belegarten, beteiligte Rollen.

## 3. Soll-Prozess (To-Be)

Zielablauf in EWM. Schrittfolge, auslösende Belege, Lagerprozessart,
Lagerauftragserstellungsregel, Bestätigungslogik, Ausnahmen.

## 4. Fit / Gap

| Bewertung | Begründung |
|---|---|
| Fit (Standard) / Gap (Erweiterung) / Workaround | |

Bei Gap: geplante Umsetzungsart (BAdI, PPF-Aktion, Erweiterung, RF-Transaktion,
Fiori-App, Add-on) und Aufwandsschätzung.

## 5. Abhängigkeiten

- Vorgelagerte/nachgelagerte Prozesse
- Schnittstellen (ERP/S4-Core, MFS, TM, Drucksystem, Waage, Scanner, Fremd-WMS)
- Stammdaten (Lagerprodukt, Verpackungsvorschrift, HU-Typen, Lagerplatztypen)
- Organisationsstruktur (Lagernummer, Lagertyp, Lagerbereich, Aktivitätsbereich)

## 6. Akzeptanzkriterien

Prüfbar formulieren (Given/When/Then oder nummerierte Kriterien).

1.
2.

## 7. Testhinweise

- Testfall-ID(s)
- Benötigte Testdaten
- System/Mandant (nicht in öffentlichen Ablagen dokumentieren)

## 8. Offene Punkte / Fragen

| # | Frage | Adressat | Status |
|---|---|---|---|

## 9. Entscheidungen

| Datum | Entscheidung | Entscheider | Quelle |
|---|---|---|---|
