gen_list = [i for i in range(10) if i%3]
gen_set  = {i for i in range(10) if i%3}
gen_dict = {i: str(i) for i in range(10) if i%3}
gen_gen  = (i for i in range(10) if i%3)

print(gen_list)
print(gen_set)
print(gen_dict)
print(gen_gen)
