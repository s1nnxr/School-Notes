# ADT - Abstraktní datové typy, sekvenšní datové struktury
# - ***Datová struktura***: způsob organizace dat v paměti počítače
# - ***ADT***: koncepční model, který definuje sadu operací a chování pro datovou strukturu (interface, rozhraní), aniž by specifikoval, jak jsou tyto operace implementovány, ani jak jsou data organizována v paměti.
# - abstrakce ("odtažení"): skrývání detailů

# Příklady ADT
# - Některé ADT jsou v Pythonu vestavěné, jiné je třeba importovat z knihoven nebo implementovat.
# - seznam (list)
# - seřazený seznam (ordered list)
# - ntice (tuple)
# - množina (set)
# - mapa/asociativní pole (dict, dictionary)
# - fronta (queue)
# - prioritní fronta (priority queue)
# - fronta s dvěmi konci (double-ended queue, deque)
# - zásobník (stack)
# - spojový seznam (linked list)
# - dvojitý spojový seznam (double-linked list)
# - graf (graph)
# - strom (tree)

# Upravte implementaci fronty:
# 
# do konstruktoru přidejte volitelný parametr maxSize: int, který (pokud je zadaný) určí maximální délku fronty. Pokud je fronta plná (dosáhla maximální délky), metoda push() prvek do fronty nepřidá, a buď vyvolá výjimku QueueError nebo vrátí False, podle vaší volby.
# přidejte metodu isFull() → bool, která vrátí True, pokud je fronta plná
class Queue:
    def __init__(self, maxSize:int |None=None):
        self._items:list[object]=[]
        self.maxSize:int | None= maxSize
    def isEmpty(self):
        return 0 == self.size()

    def size(self):
        return len(self._items)

    def push(self, item:int): # also: put / enqueue
        self._items.append(item)

    def front(self):
        # raises an exception if empty
      return self._items[0]

    def pop(self):        # also: get / dequeue
        # raises an exception if empty
        return self._items.pop(0)
    
    def __str__(self):
        return str(self._items)


q = Queue()
q.push("Alena")
q.push(True)
q.push(0)
q.push("Pavel")
q.push(5.6)

print(q.pop())
print(q.pop())
print(q)
print(q.front())
print(q.pop())
print(q.pop())
print(q.pop())
# print(q.pop()) # IndexError: pop from empty list
