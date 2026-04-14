# Master Theorem
## Věta:
nechť $a,c$ jsou cela čísla, $a\geq 1, c>1$ nechť $T(n)=a*T(n/c)+f(n)$ 
kde $f(n)$ je asymptoticky pozitivní funkce. Pak platí:
1. Pokud $f(n)=O(n^{\log_c a-\epsilon})$ pro nějaké $\epsilon > 0$, pak $T(n)=\Theta(n^{\log_c a})$.
2. Pokud $f(n)=\Theta(n^{\log_c a})$, pak $T(n)=\Theta(n^{\log_c a} \log n)$.
3. Pokud $f(n)=\Omega(n^{\log_c a+\epsilon})$ pro nějaké $\epsilon > 0$ a pokud $a*f(n/c) \leq k*f(n)$ pro nějaké konstantní $k < 1$ a dostatečně velné $n$, pak $T(n)=\Theta(f(n))$.

