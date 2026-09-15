# NTT Gespräch 2 – Vorbereitung Referenzprojekte (Miele mDeep)

**Datum:** 14.09.2026, 10:57 Uhr
**Teilnehmer:** Mario Keller (NTT, Transformationsverantwortlicher mDeep), Kapil Mandru, sowie zu Beginn ein Recruiter (Frank Recruitment Group)
**Typ:** Zweites, vorbereitendes Coaching-Gespräch vor dem eigentlichen Miele-Interview – Vertiefung von zwei Referenzprojekten
**Aufnahme:** Bildschirm + Ton, lokal abgelegt unter `meeting notes/Aufnahmen/2026-09-14_10-57_NTT - Miele.mp4`
**Bezug:** Folgegespräch zu [2026-09-10 – Erstinterview NTT](./2026-09-10-NTT-Interview-Miele-mDeep.md)

## Wichtigste Take-aways

1. **Zweck des Calls:** Kein neues Interview, sondern ein **Coaching/Deep-Dive**, um die zwei Referenzprojekte für das kommende Miele-Interview inhaltlich und in der Präsentationsform zu schärfen.
2. **Feedback zur Kommunikation:** Herr Keller lobt die klare, knappe Art ("kurz und knackig", "auf den Punkt") ausdrücklich mehrfach – das soll im Miele-Termin beibehalten werden.
3. **Zeitformat für den Miele-Termin:** Jedes der zwei Referenzprojekte soll in **ca. 5–6 Minuten** vorgestellt werden (Ausgangslage, eigene Rolle, Vorgehen, Ergebnis). Innerhalb einzelner Aussagen empfiehlt Keller sogar **~2 Minuten pro Kernaussage**, da das Publikum (Miele-Fachleute) selbst SAP-Profis sind und primär "abhaken" wollen: Aktivierung, Template, Lokalisierung, Verständnis, dass ein globales Master-Template realistisch nur 80–90 % abdeckt und der Rest lokal gelöst werden muss.
4. **Wichtiger Hinweis zur Architekturfrage (decentralized vs. embedded EWM):** Diese Entscheidung ist in der Praxis **immer schon vom Kunden bzw. mit dem Implementierungspartner getroffen**, bevor der Kandidat ins Projekt kommt. Kapil soll das bei Miele **nicht als eigene Entscheidung darstellen**, sondern anbieten, eine **Pro-/Contra-Analyse (3–5 Punkte)** zu liefern, falls gewünscht – das wirkt seriös, ohne eine Kompetenz vorzutäuschen, die er in der Vergangenheit nicht hatte.
5. **Nächster Schritt:** Mario Keller übernimmt die **Terminkoordination für das Miele-Gespräch persönlich** und sendet die Einladung/E-Mail in den nächsten Tagen.
6. **Zweites Referenzprojekt:** Vorschlag von Keller – **Stihl** weiterverwenden, da das Geschäftsmodell vergleichbar ist (Gerätehersteller + Aftersales/Supply-Chain), alternativ Pharma-, Coca-Cola-/FMCG-Projekte.
7. Am Rand: Vorstellung der Recruiting-Firmenstruktur durch den anwesenden Recruiter – **Frank Recruitment Group** mit Marken je Technologie: **Washington Frank** (SAP/ERP), **Nigel Frank** (Microsoft), **Mason Frank** (Salesforce), **Jefferson Frank** (AWS), **Anderson Frank** (NetSuite/Oracle) – größte Bereiche in Deutschland: Microsoft und SAP.

## Vertiefung Referenzprojekt 1: ZF Automotive (im Detail durchgesprochen)

Kapil Mandru stellt sein ZF-Projekt strukturiert nach Ausgangslage → Rolle → Vorgehen → Ergebnis vor:

- **Stakeholder-Umfeld:** enge Zusammenarbeit mit dem Global Process Owner (GPO), dem Global Lead für Rollout-Projekte und dem Senior Vice President Logistics.
- **Aufgabe:** Aufbau eines globalen Templates für **400 ZF-Werke**; Zielbild von Anfang an: globales Template deckt **~90 %** ab, die restlichen **~10 %** werden je Werk über ein Custom-/Lokalisierungskonzept ergänzt (Prozessaufnahme, Process Mapping, Gap-Identifikation, ggf. Neudefinition, Systemumsetzung/Customizing, Testing (SIT, Functional Test, UAT), Dokumentation, Key-User-Training / Train-the-Trainer).
- **Eigenes Werk:** **Shangjiagang** (nahe Shanghai, China) – eines der komplexesten und wichtigsten Werke. Da im Global Template bereits Standard, war der eigene Beitrag primär, die **nicht-standardisierten lokalen Prozesse** zu identifizieren und zu lösen (inkl. Vor-Ort-Besuchen; keine Mandarin-Kenntnisse, Zusammenarbeit mit englischsprachigen lokalen Kollegen als fachliche "Dolmetscher").
- **Konkretes Problem & Lösung (3PL/Lager):** Das Werk hatte **40–50 3PL-Lager**, ursprünglich gemischt für Inbound und Outbound genutzt → führte zu Verzögerungen, da beide zeitgleich stattfanden. Lösung (vom Kandidaten vorgeschlagen und umgesetzt): **Trennung in dedizierte Inbound- und Outbound-3PLs**.
  - **Outbound:** Yard Management, Freight Unit Building, Route-Optimierung/Konsolidierung verschiedener Ausgangssendungen.
  - **Inbound:** automatisiertes Replenishment – 3PL überwacht proaktiv Bestände/Behälter und liefert automatisch nach (löste bis dahin manuelle Bestandsführung/telefonische Nachbestellung ab); Wareneingänge/-ausgänge auf beiden Seiten (3PL und ZF) per Scan automatisiert, manuelle Buchungen entfielen.
  - Vorgabe der Projektleitung: **so weit wie möglich im SAP-Standard bleiben** (Erfahrungswert: kundenspezifische Sonderlösungen sind später schwer in den Standard zurückzuführen).
- **ERP–EWM-Integration (drittes Architektur-Thema):** Beispiele auf Nachfrage von Keller:
  - Einkaufsbestellungen werden auf ERP-Seite in **MM** verarbeitet und via **MIGO** gebucht, müssen aber zusätzlich in **EWM** eingesteuert werden.
  - **Produktionsversorgungsbereiche (PVB / Production Supply Area, PSA):** ERP/MES triggert Materialbedarf, EWM beliefert automatisch; Schnittstelle einmalig über **EDI oder API** aufgesetzt.
  - Drei in verschiedenen Projekten erfolgreich eingesetzte **Nachschub-/Replenishment-Logiken:** klassisches Replenishment, Min-Max, Kanban.
- **Transportlogistik-Beispiele (zweites Referenzprojekt-Fragment, Tschechien-Werk):** Lieferanten buchen Anlieferslots; Multi-Stop-Routen (z. B. Werk Tschechien → Zentrallager Gütersloh mit Zwischenstopps in Österreich/Schweiz) erfordern Ladereihenfolge-Planung (zuletzt beladen = zuerst entladen); unterschiedliche Frachtmodelle: dedizierte LKW (Full Control für einen Kunden), Full Truckload (FTL) und Less-than-Truckload (LTL).

## Vorbereitungsauftrag an den Kandidaten

- **Referenzprojekt 1 (ZF):** Struktur wie oben, in ~5–6 Minuten vortragbar, mit klaren technischen Nachweispunkten (MIGO, PVB/PSA, EDI/API, Replenishment-Arten) statt langer Erzählung.
- **Referenzprojekt 2:** Empfehlung Stihl (vergleichbares Geschäftsmodell zu Miele: Gerätehersteller mit Aftersales-Supply-Chain) oder alternativ ein Pharma-/FMCG-Projekt; gleiche Struktur (Ausgangslage, Rolle, Vorgehen, Ergebnis) anwenden.
- Bei Fragen zur Architektur-Entscheidung (decentralized vs. embedded) **nicht behaupten, diese getroffen zu haben** – stattdessen anbieten, eine kurze Pro-/Contra-Liste zu erarbeiten.

## Hinweis: nicht zugeordneter Transkript-Abschnitt

Ab ca. [00:37:43] wechselt das Thema abrupt zu Lieferzeiten ("10–15 Tage", Bezug zum Rotes-Meer-Konflikt), Inbound-Status und einer Erwähnung von "320 Leuten aus Südafrika" sowie Namen wie "Moral"/"Julia". Das wirkt inhaltlich nicht zum NTT-/Miele-Gespräch gehörig und dürfte ein **Aufnahme-Übergang zu einem separaten, direkt danach geführten Gespräch** sein (evtl. ein anderes laufendes Projekt des Kandidaten). Es wurde hier der Vollständigkeit halber nicht weiter ausgewertet – bei Bedarf bitte gesondert prüfen.

## Volltranskript (mit Zeitstempeln)

> "Du" = Stimme des Kandidaten (Mikrofon), unmarkierte Zeilen = weitere Stimmen aus dem Call. Automatisch generiertes Transkript, kann kleinere Fehler enthalten.

[00:03:40] Gut, danke. Selber?
[00:03:41] Das übliche, also nichts Besonderes, Einkaufen gewesen ein bisschen und so.
[00:03:58] Partytime is over.
[00:04:01] Ja, das war mit 25 und nicht mit 45.
[00:04:09] Alles in seiner Zeit, ja.
[00:04:17] Okay.
[00:04:37] Mit 26 schon, das ging aber schnell.
[00:04:40] Ja, ich sehe aber auch schon aus wie 32.
[00:04:45] Ja, wir haben ja das Gespräch jetzt bezüglich Vorbereitung mit Familie.
[00:05:04] Dass der Mario dir so ein bisschen einen Scope mitgibt.
[00:05:16] Einfach so auch zu einordnen, dass Situationen und Challenges jeweils auch sind.
[00:05:45] Das sind, ich sehe bei dir im Hintergrund die ganzen Firmen, die hier aufgestellt sind.
[00:06:30] Washington Frank, Nigel Frank, Anderson Frank und so.
[00:06:34] Ihr seid mit Washington Frank kenne ich, Nigel Frank kannte ich auch.
[00:06:40] Yes.
[00:06:41] Okay, Mario.
[00:06:42] Also das sind alles unsere Brands quasi und bei uns, jede Brand fokussiert sich
[00:06:47] auf eine Technologie.
[00:06:49] Washington Frank ist z.B. bei uns die Brand für alles, was in der ERP umfällt.
[00:06:55] Hauptsächlich ist SAP der größte Bereich von Washington Frank.
[00:06:59] Nigel Frank macht Microsoft, Mason Frank macht Salesforce, Jefferson Frank macht AWS,
[00:07:09] Anderson Frank macht Internet Suite.
[00:07:13] Ich bin mir nicht hundertprozentig sicher gerade.
[00:07:18] Ja, genau, also.
[00:07:20] Dann jeweils auf die eigene Technologie funktionieren und hier ist halt nochmal die Fokusareas.
[00:07:26] Also die Bereiche, in denen wir hauptsächlich haben mit denen.
[00:07:31] Und unser größter Bereich ist tatsächlich Microsoft.
[00:07:34] Microsoft und SAP, in Deutschland ist Microsoft und SAP.
[00:07:42] Okay, cool.
[00:07:43] Bisschen aus wie nach einem Fußballspiel so die Interviews mit der Sponsoren-Tafel
[00:07:49] im Hintergrund.
[00:07:51] Weißt du was ich meine?
[00:07:52] Dann hast du ja auch so viele Sponsoren etc.
[00:08:02] Die haben wir leider ein bisschen auf sich warten.
[00:08:15] Aber das ist bei Mario, vielleicht bei unserem ersten Call war der auch ein paar Minuten
[00:08:21] zu spät, richtig?
[00:08:22] Und das letzte Mal?
[00:08:24] Nein, da war der Rest hatte ich da.
[00:08:26] Dann hat das manchmal an dich.
[00:08:30] Warten wir noch ein bisschen, kann schon.
[00:08:31] Hallo Herr Keller, guten Morgen.
[00:09:09] Ich lebe das Wochenende, um sich vorbereiten, habe ich das Wochenende dadurch beeinträchtigt,
[00:09:18] dass ich mich vorbereiten muss.
[00:09:20] Das ist schon okay.
[00:09:22] Aufgrund der Projekte, die relativ kurze oder längere Dauer haben, muss ich mich dauernd
[00:09:29] vorbereiten auf ein neues Projekt.
[00:09:32] Und mittlerweile ist es so sein gespielt, dass es gar nicht so viel Vorbereitung notwendig
[00:09:37] ist.
[00:09:39] Das ist so ähnlich wie wenn sich ein Finanzbuchhalter beschweren würde, was am ersten und am
[00:09:45] zweiten und am dritten zu Monatsanfang gar keine Zeit hat für was anderes.
[00:09:54] Amando, ich hatte Ihnen ein kleines Feedback gegeben, sowohl während des Interviews,
[00:10:05] ganz zum Schluss, wo ich auch zum Ausdruck gebracht habe, dass ich mich freue an ein
[00:10:10] zweites Gespräch mit Ihnen, wo wir ein paar Dinge ein wenig detaillieren, ein bisschen
[00:10:15] spezifischer werden.
[00:10:16] Im Wesentlichen geht es da um Beschreibung eines Projektes oder zweier Referenzprojekte,
[00:10:23] aus denen Sie kurz und bündig mal die Ausgangssituation beschreiben, wo Sie Ihre
[00:10:32] spezifische Rolle detaillieren, wie Sie in diesem Teilprojekt, im Rahmen eines Gesamtprojektes
[00:10:38] eingenommen haben, wie Sie vorgegangen sind, welche Arbeiten Sie dann in der Architektur,
[00:10:46] in den Bearbeiten von Themen gemacht haben, so dass ich ein bisschen ein Gefühl kriege.
[00:10:51] Das Ganze folgt wirklich im konkreten Hintergrund, wenn wir ein Gespräch mit Ihnen, auch tatsächlich
[00:11:01] das Format.
[00:11:02] Sie würden dann in zwei mal fünf, sechs Minuten diese beiden Referenzprojekte auf
[00:11:09] den Punkt vorstellen und sagen, das habe ich gemacht, das war mein Part, so gehe
[00:11:15] ich vor, gerade vor der spezifischen Herausforderung von einem dezentralen Setup EWM, TM und
[00:11:43] ERP S4.
[00:11:46] Damit darf ich auch an überleiten und vor mir.
[00:11:53] Gerne.
[00:11:54] Ich brauche ja dann nicht so weit auszuholen, dann gehe ich mal auf einmal das Automotive
[00:11:59] Projekt, das ich hatte, das längste, wo ich war, das ZF, da habe ich gearbeitet
[00:12:06] sehr eng mit GPO, Global Process Owner, dann der Global Lead für ausrollende Projekte
[00:12:19] und auch der Senior Vice President für Logistics.
[00:12:25] Meine Aufgabe bestand am Anfang daraus, dass ich die Anforderungen, also es ging
[00:12:33] darum, in der Anfangsphase waren wir dabei, ein Template zu bauen, ein Template, welches
[00:12:38] auf die 400 Sites von verschiedenen Werken von ZF ausgerollt werden sollte und es
[00:12:49] war ZF schon auch bewusst, dass es kein Template gibt, das für alle Werke in Logistik
[00:12:56] vor allem überall perfekt passen würde, weil jedes Werk andere Herausforderungen mitbringt,
[00:13:03] andere physikalische, historisch gewachsen, nicht jedes Werk hatte gleiche Strukturen
[00:13:08] in Lage und so weiter.
[00:13:11] So war so ein allgemeiner Verständnis da, dass wir das Template zu circa 90 Prozent
[00:13:19] haben können, um das globale Template und das auf die jeweilige Welt auszurollen und
[00:13:26] die restlichen 10 Prozent, die letzten Schritte, die müssten wir dann für die jeweiligen
[00:13:31] Werke im Custom-Localization-Konzept dann nochmal herauskristallisieren, was sich
[00:13:38] ein bestimmtes Werk von anderen unterscheidet und für den genau spezifisiert wird und
[00:13:45] Prozesse, ja Process Mapping zu machen, Process Gap zu identifizieren, Prozesse, neue Prozesse
[00:13:53] eventuell zu definieren, das Ganze dann auch in System umzusetzen, das heißt die
[00:13:58] Konfiguration dazu zu machen und mit der Konfiguration alles, was dazu gehört, wie
[00:14:04] das Testing, also das System Integration Test, Functional Test, dann OIT, User Acceptance
[00:14:11] Test, dann hinterher auch natürlich die Dokumentation davon für die Key User und mit der Dokumentation
[00:14:21] auch die Key User Training, damit die Key User wiederum die Armee von anderen Usern,
[00:14:27] die sie in deren Werken haben, teilweise auch weiter selber ausbilden können.
[00:14:33] Das war das Gesamtverständnis, das habe ich dann auch so gemacht, als ich angefangen
[00:14:39] habe wurde mir das Werk in Shangjiajiang zugeordnet, das ist in China, nicht weit
[00:14:45] von Shanghai, einer der komplexesten Werke in China überhaupt und einer der wichtigsten
[00:14:51] und da das Global Template ein Standard gehalten war, war gar nicht so sehr notwendig
[00:14:59] gewesen mein Input und welche Prozesse wir noch hinaufnehmen sollen, weil das
[00:15:03] alle Standard waren und meine Aufgabe war, diese Prozesse, die nicht ein Standard
[00:15:08] sind, in China zu bringen von Shangjiajiang. Dafür bin ich auch hingeflogen mehrere
[00:15:13] Male und mir die Prozesse vor Ort angeschaut, wir hatten ein bisschen bei der Sprache,
[00:15:17] chinesisch, kann ich leider nicht, aber es gab Kollegen vor Ort, die gut Englisch
[00:15:23] konnten, einige wenige gab es, die auch dann auch, die haben zwar nicht das Verständnis
[00:15:29] gehabt von Logistik, aber die haben dann gut übersetzt, also ich habe mit Logistik
[00:15:34] gesprochen und die Kollegen waren praktisch der Dolmetsch dazwischen. Die Prozesse aufgenommen,
[00:15:40] verstanden, vor Ort eine FitGap-Analyse gemacht, eine sehr enge Verbindung mit
[00:15:46] das globale Team in Deutschland, die Kommunikation gehalten und dann aufgesagt, was noch als
[00:15:52] offene Baustelle ist, was noch bis gar nicht auf Schirm gewesen war und diese
[00:15:58] Baustelle, diese offene Lücke praktisch, wie kann man die im besten schließen? In
[00:16:03] wiefern kann man mit einem Standardprozess handeln oder muss man was ganz
[00:16:08] neu konfigurieren? Es gab beide Fälle.
[00:16:39] Configuration, Testing, Dokumentation, Train the Trainer Konzept. Bleiben Sie auf dem Level, haben Sie
[00:16:51] Kennungseffekt auf jeder Seite generiert. Wichtig ist, dass Sie jetzt die Inhalte bringen,
[00:17:02] also vom Zeitmanagement, wenn du fünf Minuten Zeit hast, zwei Minuten dafür, was Sie eben
[00:17:09] mir gerade erklärt haben. Das kriegen Sie in zwei Minuten rein. Jeder hat eine Ahnung, das ist AP,
[00:17:17] Profis. Und denen geht es am Ende des Tages darum, Check, Check, Check, Activation, Check,
[00:17:25] Template, Check, Localization. Ah, da versteht, dass man ein Master nur zu 80-90% bauen kann,
[00:17:32] 10-20% ist lokales Business, wegen lokalen Gegebenheiten, Check. Nur für Sie zur
[00:17:39] Organisation. Bleiben Sie auf der Ebene, die Terms, die Sie tropfen, die Terms, die nieder erwartet.
[00:17:45] Wichtig ist, dass Sie jetzt immer die Architektur gelöst haben, wie Sie davor gehen, transportieren.
[00:18:04] In Ordnung, verstanden. Aber diese Entscheidung, decentralized oder embedded, war bereits
[00:18:10] vorher getroffen worden. Ich kann so eine Analyse machen, was mir Sinn machen würde,
[00:19:11] mit Pros und Contras. Aber ich muss auch ehrlich gestehen, in keiner der Projekte habe ich
[00:19:17] maßgeblich beigetragen, die Entscheidung zu treffen für den Kunden. Weil diese Entscheidung
[00:19:21] bereits Kunden IT-Seite schon getroffen worden war. Oder mit Hilfe von implementierenden Partnern.
[00:19:27] Genau, das ist Ihr Thema. Sie können Seriöse in PM und andere Seiten schieben. Aber bitte,
[00:19:49] Miele, seriös. Muss ich mich reinarbeiten? Kann ich auch? Müssen wir gemeinsam Vornacht
[00:19:56] als Analyse entwickeln. Und das ist okay. Das zeigt nur, wie professionell und seriös
[00:20:04] eine Aufgabe haben. Weil eine Lösung, ohne das Problem wirklich gesehen zu haben,
[00:20:09] oder ohne das Challenge wirklich gesehen zu haben, also Fernanalyse, ein bisschen schwierig und
[00:20:14] ein bisschen gewagt. Aber das ist kein Problem. Ich kann daran arbeiten und eine 3-5-punktige
[00:20:22] Pro und Contra Liste darstellen. Das wird schon aussagekräftig sein.
[00:20:45] Ja, gut, verstehe ich. Um Solutions zu finden, muss man die Herausforderung herauskristallisieren.
[00:21:17] Oder so, genau bei diesen Werken in Shangjia-Gang hatten die rund 40-50 3PL-Lager. Und zwar
[00:21:27] alles gemischt für inbound und outbound. Und das hat zu großen Verzögerungen gesorgt,
[00:21:33] weil die inbound und outbound relativ seit gleich stattgefunden haben. Mein Vorschlag war,
[00:21:41] was auch im Endeffekt umgesetzt worden ist, dass wir die 3PL so aufteilen, dass wir nur
[00:21:46] inbound-seitige 3PLs haben und outbound-seitige 3PLs haben. Das heißt, wenn wir Material,
[00:21:54] also wir in ZF-Werk das Material beziehen, gibt es in dem Moment nicht seit gleich outbound.
[00:21:59] Also wie wichtig die outbound sind, braucht man nicht sagen, weil Kundenverträge sind sehr
[00:22:05] wichtig. Also wir mussten sicherstellen, dass sich Wagenströme zwischen ZF und dem Kunden
[00:22:10] sichergestellt sind. Und dafür waren die 3PLs notwendig, ging nicht anders aufgrund
[00:22:17] Platzkapazitäten. Und ich habe dafür die ganze Prozesse definiert und auch systemtechnisch
[00:22:25] umgesetzt. Das ist richtig, aber wir sind in Standard geblieben. Es war gewünscht
[00:22:32] von Projektführung, dass wir so weit es geht in Standard bleiben, weil das haben
[00:22:42] die früher anders erlebt. Und wie schwer solche Prozesse, die maßgeschalt entwickelt
[00:22:50] worden sind für einen bestimmten Punkt, hinterher in Standard zu bringen, wie kompliziert
[00:22:55] und schwierig das sein kann, haben die schon selber bemerkt. Also habe ich die
[00:22:59] auch alle im Standard definiert und auch umgesetzt.
[00:23:33] In dem geforderten inhaltlichen TM-Knowhow, dass es ja ausgeht, die Integration, die
[00:24:02] Yardmanagement. Verstehe ich. Also auf der Outbound-Seite waren das Yardmanagement,
[00:24:19] das wir betreut haben, das Freight-Unit-Building und natürlich auch das Root-Dot-Optimization.
[00:24:31] Das heißt, wir haben Konsolidierung gemacht von verschiedenen Ausgangssendungen und dafür
[00:24:37] auch Root-Dot-Optimization eingeführt. Auf der Outbound-Seite, auf der Inbound-Seite
[00:24:45] haben wir eingestellt, dass der 3PL selber proaktiv schauen könnte, welche Rohmaterialien
[00:24:50] oder Komponenten an bestimmten Spiegel erreicht haben, also den einzelnen Bestand
[00:24:59] und automatisch nachgeliefert hat. Das heißt, automatisch einplanigement eingeführt,
[00:25:05] was vorher nicht da gewesen ist. Vorher war das alles nur Settelwirtschaft und Telefonie.
[00:25:08] Und das haben wir gekillt, indem einfach Systemgeführt kontrolliert worden ist.
[00:25:12] Und die ganze Outbound von 3PL und Inbound zu ZF wurde auch automatisiert. Das heißt,
[00:25:20] mit einmal Scannen auf der 3PL-Seite und einmal Scannen auf der ZF-Seite waren
[00:25:26] die Buchungen nicht mehr notwendig gewesen. Wurden alle automatisiert.
[00:25:30] Outbound haben Sie gemacht, Inbound haben Sie gemacht, verstehe ich. Also auch der 3PL-Seite.
[00:25:35] Integration. Ich würde mich auf als drittes architektonisches Thema,
[00:25:42] wie sah die Integration zum ERP aus? Da würde ich auch zwei, drei Beispiele nennen.
[00:25:50] Also wenn Sie eine Steuerung, eine Planung und eine Execution entwickeln, hinter die
[00:25:59] auslösenden Funktionen in einem ERP-System hinterlegt oder in einem Supply-Chain hinterlegt,
[00:26:08] also müssen Sie das ERP-System oder Supply-Chain-System dazu bringen, diese Event-Triggers, Objekte,
[00:26:18] TM zu liefern. Waren das Production Orders, waren das Replenishment Areas oder so diese PVBs in
[00:26:32] Deutsch genannt. Also PVB ist der Produktionsversorgungsbereich, PSA, Production Supply Area.
[00:26:38] Das hat damit nichts zu tun. Also wenn die Kommunikation zwischen ERP und EWM stattfindet,
[00:26:43] ist Folgendes, auf der Einkaufsseite in MM wurden Einkäufe durchgeführt und die werden
[00:26:50] auf der MIGO-Ebene als ERP eingebucht, aber die müssen in EWM eingeführt werden.
[00:26:56] Das wird über AP schon zusammen verbunden?
[00:26:59] Das reicht. Genau so war es. Kurz und knackig. Genau so, Herr Mann, das schätze ich an Ihnen.
[00:27:05] Das ist auf den Punkt. Das funktioniert so. Erstens, Zweitens, Drittens. Nicht mehr.
[00:27:12] Das zeigt mir, ah, da weiß man, worüber er redet. Also er redet nicht nur über,
[00:27:18] sondern da redet von. Ich bin konkret.
[00:27:22] Diese PVB, wir haben gesprochen, das ist Produktionsversorgung und die wiederum findet
[00:27:27] auf der ERP-Seite mit MES gemeinsam und ERP triggert das Materialbedarf und EWM
[00:27:35] beliefert das automatisch. Das muss einmalig geschnittschön hergestellt werden,
[00:27:39] entweder durch EDI oder durch API. Wenn das einmal gestellt und getestet ist,
[00:27:43] funktioniert das auch. Einmal ist das eine In-Bahn-Kühe, einmal ist das eine Out-Bahn-Kühe
[00:27:47] und die beiden kommen nicht in die Quere und kommunizieren einfach miteinander.
[00:27:50] Da gibt es drei verschiedene Wege, Produktionsversorgung. Einmal ist das Replenishment,
[00:27:54] einmal ist es Min-Max, einmal ist es Kan-Bahn. Alle drei erfolgreich in viele verschiedene
[00:28:01] Projekte eingesetzt. Kurz, präzise und das vermittelt dem das enorme Know-how,
[00:28:15] was sie mitbringen. Dann lassen Sie uns in der verbleibenden Zeit, was ist Ihr zweites
[00:28:21] Referenzprojekt? Was ist denn für Sie noch wichtig? Ich kann da viele verschiedene,
[00:28:30] also aus der Pharma-Bereich nehmen, aus der Coca-Cola, der FMCG, wir können Stil nehmen.
[00:28:38] Ein Fertigungswerk in Tschechien. Global Master wird gebaut. Erste Idee einen kleineren
[00:28:52] Fertigungswerk anzufangen. Aber Schub, wichtig, also aus Sicht des Fertigungswerkes. Ich muss
[00:29:02] einen In-Bahn-Prozess organisieren, bei denen Lieferanten ihre Lieferslots buchen,
[00:29:12] weil sie die Anlieferungen vorführen können. Die Einlagerung ins Lager,
[00:29:29] Management für ausgewählte Komponenten. Ein In-Bahn-Prozess ist auf Plenarbedarfen,
[00:29:39] also nicht Customer Orders von Plenarbedarfen, wird eine Fertigung geplant und dann
[00:29:50] für Polen, Spülmaschinen, Waschmaschinen für Dachraum. Das ist die triviale Logik. Ich
[00:30:05] weiß erst im Naheinland, was ich produziert habe. Ich weiß aber in dem Moment, wo die
[00:30:09] Ware da steht, ich muss die freigeben, ich muss ja den Laster schieben. So, dann haben wir das
[00:30:14] Teil Lagerproduktion. Hier haben wir die Milk-Crumbs, also über Kommissionierplanung
[00:30:22] und Steuerung, Kommissionierungen. Das ist typisch. Aber ich arbeite mit 3 PLs,
[00:30:37] ich gehe davon aus. Ja, ich arbeite mit PLs. Das geht sogar so weit, dass man also nicht
[00:30:44] nur einen Stadtpunktwerk in Tschechien hat und Endpunkt Zentrales Waren-Verteil-Zentrum
[00:30:53] in Büttersloh, sondern dass man unterwegs noch zwei, drei Stationen hat auf dem Weg,
[00:30:59] wo der Laster dann ein Werk in Österreich oder in einem Werk in der Schweiz. Ja, okay,
[00:31:11] da gibt es ja Freitagsbilder, das ist sehr wichtig für die, weil die müssten ja wissen,
[00:31:14] wie sie den LKW beladen, damit sie nicht bei jedem Stand komplett alles ausladen
[00:31:18] müssten, sondern der, der zuerst beladen wird, ist der, der zuletzt entladen wird.
[00:31:23] Das heißt, das mit, auf jeden Fall sehr stark mitproduziert.
[00:31:26] Ja, also ein Projekt, wo ich all das in einem Projekt gemacht habe, war das nicht so,
[00:32:08] ich habe alle Punkte gemacht in verschiedenen Projekten. Ja, wir hatten Delikate Trucks gehabt,
[00:32:13] das heißt, der LKW, also der, der, der, der Kunde hatte keine eigene LKW-Flotte. Die
[00:32:19] gemietet irgendwo, ja. Und der Spediteur hat gesagt, okay, dieser LKW fährt nur für dich,
[00:32:23] lieber Kunde, von A nach B, wo du willst, kannst du ihn einsetzen, ja. Das heißt,
[00:32:27] der, der Kunde hat den 3PL, also den Freit, den Spediteur, die die Flotte benutzt und
[00:32:34] selber eingeplant, das ist machbar. Dann gibt es, der Kunde sagt, okay, ich habe jeden Tag in
[00:32:40] meinem Werk in Tschechien Frachtstehen von zehn LKWs. Wer mir das beste Angebot macht,
[00:32:46] darf die Fracht haben, für ein LKW, zwei, drei oder acht, alles zusammen, ja. Das ist ein
[00:32:51] Full Truckload. Oder der Kunde sagt, ich habe für eine Route, zum Beispiel Tschechien, Spanien,
[00:32:57] da habe ich nicht so viel, da habe ich nur drei Paletten pro Tag, da habe ich LTL,
[00:33:01] Lesson Truckload. Genau diese Dinge, wo sie alles drin haben, wichtig ist,
[00:33:20] nehmen sie ein zweites Referenz, wo sie mit ihrer klaren Kommunikationsart, die mir sehr,
[00:33:27] sehr gefällt, ja, ist darstellen. Das war die Ausgangssituation. Also Beispiel ZF Automotive,
[00:33:35] ja, ich habe mit dem Global Product Owner gearbeitet, mit dem Senior Vice President
[00:33:41] Logistics, ja. Insgesamt ging es um einen Aufbau eines globalen Templates über 400
[00:33:48] Werke. Nicht alle Werke sind gleich, aber trotzdem hat man mit dem Master versucht, möglichst
[00:33:54] viel abzudecken. Localization habe ich in China verantwortet, ja, zehn Prozent für die
[00:34:02] lokalen Prozesse, lokalen Steuerungssysteme. Detail drauf ein und sagen, pass mal auf, es
[00:34:12] waren 40 bis 50 3PLs, ja. Wir haben das Ganze strukturiert, es gab dann am Ende des Tages so
[00:34:19] unsere Lösung, die von ZDF umgesetzt worden ist, inbound, outbound. Und jetzt haben wir konkret
[00:34:26] aufgrund von dieser Topologie, erstens, zweitens, drittens, Replenishment Logik. War ein bisschen
[00:34:37] schwieriger, weil Location, eine Steuerung, sehr realisiert und chargengeführt erhalten.
[00:34:56] Dann ist es eine Story. Und genauso nehmen sie ihr zweites Referenzprojekt. Dann kann man
[00:35:01] Stil nehmen. Stil sehr gut, weil das Geschäftsmodell sehr vergleichbar ist. Ich baue das Gerät und
[00:35:11] habe hinterher noch ein Salesnetz, der drauf in der Supply-Chain am Ende des Tages immer
[00:35:32] Ich finde, Sie haben eine ausgesprochen gute Ausgangslage. Und wenn Sie Ihre positive und mitnehmende und klare Art nutzen,
[00:35:47] ich kann Ihnen da nur sagen, die Vorstellung von Ihnen, da hat man immer noch Zeit, genau diese Beispiele zu nennen.
[00:36:19] Denken Sie mal dran, wenn Sie Ihnen mal ein Beispiel liefern, Kernprozesse, so, über die MIGO, über die SISO, habe ich realisiert.
[00:36:31] Super. Keine Töne mehr.
[00:36:33] Für mich ist das eine sehr gute Vorbereitung. Ich würde dann in die Terminkoordination mit Ile gehen.
[00:36:40] Schauen. Glück zu dir.
[00:36:49] Du hast ein Gespräch, die Koordination direkt von Ihnen machen.
[00:37:03] Ich mache die Terminkoordination direkt. Habe ich die E-Mail vom Herrn?
[00:37:06] Lass ich dir zukommen. Lass ich dir zukommen.
[00:37:09] Dann werden wir etwas Zeit nach die Woche machen.
[00:37:12] Okay, in Ordnung. Danke auch und schön, dass du da bist.
[00:37:16] Danke schön. Wiedersehen. Tschüss.

*(Ab hier vermutlich separater, nicht zugehöriger Gesprächsteil – siehe Hinweis oben)*

[00:37:43] Es dauert mehr als 10 Tage, aber 10-15 Tage, würde ich sagen.
[00:37:48] Es ist mit dem Red Sea und dem Konflikt.
[00:37:57] Es gibt keine Probleme auf der Inbound-Seite.
[00:38:02] Wir haben angefangen, die Inbounds zu bekommen.
[00:38:05] Die Inbounds werden etwas Zeit nehmen, aber die Inbounds kommen jetzt.
[00:38:09] Das ist ein Update von meiner Seite.
[00:38:12] Lass mich wissen, ob Sie noch Fragen haben.
[00:38:14] Danke, Moral.
[00:38:17] Moral, sorry Julia, ich habe nur eine Frage.
[00:38:21] In der Inbound-Seite sind etwa 320 Leute, die aus Südafrika sind.
[00:38:29] Sind Sie sagen, dass sie alle zu Ihnen sind?
