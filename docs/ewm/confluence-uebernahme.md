# Requirements aus Confluence in die Projektwissensbasis übernehmen

## Ausgangslage

Kunden-Confluence-Instanzen liegen in der Regel hinter dem Unternehmens-SSO
und sind nur aus der Kundenumgebung (VPN/Citrix, Kundenkonto) erreichbar.
Aus einer Claude-Code-Session heraus sind sie **nicht** lesbar, solange kein
Atlassian-Connector mit einem berechtigten Konto verbunden ist.

Prüfreihenfolge, bevor Aufwand entsteht:

1. Ist ein Atlassian-/Confluence-Connector in Claude verbunden und für den
   Chat aktiviert? (Einstellungen → Connectors)
2. Erlaubt die Kunden-IT die Anbindung externer Clients an Confluence?
   In vielen Konzernen ist das untersagt — dann bleibt nur der manuelle Weg.
3. Gibt es einen genehmigten Export (Space-Export, PDF/Word) statt API-Zugriff?

## Manueller Weg (Standardfall)

1. Im Confluence-Space die Requirement-Seiten identifizieren
   (Seitenbaum, Labels, Filter nach Prozessbereich).
2. Je Seite **nur lesend** erfassen: Titel, Seiten-ID/Link, letzte Änderung,
   Autor, Status.
3. Inhalt in die Vorlage `requirement-template.md` überführen — nicht
   Rohtext kopieren, sondern strukturieren (As-Is, To-Be, Fit/Gap,
   Akzeptanzkriterien, offene Punkte).
4. Ablage in der **privaten** Projektablage. Öffentliche Repositories sind
   dafür ungeeignet.
5. Übersichtstabelle pflegen: ID, Titel, Bereich, Status, Priorität, Quelle,
   Stand.

## Übersichtstabelle (Vorlage)

| ID | Titel | Bereich | Status | Priorität | Confluence-Link | Stand |
|---|---|---|---|---|---|---|
| | | | | | | |

## Qualitätskriterien beim Sichten

- Ist die Anforderung **prüfbar** formuliert (Akzeptanzkriterien vorhanden)?
- Ist der Prozessbereich eindeutig zugeordnet?
- Gibt es Widersprüche zu anderen Requirements oder zum Template-Standard?
- Ist erkennbar, ob Standard (Fit) oder Erweiterung (Gap)?
- Wer hat freigegeben, und in welcher Version?

Alles, was unklar bleibt, wird als offener Punkt mit Adressat notiert —
nicht interpretiert.
