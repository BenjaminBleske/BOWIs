# Bottroper Wahlplakat-Management und Informationssystem (BOWIs)

https://benjaminbleske.github.io/BOWIs/ 

## Projektübersicht
Das BOWIs ist ein webbasiertes System zur digitalen Erfassung, Verwaltung und Visualisierung von Wahlplakat-Standorten für die CDU Bottrop. Es ermöglicht eine einfache und effiziente Kommunikation der Plakatierungsdaten durch Helfer:innen via WhatsApp-Standortmeldungen.

## Ziel
- Vereinfachung der Plakat-Standortmeldung im Wahlkampf
- Vermeidung manueller, fehleranfälliger Erfassungen
- Elektronische Aufbereitung und Visualisierung der Standorte in interaktiven Karten
- Unterstützung der strategischen Plakatplanung durch Datenanalyse

## Komponenten
- **Standort-Manager:** Webanwendung zur Erfassung und Verwaltung der eingehenden Standortdaten
- **Plakatstandortkarte:** Interaktive Karte zur Visualisierung der aktuellen Plakatstandorte mit Cluster-Funktionalität
- **CSV API Karte (Server Fastify):** Server-seitige Schnittstelle zur Bereitstellung und schnellen Darstellung der Standortdaten

## Funktionsweise
1. Plakathelfer:innen senden nach dem Aufhängen eines Plakats ihren Standort per WhatsApp als aktuellen Standort-Link an eine zentrale Nummer.
2. Der Standort wird automatisch erfasst, validiert und in das System eingespeist.
3. Über den Standort-Manager können die Daten überprüft und als CSV-Datei exportiert werden.
4. Die Plakatstandortkarte visualisiert die Standorte übersichtlich und ermöglicht eine Cluster-Ansicht zur besseren Übersicht.
5. Die CSV API Karte stellt die Daten serverseitig zur Verfügung und ermöglicht schnelle Zugriffe über eine API.

## Technologie-Stack
- Frontend: React, Leaflet.js
- Backend: Node.js mit Fastify-Server
- Datenformat: CSV, GeoJSON
- Hosting: Glitch


## Kontakt
Projektverantwortlicher: Benjamin Bleske  


*Stand: Juni 2025*

https://glitch.com/edit/#!/panoramic-fifth-pyrite
https://glitch.com/edit/#!/majestic-somber-dracopelta
