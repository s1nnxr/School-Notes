
---

### OBSAH PŘEDNÁŠKY

---
### ASYMETRICKÁ KRYPTOGRAFIE
- princip :
- jeden klíč pro šifrování
- druhý klíč pro dešifrování
	-  odlišný od prvního klíče
	- nelze ho prakticky odvodit z prvního klíče
	-  tzv. kryptografie s veřejným klíčem ( jeden z klíčů lze zveřejnit)

začátek komunikace Alice <-> Bořek

### Kryptografie s veřejným klíčem
princip:
- jeden klíč = (tajný, privat)
	-  bezpečně ukryt
- druhý klíč = veřejný (public)
	- nelze z něho prakticky odvodit privátní klíč
	- věrohodně zveřejnit
- 2 způsoby  použití
	- šifrování a dešifrování
	- podepisování  + ověření podpisu
- další způsoby použití
	- kombinace předchozích dvou ( šifrování + dešifrování )
	- hybridní kryptosystémy ( symetrická + asymetrická)

Výhody
- správa klíčů - jednodušší
	- není nutný zabezpečený přenos
	- snadná výměna a správa klíčů
	- veřejný klíč je možné zveřejnit
- využití i pro digitální podpis
	- podepisování soukromým klíčem
	-  ověřování podpisu veřejným klíčem
zajišťuje-
-  nepopiratelnost odpovědnosti za zprávu
	-  prověřování digitálního podpisu pomocí veřejného kůíče nenarušuje odpovědnost uživatele za ochranu svého soukromého klíče

Nevýhody
- pomalejší než
