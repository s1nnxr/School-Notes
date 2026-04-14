# Jak vytvořit kolekce
# - Kolekce = objekt, jehož hlavní funkce je uchovat jiné objekty
# - Kolekce které už známe:
#   - List = kolekce, která uchovává objekty v určitém pořadí
#   - Dict = kolekce, která uchovává objekty ve dvojicích klíč-hodnota
#   - Tuple = kolekce, která uchovává objekty v určitém pořadí, ale je neměnná
# Další kolekce:
# - Zásobník (stack)
# - Operace:
#   - `push(obj)` = vloží objekt na vrchol zásobníku
#   - `pop()` = odstraní a vrátí objekt z vrcholu zásobníku (naposledy vložený)
#   - NEDEFINOVANÁ OPERACE ZÁSOBNÍKU!!! `empty()` = vrátí True, pokud je zásobník prázdný, jinak False
class Stack:
    def __init__(self): # Vytvoří prázdný zásobník
        self._storage = []
    def push(item) -> None: # Vloží položku na vrchol zásobníku
        self._storage.append(item)
    def pop(self) -> Any: # any vrací libovolný typ co není None
        if len(self._storage):
            return self._storage.pop()
        else:
            raise ValueError("Stack is empty")
    # Verze pro ADT(Abstraktní datový typ) milovníky aka kokoty
    def empty(self) -> bool:
        return not self._storage # je-li seznam pravdivý je prázdný, jinak ne
    # Sintatické pozlátko:
    # Verze pro pythonisty aka kokoty
    def __bool__(self) -> bool: # Pokud je zásobník prázdný, vrátí False, jinak True
        return bool(self._storage)
# - Fronta (queue)
# - Operace:
#   - `enqueue(obj)` = vloží objekt na konec fronty
#   - `dequeue()` = odstraní a vrátí objekt z přední části fronty (prvně vložený)
#   - NEDEFINOVANÁ OPERACE FRONTY!!! `empty()` = vrátí True, pokud je fronta prázdná, jinak False

class Queue:
    def __init__(self): # Vytvoří prázdný zásobník
        self._storage = []
    def enqueue(item) -> None: # Vloží položku na vrchol zásobníku
        self._storage.append(item) # složitost operace enqueue je O(1)
    def dequeue(self) -> Any: # any vrací libovolný typ co není None
        if len(self._storage):
            return self._storage.pop(0) # složitost operace dequeue je O(n) protože musí posunout všechny prvky o jedno místo dopředu
        else:
            raise ValueError("Queue is empty")
    # Verze pro ADT(Abstraktní datový typ) milovníky aka kokoty
    def empty(self) -> bool:
        return not self._storage # je-li seznam pravdivý je prázdný, jinak ne
    # Sintatické pozlátko:
    # Verze pro pythonisty aka kokoty
    def __bool__(self) -> bool: # Pokud je zásobník prázdný, vrátí False, jinak True
        return bool(self._storage)

# - Omezený slovník (slovníková mezipaměť)
# - Operace:
#   - `put(key, value)` = vloží dvojici klíč-hodnota
#   - `get(key)` = získání hodnoty podle klíče
#     - `put` vkládá novou hodnotu, pokud je v cache místo, jinak přepíše existující klíč (a hodnotu)
#       - Strategie, jaká hodnota bude přepsaná
#         - nejméně používaná (LRU - Least Recently Used)
#         - nejdéle používaná (LFU - Least Frequently Used)
#         - nejdéle alokovaná (FIFO - First In First Out)
#         - náhodná (Random Replacement)
#   - Implementujeme FIFO, je to nejjednodušší a docela effektivní
class Cache:
    def __init__(self, capacity: int): # capacity > 0
        self._capacity = capacity
        self._storage = {}
    def put(self, key: Any, value: Any) -> None:
        if key in self._storage:
            raise ValueError("Cache is not rewritable")
        if len(self._storage) < self._capacity:
            self._storage[key] = value
        if len(self._storage) >= self._capacity:
            del_key = next(iter(self._storage)) # získá první klíč z dictionary
            del self._storage[del_key] # smaže první klíč a jeho hodnotu
        self._storage[key] = value
        
    def get(self, key) -> Any:
        return self._storage[key]
    def __repr__(self) -> str:
        return f"Cache(capacity={self._capacity}, storage={self._storage})"
