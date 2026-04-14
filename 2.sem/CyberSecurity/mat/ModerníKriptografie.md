# Principy Šifrování
- Matematické algoritmy pro šifrování a dešifrování dat
- Fyzické postupy pro randomizaci dat
- Nuté zvážit
    - učel šifrování
    - požadavaný stupeň bezpečnosti
    - rychlost šifrování a dešifrování
        - proudové, blokové šifry
    - pravní aspekty použití šifrování
## Bytové a proudové šifry
- prodloužení bloků o.t. a dékly klíče
    - zajištění bezpečnosti
## Symetrické a asymetrické šifry
- Počet klíčů
    - Symetrické: jeden klíč pro šifrování i dešifrování
    - Asymetrické: dva klíče (veřejný a soukromý)
## Kryptografické s veřejným klíčem
- Používají se pro zabezpečení komunikace a digitální podpisy
## Šifrování x hashování
- vytvoření otisku pevně dané delky
## Symetrická kryptografie
### Probém s klíčem
- Musí být tajný pro každou komunikaci cvojici **A<--> B**
- Vyměněna tajného klíče -> důvěryhodný kanál
- udržení tajnosti klíče
- Potřebujeme exponenciální počet klíčů pro komunikaci mezi n účastníky
### Problém s asymetrickou kryptografií
- Pomalejší než symetrická kryptografie
- Vhodná pro šifrování malých dat nebo pro výměnu klíčů
- Používá se pro zabezpečení komunikace a digitální podpisy
- Vyměněna veřejného klíče -> důvěryhodný kanál
- Udržení tajnosti soukromého klíče
- Potřebujeme pouze jeden pár klíčů pro každého účastníka
## Symetrické kryptosystémy
- Pro dlouhé texty
    - Rychlé šifrování a dešifrování
    - nutné předat klíšč bezpečným kanálem
## Asymetrické kryptosystémy
- Pro krátké texty
    - Pomalejší šifrování a dešifrování
    - Vhodné pro šifrování malých dat nebo pro výměnu klíčů
    - Používá se pro zabezpečení komunikace a digitální podpisy
## Kryptografie s veřejným klíčem
- Pro zabezpečení komunikace a digitální podpisy
    - Vyměněna veřejného klíče -> důvěryhodný kanál
    - Udržení tajnosti soukromého klíče
    - Potřebujeme pouze jeden pár klíčů pro každého účastníka
### Ověřování a podepisování dat
- Digitální podpisy
    - Zajišťují autenticitu a integritu dat
    - Vytvořeny pomocí soukromého klíče a ověřeny pomocí veřejného klíče
### Šifrování a dešifrování podepsaných dat
- Šifrování dat pomocí veřejného klíče příjemce a podepisování dat pomocí soukromého klíče odesílatele
- Dešifrování dat pomocí soukromého klíče příjemce a ověřování podpisu pomocí veřejného klíče odesílatele
### Hybridní kryptosystémy
- Kombinace symetrické a asymetrické kryptografie
    - Používají asymetrickou kryptografii pro výměnu klíčů a symetrickou kryptografii pro šifrování dat
    - Zajišťují rychlé šifrování a dešifrování dat a bezpečnou výměnu klíčů
### Feistelův princip
- Vlastnosti
    - k funkci F nemusím hledat inverzní funkci
        - inverzní funkce nemusí vůbec existovat
    - Pro dešifrování stejný postup jako pro šifrování, jen se zamění klíče
    - Používá stejný klíč
    - dlouhodobá ověřenost bezpečnosti šifry
    - zakladem mnoha moderních blokových šifer (DES, Blowfish, Twofish)
### DES (lucifer)
- Počátešní (vstupní) permutace bloků
    - PP na 64b
- Rozložení bloků na poloviny L_0 a R_0
    - 2*32b
- Výpočet L_i a R_i pro i=1,...,16
    - Expanze (e-box) na 48b
    - Substituce pomocí S-boxů na 32b
    - Permutace (p-box) na 32b
        - 16 rund
- Sloučení L_16 a R_16 a konečná (inverzní) permutace
    - IP^-1 na 64b
- Vlastnosti
    - PP a PP^-1 nemají žádný kryptografický význam
    - Pro komunikaci
    - šifrování soubourů na HD
### AES (Rijndael)
- Advanced Encryption Standard
- Iterační symertická bloková šifra
    - s proměnou délkou bloku a klíče
        - Bloky 128b, klíče 128, 192 nebo 256
## Rijndael
- Autoři Vincent Rijmen a Joan Daemen
- Nahradil DES
    - NIST vyhlásil 2.1.1997 vyřejnou a otevřenou soutěž
    - schválil jako federální standard v usa
- Vlastnosti
- blok 128b
- klíč 128, 192 nebo 256b
   - označení AES-128, AES-192, AES-256
- 10, 12 nebo 14 rund
    - v závislosti na délce klíče
- poslední blok je nutné doplnit o padding
