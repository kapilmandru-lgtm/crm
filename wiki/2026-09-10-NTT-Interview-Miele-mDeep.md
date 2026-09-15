# NTT Interview – Miele-Transformation (mDeep)

**Datum:** 10.09.2026, 11:10 Uhr
**Teilnehmer:** NTT (Herr Keller), Kapil Mandru
**Typ:** Erstgespräch / Bewerbungsinterview für eine Rolle als Senior SAP Consultant (EWM/TM/SD) im Miele-Transformationsprogramm
**Aufnahme:** Bildschirm + Ton, lokal abgelegt unter `meeting notes/Aufnahmen/2026-09-10_11-10_Interview.mp4`
**Quelle:** automatisch transkribiertes Word-Dokument (`20260910_1110_Interview.docx`), Volltranskript siehe Anhang
**Folgegespräch:** [2026-09-14 – NTT Gespräch 2: Vorbereitung Referenzprojekte](./2026-09-14-NTT-Gespraech-2-Miele-Vorbereitung.md)

## Zusammenfassung

Herr Keller (NTT, Transformationsverantwortlicher für das Projekt "mDeep") führt ein erstes qualifizierendes Gespräch mit Kapil Mandru für eine mögliche Rolle im Großtransformationsprojekt bei Miele. Nach einer Einordnung des Projekts stellt Kapil Mandru seinen fachlichen Werdegang vor (3PL-Logistik, SAP EWM/TM/SD, mehrere GPO-/Teamlead-Erfahrungen). Herr Keller zeigt sich überzeugt und kündigt einen nächsten Schritt an: Vorstellung bei den Geschäftsverantwortlichen von Miele (30–45 Minuten Interview), für den der Kandidat zwei Referenzprojekte als Story aufbereiten soll. Abschließend werden Verfügbarkeit und Reisebereitschaft geklärt.

## Projektkontext: Miele-Transformation

- Miele kommt aus einer über 20 Jahre gewachsenen, **föderalistischen ECC-Landschaft**: konsensorientierte Unternehmenskultur, dezentrale Gesellschaften/Fertigungsstandorte mit hoher Eigenständigkeit, Standardisierung bisher nur bilateral/multilateral verhandelt statt zentral vorgegeben.
- Ergebnis: ECC-Strategie ist **nicht mehr innovations-, skalierungs- oder konversionsfähig** → Entscheidung für eine strikte **Clean-Core-/Greenfield-Strategie** mit Best Practices und klarer Architektur Richtung SAP BTP.
- Übergeordnetes IT-Gesamttransformationsprogramm gliedert sich in zwei Stränge:
  1. **Vertriebsgesellschaften** (Verkauf der Maschinen, B2C, Aftersales) – nicht Gegenstand dieses Gesprächs.
  2. **Projekt M / "mDeep"** (Digital Engineering and Manufacturing) – Fertigung, Logistik, ausgewählte zentrale Funktionen wie Einkauf; Umbau in zentral geplante/gesteuerte Verantwortlichkeiten.
- Zielarchitektur: **One-ERP-Strategie** – alle Vertriebs- und Fertigungswelten laufen in einem gemeinsamen **S/4 RISE**-System zusammen.
- Meilenstein: **1. April 2028** – erster Fertigungsstandort live (ca. 18 Monate ab Gesprächsdatum); ab **1. November** Start der Realize-Phase; parallel Ablösung einer bestehenden MES-Lösung durch Digital Manufacturing (DM).
- Architektur-Fundament (Process House / Data House / System House) ist **zu 70–80 % robust definiert und mit Miele validiert**, einzelne Punkte sind noch offen.
- **Setup-Entscheidung:** Side-by-Side (EWM als separates System vom ERP), kein embedded EWM – Begründung: Entkopplung von Logistik/Lager und ERP, damit ein Ausfall von TM das ERP-System nicht mit runterzieht.
- Implementierungspartner: **NTT** (Pitch gewonnen, u. a. Aufbau von Process House, Data House, System House sowie Discovery-/Explore-Phasen mit iterativer Verfeinerung).

### Offene Architekturfrage: Platzierung von TM

- Bislang noch **keine finale Architekturentscheidung**, ob Transportation Management (TM) auf der ERP- oder der EWM-Seite verortet wird; Ergebnis der Vorstudie soll nochmal aufgerollt werden, da SAP jetzt stärker eingebunden wird.
- Empfehlung des Kandidaten: **TM auf ERP-Seite**, da TM enger mit SD verknüpft ist als mit EWM.
- Kandidat weist zusätzlich darauf hin, dass Side-by-Side-Setups von Anfang an intensives Testen brauchen, sobald in beiden Systemen (ERP und EWM) valide Stammdaten vorhanden sind – im ERP i. d. R. vorhanden, im leeren EWM-System müssen sie erst aufgebaut werden.
- Advanced Shipping & Receiving war laut Kandidat in seinen bisherigen Projekten oft aus Kosten-/Lizenz- und politischen Gründen nie vollständig ausgetestet.

## Interviewer: Herr Keller (NTT)

- Transformationsverantwortlicher NTT-seitig für "mDeep".
- Erfahrung mit großformatigen Konzern-Transformationen: **Sanofi** (Deutschland, Frankreich), **Heidelberger Druckmaschinen** (Deutschland, USA).
- 15 Jahre im Private-Equity-Umfeld / Restrukturierung, u. a. als interimistischer CIO.
- Positioniert NTT als Partner, der nicht nur berät/präsentiert, sondern **Ownership für die Transformation übernimmt**.

## Kandidat: Kapil Mandru

**Herkunft & Werdegang:** aus Indien, seit 1991 in Deutschland; seit 2004 in der Logistik/3PL-Branche tätig (Bereiche EWM, TM/Transportation Management, Freight Forwarding – See-, Luft- und Landfracht).

| Station | Rolle / Fokus |
|---|---|
| DAMCO (Teil von Maersk) | Seefracht |
| DHL Global Forwarding | Luftfracht (damals Nr. 2 am Markt) |
| Weiterer Arbeitgeber (bis 2018) | IT-Wesen erlernt; zuletzt Customer Solutions Manager für Europa; größter betreuter Kunde: **Siemens** (ICS-Bereich, Aftersales/Spare-Parts + Transport) |
| Seit 2018 | Selbstständig / eigene Firma – reiner SAP-Supply-Chain-Fokus (EWM, TM, SD u. verwandte Module) |
| Pharma-Kunden | Roche (Basel), CSL, Thermo Fisher |
| **Stihl** | Global Process Owner (GPO), extern |
| **ZF** | ca. 3 Jahre, mehrere Rollen (Details unten) |

### Projekt Stihl (GPO-Rolle)

- Stihl (Weltmarktführer Kettensägen) hatte auf Produktebene ein perfektes, detailverliebtes Vorgehen – auf IT-/Projektebene hingegen **massive Governance-Probleme**.
- Ursache: Stihl und Implementierungspartner **Accenture** konnten die Verantwortlichkeiten ("wer führt/entscheidet") nie klar trennen; Stihl mischte sich fortlaufend ein.
- Folge: ständig neue Anforderungen aus Quality, Production, Sales, Einkauf → das globale Template wurde **nie fertig**.
- Kandidat war in dieser Konstellation GPO – sehr hoher Stressfaktor; seither übernimmt er GPO-Positionen **nicht mehr freiwillig**, konzentriert sich lieber auf Themen, die er inhaltlich beherrscht.

### Projekt ZF

- Einstieg als normales Teammitglied im **Requirement Gathering** (Build-Seite).
- Template-Ansatz für **400 Werke**; globales Template erreichte ca. **90–92 % Abdeckung** (laut Kandidat das praktische Maximum), Rest über Lokalisierungskonzept bei Rollouts.
- Nach Bewährung informell zum **Teamlead** aufgestiegen (offiziell nicht möglich, da diese Position laut ZF-Regelung nur internen Mitarbeitenden vorbehalten ist – de facto aber in dieser Funktion anerkannt).
- Wechsel ins **IT-Team**: Hands-on-Customizing und Architekturarbeit (Abgrenzung TM/EWM vs. Integration zum ERP).
- Anschließend weltweit im Einsatz für **Rollouts**: China, Tschechien, Südkorea, England, Deutschland, Brasilien, USA.
- Vertragsende bedingt durch politischen Druck bei ZF (interne Entlassungswelle bei gleichzeitig hoher Zahl Externer in der Automotive-Krise).

### Weitere fachliche Aussagen des Kandidaten

- Erfahrung mit **embedded UND Side-by-Side EWM** – Customizing ist inhaltlich identisch, Unterschiede liegen in der initialen Infrastruktur-Anbindung.
- Sieht sich als Prozess-/Business-Kenner mit IT-Umsetzungskompetenz, nicht als reinen ITler ("Ich kann Prozesse sehr schnell verstehen und neu designen, Fit-Gap-Analysen machen").

## Nächste Schritte

1. Herr Keller bereitet ein **Briefing/Vorschlag** für den Kandidaten vor, um das anstehende Miele-Gespräch gemeinsam vorzubereiten.
2. Kandidat soll **zwei Referenzprojekte** aufbereiten:
   - Ausgangslage des Gesamtprojekts
   - Abgrenzung des eigenen Verantwortungsbereichs
   - Vorgehen innerhalb des Projekts
   - Erfolge & Deliverables
   - **Format: keine PowerPoint** – als nachvollziehbare Geschichte erzählen.
3. Danach: Termin bei den **Geschäftsverantwortlichen von Miele** (30–45 Minuten Interview); die Kundenseite entscheidet final, ob der Kandidat zu NTT/zum Projekt passt.

## Verfügbarkeit & Konditionen

- Aktuelles Projekt: **100 % ausgelastet**, läuft Anfang nächsten Jahres aus.
- Kurzfristiger Wechsel möglich: ca. **2 Wochen Vorlauf**, realistischer Start **ab Oktober**.
- Wohnort: **Buseck bei Gießen**.
- Vor-Ort-Präsenz in **Gütersloh** (Miele-Standort, ca. 2–2,5 Std. Anfahrt):
  - Erste ca. **4 Wochen**: hohe Präsenz gewünscht (Empfehlung NTT: 2–3 Tage inkl. An-/Abreise).
  - Danach: eher **14-tägige** Präsenzblöcke (z. B. 2 Tage Workshops inkl. Vor-/Nachbereitung), sonst Homeoffice.
  - Zusätzliche Präsenzpflicht bei **Testphasen** (Functional Unit Test, System Integration Test) wird erwartet und akzeptiert.
- Kandidat lehnt **dauerhafte** Vollzeit-Vor-Ort-Präsenz über ein ganzes Jahr ab (Erfahrungswert aus einem früheren Projekt mit sehr langen Anreisen nach Österreich/Schweiz bei Stihl) – familiär bedingt. Bei Bedarf ist er aber vor Ort verfügbar.

## Offene Punkte

- Finale Architekturentscheidung zur **TM-Platzierung** (ERP/SD-Seite vs. EWM-Seite) steht noch aus und wird im Zuge der stärkeren SAP-Einbindung nochmal diskutiert.
- Konkretes Briefing/Termin für das Miele-Gespräch von NTT-Seite steht noch aus.

## Volltranskript (mit Zeitstempeln)

> "Du" = Stimme des Kandidaten (Mikrofon), unmarkierte Zeilen = weitere Stimmen aus dem Call (Herr Keller u. a.). Automatisch generiertes Transkript, kann kleinere Fehler enthalten.

[00:04:31] Eine kurzfristige Verschiebung ist wie im richtigen Leben und dann schläft es.
[00:04:42] Gerade war es sowieso ein Alarm. War das mal auch bei euch so in der Gegend oder war das so bei euch?
[00:04:47] Ja, Deutschlandweit.
[00:04:49] Okay, gut. Weil das hat er eh gestört.
[00:04:54] Weiß ja wen.
[00:05:08] Gut, dass wir dann doch verschoben haben, weil das hat dann schon wahnsinnig gestört.
[00:05:15] Das war schon sehr, sehr laut.
[00:05:22] Und dann ist hauptsächlich ihr sehr beeindruckender Lebenslauf, den ich mit Freude gelesen habe, was sie alles gemacht haben,
[00:06:14] im Gegenstand unseres weiteren Meetings.
[00:06:17] Wir reden über ein sehr großformatiges Transformationsprojekt im Large Enterprise Umfeld.
[00:06:25] Wir reden über Miele, wir reden über den Bau aus RIF als Brand, durchleucht ein.
[00:06:42] Das ist so ein bisschen der Startpunkt.
[00:06:47] Bislang föderalistische Systeme, sehr Konsensorientierte Unternehmenskultur als föderal funktioniert hat.
[00:07:01] Jedem Gesellschaft war Ergebnis verantwortlich.
[00:07:03] Fertigungsstandort war verordentlich.
[00:07:06] Also die Einheiten haben tatsächlich sehr alltag arbeiten können.
[00:07:09] Und wenn es um Harmonisierung, Standardisierung und Best Practices geht,
[00:07:13] war das am Ende des Tages eine bilateral oder multilaterale Verhandlung.
[00:07:18] So ist das Unternehmen in den letzten 20 Jahren im Markt aufgetreten.
[00:07:23] So sieht auch die Landschaft hinten dran aus,
[00:07:27] nämlich über 20 Jahre entwickelte ECC-Landschaften,
[00:07:32] führend mit einem großen SAP-Team immer wieder weiterentwickelt
[00:07:38] und aufgrund der föderalen Struktur dann oft Einzellösungen,
[00:07:43] die jetzt nicht unbedingt in die Fläche gebracht worden sind, was dazu führt.
[00:07:46] Und das hat viele so auch erkannt, dass sie in ihrer ECC-Strategie
[00:07:54] nicht mehr innovationsfähig sind, nicht mehr skalierbar sind in einer Art und Weise,
[00:08:01] wie sie es sich gerne vorgestellt hätten in den letzten Jahren,
[00:08:04] plus sie nicht konversionsfähig sind.
[00:08:07] In Leisen, in dem Fall nur Greenfield-Leisen,
[00:08:12] kann in dem Fall als Erkenntnis der letzten 20 Jahre
[00:08:16] eine strikte Clean-Core-Strategie sein,
[00:08:20] Best-Practices-Strategie mit einer klaren architektonischen Aufteilung in Richtung BTP und so weiter.
[00:08:26] Das führte dazu, dass wir über ein übergeordnetes Transformations aus dem Business reden
[00:08:34] und daraus sind einzelne Transformationsstränge auch unter einem IT-Gesamt-Transformationsprogramm aufgelistet.
[00:08:46] Wesentliche Teile der Miele-Transformation unterteilen sich in Verkriebsgesellschaften,
[00:08:53] mit dem Verkauf der Maschinen, B2C-Geschäfte,
[00:08:57] in irgendwelcher Form Aftersales und so weiter.
[00:09:01] Darüber, Herr Mantow, reden wir nicht.
[00:09:05] Die zweite Struktur, die zweite Transformation,
[00:09:11] das ist das Projekt M, die Digital Engineering and Manufacturing
[00:09:18] der Fertigungswelt zu tun hat, mit der Logistikwelt zu tun hat,
[00:09:25] mit ausgewählten zentralen Funktionen, wie beispielsweise Einkauf.
[00:09:29] Und hier haben wir den Umbau des Businesses in zentral planende und gesteuerte Funktionalitäten und Verantwortlichkeiten.
[00:09:42] Dazu ziehen wir die S4 ERP-Landschaft auf.
[00:09:49] Und jetzt darum auch die Bemerkung mit dem ersten Strang in der Vertriebswelt.
[00:09:55] Es ist eine One ERP-Strategie.
[00:09:58] Das heißt, sämtliche Vertriebswelten, sämtliche Fertigungswelten
[00:10:02] sollen sich in einem One ERP S4 RISE-System treffen.
[00:10:08] Das hat natürlich weitere Herausforderungen, gerade bei zentralen Objekten.
[00:10:13] Wer ist Implementierungspartner? Wie ist die Angehensweise von Miele gewesen?
[00:10:20] Der Implementierungspartner ist Entity.
[00:10:23] Also wir haben hier, was den Pitch anbetrifft, offensichtlich einen überzeugenden Aufschlag geleistet.
[00:10:28] Der basiert allerdings Unternehmensberatung mit auch einem sehr berühmten Label.
[00:10:43] Die ganze BPMN-Bekleidigung hat vorgenommen, dass wir über das Prozesshaus verfügen,
[00:10:50] dass wir über das Data-Haus verfügen, dass wir über das System-Haus, über die Artikulation,
[00:10:55] über die Composites, im Bereich den Satz zu in der SAP.
[00:11:15] Ich würde sagen, dass die Discoverys machen jetzt nochmal so eine kleine Schleife
[00:11:38] durch die Explorer zur Verfeinerung, ab und zu auch ein bisschen zu korrekt.
[00:11:42] Aber das ist wie im richtigen Leben.
[00:11:46] Besser werden mit jeder Woche, mit jedem Monat.
[00:11:51] Ziel ist, am 1. April 2028,
[00:11:56] den ersten Fertigungsstandort an den Start zu bekommen.
[00:12:00] Das sind jetzt noch 18 Monate.
[00:12:02] Und das bedeutet in dem Zusammenhang, dass wir ab 1. November nominell in den Realize bis dahin
[00:12:12] Verabschiedet haben, Digital Manufacturing, also Ablösung einer MES-Lösung durch DM.
[00:12:37] Und daraus ergeben Sie sprechen.
[00:12:54] Also das ist so ein bisschen über die Formatigkeit.
[00:12:58] Ich bin der Transformationsverantwortliche gespiegelt auf der NTT-Seite für mDeep.
[00:13:08] Ich bin solche großformatigen Transformationen durchaus gewohnt.
[00:13:14] Man sieht vielleicht, dass ich mich gestern in der Uni verlassen habe.
[00:13:18] Ich bringe die Transformationen im Konzernkontext mit Sanofi in Deutschland, in Frankreich,
[00:13:29] beziehungsweise Heidelberger Druckmaschinen in Deutschland und in den USA.
[00:13:33] Ich war die letzten 15 Jahre im Private Equity Umfeld in der Restrukturierung unterwegs.
[00:13:38] Also als CIO, als internavistischer CIO und Arbeit und Weg zur NTT.
[00:13:49] Die NTT lässt sich auch daraus begründen, die NTT investiert sehr massiv in Advisory and in Strategy.
[00:13:56] Und im Verständnis von NTT heißt das nicht nur Theoretisieren und High-Level-Präsentation,
[00:14:03] sondern auch Ownership übernehmen für eine solche Transformation.
[00:14:07] Dann hat die NTT nicht offensichtlich ein Win-Win vorgefunden.
[00:14:13] Nicht den Zeitjahresanfang weiter.
[00:14:17] So weit dann auch die Überleitung von der Transformation über meine Person rein ins Projekt.
[00:14:23] Und damit würde ich gerne überleiten an Sie mit einer Kurzvorstellung.
[00:14:29] Was interessiert, sind die Ausgangslage von dem Projekt gewesen.
[00:14:42] Bringen Sie hier als Senior Consultant mit ins Spiel.
[00:14:45] Da erwarte ich eine gewisse Selbstständigkeit und auch ein gewisses Abholen.
[00:14:50] Wie Transformationen mit einem Kunden mit Business, mit einem Kunden-IT.
[00:14:59] Damit man auf Konzepte kommt, die umsetzt, die auch mal über den Haufen wirft.
[00:15:05] Auch dann systematisch durch sämtliche Realized Deployments, Migrationen bis hin zum Transition Service.
[00:15:12] Das ist das, was mich interessiert. Das ist das, was mich interessieren wird.
[00:15:18] Wenn wir zu einer Kenntnis kommen, dass es für Sie ein interessantes Arbeitsgebiet sein kann.
[00:15:26] Wird der nächste Schritt dann initiiert mit einer Vorstellung bei den Geschäftsverantwortlichen.
[00:15:35] Dann werden Sie dort auch einen 30 Minuten, 45 Minuten Interviewtermin erhalten.
[00:15:42] Die Kunden entscheiden natürlich auch, ob sie zu NTT passen.
[00:15:51] Das ist das Game, das Sie als Profisäger beherrschen.
[00:15:56] Damit zu Ihnen, Herr Mann.
[00:15:59] Vielen Dank, Herr Keller.
[00:16:01] Kapil Mandru stammt aus Indien ursprünglich seit 1991 in Deutschland.
[00:16:06] Als Kind rübergekommen, aufgewacht zum Schulübersuch, studiert und seit 2004 im Logistikfeld tätig.
[00:16:14] Auf der 3PL Seite.
[00:16:19] Ich habe das EWM, TEM, Transportation Management, Freight Forwarding.
[00:16:23] Auf der anderen Seite war wirklich von sämtlichen Rezepten durchgelebt.
[00:16:28] Das heißt die Lagerführung, wie das gemacht werden soll.
[00:16:37] Für große oder kleinere mittelständische Unternehmen.
[00:16:40] Für Seefracht.
[00:16:42] Da war ich bei der Firma namens DAMCO.
[00:16:44] Die gehörten zu MERSC, damals die größte Rederei der Welt.
[00:16:49] Das EFRED Geschäft habe ich bei DHL Global Forwarding gelernt.
[00:16:54] Damals waren sie die Nummer 2.
[00:16:57] Nach kühlen Nageln, nach Größen her.
[00:16:59] Das IT Wesen habe ich bei Expelleiters gelernt.
[00:17:04] Und zu Schluss, 2018, als ich meinen angestellten Job beendet habe,
[00:17:14] war ich Manager für Customer Solutions Manager für Europa zuständig.
[00:17:19] Das ist gut gelaufen, hat Spaß gemacht.
[00:17:23] Auf der P-Seite haben Sie dann das Customer Management gemacht.
[00:17:29] Das heißt, wenn ein Industriekunde kam und sagte,
[00:17:32] ich habe Frachtthemen, Lagerthemen, Logistikthemen,
[00:17:35] ich gerne outsourcen würde,
[00:17:37] wie hatten Sie die Funktion?
[00:17:40] Customer Solutions Manager.
[00:17:42] Die Kunden hatten wir von Expelleiters.
[00:17:45] Die Firma hat daran geglaubt, dass sukzessive Wachstum nur gesunder Wachstum ist.
[00:17:51] Kunden hatten wir in einem bestimmten Bereich.
[00:17:53] In Seefracht, Luftfracht oder Customs.
[00:17:57] Da haben wir das peu à peu ausgearbeitet.
[00:18:00] Dann versucht, die Gesamtlösungen als einheitliche Lösungen zu bieten.
[00:18:04] Hat auch gut funktioniert.
[00:18:06] Der größte Kunde, den wir damals bedient haben, war die Firma Siemens.
[00:18:10] Welche Siemens? Mit vielen Siemens?
[00:18:15] Ja, das war Siemens, für die ich zuständig war.
[00:18:21] Wie die Entity in sich hieß, weiß ich gar nicht mehr.
[00:18:25] Aber die haben die ICS-Süge gebaut.
[00:18:28] Da gab es einen speziellen Namen unter denen, aber das weiß ich nicht mehr.
[00:18:35] Das ist dann die Logistik, die Prozesse übernommen nach Aftersales.
[00:18:50] Transport. Aftersales und Transport.
[00:18:53] Aftersales ist Spare Part Management.
[00:18:56] Und die Transportansicht ist stattgefunden.
[00:19:00] Richten Sie mir noch mal um Reisen in der Übersicht.
[00:19:12] Das zeigt mir, dass Sie in der Lage sind, das ganze Top-Down darzustellen.
[00:19:18] In den Business-Kontext zu bringen, das gefällt mir.
[00:19:21] Gehen wir mal tatsächlich in ein oder zwei Projekte, wo Sie mir kurz die Ausgangssituation, den Verlauf, Größe schicken.
[00:19:27] 2018 sind wir selbstständig gemacht als Freelancer.
[00:19:31] Kurz darauf haben wir eigene Firmen gegründet.
[00:19:34] Unsere Services, die wir anbieten, sind rein auf Supply-Chain basiert.
[00:19:40] Nur EBM, TM, SD und dazu relevante Module.
[00:19:47] Die Kunden, die ich hatte, waren überwiegend in Pharma-Bereich und Manufacturing.
[00:19:53] Pharma und Automotive, das sind die zwei, die die höchste Standards festlegen.
[00:19:59] Pharma getragen durch die Regulierungsbehörden und Automotive aufgrund der Geschichte.
[00:20:04] Weil die müssen so stark getaktet sein, damit überhaupt die profitabel sein können.
[00:20:09] Und die haben auch den höchsten Bedarf.
[00:20:12] In Pharma hatte ich Kunden für Roche, Basel, CSL, Thermal Fisher.
[00:20:18] In Maschinenbau war die Firma Stihl.
[00:20:24] Stihl war damals sehr ähnlich wie Miele jetzt auch. Dazu komme ich gleich.
[00:20:30] Dann die Firma ZF.
[00:20:32] Bei der Firma ZF habe ich verschiedene Positionen begleitet.
[00:20:36] Ich war fast drei Jahre da.
[00:20:39] Angefangen habe ich als ganz normaler Teammitglied, Teammember.
[00:20:44] Aufgrund meiner Erfahrung, die ich schon hatte, weil ich das Geschäft von Peek aus kenne.
[00:20:50] Ich bin kein gelernter, reiner ITler, der nur die IT-Kodierung macht.
[00:20:56] Aber ich habe das Luft- und Seelfracht- und LKW-Geschäft weltweit kennengelernt.
[00:21:03] Ich habe die ganzen Strukturen gesehen, kennengelernt, wie das bei Kunden gelebt wird.
[00:21:09] Somit kann ich mir das sehr schnell aneignen, wie die Prozesse sind.
[00:21:14] Ich kann die Prozesse sehr schnell verstehen und Prozesse neu designen.
[00:21:18] Prozesslücken, Fitcap-Analysen machen und neu prozessdesignen ist überhaupt kein Problem.
[00:21:23] Weil ich das jahrelang gemacht habe, als Teamleiter auch.
[00:21:27] Das nehme ich Ihnen an.
[00:21:29] Dann war ich bei ZF angefangen als normaler Teammember.
[00:21:33] Damals habe ich mit dem GPO eng zusammen gearbeitet.
[00:21:37] Er hat gemerkt, dass ich das kann und wurde dann befördert.
[00:21:41] Ich war ein externer Teamlead, aber offiziell dürfte das so nicht sein.
[00:21:46] Weil Teamleads dürften nur ZF-Mitarbeiter sein.
[00:21:49] Aber ich habe den ZF-Mitarbeiter unterstützt.
[00:21:53] Aber inoffiziell hatte ich die Position von Teamlead.
[00:21:56] Das wusste man auch intern.
[00:21:58] Am Anfang waren wir auf der Build-Seite, also Requirement Gathering.
[00:22:02] Wir haben ein Template-Approach für 400 Werke.
[00:22:06] Das geht nicht anders.
[00:22:08] Wir haben ein Gesamt-Template gebaut.
[00:22:10] Dafür haben wir die grundlegenden Prozesse, die in einem Template enthalten sein müssen, aufgenommen.
[00:22:18] Das Build-Team hat das gebaut.
[00:22:21] Das war das zweite Team.
[00:22:23] Irgendwann hatten wir die Requirement-Seite 90 bis 92 Prozent erreicht.
[00:22:29] Ein globales Template kann man das maximal erreichen.
[00:22:34] Das weitere Schöne ist, dass man auf das Lokalisation-Konzept gehen muss, wenn man Rollouts macht.
[00:22:47] Nichts zu danken.
[00:22:50] Das Business-Seite ist relativ schnell gemacht, weil man weiß, wovon man spricht.
[00:22:57] Wenn es auf der Profi zu unterhalten ist, geht es relativ fast.
[00:23:00] Da hat man die Requirements aufgenommen.
[00:23:02] Aber das Umsetzen in der IT kann manchmal ein bisschen länger dauern.
[00:23:05] Da hat man ein riesiges Backlog.
[00:23:08] Dann bin ich in ein IT-Team gewechselt.
[00:23:11] Ich habe die Hands-On-Erfahrung mit Customizing gemacht und systemseitig umgesetzt.
[00:23:18] Das war dann auch irgendwann erbracht.
[00:23:21] Sie können Customizing, Sie können auch an der Stelle architektonisch arbeiten.
[00:23:27] Im Sinne von was mache ich im TMWM, was mache ich in der Integration zu ERP.
[00:23:32] Ja, das kann ich.
[00:23:34] Zu guter Letzt war ich für die Firma ZF weltweit unterwegs gewesen.
[00:23:42] Ich habe mir die Werke vor Ort angeschaut.
[00:23:44] Ich habe auch das Integration gemacht.
[00:23:46] Wir haben Rollouts gemacht.
[00:23:48] In China, in Tschechien.
[00:23:50] Ich muss mal von Ost nach West gehen.
[00:23:52] Ich meine China, Tschechien, Südkorea, England, Deutschland, Brasilien und USA.
[00:23:59] Die Werke live gebracht.
[00:24:01] Die Situation in Automotive, wie sie ist, ist allen bekannt.
[00:24:07] ZF hat in großen Maßen interne Leute entlassen.
[00:24:12] Aufgrund verschiedener politischer Entscheidungen.
[00:24:15] Das möchte ich nicht äußern.
[00:24:17] Aber die haben einen Druck bekommen vor der Politik.
[00:24:20] Wie kann das sein, dass so viele externe angeheuert sind, aber interne gehen müssen.
[00:24:25] Und somit mussten die externen auch irgendwann gehen.
[00:24:28] Wir haben aber unseren Java erledigt.
[00:24:30] Das hat die interne Leute so weit dazu gebracht, dass sie eigenständig arbeiten konnten.
[00:24:36] Wir haben mehrere Werke live gebracht.
[00:24:38] Und dann auf eine kleinere Flamme konnten sie eigenständig weiterarbeiten.
[00:24:45] Dann hatte ich die Firma Stihl.
[00:24:47] Da war ich aber vor ZF.
[00:24:50] Die hatten ähnliche...
[00:24:54] Die sind ja auf dem Weltmarkt Weltführer in Kettensägen.
[00:25:00] So wie Miele in Waschmaschinen.
[00:25:02] Da gibt es keine Zweiten.
[00:25:04] Die Unternehmstruktur war so, dass sie in ihrem Produkt so einzigartig, so perfekt waren.
[00:25:10] Weil die so detailverliebt waren.
[00:25:13] Die haben wirklich nur dann etwas rausgebracht, wenn es nur 100% perfekt ist.
[00:25:17] Das war auf Produkt-Ebene das perfekte Lösung.
[00:25:21] Aber auf IT-Ebene, Projektumsetzung, war das eine Katastrophe.
[00:25:25] Weil Stihl und der Implementierungspartner damals, Accenture, konnten sich nie wirklich klar werden, wer hat das Lied.
[00:25:35] Wer hat das an.
[00:25:37] Stihl macht zwar die perfekte Produkte, aber Accenture hat die IT-Erfahrung.
[00:25:41] Und Stihl hat sich immer dazwischen geredet.
[00:25:43] Und somit war das so, dass die Requirements immer wieder neu kamen.
[00:25:47] Zwar nicht von Logistik, aber von Quality, von Production, von Sales, von Einkauf.
[00:25:54] Und wenn immer neue Requirements kommen, kann das Template niemals fertig werden.
[00:26:01] Oder beispielsweise ein GPO, Global Process Owner.
[00:26:07] Diese Position hatte ich als Externer.
[00:26:09] Ich habe mir sehr geehrt gefühlt.
[00:26:11] Das war wahnsinnig, wahnsinnig viel Arbeit.
[00:26:14] Aber seit dem Projekt habe ich aufgehört, Lied und Position freiwillig zu übernehmen.
[00:26:21] Weil ich weiß, wie viel Stress das mit sich gebracht hat.
[00:26:24] Und das war mir niemals wieder wert gewesen.
[00:26:28] Ich mache sämtliche Arbeiten.
[00:26:31] Wichtig ist, dass man das Gesicht sieht, was man kann, was man möchte.
[00:26:38] Und wenn man solche Global Ownerships sich nicht gut fühlt,
[00:26:44] wäre es ein Fehler, dieses weiter machen zu wollen.
[00:26:49] Das ist aber kein Fehler, wenn man sich dann in das Thema verlegt, was man beherrscht.
[00:26:56] Ich brauche tatsächlich von Ihnen noch mal zwei, drei Informationen.
[00:27:01] Architekturentwicklung.
[00:27:04] Wenn Sie Global Process Owner waren, dann ist Ihnen klar,
[00:27:09] dass man über ein Process House mit der Integration EAP, mit der Integration TM, EWM
[00:27:15] über das Process House eine solide Grundlage erhält.
[00:27:20] Man leitet das Data House ab, um die Verteilung der Datenobjekte zu designen.
[00:27:25] Und hat schlussendlich dann auch ein bisschen das System House mit der Architektur.
[00:27:32] Was macht TM, was macht EWM?
[00:27:34] Nummer eins, Sie werden nicht eine Situation vorfinden,
[00:27:40] dass das Process House, Data House, System House grundsätzlich verkehrt ist.
[00:27:50] Es steht zu 70-80% robust.
[00:27:56] Das ist von den strategischen Unternehmen entwickelt.
[00:27:59] Das ist von Miele mit uns validiert.
[00:28:02] Und an einigen Stellen müssen wir jetzt noch bearbeiten.
[00:28:04] Aber wichtig ist jetzt für mich von Ihnen zu wissen,
[00:28:10] das Setup ist ein Side-by-Side Setup.
[00:28:14] Also EAP in einem System, EWM in einem separaten System,
[00:28:20] um EAP unabhängig vom Logistik, also vom Lager zu halten,
[00:28:27] dass die sich nicht gegenseitig beeinflussen.
[00:28:29] Sollte TM runtergezogen werden,
[00:28:33] dann hat man zumindest mal ein weiter lauffähiges EAP-System.
[00:28:39] Das ist eine Setzung, die ist bewertet worden.
[00:28:42] Also man geht nicht auf einen embedded Ansatz,
[00:28:45] man geht auf einen Side-by-Side Ansatz.
[00:28:47] Man hat ein dezentrales EWM, das ist okay, das funktioniert.
[00:28:50] Man kann wunderbare Idealfüllstellen machen.
[00:28:53] Habt ihr Erfahrungen?
[00:28:55] Ja, habe ich.
[00:28:56] Wir haben ein embedded EWM gehabt, wir haben auch Projekte gehabt,
[00:29:00] wo wir das dezentrale EWM hatten.
[00:29:04] Also das Customizing an sich ist überall das Gleiche,
[00:29:07] nur die infrastrukturen Anbindungen,
[00:29:12] die am Anfang gemacht werden müssen, sind anders.
[00:29:17] Was ist Ihr Rat zu diesen Punkten, wo Sie sagen,
[00:29:22] so ein Side-by-Side, da muss man sagen,
[00:29:25] dass man es auch nicht falsch macht?
[00:29:34] Das weiß ich gar nicht so genau.
[00:29:36] Ich würde sagen, da muss wahnsinnig viel getestet werden
[00:29:41] von Anfang an, ohne dass man, bevor man die Masterdaten hat
[00:29:47] in beiden Systemen.
[00:29:49] Also das ist schon wirklich sehr schwierig zu sagen.
[00:29:52] Also dass die ganzen Ideal-Schnittstellen stehen
[00:29:57] und die kommunizieren können, müssen ja beide Systeme
[00:29:59] mit Daten gefüttert werden.
[00:30:01] Mit Masterdaten, mit Trans-National-Systemen.
[00:30:03] Auf ERP-Systemen sind in der Regel vorhanden,
[00:30:05] auf das leere EWM-System in der Regel nicht.
[00:30:09] Die müssten ja auch gefüllt werden.
[00:30:11] Erst wenn die drin sind, dann kann man wirklich sagen,
[00:30:14] kann man belastbare Ergebnisse herausfinden,
[00:30:19] ob es funktioniert.
[00:30:21] Würden Sie TM unterbringen, oder würden Sie TM auf der Seite EWM?
[00:30:29] ERP, weil TM ist enger mit SD verknüpft als mit EWM.
[00:30:33] Das ist nämlich noch eine fundamental Architekturentscheidung,
[00:30:41] die noch nicht verabschiedet ist.
[00:30:43] Das war das Ergebnis der Vorstudie.
[00:30:52] Wir versuchen aber diese Diskussion nochmal aufzubrechen.
[00:30:57] Wir nehmen SAP gerade mit an Bord und sagen,
[00:31:00] wir müssen nochmal die Seite näher mit SD.
[00:31:18] Gibt es eigentlich mehr, das dort zu tun?
[00:31:29] Es kommt ein sehr lange her.
[00:31:32] Nicht viel, weil die meisten Kundenprojekte,
[00:31:38] wo ich gearbeitet habe, waren das nicht das Thema gewesen.
[00:31:41] Advanced shipping receiving, ja, das war.
[00:31:44] Dann muss man dafür bestimmte Lizenzen kaufen.
[00:31:47] Die waren so teuer, es wurde so viel diskutiert.
[00:31:51] Das war zwar Teil des Projektes,
[00:31:53] aber aufgrund der Kosten und politischen Entscheidungen
[00:31:56] wurden die Entscheidungen so spät getroffen,
[00:31:59] bis es da war, und man konnte es nicht wirklich ausgiebig testen.
[00:32:04] Theoretisch weiß ich, wie das funktioniert.
[00:32:08] Aber ich habe bisher keinen Kunden gehabt,
[00:32:13] der das wirklich in dem Maß ausgelebt hat, wie es sein soll.
[00:32:17] Ich würde gerne ein Briefing für Sie für eine konkrete Vorbereitung,
[00:32:45] wie wir den Miele-Termin gemeinsam gestalten werden.
[00:32:50] Ich habe dazu auch ein bisschen einen Vorschlag,
[00:32:55] den lasse ich Ihnen auch überkommen, sich vorzubereiten.
[00:33:05] Auch sehr kurzfristig vorzubereiten.
[00:33:08] Da geht es um tatsächlich, was ich eingangs erwähnt habe,
[00:33:11] nimm zwei Referenzprojekte.
[00:33:13] Stell die Ausgangslage da.
[00:33:15] Schreibe das Gesamtprojekt und definiere den Teilbereich,
[00:33:23] den du verantwortet hast.
[00:33:25] Schreibe, wie innerhalb des Projektes gearbeitet,
[00:33:33] was waren dann die Erfolge und Deliveries.
[00:33:36] Über diese beiden Referenzprojekte kommt man wirklich gut in Dialoge.
[00:33:42] Das ist keine Powerpoint-Präsentation. Bitte nicht.
[00:33:45] Lieber eine gute Geschichte.
[00:33:48] Ich will Ihnen persönlich noch mal ein Kompliment aussprechen,
[00:33:52] so wie Sie das gerade gemacht haben.
[00:33:54] Über die Tonspur, über die Struktur, die Story erzählen.
[00:33:58] Das können Sie. Das ist kommunikativ hervorragend.
[00:34:01] Das wird einen guten Eindruck hinterlassen.
[00:34:07] Letzte Frage. Sie wohnen wo?
[00:34:10] In Gießen. Also im Busseck in der Nähe von Gießen.
[00:34:14] Kennen Sie das?
[00:34:16] Ja, cool.
[00:34:17] Kurzfristig wäre es wirklich kein Problem.
[00:34:37] Das Projekt, das wir jetzt haben...
[00:34:39] Wie viel Prozent?
[00:34:40] 100 Prozent. Das läuft im nächsten Jahr aus.
[00:34:42] Kurzfristig heißt dann zwei Wochen.
[00:34:45] Wir fangen ja nicht morgen an.
[00:34:47] Ab Oktober?
[00:34:48] Ja, genau.
[00:34:49] Und Leipzig in Czernist.
[00:34:58] Zunächst gilt es noch vieler mit der zentral verantwortlichen,
[00:35:04] mit der zentral verantwortlichen Business,
[00:35:06] zentral verantwortlichen Partie vorzunehmen.
[00:35:11] Kulturbedingt empfehle ich eine hohe Präsenz in Gütersloh bei Miele.
[00:35:17] Das sind hinaus zwei Stunden, zweieinhalb Stunden.
[00:35:23] Wie ist Ihre Vor-Ord-Verfügbarkeit?
[00:35:29] Grundsätzlich habe ich nichts dagegen vor Ort zu sein.
[00:35:32] Es kommt darauf an, in welcher Phase das Projekt, das man ist.
[00:35:36] Ich bin in vielen Projekten schon sehr viel gereist.
[00:35:39] Aber jede Woche drei Tage, vier Tage irgendwo so sein,
[00:35:42] das kann ich nicht machen.
[00:35:43] Das frage ich nicht, was Sie nicht können.
[00:35:46] Das frage ich, was Sie am lieben.
[00:35:49] Also bei Bedarf, da wo es notwendig ist, werde ich da sein.
[00:35:52] Da würde ich...
[00:36:08] Ja, hohe Präsenz. Ich sage zwei bis drei Tage.
[00:36:14] Anreise mit Abreise.
[00:36:21] Das wird weniger werden.
[00:36:24] Vielleicht 14-tägige Anwesenheiten.
[00:36:27] Dann auch sinnvollerweise so organisiert,
[00:36:30] dass man zwei Tage Workshops aufstellt, vorbereitet,
[00:36:33] durchführt, nacharbeitet und dann wieder
[00:36:36] sich zurückzieht in dem Homeoffice.
[00:36:39] Aber zunächst, diese vier Wochen sind entscheidend
[00:36:45] mit einer hohen Präsenz.
[00:36:46] Könnten Sie das einrichten?
[00:36:48] Solange es nicht dauerhaft ist, ein ganzes Jahr lang.
[00:36:52] Weil das war der Grund, warum ich bei Stiel aufgehört habe.
[00:36:55] Und ich habe eine Familie.
[00:36:59] Und das war dann auch noch... Wo war das denn?
[00:37:02] In Österreich und in der Schweiz.
[00:37:04] Und immer diese sehr lange Anreisen.
[00:37:07] Das war mir viel zu anstrengend.
[00:37:08] Anreise ein bisschen anständlich.
[00:37:12] Aber für mich heißt es auch, Sondas ins Auto stehen.
[00:37:25] Mittwochs, Donnerstags dann wieder zurück.
[00:37:28] Es sind Kunden, die man in Wandenkung
[00:37:32] in Präsenz nehmen muss.
[00:37:33] Einfach von der Kultur her.
[00:37:37] Eingeschwungen hat, wenn man die Connects hat.
[00:37:39] Wenn man die sicherlich in hoher Ansehung auch nicht.
[00:37:49] Aber es gibt dann immer wieder, so wie Sie sagen,
[00:37:52] wenn man Testfaser hat, Functional Unit Test,
[00:37:55] System Integration Test, heißt natürlich auch wieder Präsenz.
[00:37:58] Aber so.
[00:37:59] Also, wir sehen uns wieder.
[00:38:00] Wir hören voneinander.
[00:38:01] Herr Mandru, ich bedanke mich wirklich für Ihre Zeit
[00:38:04] und für Ihren eindrucksvollen Stil.
[00:38:07] Vielen Dank für Ihre Zeit.
[00:38:09] Bis bald.
[00:38:10] Bis bald.
[00:38:11] Tschüss.
[00:38:12] Fabio, hast du vielleicht noch mal eine Minute für mich?
[00:38:14] Eine Minute habe ich.
[00:38:15] Cool.
[00:39:33] Noch eine Minute hier noch.
[00:39:38] Okay, ich werde den der nächste Tag immer fragen.
