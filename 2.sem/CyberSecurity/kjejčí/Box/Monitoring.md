# Monitoring

---

## Provozní

> [!INFO]
> Kontrola funkce
### Příklady:
    - Konzum tonnerů
    - Stav napájení
    - Stav připojení k síti
### Proč:
Umožňuje včasné odhalení problémů a minimalizaci výpadků, zajišťuje optimální výkon a prodlužuje životnost zařízení.
### Pouzívané nástroje:
    - LibreNMS
    - Zabbix (jako libreNMS, ale s agentem)
    - Nagios (provozní služby)
    - SNMP (Simple Network Management Protocol) pro sběr dat o síťových zařízeních
    - Cacti (pro vizualizaci dat z SNMP)

---

## Bezpečnostní

> [!Definition]
> Analýzá nenormálního chování a aktiv která mohou být identifikátoren nežádoucího chování

### Příklady:
    - Detekce neobvyklých přístupů
    - Zapnutí zařízení mimo pracovní dobu

# Monitoring = sledování

- SLA (Service Level Agreement) = dohoda o úrovni služeb, která stanovuje očekávanou úroveň výkonu a dostupnosti služby
- SLO (Service Level Objective) = konkrétní cíl, který je součástí SLA, definující měřitelnou úroveň služby

## Zbýrané metody monitoringu:
- Stav aplikačních procesů a demonů
- kontrola zavislosti služeb
- aplikační metriky:
  - doba odezvy
  - chybovost
  - počet požadavků
- Detekce funkčních a lofických chyb

# Notifikace a eskalace

- Definice prahových hodnot (tresholdů)
- Stavové přechody (ok, warning, critical)
- Automatické upozornění (e-mail, SMS, webhooky)
- Eskalace (při neřešení problému včas)

## Výběr metody závisí na
- Druhy sledovaných systémů
- Požadované granularitě dat
- Bezpečnost požadavcích
- Schopnosti nasadit agenty na cílové systémy

# Logování = zaznamenávání

> [!WARNING]
> Logujeme v jednotném čase

## Log-Management a SIEM (Security Information and Event Management)
    = sběr, analýza a korelace logů pro detekci bezpečnostních incidentů a hrozeb

# Audit = kontrola
