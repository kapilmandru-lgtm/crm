# Mandrudi CRM

## Lokal auf allen Macs (Mandrudi-OneDrive)

Die App ist eine einzige Datei (`index.html`) und läuft ohne Server und ohne Cloud-Konto. Die Daten liegen in **einem Ordner im Mandrudi-OneDrive** (z. B. `CRM-Daten`), den alle Macs gemeinsam nutzen.

**Einrichten (pro Mac, einmalig)**
1. `index.html` in den Mandrudi-OneDrive legen (z. B. `OneDrive - Mandrudi/CRM/`) und in **Chrome oder Edge** öffnen — Safari kann keine Dateien direkt speichern.
2. „OneDrive-Ordner wählen“ → auf dem ersten Mac einen leeren Ordner `CRM-Daten` anlegen und wählen, auf allen weiteren Macs **denselben** Ordner wählen.
3. Im Finder für den Ordner „Immer auf diesem Gerät behalten“ einstellen, damit die Daten auch offline da sind.

Beim nächsten Start reicht ein Klick auf „Weiter mit CRM-Daten“ (Chrome fragt ggf. einmal nach der Erlaubnis).

**Wie die Macs zusammenarbeiten:** Jeder Mac (genauer: jeder Browser) schreibt nur seine eigene Datei `geraet-<id>.json` in den Ordner und liest die Dateien der anderen — so kann OneDrive nie einen Schreibkonflikt bekommen. Änderungen der anderen Macs kommen automatisch an (alle 15 s und beim Zurückkehren ins Fenster), sobald OneDrive sie synchronisiert hat. Ändern zwei Macs denselben Datensatz, gewinnt die neuere Änderung; Löschungen werden ebenfalls übernommen. Die `geraet-*.json`-Dateien bitte nicht von Hand ändern oder löschen.

**Alte Cloud-Daten übertragen (einmalig, auf einem Mac):** Startbildschirm → „Alte Cloud-Daten übertragen (Login)“ → anmelden → unten links „In OneDrive übertragen…“ → Ordner `CRM-Daten` wählen. Danach arbeitet die App nur noch lokal.

**DokuApp-Dokumente verknüpfen:** In einem Deal oder einer Firma „📎 Dokument verknüpfen“. Beim ersten Mal wird der Dokumente-Ordner der DokuApp im Mandrudi-OneDrive gewählt; gespeichert wird nur der Pfad relativ zu diesem Ordner, so öffnet jeder Mac das Dokument aus seinem eigenen OneDrive.

**Backup:** „Export“ → „Vollständiges Backup (JSON)“ enthält alle Projekte; einspielen über „OneDrive-Ordner…“ → „JSON-Backup einlesen“.

**Hinweis Outlook-Import:** Der Microsoft-Login funktioniert nicht, wenn `index.html` direkt geöffnet wird (`file://`). Dafür die App über die Web-Adresse oder `http://localhost` öffnen — die Daten bleiben trotzdem im OneDrive-Ordner.
