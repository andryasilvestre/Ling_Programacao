# Juntar coleções tipo set

set1 = {'Maggie', 'Petunia', 'Freddie', 'Melgs', 1}
set2 = {1, 2, 3, 4, 5}

# set1.update(set2)     # --- modifica o set1
# print(set1)

set3 = set1.union(set2)
print(set3)

# set1.intersection_update(set2)
# print(set1)

set1.symmetric_difference_update(set2)      # o que é diferente nos 2 e modifica as coleções originais.
print(set1)

set1 = {'Maggie', 'Petunia', 'Freddie', 'Melgs', 1}
set2 = {1, 2, 3, 4, 5}

set3 = set1.symmetric_difference(set2)
print(set3)