# Übergabe an die Agentur (neue Next.js-Seite)

Verliebte Zahlen ist eine **statische Web-App ohne Build**. Kein Framework, keine Abhängigkeiten, kein Backend.

## Was einzubauen ist
Den Repo-Inhalt (ohne `docs/`, `wix/`, `tools/`, `.git`) als Ordner `verliebte-zahlen/` ausliefern:

```
index.html   manifest.webmanifest   sw.js
icon.svg   icon-192.png   icon-512.png   apple-touch-icon.png
fonts/baloo2-latin.woff2   fonts/OFL.txt
img/logo.png   img/logo-kopf.png
```

## Next.js
- Ordner nach `public/verliebte-zahlen/` kopieren. Next.js liefert `public/` statisch aus, **aber nicht automatisch `index.html` eines Unterordners.** Aufruf daher `/verliebte-zahlen/index.html`, oder für die kurze URL einen **Redirect** (kein Rewrite, sonst brechen die relativen Pfade):
  ```js
  // next.config.js
  async redirects() {
    return [{ source: '/verliebte-zahlen', destination: '/verliebte-zahlen/index.html', permanent: false }];
  }
  ```
- Alle Pfade im Spiel sind relativ. Das Spiel funktioniert in jedem Unterpfad.
- Das Spiel soll **nicht** in React umgeschrieben werden. Es als eigenständige Seite oder per Link/iFrame einbinden.

## Server-Header
- `sw.js` und `index.html` mit `Cache-Control: no-cache` ausliefern, damit Updates ankommen. Alles andere darf lang gecacht werden.
- `sw.js` braucht keinen besonderen Header. Der Service Worker läuft nur über **https**.
- Eine Content-Security-Policy muss erlauben: `default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data:`. Es werden keine fremden Hosts kontaktiert.

## Datenschutz
- Keine externen Anfragen: Schrift ist lokal eingebunden, kein Tracking, keine Cookies, kein Server.
- Gespeichert wird im `localStorage` des Browsers: Schlüssel `verliebte-zahlen.profile.v1` (Vorname, Rekorde pro Stufe) und `verliebte-zahlen.game.v1` (laufende Runde). Der Vorname ist eine freie Eingabe von Kindern und bleibt auf dem Gerät.
- Ob und wie das in der Datenschutzerklärung stehen muss, ist rechtlich zu klären. Das ist keine Rechtsberatung.

## Einbindung in die Seite
- Bevorzugt: Eigene Seite/Link, oder iFrame mit `src="/verliebte-zahlen/index.html"` auf **derselben Domain**. Dann funktioniert die Speicherung auch in Safari, weil der Rahmen nicht "third-party" ist.
- Im iFrame erscheint automatisch ein Link "Im eigenen Fenster öffnen". Die Adresse steht als `PLAY_URL` am Anfang des Scripts in `index.html` und muss auf die endgültige Adresse zeigen.

## Anpassungen
- Farben: Variablen oben im `<style>` (`--gold`, `--blue`, `--cream`).
- Schwierigkeit und Punkte: Konstanten `LEVELS`, `PTS_*`, `HINT_COST` im Script.
- Schrift: `@font-face` im `<style>`. Eine andere Hausschrift als `.woff2` in `fonts/` legen und dort eintragen. Lizenz prüfen.
- Nach jeder Änderung in `sw.js` die Version (`verliebte-zahlen-v4`) hochzählen und neue Dateien in die Liste `FILES` aufnehmen, sonst laden installierte Apps die alte Fassung.

## Adresse und gespeicherte Daten
Das Spiel läuft aktuell unter `https://spiele.diemathefluesterin.net/verliebte-zahlen/`. Gespeicherte Daten (Name, Rekorde) hängen an dieser **Adresse** (genauer: an der Domain). Zieht das Spiel auf eine andere Domain oder Subdomain um, gehen sie verloren. Bitte die endgültige Adresse **vor** dem Livegang mit der Fachseite abstimmen. Bei einem Umzug die Konstante `PLAY_URL` in `index.html` anpassen.

## Qualität
Keine Abhängigkeiten, daher nichts zu aktualisieren. Getestet wurde in Chromium im Handyformat (komplette Runden, Speichern, Neuladen). Auf echten iOS-Geräten ist es nicht getestet, bitte dort kurz durchspielen.
