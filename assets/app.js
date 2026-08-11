// Vertraut — gemeinsame Shell: Navigation, Footer, Dokument-Chrome, Markdown-Renderer, Reveal
(function () {
  document.body.classList.add('js');
  var B = document.body;
  var prefix = B.getAttribute('data-prefix') || '';
  var active = B.getAttribute('data-active') || '';

  var DEPTS = [
    ['strategie', 'Strategie & Markt'], ['gruendung', 'Gründung & Recht'],
    ['anerkennung', 'Anerkennung & Qualität'], ['personal', 'Personal & Recruiting'],
    ['finanzen', 'Finanzen & Preis'], ['it-plattform', 'IT, Plattform & App'],
    ['vertrieb', 'Vertrieb & Marke'], ['betrieb', 'Betrieb & Kundenprozess']
  ];
  var TOP = [['index', 'Übersicht'], ['gap-analyse', 'GAP-Analyse'], ['was-fehlt', 'Was fehlt'], ['dokumente', 'Dokumente']];
  var DEPT_MAP = {}; DEPTS.forEach(function (d) { DEPT_MAP[d[0]] = d[1]; });

  function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

  function navHTML() {
    var dd = DEPTS.map(function (d) {
      return '<a class="dditem' + (active === d[0] ? ' active' : '') + '" href="' + prefix + d[0] + '.html">' + d[1] + '</a>';
    }).join('');
    function top(s, l) { return '<a class="link' + (active === s ? ' active' : '') + '" href="' + prefix + s + '.html">' + l + '</a>'; }
    var ddopen = DEPT_MAP[active] ? ' active' : '';
    return '<header class="nav"><a class="brand" href="' + prefix + 'index.html">Ver<b>traut</b><small>Betreuung Köln · NRW</small></a>' +
      '<button class="burger" aria-label="Menü" onclick="document.getElementById(\'m\').classList.toggle(\'open\')">☰</button>' +
      '<ul id="m">' + top('index', 'Übersicht') +
      '<li class="dd"><button class="link ddtoggle' + ddopen + '" onclick="this.parentNode.classList.toggle(\'open\')">Abteilungen ▾</button>' +
      '<div class="ddmenu">' + dd + '</div></li>' +
      top('gap-analyse', 'GAP-Analyse') + top('was-fehlt', 'Was fehlt') + top('dokumente', 'Dokumente') + '</ul></header>';
  }
  function footHTML() {
    return '<footer><div class="wrap"><div><div class="fbrand">Vertraut</div>' +
      '<div style="color:var(--muted2);font-size:12.5px;margin-top:4px">Betreuungsdienst Köln / NRW · interne Firmenplattform</div></div>' +
      '<div class="fmeta">Arbeitsstand August 2026 · Markenname Arbeitstitel<br>Rechts-/Steuer-/Regulatorik-Angaben ohne Gewähr — vor Umsetzung fachlich prüfen</div></div></footer>';
  }

  // ---- Mini Markdown Renderer (für die kontrollierten Fachdokumente) ----
  function inline(t) {
    t = esc(t);
    t = t.replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2">$1</a>');
    t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    t = t.replace(/`([^`]+)`/g, '<code>$1</code>');
    t = t.replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<em>$2</em>');
    return t;
  }
  function md2html(src) {
    var lines = src.replace(/\r/g, '').split('\n');
    var out = [], i = 0;
    function flushP(buf) { if (buf.length) { out.push('<p>' + inline(buf.join(' ')) + '</p>'); } }
    var para = [];
    while (i < lines.length) {
      var l = lines[i];
      if (/^\s*$/.test(l)) { flushP(para); para = []; i++; continue; }
      var h = l.match(/^(#{1,6})\s+(.*)$/);
      if (h) { flushP(para); para = []; out.push('<h' + h[1].length + '>' + inline(h[2]) + '</h' + h[1].length + '>'); i++; continue; }
      if (/^\s*[-*]\s+/.test(l) && !/^\s*[-*]\s*$/.test(l)) {
        flushP(para); para = []; var items = [];
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) { items.push('<li>' + inline(lines[i].replace(/^\s*[-*]\s+/, '')) + '</li>'); i++; }
        out.push('<ul>' + items.join('') + '</ul>'); continue;
      }
      if (/^\s*\d+\.\s+/.test(l)) {
        flushP(para); para = []; var oi = [];
        while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) { oi.push('<li>' + inline(lines[i].replace(/^\s*\d+\.\s+/, '')) + '</li>'); i++; }
        out.push('<ol>' + oi.join('') + '</ol>'); continue;
      }
      if (/^\|(.+)\|\s*$/.test(l) && i + 1 < lines.length && /^\|[\s:|-]+\|\s*$/.test(lines[i + 1])) {
        flushP(para); para = [];
        function cells(row) { return row.replace(/^\||\|\s*$/g, '').split('|').map(function (c) { return c.trim(); }); }
        var head = cells(l); i += 2; var rows = [];
        while (i < lines.length && /^\|(.+)\|\s*$/.test(lines[i])) { rows.push(cells(lines[i])); i++; }
        var th = '<tr>' + head.map(function (c) { return '<th>' + inline(c) + '</th>'; }).join('') + '</tr>';
        var tb = rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>'; }).join('');
        out.push('<table>' + th + tb + '</table>'); continue;
      }
      if (/^\s*>\s?/.test(l)) { flushP(para); para = []; var q = []; while (i < lines.length && /^\s*>\s?/.test(lines[i])) { q.push(inline(lines[i].replace(/^\s*>\s?/, ''))); i++; } out.push('<blockquote>' + q.join(' ') + '</blockquote>'); continue; }
      if (/^\s*(---|___|\*\*\*)\s*$/.test(l)) { flushP(para); para = []; out.push('<hr>'); i++; continue; }
      para.push(l.trim()); i++;
    }
    flushP(para);
    return out.join('\n');
  }

  // ---- Inject shell ----
  if (B.classList.contains('doc')) {
    var d = B.dataset;
    var mdEl = document.getElementById('md');
    var body = mdEl ? md2html(mdEl.textContent) : '';
    var warn = d.status === 'extern'
      ? '<div class="callout warn" style="margin:0 auto 26px;max-width:820px">⚠︎ <b>Entwurf.</b> Vor Verwendung fachlich prüfen lassen (Anwalt, Steuerberater bzw. Stadt Köln). Kein Ersatz für Rechts-/Steuerberatung.</div>'
      : '';
    var docnav = '<div class="docnav"><a class="brand" href="' + prefix + 'index.html">Ver<b>traut</b></a>' +
      '<div class="actions"><a href="' + prefix + 'dokumente.html">← Alle Dokumente</a>' +
      '<a href="' + prefix + d.dept + '.html">' + (DEPT_MAP[d.dept] || '') + '</a>' +
      '<a href="#" onclick="window.print();return false;">Drucken / PDF</a></div></div>';
    var paper = '<div class="paper"><div class="dochead"><span class="doctype">' + esc(d.typ) + ' · ' + esc(d.prio) + '</span>' +
      '<div class="docbrand">Ver<b>traut</b><small>Betreuung Köln · NRW</small></div>' +
      '<h1 class="dt">' + esc(d.title) + '</h1><div class="dsub">' + esc(d.teaser) + '</div>' +
      '<div class="meta-row"><span>Abteilung: <b>' + (DEPT_MAP[d.dept] || '') + '</b></span><span>Stand: <b>August 2026</b></span><span>Status: <b>Entwurf</b></span></div></div>' +
      warn + '<div class="prose">' + body + '</div></div>' +
      '<div class="docfoot">Vertraut · Betreuungsdienst Köln/NRW · interner Arbeitsstand August 2026 (Arbeitstitel). Angaben ohne Gewähr; regulatorische, rechtliche und steuerliche Punkte vor Umsetzung fachlich prüfen lassen.</div>';
    B.insertAdjacentHTML('afterbegin', docnav);
    B.insertAdjacentHTML('beforeend', paper);
  } else {
    B.insertAdjacentHTML('afterbegin', navHTML());
    B.insertAdjacentHTML('beforeend', footHTML());
  }

  // ---- Reveal ----
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) e.target.classList.add('in'); }); }, { threshold: .12 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.dd')) document.querySelectorAll('.dd.open').forEach(function (d) { d.classList.remove('open'); }); });
})();
