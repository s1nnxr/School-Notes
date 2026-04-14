# cisla = [5,2,1,33,8,3,6,11,2]
# bubble sort
# for iopak in range(len(cisla)):  

#     for idx in range (len(cisla)-1-iopak):
#         if cisla[idx] > cisla[idx +1]:
#             cisla[idx], cisla[idx +1] = cisla[idx+1], cisla[idx]
                
# print(cisla)

# cisla = [5,2,1,33,8,3,6,11,2]
# # selection sort
# for iopak in range(len(cisla)):  
#     max_idx = iopak #kde to zacne po kazdm cyklu
#     for idx in range (iopak+1,len(cisla)): 
#         if cisla[idx] > cisla[max_idx]:
#             tmp = cisla[idx]
#             cisla[idx] = cisla[max_idx]
#             cisla[max_idx] = tmp
#            #cisla[iopak],cisla[max_idx] = cisla[max_idx],cisla[iopak] //toto je pythonsky,ale pres temp to taky jde

# print(cisla)
#---------------------------------
# cisla = [5,2,1,33,8,3,6,11,2]
# #insertion sort

# for idx in range(1,len(cisla)):
#     next_num = cisla[idx]
#     current_num = idx - 1

#     while current_num >=0 and next_num < cisla[current_num]:
#         cisla[current_num+1] = next_num[current_num]
#         current_num -= 1
#     cisla[current_num+1] = next_num

# print(cisla)

cisla = [5,2,1,33,8,3,6,11,2]
for iopak in range(1, len(cisla)):
    prehozeno = False
    for izpet in range(iopak-1,-1-1):
        if cisla[izpet] > cisla[iopak]:
            cisla.insert(izpet+1,cisla.pop(iopak))
            prehozeno = True
        else:
            if not prehozeno:
                cisla.insert(0,cisla.pop(iopak))
        print(cisla)

print(cisla)
