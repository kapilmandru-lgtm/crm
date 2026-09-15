# Referenzprojekt 2: Stihl – Global Process Owner Logistik

Vorbereiteter Sprechtext für das Miele-Interview, gemäß Coaching-Vorgabe von Mario Keller (NTT) aus dem [Gespräch vom 14.09.2026](./2026-09-14-NTT-Gespraech-2-Miele-Vorbereitung.md): **~5–6 Minuten**, als Story erzählt (keine PowerPoint), Kernaussagen jeweils in ~2 Minuten auf den Punkt. Keller empfiehlt gerade Stihl als zweites Referenzprojekt, weil das Geschäftsmodell zu Miele passt: Gerätehersteller mit nachgelagertem Sales-/Aftersales-Supply-Chain-Netz.

> **Hinweis:** Die Governance-Geschichte stammt aus dem Ersttranskript, das konkrete technische Beispiel (Yard Management, Freight Unit Builder, Package Builder) wurde von dir ergänzt, da es in keinem der beiden Transkripte enthalten war.

---

**Ausgangslage**

Vor meiner Zeit bei ZF war ich bei Stihl – dem Weltmarktführer für Kettensägen, ganz ähnlich wie Miele in seinem Segment ohne echten zweiten Wettbewerber. Auf Produktebene war Stihl extrem detailverliebt und hat ein Produkt nur dann herausgebracht, wenn es zu hundert Prozent perfekt war. Auf IT- und Projektebene sah die Realität anders aus: Stihl und der damalige Implementierungspartner Accenture konnten sich nie klar darüber einigen, wer im Projekt eigentlich die Führung hat. Die Folge: Stihl mischte sich ständig in die Umsetzung ein, und aus Quality, Production, Sales und Einkauf kamen laufend neue Anforderungen – nicht aus der Logistik selbst. Wenn aber ständig neue Requirements nachkommen, kann ein Template nie fertig werden.

**Meine Rolle**

In diesem Umfeld war ich als externer **Global Process Owner (GPO)** für die Logistikprozesse eingesetzt. Eine Position, auf die ich einerseits sehr stolz war, die aber gleichzeitig enorm viel Verantwortung und politischen Druck mit sich brachte – ich musste zwischen den wechselnden Anforderungen der Fachbereiche und den eigentlichen Projektzielen vermitteln, ohne dass die Governance-Frage zwischen Kunde und Implementierungspartner geklärt war.

**Vorgehen – ein konkretes Beispiel**

Trotz der instabilen Anforderungslage habe ich in dieser Zeit den kompletten Outbound-Transportprozess in SAP TM aufgebaut – bei Stihl ausschließlich als reine LKW-Transporte, ohne andere Verkehrsträger. Die Besonderheit war, dass eine Tour häufig **mehrere Kunden im Multi-Stop** beliefert hat, also ein LKW auf einer Route verschiedene Kunden nacheinander anfährt. Damit das funktioniert, habe ich drei Bausteine ineinandergreifen lassen:

- **Package Builder:** Bevor überhaupt eine Frachteinheit entsteht, werden die einzelnen Auslieferungen zu Packstücken bzw. Handling Units zusammengefasst – kundengenau getrennt, damit auf dem LKW später klar ist, welches Paket zu welchem Stopp gehört.
- **Freight Unit Builder:** Aus diesen Packstücken werden automatisch Frachteinheiten gebildet und für die Multi-Stop-Tour in der richtigen Reihenfolge zusammengestellt – der Kunde, der zuerst angefahren wird, muss auf dem LKW zuletzt beladen sein, damit beim ersten Stopp nicht die ganze Ladung umgeladen werden muss.
- **Yard Management:** Auf dem Werksgelände habe ich zusätzlich die Steuerung der LKWs auf dem Hof verantwortet – Andockzeiten an den Toren so getaktet, dass die Beladereihenfolge für die Multi-Stop-Touren auch tatsächlich eingehalten werden konnte.

Das Ergebnis war ein robuster, standardisierter Multi-Stop-Prozess, der unabhängig von den politischen Diskussionen um Requirements aus Quality, Production, Sales und Einkauf sauber funktioniert hat – genau der Beweis, dass man auch in einem governance-technisch schwierigen Projekt fachlich und technisch sauber liefern kann, wenn man den eigenen Verantwortungsbereich klar abgrenzt.

**Ergebnis / Lehre daraus**

Die wichtigste Erkenntnis aus diesem Projekt: Governance und klare Verantwortlichkeiten zwischen Kunde und Implementierungspartner sind die absolute Grundvoraussetzung, bevor man überhaupt mit der Umsetzung beginnt – sonst wird aus fachlicher Exzellenz auf Produktebene keine funktionierende IT-Transformation. Seit diesem Projekt übernehme ich GPO-Positionen nicht mehr leichtfertig freiwillig, sondern konzentriere mich auf die Themen, wo ich konkret und nachweisbar liefern kann. Genau das macht mir Mut für Miele: Hier ist die Rollenverteilung zwischen Miele und NTT von Anfang an klar geregelt, und NTT übernimmt bewusst Ownership statt nur zu beraten – das war bei Stihl damals genau der fehlende Baustein.

---

*(≈ 480 Wörter / ca. 4 Minuten in normalem Sprechtempo – im Rahmen der angestrebten 5–6 Minuten.)*
