class OrderedList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)


    def glob_max(self,lst):
        max, imax = lst[0], 0
        for i in range(1, len(lst)):
            if max < lst[i]:
                max, imax = lst[i], i
        return imax, max

    def glob_min(self,lst):
        min, imin = lst[0], 0
        for i in range(1, len(lst)):
            if min > lst[i]:
                min, imin = lst[i], i
        return imin, min
    
    def k_max(self,lst,k):
        if k > len(lst):
            return lst
        max_list = []
        for i in range(k):
            imax, max = self.glob_max(lst)
            max_list.append(max)
            lst.pop(imax)
        return max_list

    def k_min(self,lst,k):
        if k > len(lst):
            return lst
        min_list = []
        for i in range(k):
            imin, min = self.glob_min(lst)
            min_list.append(min)
            lst.pop(imin)
        return min_list
    
OL= OrderedList()
for i in range(1, 11):
    OL.add(i)

print(OL.data)
print(OL.k_max(OL.data,3))
print(OL.k_min(OL.data,3))

