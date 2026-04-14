# Spojové Datové Struktury
paměťová struktura tvořena systémem uzlů propojených vzájemnými odkazy
využití:
- Reprezentace grafů (grafových struktur)
- Spojové seznamy (linked lists)


---
## Jak fungují spojové datové struktury
```
| head  | 
   ↓
| Value |               | Tail  |
| next  | → | Value |      ↓
            | next  | → | Value | 
                        | next  | → None
```

---
## K čemu je head a tail
- head: odkaz na první uzel v seznamu, umožňuje přístup k celé struktuře
- tail: odkaz na poslední uzel, usnadňuje přidávání nových uzlů na konec seznamu


---
## Odstranění prvního uzlu
- Aktualizace head na další uzel v seznamu
- Garbage collector odstraní původní první uzel, pokud již není referencován
- Když je seznam prázdný, head a tail jsou nastaveny na None, což indikuje prázdný seznam


---
# Logický návrh
```python
class Node:
    def __init__(self, value):
        ...
    def append(self, new_node):
        ...

class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        ...
    def preppend(self, value):
        ...
    def append(self, value):
        ...
    def pop_first(self):
        ...
```

---
# Implementace

```

   Self
    ↓
| Value |
| next  | → | Value | 
            | next  | → None
new_node      ↑
    ↓         ↑ 
| Value |     ↑
| next  | →   ↑
# bum bác
| Value |
| next  | → | Value | 
            | next  | → None
   Self       ↑
    ↓         ↑ 
| Value |     ↑
| next  | →   ↑
```
```python
class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def append(self, new_node):
        new_node.next = self.next

class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
        self.tail = None
    def preppend(self, value):
        new_node = _Node(value)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def append(self, value):
        new_node = _Node(value)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop_first(self):
        if self.empty():
            raise IndexError("Cannot pop from an empty list")
        self.head = self.head.next
        # Problém. když máme jen jeden uzel, musíme aktualizovat i tail
        if self.head is None:
            self.tail = None
        return self.head.value
    def to_list(self):
        result =[]
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result
    def empty(self)-> bool:
        # assert self.
        return self.head is None and self.tail is None
s = LinkedList()
```

