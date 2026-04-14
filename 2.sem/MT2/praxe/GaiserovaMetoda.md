# Příklad 1
```
x+2y-z=0
x-2y+z=0
2x-3y=1
```
## Převedení do matice a serazení do trojúhelníkového tvaru
```
| x  y  z | Vysledek | ~                       | x  y  z | Vysledek | ~          | x  y  z    | Vysledek |
| 1  2 -1 | 0        | ~ Sčítací metoda Z toho | 1  2 -1 | 0        | ~          | 1  2  -1   | 0        |
| 1 -2  1 | 0        | ~ Sčítací metoda sem    | 0 -4  2 | 0        | ~ /*(-7/4) | 0  7  -7/2 | 0        |
| 2 -3  0 | 1        | ~ Sčítací metoda sem    | 0 -7  2 | 1        | ~          | 0  0  -3/2 | 1        |
```
## Vyjádření z poslední řádky
```
-3/2z=1
z=-2/3

7y-7/2z=0
7y-7/2*(-2/3)=0
7y+7/3=0
7y=-7/3
y=-1/3

x+2y-z=0
x+2*(-1/3)-(-2/3)=0
x-2/3+2/3=0
x=0
```
## Výsledek
```
[x y z] = [0 -1/3 -2/3]
```

# Příklad 2
```
-x+y-2z=1
x+y+2z=-1
x+3y-2z=-1
```
## Převedení do matice a serazení do trojúhelníkového tvaru
```
| x  y  z | Vysledek | ~                       | x  y  z | Vysledek | ~                       | x  y  z | Vysledek |
| -1 1 -2 | 1        | ~ Sčítací metoda Z toho |-1  1 -2 | 1        | ~                       |-1  1 -2 | 1        |
| 1  1  2 | -1       | ~ Sčítací metoda sem    | 0  2  0 | 0        | ~ Sčítací metoda Z toho | 0  2  0 | 0        |
| 1  3 -2 | -1       | ~ Sčítací metoda sem    | 0  4  0 | 0        | ~ Sčítací metoda sem    | 0  0  0 | 0        |
```
## Vyjádření z poslední řádky
```
-x+y-2z=1-> x=-2t-1
2y=0-> y=0
0=0->z=t,t∈R
```
## Výsledek
```
[x y z] = [-2t-1 0 t],t∈R
```
# Příklad 3
```
1+x+2z=0
x+y=0
-x+1=y
x+y=-z
```
## Uprava rovnic
```
x+y=0->y=-x
-x+1=y->-x+1=-x->1=0
```
## Výsledek
```
Neexistuje řešení (1 není rovno 0)
```
# Příklad 4
```
-x_1+3x_2+x_4=0
2x_1-5x_2+x_3-x_4=1
x_2+x_3+x_4=1
x_1+x_2+x_3=0
```
## Převedení do matice a serazení do trojúhelníkového tvaru
```
| x_1 x_2 x_3 x_4 | Vysledek | ~                       |
| -1   3   0   1  | 0        | ~ Sčítací metoda Z toho |
|  2  -5   1  -1  | 1        | ~ Sčítací metoda sem    |
|  0   1   1   1  | 1        | ~                       |
|  1   1   1   0  | 0        | ~ Sčítací metoda sem    |
```

# Příklad 5
```
x_1+x_2+x_3+x_4=0
2x_+-3x2+x_3-X_4=1
-x_1+x_2-2x_3-x_4=-2
-x_1+x_2-2x_3-x_4=-2
4x_1-3x_2+4x_3-x_4=0
```
---
# Druhá metoda
# Jordanova eliminace (Gaussova eliminace s úplnou redukcí)
- Převedení do matice a serazení do trojúhelníkového tvaru a následně do diagonálního tvaru
