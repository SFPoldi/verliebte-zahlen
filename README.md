# Verliebte Zahlen

Lern-App für Grundschulkinder: Finde Zahlen, die zusammen 10 ergeben ("verliebte Zahlen", 3 + 7) oder gleich sind ("Zwillinge", 4 und 4).
Reine Web-App, ein HTML-File, kein Build, keine Werbung, keine Server-Anbindung. Läuft auf Android, iOS und Desktop.

## Spielregeln
- Zwei Zahlen bilden ein Paar, wenn sie gleich sind oder zusammen 10 ergeben.
- Sie müssen waagerecht, senkrecht oder schräg nebeneinander liegen. Leere Felder dazwischen sind erlaubt.
- Zeilenende und nächster Zeilenanfang zählen als Nachbarn.
- "Mehr Zahlen" hängt alle übrigen Zahlen hinten an (begrenzte Anzahl pro Runde).
- Das Spiel zeigt beim Fehlversuch die Summe ("3 + 5 = 8. Das sind nicht 10.").

## Stufen
Immer Ziffern 1 bis 9. Die Stufen unterscheiden sich in Menge, "Mehr Zahlen"-Chancen und Verteilung.

| Stufe | Zahlen | Zeilen | Mehr Zahlen | Verteilung |
|---|---|---|---|---|
| Leicht | 27 | 3 | 6 | Partner liegen paarweise nebeneinander |
| Mittel | 36 | 4 | 4 | reiner Zufall |
| Schwer | 54 | 6 | 3 | Zufall, dann so lange umgewürfelt, bis höchstens 24 Paare sichtbar sind |

Werte stehen als Konstanten (`LEVELS`) oben im Script in `index.html`.

## Punkte
| Ereignis | Punkte |
|---|---|
| Paar gefunden | +10 |
| Zeile komplett geleert | +25 pro Zeile |
| Ganzes Feld geleert | +100 |
| Tipp (zeigt ein Paar) | -5 |
| Tipp, der nur auf "Mehr Zahlen" zeigt (kein Paar mehr) | kostenlos |

Tipps sind unbegrenzt. Der Punktestand fällt nie unter 0. "Zurück" nimmt Tipp-Abzüge nicht zurück.
Der Rekord wird pro Stufe gespeichert.

## Speicherung
Vorname (Standard "Superstar"), Rekorde und die laufende Runde liegen im `localStorage` des Browsers.
Es wird nichts an einen Server gesendet und kein Cookie gesetzt. Die Daten gelten pro Gerät und Browser
und gehen verloren, wenn Website-Daten gelöscht werden.

## Hosting
- **Wix (aktuelle Seite):** siehe [docs/WIX.md](docs/WIX.md), mit Schritt-für-Schritt-Anleitung für Button, Einbetten und Code-Einfügen.
- **Neue Next.js-Seite:** siehe [docs/UEBERGABE.md](docs/UEBERGABE.md), für die Agentur.
- Fertige Einzeldatei zum Einfügen in Wix: `wix/embed.html` (neu erzeugen mit `python3 tools/build-wix-embed.py`).

## Installieren
Android (Chrome): Menü, "App installieren". iOS (Safari): Teilen, "Zum Home-Bildschirm". Nur im eigenen Fenster, nicht eingebettet.

## Updates
Nach Änderungen die Cache-Version in `sw.js` (`verliebte-zahlen-v3`) hochzählen.

## Design
Markenfarben: Gold `#FFC82B`, Blau `#0B567B`, Creme `#FBFAF1`.
Schrift: Nunito (SIL Open Font License), lokal eingebunden, keine Anfrage an Google. Die Ziffern ähneln der Schulschrift (4 oben geschlossen, 1 mit Haken, 7 ohne Querstrich).
Logo der Mathe-Flüsterin in `img/` (`logo.png` vollständig, `logo-kopf.png` ohne Schriftzug für die Kopfzeile).
