# Verliebte Zahlen auf der Wix-Seite einbauen

Stand: Wix-Details stammen aus der Wix-Hilfe. Menünamen können je nach Editor (Wix Editor oder Studio Editor) leicht abweichen.

## Was du wissen musst
- Wix bettet fremde Inhalte in einen **festen Rahmen (iFrame)** ein. Der Rahmen ist **nicht responsiv**, hat also eine feste Größe pro Ansicht (Desktop und Handy getrennt einstellen).
- Nur **https**-Adressen werden angezeigt.
- **Safari (iPhone, iPad, Mac) speichert Daten in eingebetteten Rahmen nur flüchtig**, gelöscht beim Beenden des Browsers. Vorname und Rekorde gehen dort verloren. Das Spiel läuft trotzdem, und im Rahmen erscheint dann automatisch der Link "Im eigenen Fenster öffnen".
- "Als App installieren" und der Offline-Modus gehen nur, wenn das Spiel **in einem eigenen Fenster** läuft, nicht im Rahmen.

## Die drei Wege im Vergleich

| | A: Button/Link (empfohlen) | B: Einbetten per Adresse | C: Code einfügen |
|---|---|---|---|
| Rekorde und Name gespeichert | ja, überall | Chrome ja, Safari nur flüchtig | wie B |
| Als App installierbar, offline | ja | nein | nein |
| Sieht aus wie Teil der Seite | nein (öffnet eigenes Fenster) | ja | ja |
| Braucht Hosting außerhalb von Wix | ja (GitHub Pages) | ja (GitHub Pages) | nein |
| Update | automatisch | automatisch | Code neu einfügen |

**Empfehlung:** A als Hauptweg, dazu optional B auf derselben Seite. Dann sehen alle das Spiel, und wer es speichern will, öffnet es im eigenen Fenster.

## Schritt 0: Spiel auf GitHub Pages veröffentlichen (für A und B)
1. Auf github.com das Repo `SFPoldi/verliebte-zahlen` öffnen, **Settings**, **Pages**.
2. Unter "Build and deployment" bei **Source** "Deploy from a branch" wählen, Branch **main**, Ordner **/ (root)**, **Save**.
3. Nach 1 bis 2 Minuten steht oben die Adresse: `https://sfpoldi.github.io/verliebte-zahlen/`
4. Im Browser öffnen und prüfen, dass das Spiel startet.

Das Repo ist öffentlich, deshalb ist Pages kostenlos. Der Code ist dann für alle lesbar. Er enthält keine Zugangsdaten.

## Weg A: Button auf der Wix-Seite
1. Seite bearbeiten, **Hinzufügen**, **Button**.
2. Beschriftung z. B. "Spiel starten".
3. Link: **Webadresse**, `https://sfpoldi.github.io/verliebte-zahlen/` eintragen, **In neuem Tab öffnen** aktivieren.
4. Veröffentlichen.

Kindern auf dem Handy kann man erklären: Im Spiel Teilen/Menü, "Zum Home-Bildschirm". Dann ist es eine App.

## Weg B: Einbetten per Adresse
1. Seite bearbeiten, **Hinzufügen**, **Einbetten** (Embed Code), **HTML-iFrame** wählen.
2. **Webadresse eingeben**, `https://sfpoldi.github.io/verliebte-zahlen/` eintragen.
3. Größe festlegen:
   - Desktop: Breite 480 bis 520 px (das Spiel zentriert sich selbst), Höhe etwa 800 px.
   - Handy: Handy-Ansicht des Editors öffnen und das Element einzeln anpassen, Breite volle Bildschirmbreite, Höhe etwa 720 bis 780 px. Wix-Elemente haben getrennte Größen für Desktop und Handy.
4. Direkt darunter einen Textlink oder Button wie bei Weg A setzen, damit Safari-Nutzer speichern können.
5. Auf einem echten Handy testen. Bildet sich unten eine zweite Scrollleiste, die Höhe ein paar Pixel reduzieren oder erhöhen.

Hinweis aus der Wix-Hilfe: Seiten, die das Einbetten verbieten, erscheinen nicht. Bei GitHub Pages ist das nicht der Fall.

## Weg C: Code direkt einfügen (ohne GitHub Pages)
1. Datei `wix/embed.html` aus diesem Repo öffnen und den gesamten Inhalt kopieren. Die Datei ist komplett eigenständig (Schrift ist eingebaut).
2. In Wix **Hinzufügen**, **Einbetten**, **HTML-iFrame**, **Code eingeben**, Inhalt einfügen, **Übernehmen**.
3. Größe wie bei Weg B.

Bei Updates den Code neu einfügen. Den "Im eigenen Fenster öffnen"-Link füllt `PLAY_URL` in `index.html`. Ohne GitHub Pages zeigt er ins Leere, dann ist Weg C nicht zu empfehlen.

## Optional: schöne Adresse spiel.diemathefluesterin.net
Statt `sfpoldi.github.io/...` kann das Spiel unter einer eigenen Unterdomain laufen.
1. GitHub: Settings, Pages, **Custom domain**: `spiel.diemathefluesterin.net`, speichern. Haken **Enforce HTTPS** setzen, sobald er auswählbar ist.
2. Wix: **Domains**, bei `diemathefluesterin.net` **DNS-Einträge verwalten**, bei **CNAME** neuen Eintrag: Host `spiel`, Wert `sfpoldi.github.io` (ohne Repo-Namen, so verlangt es GitHub).
3. In `index.html` die Konstante `PLAY_URL` auf `https://spiel.diemathefluesterin.net/` ändern, `python3 tools/build-wix-embed.py` ausführen, committen.
4. Wartezeit bis zur Gültigkeit der DNS-Änderung: Minuten bis Stunden.

Ist die Domain nicht bei Wix registriert, den CNAME beim jeweiligen Anbieter eintragen.

## Testliste nach dem Einbau
- [ ] iPhone (Safari): Seite lädt, Spiel startet, Button öffnet eigenes Fenster
- [ ] Android (Chrome): dasselbe, dazu "App installieren"
- [ ] Im eigenen Fenster: Namen eingeben, Runde spielen, Browser schließen, wieder öffnen: Name und Rekord sind noch da
- [ ] Flugmodus nach erstem Laden (nur eigenes Fenster): Spiel startet weiter
- [ ] Wix-Handy-Ansicht: kein abgeschnittenes Spielfeld, keine zweite Scrollleiste

## Quellen
- [Wix: Eine Seite oder ein Widget einbetten](https://support.wix.com/en/article/adding-html-code)
- [Wix: Subdomain mit externer Ressource verbinden](https://support.wix.com/en/article/connecting-a-subdomain-to-an-external-resource)
- [GitHub: Custom Domain für Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [WebKit: Storage Access API](https://www.webkit.org/blog/8124/introducing-storage-access-api)
