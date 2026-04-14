# Proč aproximujeme?
# - Někdy nemáme dostatek dat, aby jsme mohly použít data potřebujeme chybějící data odhadnout nějakou jednoduchou funkcí.
## --- Interpolace ---
# - máme n+ mavzájem různých bodů {x_0, x_1,... ,x_n}, které budeme nazývat uzlové body, a funkční hodnoty v chechto uzlových bodech, {f_0, f_1,... ,f_n}. Potom je úlohou interpolace nalézke tunkci, nejčastěji polynom, P_n(x), takovou, aby platilo, že, P(x_i) = f_i pro i=0,1,...,n. Kromě rovnosti funkčních hodnot požadujeme, aby P_n(x) byla co nejjednodušší funkcí, tedy aby její stupeň byl co nejmenší. Pro n+1 uzlových bodů existuje právě jeden polynom stupně n, který prochází všemi těmito body. Tento polynom se nazývá interpolující polynom.

## - Linearní interpolace: spojení dvou bodů přímkou
## - Vandermontova matice: pro n+1 uzlových bodů existuje právě jeden polynom stupně n, který prochází všemi těmito body. Tento polynom se nazývá interpolující polynom. Pro výpočet koeficientů interpolujícího polynomu můžeme použít Vandermondovu matici, která je tvořena hodnotami uzlových bodů. Koeficienty interpolujícího polynomu lze získat řešením soustavy lineárních rovnic, kde Vandermondova matice je koeficientová matice a vektor funkčních hodnot je pravou stranou rovnic.
## - Lagrangeova interpolace: Lagrangeova interpolace je metoda pro konstrukci interpolujícího polynomu, který prochází zadanými body. Lagrangeův polynom se skládá z lineárních kombinací tzv. Lagrangeových bázových funkcí, které jsou definovány tak, aby byly rovny 1 v jednom z uzlových bodů a 0 ve všech ostatních uzlových bodech. Tímto způsobem se zajišťuje, že výsledný polynom prochází všemi zadanými body. Lagrangeova interpolace je často používána pro svou jednoduchost a přehlednost, ale může být numericky nestabilní pro velké množství uzlových bodů.
## - Newtonova interpolace: Newtonova interpolace je další metoda pro konstrukci interpolujícího polynomu. Tato metoda využívá tzv. dělené diference, které jsou založeny na hodnotách funkce v uzlových bodech. Newtonův polynom se skládá z lineárních kombinací těchto dělených diferencí a faktorů, které závisí na rozdílech mezi uzlovými body. Výhodou Newtonovy interpolace je, že umožňuje snadné přidávání nových uzlových bodů bez nutnosti přepočítávat celý polynom, což ji činí efektivní pro postupné zvyšování přesnosti interpolace.
## - Hermiteova interpolace: Hermiteova interpolace je metoda pro konstrukci interpolujícího polynomu, která zohledňuje nejen hodnoty funkce v uzlových bodech, ale také jejich derivace. Tato metoda se používá, když máme k dispozici informace o hodnotách funkce a jejích derivacích v uzlových bodech. Hermiteův polynom se skládá z lineárních kombinací tzv. Hermiteových bázových funkcí, které jsou definovány tak, aby byly rovny 1 v jednom z uzlových bodů a 0 ve všech ostatních uzlových bodech, a zároveň zohledňují hodnoty derivací. Tímto způsobem se zajišťuje, že výsledný polynom prochází všemi zadanými body a má správné hodnoty derivací.
## - Interpolace trigonometrickými polinomy: Interpolace trigonometrickými polynomy je metoda pro konstrukci interpolujícího polynomu, která využívá trigonometrické funkce, jako jsou sinus a kosinus. Tato metoda se často používá pro interpolaci periodických funkcí nebo funkcí definovaných na intervalech, které jsou vhodné pro použití trigonometrických funkcí. Interpolace trigonometrickými polynomy může být efektivní pro zachycení periodických vzorů v datech a může být numericky stabilní pro velké množství uzlových bodů.
## - Splajny
### - Kubické splajny: Kubické splajny jsou metoda pro konstrukci interpolujícího polynomu, která využívá kubické polynomy k interpolaci mezi uzlovými body. Tato metoda se často používá pro interpolaci dat, která jsou hladká a mají spojité první a druhé derivace. Kubické splajny se skládají z lineárních kombinací kubických polynomů, které jsou definovány na intervalech mezi uzlovými body. Tímto způsobem se zajišťuje, že výsledný polynom prochází všemi zadanými body a má správné hodnoty derivací.
## Beziérovy křivky: Beziérovy křivky jsou metoda pro konstrukci interpolujícího polynomu, která využívá Beziérovy křivky k interpolaci mezi uzlovými body. Tato metoda se často používá pro interpolaci dat, která jsou hladká a mají spojité první a druhé derivace. Beziérovy křivky se skládají z lineárních kombinací Beziérovy křivky, které jsou definovány na intervalech mezi uzlovými body. Tímto způsobem se zajišťuje, že výsledný polynom prochází všemi zadanými body a má správné hodnoty derivací.
## - Extrapolace: Extrapolace je metoda pro odhad hodnot funkce mimo interval, na kterém máme k dispozici data. Tato metoda se často používá, když potřebujeme odhadnout hodnoty funkce pro vstupy, které jsou mimo rozsah našich dat. Extrapolace může být prováděna pomocí různých metod, jako jsou lineární extrapolace, polynomická extrapolace nebo exponenciální extrapolace. Je důležité si uvědomit, že extrapolace může být méně spolehlivá než interpolace, protože se snaží odhadnout hodnoty mimo rozsah dat, což může vést k větším chybám.

## --- Aproximace ---
# - Mějme sadu měření, kdy každému uzlovému bodu {x_0, x_1,... ,x_n} odpovídá sudá funkce hodnot {f_0, f_1,... ,f_11,f12,...,f_n1,f_n2}. Potom je úlohou aproximace nalézt vhodnou funkci, která prochází k zadaným bodům v určitém smyslu nejblíže. Vhodnost uvažované funkce lze posuzovaz pomocí minimalizace kvadradické odchylky. 

# Uloha 1 
# Vygenerovat 2 náhodné body a použít vzorec dole pro najdutí bodů mezi
### 1000% můj kód
import numpy as np
import matplotlib.pyplot as plt

"""Ukázka lineární interpolace funkce f(x) = -x^3 + 10x^2 + 6.

Program porovnává přesný průběh funkce s její poúsečkovou lineární aproximací
mezi zadanými uzly a vykreslí obě křivky do jednoho grafu.
"""

def f(x):
    """Vrátí hodnotu funkce f(x) = -x^3 + 10x^2 + 6 pro x (skalár i pole)."""
    return -x**3 + 10 * x**2 + 6

def linearni_interpolace(x0, x1, x, y0, y1):
    """Spočítá lineární interpolaci v bodě/bodech x mezi body (x0, y0) a (x1, y1)."""
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def po_useckach(uzly_x, x):
    """Provede lineární interpolaci po jednotlivých úsecích daných uzly_x."""
    uzly_x = np.array(uzly_x, dtype=float)
    uzly_y = f(uzly_x)
    y_interp = np.empty_like(x, dtype=float)

    for i in range(len(uzly_x) - 1):
        x0, x1 = uzly_x[i], uzly_x[i + 1]
        y0, y1 = uzly_y[i], uzly_y[i + 1]
        maska = (x >= x0) & (x <= x1) if i == len(uzly_x) - 2 else (x >= x0) & (x < x1)
        y_interp[maska] = linearni_interpolace(x0, x1, x[maska], y0, y1)

    return uzly_y, y_interp

def hlavni():
    """Nastaví uzly, vypočítá interpolaci a vykreslí výsledný graf."""
    uzly_x = [-2, 0, 2, 4, 6, 8, 10, 12]

    x = np.linspace(uzly_x[0], uzly_x[-1], 600)
    y_f = f(x)
    uzly_y, y_interp = po_useckach(uzly_x, x)

    print("Uzly (x, f(x)):")
    for x_u, y_u in zip(uzly_x, uzly_y):
        print(f"({x_u:.2f}, {y_u:.2f})")

    plt.figure(figsize=(9, 5))
    plt.plot(x, y_f, label="f(x) = -x^3 + 10x^2 + 6")
    plt.plot(x, y_interp, "--", label="lineární interpolace")
    plt.scatter(uzly_x, uzly_y, color="red", label="uzly")

    plt.title("Lineární interpolace")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    hlavni()


