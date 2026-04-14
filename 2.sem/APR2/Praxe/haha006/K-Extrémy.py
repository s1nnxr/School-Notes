from typing import TypeAlias
Idx: TypeAlias = int
Val: TypeAlias = int|float

def k_max(lst: list[Val], k:int=1) -> list[tuple[Val,Idx]]|None:
  '''Return k max. items as a sorted list of tuples (value,index)'''

  if not lst or k<1: return None    # ensure correct data

  # result, with up to k candidates from the list front
  res = [(val,i) for i,val in enumerate(lst[:k])]

  # process the rest of the list
  minMax = min(res)                 # minimal (the worst) candidate
  for i,val in enumerate(lst[k:]):
    item = (val,i+k)
    if minMax < item:               # if item is a better candidate,
      res[res.index(minMax)] = item # replace the worst candidate
      minMax = min(res)             # the new worst candidate

  return sorted(res, reverse=True)  # sorted result

# test
lst: list[Val] = [2, 3, 5, 1, 6, 7, 0, 30]
print(k_max(lst, 4))
