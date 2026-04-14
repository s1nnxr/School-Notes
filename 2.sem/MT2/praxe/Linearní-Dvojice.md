# Cvičení 1
## Zadání
$$2x+3y=7$$
$$2x-y=3$$
## Řešení normálně
>Nejprve si z druhé rovnice vyjádříme $x$:
$$2x-y=3 \Rightarrow 2x=3+y \Rightarrow x=\frac{3+y}{2}$$
>Nyní tento výraz pro $x$ dosadíme do první rovnice:
$$2\left(\frac{3+y}{2}\right)+3y=7$$
Zjednodušíme:
$$3+y+3y=7$$
$$4y=4$$
$$y=1$$
>Nyní, když známe hodnotu $y$, můžeme ji dosadit zpět do výrazu pro $x$:
$$x=\frac{3+y}{2}=\frac{3+1}{2}=\frac{4}{2}=2$$
## Řešení pomocí linearní funkce
$$3y=7-2x$$
$$y=-\frac{2}{3}x+\frac{7}{3}$$
$$y=-2x+3$$
### Určíme si prusečíky s x a y a střed je výsledný bod
# Cvičení 2
$$x-2y=1\rightarrow x=1+2y$$
$$4y-2x=-2\rightarrow y=\frac x2-\frac12$$

---
$$4y-2(1+2y)=-2=>-2=-2$$

> [!Shrnutí]
> Prostě zjistíme průsečíky s osami a střed nám dá řešení. V tomto případě je to nekonečně mnoho řešení, protože obě rovnice jsou ve skutečnosti stejné.
## Zapis parametrické vyjadření přímky
$x=a$
$y=\frac a2-\frac12, a\in\mathbb{R}$
$x=1+2b$
$y=b, b\in\mathbb{R}$

---
# Uvod do vektorů
## Příklad
$(2;3)$
## Grafické znázornění vektoru
```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [0,2,0,3]
disableZoom: true
grid: true
---
y=x*1.5
```

$Směrnicové\ výjádření:y=ax+b\rightarrow a\ je\ směrnice$
# Přímka procházející počátkem
$[x;y]=[0;0]$
$0=a*0+b\to b=0$
$y=a*x$
# Pro x=1 je y=a

---
## 2x-y=5 a -6x+4y=1
$6x-3y=15$
$-6x+4y=1$
Součet rovnic:
$0=16$
> [!Shrnutí]
> Neexistuje žádné řešení, protože rovnice jsou nekonzistentní. To znamená, že přímky jsou rovnoběžné a nikdy se neprotnou.
### vyjádření
$y=2x-5$
### Průsečíky
Px: $y=0\to 2x-5=0\to x=\frac52$
Py: $x=0\to y=-5$

### vyjádření
$3y=1+6x\to y=\frac{1}{3}+2x$
### Průsečíky
Px: $y=0\to \frac{1}{3}+2x=0\to x=-\frac{1}{6}$
Py: $x=0\to y=\frac{1}{3}$

# -x+y-2z=1 a x+y+2z=-1 a x+3y+2z=-1

---
$-x=y-2z+1$
$0+2y+0=0\to y=0$
$x+3y+2z=-1$

---
$-x=y-2z+1$
$y=0$
$x+3y+2z=-1\to0=0$
> [!Shrnutí]
> Jelikož nám 3tí rovnice vychází jako 0=0, volíme parametr na příklad x=c, $c\in R$
## Parametrické vyjádření:
$x=c$
$y=0$
$z=-\frac{1}{2}c-\frac{1}{2}$

---
# 2x-3y+z=1 a -x+2z=0 a 3x-3y-z=1
## Vyjadření Z
$-x+2z=0\to x=2z$
## Dosazení do první rovnice
$2(2z)-3y+z=1\to 5z-3y=1$
## Dosazení do třetí rovnice
$3(2z)-3y-z=1\to 5z-3y=1$
> [!Shrnutí]
> Obě rovnice nám dávají stejnou rovnici, takže máme nekonečně mnoho řešení. Zvolíme parametr z=d, $d\in R$
> Vysledek je tedy:
> $x=2d$
> $y=\frac{5d-1}{3}$
> $z=d$
---
# x-2y+z=5 a -2x+3y+z=1 a x+3y+2z=2
## Vyjadření x
$x=5+2y-z$
## Dosazení do druhé rovnice
$-2(5+2y-z)+3y+z=1\to -10-4y+2z+3y+z=1\to -10-y+3z=1\to -y+3z=11$
## Dosazení do třetí rovnice
$(5+2y-z)+3y+2z=2\to 5+2y-z+3y+2z=2\to 5+5y+z=2\to 5y+z=-3$
## Vyjádření z první rovnice
$z=5+2y-x$
## Vyjadření z druhé rovnice (y)
$y=3z-11$
## Dosazení do třetí rovnice
$5(3z-11)+z=-3\to 15z-55+z=-3\to 16z=52\to z=3.25$
## Dosazení z do rovnice pro y
$y=3(3.25)-11\to y=-1.75$
## Dosazení z a y do rovnice pro x
$x=5+2(-1.75)-3.25\to x=5-3.5-3.25\to x=-1.75$
---
# x-y+3z=0 a x+2y-3z=0 a 2x+y=0
> [!Trivialní řešení]
> Veškeré body se setkají alespoň v jednom bodě, a to v počátku (0;0;0).

## ale uchylům to nestačí tak počítáme dál
## Vyjadření y z třetí rovnice
$y=-2x$
## Dosazení do první rovnice
$x-(-2x)+3z=0\to 3x+3z=0\to x+z=0\to z=-x$
## Dosazení do druhé rovnice
$x+2(-2x)-3(-x)=0\to x-4x+3x=0\to 0=0$
## Výslede:
$x=e, e\in R$
$y=-2e$
$z=-e$

Příští tejden parametrické řešení 2 rovniřešení 2 rovnic
---

$x+2y=4$
$2x+4y=8$
