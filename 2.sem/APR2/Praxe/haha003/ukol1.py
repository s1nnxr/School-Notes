## ❖ Úloha

#Doplňte do třídy Book metody `__repr__` a `__str__`.

#<!-- ```python
class Book:
  def __init__(self, name: str, abstract: str = ''):
    
    self.name     = name
    self.abstract = abstract

  def __str__(self):
    return self.name

  def __repr__(self):
    return f'{self.name} [{self.abstract}]'

library = [
  Book('Lord of the Rings', 'One ring to rule them all!'),
  Book('Silmarillion',      'Ainulindalë, Valaquenta, ...')
]

for book in library:
  print(book)

for book in library:
  print(repr(book))
#``` -->

