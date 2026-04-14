# Účtování
- Účtování (Accounting) je proces sledování a zaznamenávání aktivit uživatelů nebo systémů pro účely auditu.

## Průběh útoku (Kill Chain)
1. Rekognoskace (Reconnaissance): Útočník shromažďuje informace o cíli.
2. Zbrojení (Weaponization): Útočník vytváří škodlivý nástroj nebo zbraň.
3. Doručení (Delivery): Útočník doručuje škodlivý nástroj cíli.
4. Exploatace (Exploitation): Útočník využívá zranitelnosti k získání přístupu.
5. Instalace (Installation): Útočník instaluje škodlivý software na cílový systém.
6. Command and Control (C2): Útočník navazuje komunikaci s kompromitovaným systémem.
7. Akce na cíli (Actions on Objectives): Útočník provádí své cíle, jako je krádež dat, poškození systému nebo další škodlivé aktivity.
8. Uklid (Obfuscation): Útočník se snaží skrýt své stopy a ztížit forenzní analýzu.

---
## Forenzní analýza / vyšetřování
- Zaznamenáváme události které poté zkoumáme
- Vyšetřovací postup nad digitálními daty používaný k získávání důkazů o aktivitách uživatelů (útočníků) v oblasti informačních a komunikačních technologií

---
## Bezpečnostní incident
- Porušení nebo bezprostřední hrozba porušení bezpečnostních politik

---
## Události
- Udalost je incident, který se vyskytne v systému a může být důležitý pro bezpečnostní analýzu.
  - Vyhodnocování incidentů

  |       |   Incident   |   Incident   |
  |-------|--------------|--------------|
  |Udalost|       +      |       -      |
  |   +   |OK            |False Positive|
  |   -   |False Negative|True Positive |

    - False Positive: Systém detekoval událost jako incident, ale ve skutečnosti se nejedná o [hrozbu](./Hrozba.md).
    - False Negative: Systém neidentifikoval událost jako incident, i když se skutečně jedná o [hrozbu](./Hrozba.md).
    - True Positive: Systém správně identifikoval událost jako incident.
    - True Negative: Systém správně identifikoval událost jako neincident.
