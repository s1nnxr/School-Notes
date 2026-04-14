# Důležité vlastnosti řadicích algoritmů:
# - časová náročnost (složitost) [O(?)](https://en.wikipedia.org/wiki/Time_complexity)
# - stabilita (zachování pořadí stejných prvků)
# - in-place (třídí na místě, v původním seznamu)
# - paměťová náročnost (složitost)  [O(?)](https://en.wikipedia.org/wiki/Time_complexity)
# Bubble sort
from typing import TypeAlias
Idx: TypeAlias = int
Val: TypeAlias = int|float

def bubbleSort(lst: list[Val]) -> None:
  '''Brute-force bubble sort'''
  def qswap(i: int):
    '''Exchanges items at [i] and [i+1], if needed.'''
    if lst[i] > lst[i+1]:
      lst[i], lst[i+1] = lst[i+1], lst[i]

  # O(n**2)
  ll = len(lst)
  for _ in range(ll-1):
    for i in range(ll-1):
      qswap(i)

from typing import Callable

class TestException(Exception):
  def __init__(self, lst:list, lst2:list):
    super().__init__(f'failed to sort {lst}, got {lst2}')

class TestSort:
  def __init__(self, algorithm: Callable[[list], None]):
    self.algo = algorithm
    self.runCnt = 0

  def testSort(self, lst: list):
    '''Test sorting a single list'''
    # sort a copy of the list
    lst2 = lst.copy()
    self.algo(lst2)
    # compare with the built-in sort
    if lst2 != sorted(lst):
      raise TestException(lst, lst2)
    # count tests
    self.runCnt += 1

  @staticmethod
  def randLst(n: int, lo=0, hi=100) -> list[int]:
    '''Generate a list of n random integers between lo and hi'''
    from random import randint
    return [randint(lo,hi) for _ in range(n)]

  def __run(self):
    '''Run tests'''

    # specific lists
    cornerCases = [
      [], [1], [1,1,1,1,1],
      [1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1]
    ]

    for lst in cornerCases:
      self.testSort(lst)

    # random lists
    for n in range(120):
      self.testSort(self.randLst(n))

  def run(self):
    try:
      self.__run()
      print('OK,', self.runCnt, 'tests run')
    except TestException as e:
      print(e)

if __name__ == '__main__':
    TestSort(bubbleSort).run()


