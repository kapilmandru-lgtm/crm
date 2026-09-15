# Architektur-Analyse: TM dezentral vs. embedded

Vorbereitete Pro-/Contra-Liste, wie von Mario Keller (NTT) im [Gespräch vom 14.09.2026](./2026-09-14-NTT-Gespraech-2-Miele-Vorbereitung.md) angefragt: "Ich kann so eine Analyse machen, was mir Sinn machen würde, mit Pros und Contras … eine 3–5-punktige Pro-und-Contra-Liste." Wichtig laut Keller: **nicht als eigene Entscheidung darstellen** – die Architekturentscheidung trifft der Kunde/Implementierungspartner, hier wird nur eine fundierte Abwägung angeboten.

## Ausgangsposition

Der Kunde hat bereits ein **dezentrales EWM** (separates System vom ERP, Side-by-Side) und möchte konsequent auch ein **dezentrales TM** (Transportation Management ebenfalls als separates System, statt embedded im S/4-ERP).

## TM dezentral (Side-by-Side)

**Vorteile**

- **Konsistente Architektur:** Passt zum bereits bestehenden dezentralen EWM – ein einheitliches Integrationsmuster (ERP ↔ separate Logistiksysteme) statt eines Mischbetriebs aus embedded und side-by-side.
- **Entkopplung/Stabilität:** Ein Problem oder eine hohe Last im TM (z. B. Optimizer-Läufe, Routenberechnung) zieht das ERP-System nicht mit runter – analog zur Begründung für das dezentrale EWM.
- **Unabhängige Releases/Upgrades:** TM kann eigenständig gepatcht, erweitert oder skaliert werden, ohne an den ERP-Upgrade-Zyklus gebunden zu sein.
- **Skalierbarkeit:** Bei hohem Transportvolumen/vielen Touren lässt sich TM unabhängig vom ERP skalieren (eigene Ressourcen, eigene Performance-Optimierung).
- **Gleiches Betriebsmodell wie EWM:** Support-, Monitoring- und Integrationsteam kann dieselben Prozesse/Skills für EWM und TM nutzen, statt zwei unterschiedliche Architekturmuster zu betreiben.

**Nachteile**

- **Zusätzliche Integrationskomplexität:** Stammdaten (Geschäftspartner, Standorte, Beförderungsmittel) müssen zwischen ERP und TM synchron gehalten werden (EDI/API), inklusive Fehleranfälligkeit bei der Synchronisation.
- **Höherer Betriebsaufwand/TCO:** Ein zusätzliches System bedeutet eigene Infrastruktur, eigene Wartung, eigene Basis-Tätigkeiten.
- **Latenz bei Prozessen:** Ereignisse aus dem ERP (z. B. Lieferungserstellung) müssen erst an TM übertragen werden, bevor eine Frachteinheit entsteht – keine echte Echtzeit-Konsistenz wie bei embedded.
- **Höherer Testaufwand:** Wie beim dezentralen EWM gilt – bevor beide Systeme mit validen Stammdaten gefüllt sind, lassen sich Schnittstellen nicht belastbar testen (siehe Erfahrungswert aus dem Erstinterview).
- **Getrenntes Berechtigungskonzept:** Nutzer- und Rollenverwaltung muss in zwei Systemen gepflegt werden.

## TM embedded (im S/4-ERP)

**Vorteile**

- **Einfachere Landschaft:** Ein System statt zwei – Stammdaten sind nativ gemeinsam nutzbar, keine Replikation nötig.
- **Echtzeit-Konsistenz:** TM greift direkt auf ERP-Objekte zu (z. B. Lieferungen, Aufträge), keine Integrationsverzögerung.
- **Geringerer Betriebsaufwand:** Ein System zu patchen/warten/hosten senkt die Gesamtbetriebskosten gegenüber einer Side-by-Side-Lösung.
- **Einfacheres Berechtigungskonzept:** Ein einheitliches Rollen-/User-Management für ERP und TM.
- **Schnellerer Time-to-Value:** Für überschaubare Transportnetz-Komplexität oft die pragmatischere, schneller umsetzbare Lösung.

**Nachteile**

- **Kopplungsrisiko:** Eine hohe Last im TM (z. B. Optimizer-Lauf) kann die Performance/Stabilität des produktiven ERP-Systems beeinträchtigen – genau das Argument, mit dem der Kunde sich beim EWM bereits für dezentral entschieden hat.
- **Gemeinsamer Release-Zyklus:** TM und ERP lassen sich nicht unabhängig voneinander upgraden/patchen.
- **Architektonischer Bruch:** Da EWM bereits dezentral läuft, entstünde mit embedded TM ein **Mischbetrieb aus zwei Integrationsmustern** – in Summe eher mehr als weniger architektonische Komplexität, trotz der pro System einfacheren TM-Anbindung.
- **Eingeschränkte Skalierbarkeit:** TM teilt sich die Systemressourcen mit dem ERP – bei sehr hohem Transportvolumen ein Risiko.
- **Schwerer nachträglich zu entkoppeln:** Wächst der Bedarf später, ist ein nachträglicher Wechsel auf eine dezentrale TM-Lösung aufwändiger, als von Anfang an dezentral zu planen.

## Fazit / Gesprächsleitfaden für Miele

Gegeben, dass der Kunde EWM bereits bewusst dezentral aufgesetzt hat (Begründung: Entkopplung von ERP), spricht die **Konsistenz des Architekturmusters** stark für ein ebenfalls dezentrales TM – die Nachteile (Integrationsaufwand, Testaufwand) sind bereits aus dem EWM-Projekt bekannt und können mit denselben Methoden adressiert werden. Embedded TM wäre nur dann die bessere Wahl, wenn Transportvolumen und Systemlandschaft bewusst schlank gehalten werden sollen und die Kopplungsrisiken zum ERP als akzeptabel bewertet werden.
