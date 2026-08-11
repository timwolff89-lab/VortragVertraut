# Vertraut — Firmenplattform (Betreuungsdienst Köln/NRW)

Interne, statische Firmenplattform: bündelt den gesamten Aufbaustand des Betreuungsdienstes,
die GAP-Analyse, die offenen Punkte und 33 Fachdokumente als druckbare Seiten.

> Arbeitstitel „Vertraut" (Markenname austauschbar). Stand: August 2026.
> Alle Rechts-/Steuer-/Regulatorik-Angaben ohne Gewähr — vor Umsetzung fachlich prüfen.

---

## 🚀 Live stellen — drei Wege

### Weg A — am schnellsten (ohne GitHub, ~1 Minute)
1. ZIP entpacken.
2. Auf **https://vercel.com/new** gehen → Reiter **„Deploy"** / **„Browse"**.
3. Den entpackten Ordner **`vertraut-site`** per Drag & Drop hineinziehen.
4. **Deploy** klicken → fertig, du bekommst eine `…vercel.app`-URL.

*(Kein Framework, kein Build-Schritt nötig — es ist eine reine statische Seite.)*

### Weg B — über GitHub (für dauerhaftes Repo + Auto-Deploys)
1. Neues Repo auf **github.com/new** anlegen (z. B. `vertraut-plattform`).
2. Auf der Repo-Seite **„uploading an existing file"** klicken und den **Inhalt** des entpackten
   Ordners hochladen (alle `.html`, den Ordner `dokumente/`, `assets/`, `vercel.json`).
   *Oder per Git:* `git init && git add . && git commit -m "Vertraut" && git push`.
3. Auf **vercel.com/new** das GitHub-Repo importieren → **Deploy**.
4. Ab jetzt löst jeder Push automatisch ein neues Deployment aus.

### Weg C — Vercel CLI
```bash
npm i -g vercel
cd vertraut-site
vercel --prod
```

---

## Struktur
```
index.html            Übersicht / Cockpit
strategie.html …      8 Abteilungsseiten (Strategie, Gründung, Anerkennung,
                      Personal, Finanzen, IT, Vertrieb, Betrieb)
gap-analyse.html      GAP-Analyse (Soll-Ist)
was-fehlt.html        Priorisierte Liste offener Unterlagen
dokumente.html        Dokumentenbibliothek
dokumente/*.html      33 Fachdokumente (druckbar / als PDF speicherbar)
assets/style.css      Design-System
assets/app.js         Navigation, Renderer, Interaktivität
_content/             Quelltexte (Markdown-Dokumente + Seiten-Fragmente)
build.py              Baut alle Seiten neu (python3 build.py)
```

## Neu bauen (optional)
```bash
pip install markdown --break-system-packages   # nur falls Quellen geändert werden
python3 build.py
```

Marke, Farben und Texte lassen sich zentral anpassen: `assets/style.css` (Farben),
`assets/app.js` (Navigation/Branding), `_content/` (Inhalte) → danach `python3 build.py`.
