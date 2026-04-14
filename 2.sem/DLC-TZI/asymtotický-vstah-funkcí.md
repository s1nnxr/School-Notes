# Asymptotika
věta:
jestliže $f(n)>0, g(n)>0$ pro $n>n_0$ a existují kladné konstanty $c_1, c_2$ takové, že
$$c_1 g(n) \leq f(n) \leq c_2 g(n)$$
pro $n>n_0$, pak říkáme, že $f(n)$ je asymptoticky stejné jako $g(n)$ a píšeme $f(n) = \Theta(g(n))$.

1. $$\lim_{n \to \infty} \frac{f(n)}{g(n)} \not = 0$$
$$=> f(n) \geq c_1 g(n)$ (n\in \mathbb{R))$$

2. $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = O
$$f(n) O(g(n))$$
