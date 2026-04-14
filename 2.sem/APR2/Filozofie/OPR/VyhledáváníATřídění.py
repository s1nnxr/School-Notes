# Vyhledávání
# Definice základního vyhledávání :
# - V(seznam,prvek) -> Boolian
# - V(iterovatelný objekt,prvek) -> Boolian
# Definice užitelnějšího vyhledávání :
# - V(seznam,prvek) -> index prvního prvku v seznamu nebo -1
# - V(iterovatelný objekt,prvek) -> index prvníhoprvku v iterovatelném objektu nebo -1
# Definice ještě užitelnějšího ale vypočetně nevyhodného vyhledávání :
# - V(seznam,prvek) -> všechny indexy prvku v seznamu nebo prázdný seznam
# Složitost vyhledávání :
# binární vyhledávání  : O(log n)
# - Musí být seřazené
# - Prvky musí být indexovatelné
# lineární/trivialní vyhledávání : O(n)
# hashování : O(1) v průměru, O(n) v nejhorším případě
# - Potřebuje dobrou hashovací funkci
# - Může být neefektivní, pokud je mnoho kolizí

# Třídění/Řazení
# Definice třídění -> klasifikace nepoužívat slovo třídění
# Definice řazení -> uspořádání
# Definice základního řazení :
# - V_i=0,n-1 X_i \le i+1

# Druhy oborů řazení :
# Důležité vlastnosti univerzálního řazení :
# - Porovnání
# - Výměna
# Důležité vlastnosti speciálního řazení :
# - Vkládání do balíku (bucketu)
# Rychlost řazení :
# Trivialní/univerzální řazení : O(n^2)
# Specialní : O(n)
# Stabilita řazení :
# - Stabilní řazení : zachovává původní pořadí prvků se stejnou hodnotou
# Adaptivní řazení :
# - Adaptivní řazení : využívá již částečně seřazené struktury dat k urychlení procesu řazení
# Antiadaptivní řazení :
# - Antiadaptivní řazení : quick sort

# Domácí ukol:
# Zjistit jak ne programátoři třídí.
# Druhy třídění :
# - Quick sort : Vyberte pivotní prvek a rozdělte seznam na dvě části, kde jedna obsahuje prvky menší než pivot a druhá obsahuje prvky větší než pivot. Pak rekurzivně seřaďte obě části.
# - Merge sort : Dělí seznam na dvě poloviny, seřadí každou polovinu a pak je spojí dohromady.
# - Bucketsort : Dává data do několika "kbelíků" a pak každý kbelík seřadí zvlášť.


# Dva základní trivialní algoritmy pro řazení :
## Selection sort : Pro každý prvek v seznamu najděte nejmenší prvek a vyměňte ho s aktuálním prvkem.
## Složitost : O(n^2) v nejhorším případě, O(n^2) v průměru, O(n^2) v nejlepším případě
## Složitost prohozeni : O(n) v nejhorším případě, O(n) v průměru, O(n) v nejlepším případě
## Stabilita : nestabilní
## Adaptivita : neadaptivní

## Insertion sort : Pro každý prvek v seznamu vložte ho do správné pozice v již seřazené části seznamu.
## Složitost : O(n^2) v nejhorším případě, O(n^2) v průměru, O(n) v nejlepším případě
## Složitost prohozeni : O(n) v nejhorším případě, O(n) v průměru, O(1) v nejlepším případě
## Stabilita : stabilní
## Adaptivní : ano

## Bubble sort : Pro každý prvek v seznamu porovnejte ho s následujícím prvkem a vyměňte je, pokud jsou ve špatném pořadí. Opakujte tento proces, dokud není seznam seřazen.
## Rychnolst : 2 krat pomalejší 
## Stabilita : stabilní
## Adaptivní : antiadaptivní

# 3 Specialní algoritmy pro řazení :
## Quick sort : Vyberte pivotní prvek a rozdělte seznam na dvě části, kde jedna obsahuje prvky menší než pivot a druhá obsahuje prvky větší než pivot. Pak rekurzivně seřaďte obě části.
## Složitost : O(n^2) v nejhorším případě, O(n log n) v průměru, O(n log n) v nejlepším případě
## Složitost prohozeni : O(n) v nejhorším případě, O(log n) v průměru, O(log n) v nejlepším případě
## Stabilita : nestabilní
## Adaptivní : antiadaptivní
## Volby pivotu :
## - Nahodně -> nahodnost je pomalá
## - Median : bere prostřední prvek -> může být pomalé pro již seřazené seznamy
## - První prvek : bere první prvek -> může být pomalé pro již seřazené seznamy

## Merge sort : Dělí seznam na dvě poloviny, seřadí každou polovinu a pak je spojí dohromady, vememe první 2 prvky z každé poloviny a porovnáme je a zařadíme.
## Složitost : O(n log n) v nejhorším případě, O(n log n) v průměru, O(n log n) v nejlepším případě
## Složitost prohozeni : O(n) v nejhorším případě, O(n) v průměru, O(n) v nejlepším případě
## Stabilita : stabilní
## Adaptivní : Nezáleží na vstupu, ale není adaptivní
## Stabilita : Stabilní

## Heapsort :  PŘÍŠTĚ


# Neuniverzální algoritmy pro řazení :

## Bucketsort : Dává data do několika "kbelíků" a pak každý kbelík seřadí zvlášť.
## Složitost : O(n + k) v nejhorším případě, O(n + k) v průměru, O(n + k) v nejlepším případě, kde k je počet kbelíků
## Složitost prohozeni : O(n + k) v nejhorším případě, O(n + k) v průměru, O(n + k) v nejlepším případě
## Možnost vylepšení : Použití efektivního algoritmu pro řazení kbelíků, jako je quick sort nebo merge sort

## Radix sort :  PŘÍŠTĚ
