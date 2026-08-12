// Passwortschutz für die interne Vertraut-Plattform (Vercel Routing Middleware).
// Nur wer Benutzername + Passwort kennt, sieht die Seite. Serverseitig — nicht per
// Dev-Tools umgehbar (der Server liefert nichts aus, bevor das Passwort stimmt).
//
// PASSWORT ÄNDERN — zwei Wege:
//   (A) Empfohlen: in Vercel unter Settings → Environment Variables die Variablen
//       SITE_USER und SITE_PASSWORD setzen. Dann NICHT im Code sichtbar.
//   (B) Einfach: unten die beiden Default-Werte ersetzen und neu deployen.

import { next } from '@vercel/functions';

const USER = process.env.SITE_USER || 'team';
const PASSWORD = process.env.SITE_PASSWORD || 'Vertraut!2026';

export default function middleware(request) {
  const header = request.headers.get('authorization') || '';
  const [scheme, encoded] = header.split(' ');

  if (scheme === 'Basic' && encoded) {
    let decoded = '';
    try { decoded = atob(encoded); } catch (_) { decoded = ''; }
    const sep = decoded.indexOf(':');
    const user = decoded.slice(0, sep);
    const pass = decoded.slice(sep + 1);
    if (user === USER && pass === PASSWORD) {
      return next(); // korrekt → Seite ausliefern
    }
  }

  return new Response('Zugang nur für das Team von Vertraut.', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="Vertraut - nur Team", charset="UTF-8"',
      'Content-Type': 'text/plain; charset=utf-8',
    },
  });
}
