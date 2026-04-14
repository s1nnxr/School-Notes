## Šifrovací algoritmus
- Obecná šifrovací metoda
    - dnes většinou zveřejněn
    - dříve nutné utajení - pro bezpečnost algoritmu
## Klíč (heslo)
- specifikace šifrovacího algoritmu (tajemství)
    - tajný/privatní klíč - utajení
    - veřejný klíč - není tajný
## Kryptografický protokol
- Sada pravidel pro komunikaci mezi dvěma nebo více stranami
    - Zajišťuje bezpečnou výměnu informací
    - Např. SSL/TLS pro zabezpečení internetové komunikace

## O.A
- Otevřená architektura
    - všechny znaky abecedy původního textu
## Š.A.
- Šifrovaná abeceda
    - Všechny znaky abecety šifrového textu

## Kryptosystém
- šifrovací, kryptografický systém
- systém používaných pro změnu textu s vílem učinit jej nesrozumitelným pro neautorizované osoby
## Klamač
- znak Š.A., který nemá žádný odpovídající znak v O.A.
* vkládají se dé š.t. pro zvýšení odolnosti š.sytémů pro:
    - ztížení kryptoanalýzy
    - ztížení luštění (louskání)

## Šifrování vs Dešifrování vs Luštění(louskáníú
- Šifrování: proces převodu původního textu (otevřeného textu) na šifrovaný text pomocí šifrovacího algoritmu a klíče
- Dešifrování: proces převodu šifrovaného textu zpět na původní text pomocí dešifrovacího algoritmu a klíče
- Luštění (louskání): proces pokusu o získání původního textu bez znalosti klíče, často pomocí kryptoanalýzy nebo hrubé síly

## Mezinárodní abeceda
- abeceda bez diakritiky (26 písmen)

## Rozšízená abeceda
- Mezinárodní abeceda+Mezera+Interpunkční znaménka
- A-z ,.:!?

## Národní abeceda
- Abeceda s diakritikou

## E(M)/E_K(M)
- Šifroací funkce
- E - šifrovací algoritmus
- M - původní text (otevřený text)
- K - klíč
- E(M) - šifrovaný text bez klíče
- E_K(M) - šifrovaný text s klíčem
## D(C)/D_K(C)
- Dešifrovací funkce
- D - dešifrovací algoritmus
- C - šifrovaný text (ciphertext)
- K - klíč
- D(C) - dešifrovaný text bez klíče
- D_K(C) - dešifrovaný text s klíčem
## Matematické operace
- XOR (exclusive OR)
- MOD (modulo)
- NSD(NSN) - největší společný dělitel (nejmenší společný násobek)
## Runda
- Jedno kolo výpočtu
    - skupina operací, které se opakují v šifrovacím algoritmu

# Typologie
## Podle počtu součastně šifrovaného textu
### Kloková šifra
    - šifrování skipiny znaků najednou (blok)
        + Malá náchylnost k zneužití
        + bezpečnější než proudová šifra
        - Větší náročnost na výpočetní výkon
        - Větší náročnost na paměť
### Proudová šifra
    - šifrování jednoho znaku po druhém
        + Rychlejší než bloková šifra
        + Méně náročná na výpočetní výkon
        - Větší náchylnost k zneužití
        - Méně bezpečná než bloková šifra
## Podle typu utajení klíče
### S tajným klíčem
    - Symetrická kryptografie
        + Rychlejší než asymetrická krypt
        + Méně náročná na výpočetní výkon
        - Bezpečnost závisí na utajení klíče
        - Problém distribuce klíčů
### S veřejným klíčem
    - Asymetrická kryptografie
        + Bezpečnější než symetrická kryptografie
        - Pomalejší než symetrická kryptografie
## Podle počtu kůíčů
### Symetrická kryptografie
    - jen jeden tajný klíč pro šifrování a dešifrování
### Asymetrická kryptografie
    - dva klíče: veřejný klíč pro šifrování a tajný klíč pro dešifrování

## Podle možnosti rekonstrukce původního o.t.
### šifrování
    - Pseoudojednocestné šifrování
### hashování
    - Jednocestné šifrování
## Šifrovací algoritmy
### Změna pozic znaků (klasická kryptografie)
    - transpozice
    - substituce
### Matematické funkce (moderní kryptografie)
    - modulární aritmetika
        - modulární +,-,*,a,/
        - logické operátory, např. XOR
    * prvočíselné faktory
    - disktétní logaritmy
    - eliptické křivky
### Fyzikální zákony (kvantová kryptografie)
    - kvantová mechanika
    - kvantové provázání

## Substituce znaky <--> čísla
### Interní uložení ve znakové sadě
    - binární kódování
    - ASCII
    - Unicode
### Vlastní převodní tabulka
# Matematika
## Modulární aritmetika
$Z_n={0,1,2,...,(n-1)}$
- n = modul
- redukován počet použitých císel (n)
- jako aritmetika N={1,2,3,...}
- Převádí nekonečnou množinu čísel na konečnou množinu (Z_n)
## Komutaticní zákon
$a+b=b+a$
$a*b=b*a$
## Aspcoatovmé zákon
$a+(b+c)=(a+b)+c$
$a*(b*c)=(a*b)*c$
## Distributivní zákon
$a*(b+c)=a*b+a*c$
$(a+b)*c=a*c+b*c$
## Rozdíly číselných množin
- N - přirozená čísla
    - N={1,2,3,...}
    - operace + * (nelze - /)
- Z - celá čísla
    - Z={...,-3,-2,-1,0,1,2,3,...}
    - operace + - * (nelze /)
- množina Z_n - zbytková třída modulo n
    - Z_n={0,1,2,...,(n-1)}
    - operace + - * /
### Definice relace kongurence 
    - Z_n={0,1,2,...,(n-1)}
    - Platí: a≡b (mod n) ⇔ n | (a-b)
    - a,b∈Z, n∈N
    - a,b jsou kongruentní modulo n, pokud n dělí rozdíl a-b
    - a,b jsou v stejné zbytkové třídě modulo n
#### Příklad: 20 ≡_6 8    
- 20=2*6+6
- 20/6=3 zbytek 2 8/6=1 zbytek 2 (20-8)/6=2 zbytek 0
### Pravidla kongurence
- P1: a_na(\forall a\in Z)
- P2: (a≡_n b)  ⇒ (a+c≡_n b+c) ∀c∈Z
- R3: (a≡_n b)u (b≡_n c) ⇒ (a≡_n c) (\forall a,b,c\in Z)
- P4: (a≡_n b) u (c≡_n d) ⇒ (a+c≡_n b+d) (\forall a,b,c,d\in Z)
- P5: (a≡_n b) u (c≡_n d) ⇒ ((a*c)≡_n (b*d)) (\forall a,b,c,d\in Z)

- např. 64 ≡_6 4 a 400 ≡_6 64⇒ 400 ≡_6 4
# Ukoly
## Modul n = 10
   - sečtete a odečtěte posloupnosti
   - 5 1 3 0 a 7 0 4 9 8
## Modul n=26
    - sečtete a odečtěte posloupnosti
    - 15 11 23 06 11 a 17 00 04 09 08
# Modulátní inverse
# Modulátní inverse sčítání
n=5(prvočíslo)

|  +  |  0  |  1  |  2  |  3  |  4  |  5  |
|-----|-----|-----|-----|-----|-----|-----|
|  0  |  1  |  2  |  3  |  4  |  0  |  1  |
|  1  |  2  |  3  |  4  |  0  |  1  |  2  |
|  2  |  3  |  4  |  0  |  1  |  2  |  3  |
|  3  |  4  |  0  |  1  |  2  |  3  |  4  |
|  4  |  0  |  1  |  2  |  3  |  4  |  0  |

# Prvočísla
- Vlastnosti:
    - dělitelné pouze 1 a sebou samým
    - nekonečně mnoho prvočísel
    - existují dvojčata (páry prvočísel, která se liší o 2)
    - existují Mersennova prvočísla (tvaru 2^p-1, kde p je prvočíslo)
## Eratosthenovo síto
    - pro zjištění všech prvočísel < n
    jen pro malá n

|     |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 11  |~12~ | 13  |~14~ | 15  |~16~ | 17  |~18~ | 19  |~20~ |
|~21~ |~22~ |~23~ |~24~ |~25~ |~26~ |~27~ |~28~ |~29~ |~30~ |
|~31~ |~32~ |~33~ |~34~ |~35~ |~36~ |~37~ |~38~ |~39~ |~40~ |
### Rozšíření eratosthenov algoritmus Miller-Rabin
    - pro zjištění, zda je číslo n prvočíslem
    - pro velká n
3^-1≡_29=??
#### jednoduchý způsob

| násobky | zbytky || koeficienty        |
|---------|--------||--------------------|
|         | 29     || 1       | 0        |
|         | 3      || 0       | 1        |
| 29=3*9+2| 2      || 1=9*0+1 | 0=9*1+-9 |
| 3=2*1+1 | 1      || -1      | 10       |
# Eulorova funkce φ(n)
- Co to je?
    - počet kladných celých čísel menších než n, která jsou s n nesoudělná (nemají společné dělitele kromě 1)
# Gaussův vstah
\pi(n) ~ \frac{n}{\ln(n)}
# Moderní kryptografie
- Využívá prvočíselné faktory, diskretní logaritmy, eliptické křivky
## deskrétní logaritmus
- tj. y=q^x

# Generátory
## Generátor náhodných čísel
- dobrý generátor - důležirý
- využití:
    - náhodný výběr klíče z celého prstoru
### Pravé náhodné číslo
    - založeno na fyzikálních jevech (např. radioaktivní rozpad, šum v elektronických obvodech)
### Pseudonáhodné číslo
    - založeno na algoritmech, které generují sekvence čísel, které se jeví jako náhodné, ale jsou deterministické (např. Mersenne Twister, Linear Congruential Generator)
