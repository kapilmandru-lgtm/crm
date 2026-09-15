# Referenzprojekt 1: ZF Automotive – globales Logistik-Template (400 Werke)

Vorbereiteter Sprechtext für das Miele-Interview, gemäß Coaching-Vorgabe von Mario Keller (NTT) aus dem [Gespräch vom 14.09.2026](./2026-09-14-NTT-Gespraech-2-Miele-Vorbereitung.md): **~5–6 Minuten**, als Story erzählt (keine PowerPoint), Kernaussagen jeweils in ~2 Minuten auf den Punkt.

---

**Ausgangslage**

Bei ZF habe ich fast drei Jahre an einem der größten Automotive-Logistiktransformationen mitgearbeitet: dem Aufbau eines globalen SAP-Logistik-Templates für 400 Werke weltweit. Ich habe eng mit dem Global Process Owner, dem Global Rollout Lead und dem Senior Vice President Logistics zusammengearbeitet. Klar war von Anfang an: Ein Werk in China, eines in Brasilien und eines in Deutschland lassen sich nicht eins zu eins über einen Kamm scheren. Deshalb war das Ziel ein globales Master-Template mit rund 90 Prozent Standardabdeckung – die restlichen 10 Prozent sollten je Werk über ein Lokalisierungskonzept gelöst werden.

**Meine Rolle**

Ich habe als Teammitglied im Requirement Gathering angefangen und bin aufgrund meiner Erfahrung informell zum Teamlead aufgestiegen. Verantwortet habe ich konkret das Werk Shangjiagang bei Shanghai – eines der komplexesten und wichtigsten Werke im gesamten Netzwerk. Da das Template dort größtenteils schon Standard war, lag mein Beitrag genau in den nicht standardisierten lokalen Prozessen: Fit-Gap-Analysen vor Ort, Prozessaufnahme mit den lokalen Kollegen – ohne Mandarin, über englischsprachige Kollegen als fachliche Übersetzer – und die enge Rückkopplung mit dem globalen Team in Deutschland.

**Vorgehen – ein konkretes Beispiel**

Ein zentrales Problem in Shangjiagang: 40 bis 50 3PL-Lager, gemischt für Inbound und Outbound genutzt. Das führte zu massiven Verzögerungen, weil beide Bewegungsrichtungen zeitgleich stattfanden. Mein Vorschlag, der umgesetzt wurde: strikte Trennung in dedizierte Inbound- und Outbound-3PLs.

- **Outbound:** Yard Management, Freight Unit Building, Routenoptimierung und Konsolidierung von Sendungen.
- **Inbound:** automatisiertes Replenishment – der 3PL überwacht proaktiv die Bestände und liefert selbstständig nach, statt wie vorher über Zettelwirtschaft und Telefonate. Wareneingänge und -ausgänge liefen auf beiden Seiten nur noch per Scan, ganz ohne manuelle Buchung.

Wichtig dabei: Auf Wunsch der Projektleitung sind wir konsequent im SAP-Standard geblieben – aus früheren Sonderlösungen wusste man, wie schwer es ist, die später wieder zurück in den Standard zu bringen.

Auf der Architekturseite habe ich die Integration zwischen ERP und EWM verantwortet: Einkaufsbestellungen werden in MM gebucht (MIGO) und automatisch an EWM übergeben; Produktionsversorgungsbereiche (PVB/PSA) werden von ERP und MES getriggert, EWM beliefert automatisch – die Schnittstelle einmalig über EDI oder API aufgesetzt. Je nach Werk haben wir drei verschiedene Nachschub-Logiken produktiv eingesetzt: klassisches Replenishment, Min-Max und Kanban.

**Ergebnis**

Das Werk wurde erfolgreich live gebracht, die Trennung von Inbound und Outbound hat die Verzögerungen beseitigt und ist heute Teil der globalen Best-Practice-Lösung. Insgesamt habe ich bei ZF mehrere Werke live gebracht – von China über Tschechien, Südkorea, England und Brasilien bis in die USA.

---

*(≈ 350 Wörter / ca. 3 Minuten in normalem Sprechtempo – bewusst knapper als das erlaubte Maximum von 5–6 Minuten gehalten, damit im Interview noch Raum für Rückfragen bleibt. Bei Bedarf um weitere Details zu Testing/Dokumentation/Key-User-Training ergänzbar.)*
