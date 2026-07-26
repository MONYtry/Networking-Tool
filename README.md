# 🌐 Python Networking Toolkit

Ein leistungsstarkes Kommandozeilen-Tool zur Analyse von Netzwerken und Systemen, entwickelt in **Python**. Das Projekt dient als Demonstration meiner Kenntnisse in den Bereichen **Netzwerkprogrammierung**, **Multithreading**, **Socket-Programmierung**, **Systemanalyse** und **Python-Entwicklung**.

---

# 📌 Projektbeschreibung

Dieses Projekt vereint mehrere Werkzeuge zur Netzwerkdiagnose in einer einzigen Anwendung. Ziel war es, grundlegende Netzwerkprotokolle sowie die Kommunikation zwischen Client und Server praktisch umzusetzen und dabei performante sowie übersichtliche Lösungen zu entwickeln.

Der Fokus lag dabei auf:

* Entwicklung einer modularen Python-Anwendung
* Einsatz von Multithreading für performante Portscans
* Arbeiten mit TCP-Sockets
* Kommunikation über verschiedene Netzwerkprotokolle
* Verarbeitung von Systeminformationen
* Strukturierter Aufbau einer Konsolenanwendung

---

# 🚀 Funktionen

## 📡 Ping-Test

Überprüfung der Erreichbarkeit eines Hosts mittels ICMP-Ping.

**Features**

* Erreichbarkeit von IPv4-Adressen prüfen
* Übersichtliche Statusausgabe
* Schnelle Fehlererkennung

---

## 🔍 Multithread-Portscanner

Eigenentwickelter TCP-Portscanner mit paralleler Ausführung.

**Features**

* Frei wählbarer Portbereich
* Mehrere Threads gleichzeitig
* Erkennung offener Ports
* Schnelle Scanzeiten

---

## 🛰 Service-Erkennung (Banner Grabbing)

Nach dem Finden offener Ports wird versucht, den laufenden Netzwerkdienst anhand seines Banners zu identifizieren.

Unterstützte Dienste:

* SSH
* FTP
* SMTP
* unbekannte TCP-Dienste

---

## 🔐 FTP-Verbindung über TLS

Implementierung einer verschlüsselten FTP-Verbindung.

Funktionen:

* AUTH TLS
* Login mit Benutzername und Passwort
* TLS-Verschlüsselung
* Auslesen von Serverantworten
* Kommunikation über FTP-Befehle

---

## 💻 Systeminformationen

Auslesen relevanter Windows-Systeminformationen.

Beispielsweise:

* Betriebssystem
* Hostname
* Registrierter Benutzer
* vollständige Systeminformationen

---

## 📊 Live-Systemmonitor

Anzeige wichtiger Hardwareinformationen in Echtzeit.

* CPU-Auslastung
* Arbeitsspeicher
* Aktualisierung im Sekundentakt

---

# 🛠 Verwendete Technologien

| Technologie        | Einsatz                   |
| ------------------ | ------------------------- |
| Python 3           | Programmiersprache        |
| socket             | Netzwerkkommunikation     |
| ssl                | TLS-Verschlüsselung       |
| concurrent.futures | Multithreading            |
| subprocess         | Systembefehle             |
| psutil             | Hardware- und Systemdaten |
| datetime           | Zeitstempel               |
| os                 | Betriebssystemfunktionen  |

---

# 📚 Lernziele

Mit diesem Projekt konnte ich praktische Erfahrungen sammeln in:

* Objektorientierter und modularer Python-Entwicklung
* Netzwerkkommunikation über TCP
* Socket-Programmierung
* Multithreading
* Verarbeitung von Serverantworten
* Konsolenanwendungen
* Fehlerbehandlung
* Arbeiten mit Betriebssystemfunktionen
* Performanceoptimierung

---

# ▶️ Installation

Repository klonen

```bash
git clone https://github.com/DEIN-NAME/Python-Networking-Toolkit.git
```

Abhängigkeiten installieren

```bash
pip install psutil
```

Programm starten

```bash
python main.py
```

---

# ⚠ Hinweis

Dieses Projekt wurde ausschließlich zu Lern-, Analyse- und Demonstrationszwecken entwickelt.

Netzwerkscans oder Verbindungsversuche sollten ausschließlich auf Systemen durchgeführt werden, für die eine ausdrückliche Berechtigung vorliegt.

---

# 👨‍💻 Über dieses Projekt

Dieses Projekt entstand, um meine Kenntnisse im Bereich **Python**, **Netzwerkprogrammierung** und **Systementwicklung** praxisnah zu vertiefen.

Besonderer Wert wurde auf eine verständliche Struktur, modulare Programmierung und die praktische Anwendung verschiedener Python-Bibliotheken gelegt.

Es dient gleichzeitig als Portfolio-Projekt und zeigt meine Fähigkeiten in den Bereichen:

* Python
* Netzwerktechnik
* Multithreading
* Systemprogrammierung
* Fehleranalyse
* Softwareentwicklung
