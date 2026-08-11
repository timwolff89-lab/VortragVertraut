Dieses Dokument beschreibt die technischen und organisatorischen Maßnahmen (TOM) zur Sicherheit der Verarbeitung gemäß Art. 32 DSGVO und dient als Nachweis nach Art. 5 Abs. 2 DSGVO sowie als Anlage zu Auftragsverarbeitungsverträgen (Art. 28 DSGVO).

> ⚠︎ **Prüfvorbehalt:** Wegen der Verarbeitung von **Gesundheitsdaten (Art. 9 DSGVO)** vulnerabler Personen ist ein **hoher Schutzbedarf** anzusetzen. Die hier genannten Maßnahmen sind Soll-Vorgaben und müssen durch DSB/IT-Sicherheit anhand einer **Schutzbedarfs- und Risikoanalyse** konkretisiert, umgesetzt und regelmäßig überprüft werden. Angaben in [ ] projektspezifisch belegen.

## 1. Rahmen und Schutzziele

Die Maßnahmen orientieren sich an den Schutzzielen **Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit** (Art. 32 Abs. 1 lit. b DSGVO) sowie an der Fähigkeit zur **Wiederherstellung** (lit. c) und regelmäßigen **Überprüfung/Bewertung** (lit. d). Alle Systeme werden mit **Datenstandort in der EU/im EWR** betrieben.

## 2. Übersicht: Maßnahme → Umsetzung

### 2.1 Zutrittskontrolle (T1) – physischer Zugang

| Maßnahme | Umsetzung |
|---|---|
| Zutrittsschutz Büro/Räume | [abschließbare Räume, Schließsystem, Zutritt nur befugte Personen] |
| Besucherregelung | [Empfang/Begleitung, keine unbegleiteten Dritten in Datenbereichen] |
| Aufbewahrung Papierunterlagen | abschließbare Schränke; Führungszeugnis-Einsicht dokumentiert, keine offene Ablage ⚠︎ |
| Cloud-/Rechenzentrum | Zutrittsschutz durch Hoster (Zertifikat-Nachweis, EU-Standort) ⚠︎ |

### 2.2 Zugangskontrolle (T2) – Zugang zu Systemen

| Maßnahme | Umsetzung |
|---|---|
| Authentifizierung | individuelle Benutzerkonten, starke Passwörter, **Mehr-Faktor-Authentifizierung (MFA)** für administrative und sensible Zugänge |
| Sperrmechanismen | automatische Sperre bei Inaktivität, Sperrung nach Fehlversuchen |
| Passwort-Richtlinie | Mindestlänge/-komplexität, kein Klartext, Passwort-Hashing |
| Geräteschutz | verschlüsselte Endgeräte, aktuelle Updates, Virenschutz; keine Verarbeitung auf Privatgeräten ohne Freigabe ⚠︎ |

### 2.3 Zugriffskontrolle (T3) – Berechtigungen im System

| Maßnahme | Umsetzung |
|---|---|
| Rollen-/Rechtekonzept (**R**) | rollenbasierte Rechte: Bewerber, Betreuungskraft, Fachkraft/Leitung, Verwaltung, Kunde/Angehörige, Admin – **Need-to-know / Least Privilege** |
| Gesundheitsdaten | Zugriff nur für zugeordnete Betreuungskraft, Fachkraft/Leitung und Abrechnung, streng minimiert ⚠︎ |
| Protokollierung (**L**) | **Audit-Log** über Zugriffe/Änderungen an sensiblen Daten, revisionssicher, regelmäßige Auswertung |
| Berechtigungsverwaltung | dokumentierte Vergabe/Entzug bei Ein-/Austritt, regelmäßige Rechte-Reviews |

### 2.4 Weitergabekontrolle (T4) – Transport/Übermittlung

| Maßnahme | Umsetzung |
|---|---|
| Transportverschlüsselung (**V**) | **TLS** für Website/Plattform/App und E-Mail-Transport |
| Datenträger/Versand | verschlüsselte Übertragung; keine unverschlüsselten E-Mail-Anhänge mit Gesundheitsdaten ⚠︎ |
| Abrechnungsübermittlung | gesicherte Kanäle zu Pflegekasse/Steuerberatung; Empfänger dokumentiert |
| Löschung Datenträger | sichere Löschung/Vernichtung (Aktenvernichter, Wipe) |

### 2.5 Eingabekontrolle (T5) – Nachvollziehbarkeit

| Maßnahme | Umsetzung |
|---|---|
| Protokollierung Eingaben | Erfassen/Ändern/Löschen von Datensätzen wird protokolliert (wer, wann) |
| Versionierung | Nachvollziehbarkeit der Leistungsdokumentation; nachträgliche Änderungen kenntlich |
| Vier-Augen-Prinzip | für kritische Aktionen (z. B. Löschungen, Rechtevergabe) [optional] |

### 2.6 Auftragskontrolle (T6) – Auftragsverarbeitung

| Maßnahme | Umsetzung |
|---|---|
| AV-Verträge (Art. 28) | mit allen Auftragsverarbeitern (Hosting, Software, Wartung) abgeschlossen |
| Auswahl/Kontrolle | dokumentierte Dienstleisterauswahl, Nachweise/Zertifikate, EU-Datenstandort |
| Sub-Prozessoren | Übersicht und Genehmigungsvorbehalt; kein unbemerkter Drittlandbezug ⚠︎ |
| Weisungsbindung | Verarbeitung nur auf dokumentierte Weisung |

### 2.7 Verfügbarkeitskontrolle (T7) – Schutz vor Verlust

| Maßnahme | Umsetzung |
|---|---|
| Backup (**B**) | regelmäßige, verschlüsselte Backups; **Restore-Tests**; getrennte Aufbewahrung |
| Redundanz/Schutz | [USV, Firewall, Monitoring] beim Hoster |
| Notfallkonzept | Wiederanlaufplan (RTO/RPO) [festlegen] ⚠︎ |
| Schadsoftware | Virenschutz, Patch-Management |

### 2.8 Trennungskontrolle (T8) – getrennte Verarbeitung

| Maßnahme | Umsetzung |
|---|---|
| Mandanten-/Zwecktrennung | logische Trennung von Bewerber-, Personal-, Kunden-/Gesundheits- und Abrechnungsdaten |
| Test/Produktion | getrennte Umgebungen; keine echten Gesundheitsdaten in Testsystemen ⚠︎ |
| Rollenbezogene Sichten | Datentrennung über Rollen/Rechte |

## 3. Weitere Maßnahmen

| Bereich | Umsetzung |
|---|---|
| Verschlüsselung (V) | Transportverschlüsselung (TLS); Verschlüsselung sensibler Daten „at rest" [Verfahren belegen] ⚠︎ |
| Pseudonymisierung | wo möglich (z. B. Auswertungen/Statistik) |
| Verpflichtung Beschäftigte | Verschwiegenheits-/Datenschutzverpflichtung; Datenschutz-Schulung bei Onboarding und regelmäßig |
| Data-Breach-Prozess | Melde-/Reaktionsprozess für Datenschutzverletzungen (Art. 33/34: 72-Stunden-Meldung) ⚠︎ |
| Löschkonzept | dokumentierte Löschfristen/-routinen (siehe Verzeichnis der Verarbeitungstätigkeiten) |
| Privacy by Design/Default | Datensparsamkeit in Plattform/App (Art. 25 DSGVO) |
| DSFA | Prüfung/Durchführung einer Datenschutz-Folgenabschätzung (Art. 35) für Gesundheitsdaten ⚠︎ |

## 4. Überprüfung und Aktualisierung

Die TOM werden mindestens [jährlich] sowie anlassbezogen (neue Systeme, Vorfälle, geänderte Risiken) überprüft und fortgeschrieben. Verantwortlich: [Rolle/Person].

| Angabe | Inhalt |
|---|---|
| Stand / Version | [Datum] / [v0.1] |
| Erstellt / geprüft | [Name] / [DSB/Anwält:in – ausstehend] ⚠︎ |

---

> ⚠︎ **Zwingend fachlich prüfen:** Angemessenheit der Maßnahmen zum Schutzbedarf (Gesundheitsdaten), DSFA-Pflicht (Art. 35), Data-Breach-Prozess, konkrete Verschlüsselung/Backup-Parameter, AV-/Sub-Prozessor-Kette. Dieser Entwurf ersetzt keine IT-Sicherheits- oder Rechtsberatung.
