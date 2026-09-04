# Fragenkatalog: Anforderungsaufnahme SAP EWM

Checkliste für Requirement-Workshops und für die Sichtung vorhandener
Anforderungsdokumente (Confluence, Fachkonzepte, Designdokumente).
Ziel: je Themenblock geklärter Soll-Prozess, Fit/Gap-Bewertung und offene Punkte.

## 1. Organisationsstruktur und Systemlandschaft

- Welche Lagernummern, Lagertypen, Lagerbereiche, Aktivitätsbereiche, Lagerplätze?
- Embedded EWM oder dezentrales EWM? Anbindung an den S/4-Core?
- Welche Werke/Lagerorte werden auf EWM umgestellt, welche bleiben IM/WM?
- Mehrere Mandanten/Systeme im Scope (Entwicklung, Test, Produktion)?
- Migrationsschnitt: Greenfield, Brownfield, selektive Migration?

## 2. Stammdaten

- Lagerprodukt-Pflege: Verantwortung, Pflegeprozess, Massenpflege?
- Verpackungsvorschriften, HU-Typen, Packmittel?
- Lagerplatztypen, Kapazitätsprüfung, Gefahrstoffdaten?
- Chargenpflicht, Serialnummern, Haltbarkeit (SLED/BBD)?

## 3. Wareneingang / Einlagerung (Inbound)

- Avisierung (ASN/Anlieferung), Tor-/Zeitfenstermanagement?
- Wareneingangsprozess: mit/ohne Anlieferbeleg, Retouren, Streckengeschäft?
- Qualitätsprüfung: QM-Integration, Sperrbestand, Stichprobe?
- Einlagerungsstrategien, Kreuzverteilung (Cross-Docking)?
- HU-Bildung im Wareneingang, Etikettierung?

## 4. Kommissionierung / Warenausgang (Outbound)

- Auslieferungsarten: Kundenauftrag, Umlagerung, Retoure an Lieferanten?
- Wellenmanagement: Wellenbildung, -freigabe, Kriterien?
- Kommissionierstrategien: Einzel-, Sammel-, Zwei-Stufen-Kommissionierung?
- Verpacken: Packstation, Packvorschriften, Versandeinheiten?
- Warenausgangsbuchung, Ladeprozess, Tor-/Verladesteuerung?
- Transportanbindung (TM, Spediteure, Frachtpapiere)?

## 5. Interne Prozesse

- Umlagerungen, Nachschub (Nachschubstrategien, Auslösung)?
- Inventur: jährlich, permanent, Cycle Counting (ABC), Nullkontrolle?
- Produktionsversorgung: Bereitstellung, Rückmeldung, Leergutkreislauf?
- Materialflusssystem (MFS): Fördertechnik, AKL, Regalbediengeräte?

## 6. Handling Units, Kennzeichnung, Druck

- HU-Konzept: welche Ebenen (Palette, Karton, Tray)?
- Nummernkreise, SSCC/NVE, GS1-Standards?
- Etikettendruck: Zeitpunkte, Nachdruck, Druckersteuerung, Formulare?

## 7. Mobile Ausführung (RF)

- RF-Framework (RFUI) oder Fiori/mobile Apps?
- Welche Geräte (Handscanner, Staplerterminal, Wearables)?
- Welche RF-Transaktionen je Rolle, Sprachversionen?

## 8. Schnittstellen und Integration

- ERP/S4-Core: Belegfluss, Bestandsabgleich, Fehlerbehandlung (qRFC/IDoc)?
- Fremdsysteme: Waage, Scanner, Drucker, Fördertechnik, Zoll, Kunden-/Lieferantenportale?
- Monitoring der Schnittstellen: wer, womit, welche Alarmierung?

## 9. Berechtigungen und Rollen

- Rollenschnitt fachlich (Lagerarbeiter, Meister, Inventurverantwortlicher)?
- Trennung Test-/Produktivberechtigungen, SoD-Anforderungen?

## 10. Reporting und Monitoring

- EWM-Monitor: benötigte Sichten und Knoten?
- Kennzahlen (Durchlaufzeit, Auslastung, Kommissionierleistung)?
- Analytics/BI-Anbindung?

## 11. Nicht-funktionale Anforderungen

- Mengengerüst (Positionen/Tag, Peaks), Antwortzeiten?
- Verfügbarkeit, Wartungsfenster, Notfallkonzept (Downtime-Prozess)?
- Sprachen, Zeitzonen, Standorte?
- Gesetzliche Anforderungen (GxP, Zoll, Gefahrgut, Rückverfolgbarkeit)?

## 12. Projektorganisation zur Anforderung

- Wer ist fachlicher Owner? Wer genehmigt?
- Welcher Freigabeprozess (Anzahl Stufen, Gremium)?
- Wo liegt die führende Version der Anforderung?
- Wie werden Änderungen nach Freigabe behandelt (Change-Prozess)?
