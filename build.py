#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Vertraut-Plattform in deploy-schlanker Form:
Navigation/Footer/Dokument-Chrome werden von assets/app.js injiziert;
Fachdokumente werden als kompaktes Markdown eingebettet und clientseitig gerendert."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "_content", "pages")
DOCS  = os.path.join(ROOT, "_content", "docs")
os.makedirs(os.path.join(ROOT, "dokumente"), exist_ok=True)

DEPTS = [
    ("strategie","Strategie & Markt"),("gruendung","Gründung & Recht"),
    ("anerkennung","Anerkennung & Qualität"),("personal","Personal & Recruiting"),
    ("finanzen","Finanzen & Preis"),("it-plattform","IT, Plattform & App"),
    ("vertrieb","Vertrieb & Marke"),("betrieb","Betrieb & Kundenprozess"),
]
DEPT_LABEL = dict(DEPTS)

DOCS_REG = [
 ("betreuungskonzept","Betreuungs- & Leistungskonzept (§ 45a)","anerkennung","A","Konzept","extern",
   "Einreichfähiges Kernkonzept für die AnFöVO-Anerkennung der Stadt Köln."),
 ("vertretung-beschwerde-krise","Vertretungs-, Beschwerde- & Krisenregelung","anerkennung","A","Verfahren","entwurf",
   "Pflichtbestandteil des Leistungskonzepts: Ausfall, Beschwerde, Krise."),
 ("fachkraft-kooperationsvereinbarung","Kooperationsvereinbarung verantwortliche Fachkraft","anerkennung","A","Vertrag","extern",
   "Sichert die fachliche Begleitung: häufigster Ablehnungsgrund, wenn ungeklärt."),
 ("qualitaets-jahresbericht","Qualitäts- & Jahresbericht (Vorlage)","anerkennung","C","Vorlage","entwurf",
   "Hält die Anerkennung dauerhaft: Kennzahlen und Nachweis bis 31.03."),
 ("ug-gruendungsfahrplan","UG-Gründungsfahrplan & Checkliste","gruendung","A","Leitfaden","extern",
   "Schritt für Schritt von Musterprotokoll bis BGW-Anmeldung."),
 ("gesellschafter-eckpunkte","Gesellschafter-Eckpunkte (Term Sheet)","gruendung","A","Eckpunkte","extern",
   "Cap Table, Vesting, Wandeldarlehen: Grundlage für den Anwalt."),
 ("versicherungsuebersicht","Versicherungsübersicht & Entscheidungshilfe","gruendung","A","Übersicht","extern",
   "Haftpflicht ist Anerkennungsvoraussetzung: welche Policen, welche Summen."),
 ("anforderungsprofil-betreuungskraft","Anforderungsprofil & Qualifikationsnachweis","personal","A","Profil","entwurf",
   "Für den Start: nur bereits qualifizierte Studierende: was sie mitbringen müssen."),
 ("arbeitsvertrag-werkstudent","Arbeitsvertrag Werkstudent:in (Entwurf)","personal","B","Vertrag","extern",
   "Werkstudentenmodell (max. 20 h/Woche): der Startfall."),
 ("arbeitsvertrag-minijob","Arbeitsvertrag Minijob (Entwurf)","personal","B","Vertrag","extern",
   "Minijob 2026 (603-Euro-Grenze): für ergänzende Kräfte."),
 ("verschwiegenheit-datenschutz-ma","Verschwiegenheits- & Datenschutzverpflichtung","personal","B","Erklärung","entwurf",
   "Pflicht bei sensiblen Kundendaten: von jeder Kraft zu unterschreiben."),
 ("verhaltenskodex","Verhaltenskodex","personal","B","Richtlinie","entwurf",
   "Klare Standards beim Kunden und im Team."),
 ("personalstammblatt","Personalstammblatt (Onboarding)","personal","B","Formular","entwurf",
   "Erfasst beim Onboarding IBAN, Steuer-ID, SV-Nummer, Krankenkasse und Werkstudent/Minijob-Angaben."),
 ("stellenausschreibung","Stellenausschreibung / Arbeitgeber-Onepager","personal","B","Recruiting","entwurf",
   "Geld verdienen in der Nachbarschaft: die Ansprache an neue Bewerber:innen."),
 ("bewerbungsformular","Bewerbungsformular & Personalfragebogen","personal","B","Formular","entwurf",
   "Erfasst Qualifikationsnachweis, Verfügbarkeit und Interessenprofil."),
 ("interviewleitfaden","Interviewleitfaden","personal","B","Leitfaden","entwurf",
   "Strukturierte Eignungsentscheidung, keine Bauchgefühl-Einstellung."),
 ("qualifizierungscurriculum","Qualifizierungscurriculum 40 UE (Schritt 2)","personal","C","Curriculum","entwurf",
   "Ausbaustufe: eigene Schulung, wenn ohne Vorqualifikation rekrutiert wird."),
 ("preis-abrechnungsmodell","Preis- & Abrechnungsmodell (≤ 32,50 €)","finanzen","A","Modell","extern",
   "Preis, Fahrtkosten, Lohn-Obergrenzen, zwei Abrechnungswege."),
 ("businessplan","Businessplan","finanzen","C","Plan","entwurf",
   "Zusammenhängendes Dokument für Investor, Bank und die eigene Steuerung."),
 ("kapitalbedarf-mittelverwendung","Kapitalbedarf & Mittelverwendung","finanzen","C","Finanzen","entwurf",
   "Wie viel Kapital, wofür: Grundlage des Investorengesprächs."),
 ("datenschutzerklaerung","Datenschutzerklärung (Website)","it-plattform","C","DSGVO","extern",
   "Pflichttext für Homepage und Plattform."),
 ("verarbeitungsverzeichnis","Verzeichnis von Verarbeitungstätigkeiten","it-plattform","C","DSGVO","entwurf",
   "DSGVO-Pflicht (Art. 30): besonders bei Gesundheitsdaten."),
 ("tom-datenschutz","Technisch-organisatorische Maßnahmen (TOM)","it-plattform","C","DSGVO","entwurf",
   "Wie Daten technisch und organisatorisch geschützt werden."),
 ("impressum","Impressum","it-plattform","C","Recht","extern",
   "Pflichtangaben für die Website."),
 ("erstgespraech-bedarfserhebung","Erstgespräch- & Bedarfserhebungsbogen","betrieb","B","Formular","entwurf",
   "Strukturierte Kundenaufnahme inklusive Bedarf."),
 ("kunden-interessenprofil","Kunden-Interessenprofil (Matching)","betrieb","B","Formular","entwurf",
   "Die Datengrundlage für den USP Interessen-Matching."),
 ("betreuungsvereinbarung-kunde","Betreuungs-/Leistungsvereinbarung (Kundenvertrag)","betrieb","B","Vertrag","extern",
   "Der Vertrag mit dem Kunden: Leistungen, Preis, Kündigung."),
 ("einwilligung-abrechnung-sepa","Einwilligung Abrechnung/Abtretung + SEPA","betrieb","B","Formular","extern",
   "Ermöglicht die Abrechnung des Entlastungsbetrags über die Pflegekasse."),
 ("leistungsnachweis-doku","Einsatz- & Leistungsnachweis (Dokumentation)","betrieb","B","Formular","entwurf",
   "Keine Abrechnung ohne Leistungsnachweis: die Pflichtfelder je Einsatz."),
 ("beschwerde-feedback","Beschwerde- & Feedbackformular","betrieb","B","Formular","entwurf",
   "Schließt die Qualitätsschleife und speist das Matching."),
 ("einwilligung-datenschutz-kunde","Datenschutz-Einwilligung Kunde/Angehörige","betrieb","C","DSGVO","entwurf",
   "Einwilligung in die Verarbeitung der (Gesundheits-)Daten."),
 ("agb-betreuungsplus","AGB BetreuungsPlus","betrieb","C","Recht","extern",
   "Vertragsbedingungen des privaten Abo-Modells."),
 ("widerrufsbelehrung","Widerrufsbelehrung","betrieb","C","Recht","extern",
   "Pflicht bei Verbraucherverträgen (Abo)."),
]
PRIO_LABEL = {"A":"Priorität A","B":"Priorität B","C":"Priorität C"}

def status_badge(s): return '<span class="badge b-part">Entwurf · Fachfreigabe nötig</span>' if s=="extern" else '<span class="badge b-ok">Entwurf erstellt</span>'
def prio_badge(p): return '<span class="badge %s">%s</span>' % ({"A":"b-miss","B":"b-prio","C":"b-part"}[p], PRIO_LABEL[p])

def esc_attr(s): return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;')

def write(path, htmlstr):
    with open(path, "w", encoding="utf-8") as f: f.write(htmlstr)

def page(slug, title, content, active=None):
    active = active or slug
    html = ('<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">'
      '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
      '<title>%s · Vertraut</title><link rel="stylesheet" href="assets/style.css"></head>'
      '<body data-active="%s" data-prefix="">%s<script src="assets/app.js"></script></body></html>'
      % (title, active, content))
    write(os.path.join(ROOT, slug + ".html"), html)

def fragment(slug):
    p = os.path.join(PAGES, slug + ".html")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None

def dept_docs_html(dept):
    items = [d for d in DOCS_REG if d[2]==dept]
    if not items: return ""
    cards=""
    for slug,title,_,prio,typ,status,teaser in items:
        cards+=('<a class="card doccard" href="dokumente/%s.html"><div class="doctop"><span class="dtype">%s</span>%s</div>'
          '<h3>%s</h3><p>%s</p><div class="dfoot">%s<span class="arrow">Öffnen →</span></div></a>'
          % (slug,typ,prio_badge(prio),title,teaser,status_badge(status)))
    return ('<section class="section-pad" style="background:var(--bg2)"><div class="wrap">'
      '<div class="shead"><div class="eyebrow">Dokumente dieser Abteilung</div>'
      '<h2>Zugehörige <span class="gold">Fachdokumente</span></h2></div>'
      '<div class="grid g3">%s</div></div></section>' % cards)

def build_pages():
    for slug,title in [("index","Übersicht"),("gap-analyse","GAP-Analyse"),("was-fehlt","Was noch fehlt")]:
        fr=fragment(slug)
        if fr is not None: page(slug,title,fr,active=slug)
    for slug,label in DEPTS:
        fr=fragment(slug) or ('<section class="hero"><div class="wrap"><h1>%s</h1></div></section>'%label)
        page(slug,label,fr+dept_docs_html(slug),active=slug)

def build_library():
    intro={"A":"Gründungs- & anerkennungskritisch — jetzt für die Gründungsphase.",
           "B":"Für Personal, Kunden und die ersten Einsätze.",
           "C":"Absicherung, Datenschutz, Recht und Skalierung."}
    secs=""
    for prio in ["A","B","C"]:
        cards=""
        for slug,title,dept,pr,typ,status,teaser in [d for d in DOCS_REG if d[3]==prio]:
            cards+=('<a class="card doccard" href="dokumente/%s.html"><div class="doctop"><span class="dtype">%s</span>'
              '<span class="depttag">%s</span></div><h3>%s</h3><p>%s</p>'
              '<div class="dfoot">%s<span class="arrow">Öffnen →</span></div></a>'
              % (slug,typ,DEPT_LABEL[dept],title,teaser,status_badge(status)))
        secs+=('<section class="section-pad"><div class="wrap"><div class="shead"><div class="eyebrow">%s</div>'
          '<h2>%s</h2></div><div class="grid g3">%s</div></div></section>'%(PRIO_LABEL[prio],intro[prio],cards))
    hero=('<section class="hero"><div class="wrap"><div class="kicker">Dokumentenbibliothek</div>'
      '<h1>Fach<span class="gold">dokumente</span></h1><p class="lead" style="margin-top:22px">'
      'Alle aus der GAP-Analyse abgeleiteten Unterlagen als nutzbare Entwürfe. Jedes Dokument lässt sich öffnen, '
      'drucken und als PDF speichern. <b class="em">Entwurf · Fachfreigabe nötig</b> heißt: fachlich '
      '(Anwalt/Steuerberater/Stadt Köln) final prüfen lassen.</p></div></section>')
    page("dokumente","Dokumente",hero+secs,active="dokumente")

def build_docs():
    made=0
    for slug,title,dept,prio,typ,status,teaser in DOCS_REG:
        p=os.path.join(DOCS,slug+".md")
        if not os.path.exists(p): continue
        md=open(p,encoding="utf-8").read()
        html=('<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">'
          '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
          '<title>%s · Vertraut</title><link rel="stylesheet" href="../assets/style.css"></head>'
          '<body class="doc" data-prefix="../" data-slug="%s" data-title="%s" data-dept="%s" data-typ="%s" data-prio="%s" data-status="%s" data-teaser="%s">'
          '<script id="md" type="text/markdown">%s</script>'
          '<script src="../assets/app.js"></script></body></html>'
          % (title, slug, esc_attr(title), dept, esc_attr(typ), esc_attr(PRIO_LABEL[prio]),
             status, esc_attr(teaser), md))
        write(os.path.join(ROOT,"dokumente",slug+".html"), html)
        made+=1
    return made

if __name__=="__main__":
    build_pages(); build_library(); n=build_docs()
    print("Seiten + Abteilungen + Bibliothek gebaut. Fachdokumente:", n, "/", len(DOCS_REG))
    miss=[d[0] for d in DOCS_REG if not os.path.exists(os.path.join(DOCS,d[0]+".md"))]
    if miss: print("FEHLT:", ", ".join(miss))
