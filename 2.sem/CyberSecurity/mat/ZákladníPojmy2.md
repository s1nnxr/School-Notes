# Klasické kriptosystémy
# Transpozice <- v testu
- Princip: změna(permutace) pořadí písmen textu (přesmičky)
- Varianty: - Sloupcová transpozice
                - Heslo 
            - Dvojitá transpozice
                - Algoritmus: 
                    1. 2 hesla
                    - 1. heslo + doplnění náhodnými znaky v posledním řádku
                    - 2. heslo + doplnění náhodnými znaky v posledním řádku
# Substituce <- v testu

- Princip: nahrazení jednoho znaku jiným znakem
- Odesílatel: Znak O.A. nahradit znakem Š.A.
- Adresát: Znak Š.A. nahradit znakem O.A.
    - Invertovaná substituce

- Základní typy:    - Monoalfabetická substituce
                        - jednoduchá substituce / záměna
                        - Šifrování
                            - Každý znak O.T. nahradí jiním znakem Š.T. podle předpisu <- v testu
                        - Dešifrování
                            - Nutná znalost substituční tabulky přiřazení / klíč pro tvorbu <- v testu
                        - 3 varianty
                            - Afinní šifry Klíč (tabulka přiřazení, tabulka substitucí) <- ne v testu
                            - Šifry s trivialním klíčem (posunová šifra) <- v testu
                            - Šifry s klasickým klíčem (klíčová fráze) <- v testu
                    - Homofonní substituce
                        - kažný znak O.T. se nahradí jedním znakem Š.T. podle předpisu
                            - Frekventované znaky
                                - více znaků Š.T. (např. E -> 1, 2, 3)
                            - Ne-frekventované znaky
                                - méně znaků Š.T. (např. Q -> 4)
                    - Polyalphabetická substituce
                        - Posloupnost monoalfabetických šifer
                            - Konečná, nekonečná
                        - E_i(M) = F_i(M)
                            - Fi(M) je i ta monoalfabetická šifra
                        - Pořadí použití dané abecedy
                            - Určeno klíčem
                            - Po určité době se opakuje
                        - Vigenerova šifra
                            - 16. století Blažej de Vigenère
                            - Šifrování: Vigeneruv čtverec
                                - Tabulka 26x26
                                - Vodorovně: O.T. (A-Z)
                                - Svisle: klíčová fráze (A-Z)
                                - Průsečík: Š.T.
                            - Dešifrování:
                                - Tabulka 26x26
                                - Vodorovně: klíčová fráze (A-Z)
                                - Svisle: Š.T. (A-Z)
                                - Průsečík: O.T.
                    - Polygramové substituce
                        - šifrování mezi skupinami písmen (např. dvojice, trojice)
                            - bigramová substituční šifra
                            - princip: Klíč = tabulka 5x5
                                - 25 písmen (I/J dohromady)
                                - Vodorovně: O.T. (A-Z)
                                - Svisle: Š.T. (A-Z)
                                - Průsečík: Š.T.
                            - šifrování: O.T. -> Š.T.
                                - Dvojice písmen O.T. se nahradí dvojicí písmen Š.T. podle předpisu

# Hillova šifra
- 1929 Lester S. Hill
- C=E_K(M) = K*M
- M=D_K(C) = K^-1*C
- K je matice
- K^-1 je inverzní matice k K
- Postup šifrování:
    1. Zvolíme vhodnou abecedu (např. A-Z)
    2. Substituce na čísla (A=0, B=1, ..., Z=25)
    3. Klíč = jednoduchá matice (např. 2x2)
    4. Zašifrujeme zprávu
- Postup dešifrování:
    1. Zjistíme inverzní matici K^-1
    2. Dešifrujeme zprávu pomocí vzorce M=D_K(C) = K^-1*C

## Příklad:
    - Abeceda: N=29
| A | B | C | D | E | F | G | H | I | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10| 11| 12| 13|

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25 |

- Klíč: K = | 2 3 |
            | 4 5 |
- Šifrování zprávy "HI":
    - M = | 07 |
          | 08 |
    - C = K*M = | 2 3 | * | 07 | = | 2*07 + 3*08 | = | 14 + 24 | = | 38 |
                | 4 5 |   | 08 |   | 4*07 + 5*08 |   | 28 + 40 |   | 68 |
    - C = | 38 |
          | 68 |
    - Pro zjednodušení můžeme použít modulo 29:
    - C = | 38 mod 29 | = | 9 |
          | 68 mod 29 |   | 10 |
    - Šifrový text: "KJ" (K=10, J=9)
- Dešifrování zprávy "KJ":
    - C = | 10 |
          | 9  |
    - Nejprve zjistíme inverzní matici K^-1:
        - Determinant det(K) = (2*5 - 3*4) mod 29 = (10 - 12) mod 29 = -2 mod 29 = 27
        - Inverzní determinant det(K)^-1 mod 29 = 27^-1 mod 29 = 27 (protože 27*27 mod 29 = 1)
        - K^-1 = det(K)^-1 * | 5 -3 |
                             | -4 2 |
        - K^-1 = 27 * | 5 -3 |
                      | -4 2 |
        - K^-1 = | 27*5 mod 29  27*(-3) mod 29 |
                 | 27*(-4) mod 29  27*2 mod 29 |
        - K^-1 = | 135 mod 29  -81 mod 29 |
                 | -108 mod 29  54 mod 29 |
        - K^-1 = | 19  22 |
                 | 25  25 |
    - Dešifrování:
    - M = K^-1 * C = | 19  22 | * | 10 | = | 19*10 + 22*9 | = | 190 + 198 | = | 388 |
                     | 25  25 |   | 9  |   | 25*10 + 25*9 |   | 250 + 225 |   | 475 |
    - M = | 388 mod 29 | = | 7 |
          | 475 mod 29 |   | 8 |
    - Dešifrovaný text: "HI" (H=7, I=8)

