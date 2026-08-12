# Vertraut — Firmenplattform (Betreuungsdienst Köln/NRW)

Interne, **passwortgeschützte** Firmenplattform: bündelt den gesamten Aufbaustand des
Betreuungsdienstes, die GAP-Analyse, die offenen Punkte und 39 Fachdokumente.

> Arbeitstitel „Vertraut" (Markenname austauschbar). Stand: August 2026.
> Alle Rechts-/Steuer-/Regulatorik-Angaben ohne Gewähr — vor Umsetzung fachlich prüfen.

---

## 🔒 Passwortschutz (nur fürs Team)

Die Seite ist serverseitig geschützt (Vercel-Middleware, `middleware.js`). Ohne Login
liefert der Server **nichts** aus — die Seite ist damit nicht öffentlich zugänglich.

**Standard-Login (unbedingt ändern):**
- Benutzer: `team`
- Passwort: `Vertraut!2026`

**Passwort ändern — zwei Wege:**
- **Empfohlen:** In Vercel unter *Settings → Environment Variables* die Variablen
  `SITE_USER` und `SITE_PASSWORD` setzen → dann steht das Passwort nicht im Code.
- **Einfach:** In `middleware.js` die beiden Default-Werte ersetzen und neu deployen.

---

## 🚀 Online stellen — über GitHub (empfohlen, weil geschützt)

1. Neues Repo auf **github.com/new** anlegen (am besten **privat**).
2. Den **Inhalt** dieses Ordners hochladen (alle `.html`, `dokumente/`, `assets/`,
   `middleware.js`, `package.json`, `vercel.json`).
   *Oder per Git:* `git init && git add . && git commit -m "Vertraut" && git push`.
3. Auf **vercel.com/new** das Repo importieren. Einstellungen:
   - **Framework Preset:** „Other"
   - **Build Command / Output Directory:** leer lassen (Standard)
   - Vercel installiert automatisch die Middleware-Abhängigkeit und aktiviert den Schutz.
4. **Deploy** → beim Öffnen der `…vercel.app`-URL fragt der Browser nach Benutzer + Passwort.
5. Optional: unter *Settings → Environment Variables* `SITE_USER` / `SITE_PASSWORD` setzen.

> Hinweis: Der Drag-&-Drop-Upload ohne GitHub eignet sich nur für die **ungeschützte**
> Variante — der Passwortschutz braucht den Install-Schritt, den der GitHub-Import macht.

**Alternativen zum Passwortschutz (falls gewünscht):** In Vercel unter
*Settings → Deployment Protection* gibt es „Vercel Authentication" (kostenlos, aber alle
Betrachter brauchen einen Vercel-Account) und „Password Protection" (nur im Pro-Plan).

---

## Struktur
```
index.html            Übersicht / Cockpit
strategie.html …      8 Abteilungsseiten
gap-analyse.html      GAP-Analyse (Soll-Ist)
was-fehlt.html        Priorisierte Liste offener Unterlagen
dokumente.html        Dokumentenbibliothek
dokumente/*.html      39 Fachdokumente (druckbar / als PDF)
Finanzplan_Vertraut.xlsx   Editierbarer Finanzplan
assets/               Design-System + Interaktivität
middleware.js         Passwortschutz (serverseitig)
package.json          Middleware-Abhängigkeit
_content/             Quelltexte · build.py  Baut die Seiten neu
```

---

## ⚖️ Kurz zum rechtlichen Hintergrund (keine Rechtsberatung)
Diese Plattform ist ein **internes** Firmen-Cockpit, nicht die öffentliche Kundenseite.
Solange sie **passwortgeschützt** und damit nicht öffentlich zugänglich ist, entfällt der
typische Abmahn-Vektor „öffentliche Seite ohne korrektes Impressum/Datenschutz". Sobald
später eine **öffentliche** Kundenseite online geht, müssen dort ein korrektes Impressum
und eine Datenschutzerklärung eingebunden sein — beide liegen als Entwurf in `dokumente/`.
Im Zweifel kurz anwaltlich prüfen lassen.
