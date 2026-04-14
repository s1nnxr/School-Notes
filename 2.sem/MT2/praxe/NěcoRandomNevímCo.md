```
A=(  1  3  3)
  (  2  1  4)
```

```
B=(  1  0)
  (  2  1)
  (  3  2)
```
```
C=(  3 -2)
  (  2  4)
```
```
D=(  3 -1  3)
  (  4  1  5)
  (  2  1  3)
```
```
E=(  1  2  3)
  (  4  5  6)
  (  7  8  9)
```
```
D+E=(  4  1  6)
    (  8  6 11)
    (  9  9 12)
```
# Skalární Součin
```
B*C=(  1*3 + 0*2   1*(-2) + 0*4)
    (  2*3 + 1*2   2*(-2) + 1*4)
    (  3*3 + 2*2   3*(-2) + 2*4)
=(  3   -2)
 (  8    0)
 ( 13    2)
```
## Postup pro násobení matic jako pro žáka základní školy
```
1. Vezmeme první řádek matice B a první sloupec matice C.
2. Vynásobíme první prvek řádku B (1) s prvním prvkem sloupce C (3) a získáme 3.
3. Vynásobíme druhý prvek řádku B (0) s druhým prvkem sloupce C (2) a získáme 0.
4. Sečteme výsledky z kroků 2 a 3: 3 + 0 = 3. Toto je první prvek výsledné matice.
5. Opakujeme tento proces pro každý řádek matice B a každý sloupec matice C, abychom získali všechny prvky výsledné matice.
```
# Matice na druhou
- Matice * stejná matice
- Matice musí být čtvercová
```
C^2 = (  3*3 + (-2)*2   3*(-2) + (-2)*4)
      (  2*3 + 4*2    2*(-2) + 4*4)
= (  5   -14)
  (  14   12)
```
# Inverzní Matice
- Matice A^-1 je taková matice, že A * A^-1 = I (jednotková matice)
```
(3 -2|1 0)/3~ (1  2/3|0  1/3)*(-2)~ (1 -2/3 |-1/3 0)       ~ (1 -2/3 |-1/3    0)       ~ (1 0    |-2/28+8/24 1/8)
(2  4|0 1)  ~ (2  4  |0    1)     ~ (0  16/3|-2/3 1)*(3/16)~ (0  1   |-1/8 3/16)*(2/3) ~ (0  1   |-1/8 3/16)
```
# Hodnost matice
- Hodnost matice je počet lineárně nezávislých řádků nebo sloupců v matici.
- Pro matici A je hodnost(A) = 2, protože má 2 lineárně nezávislé řádky.
