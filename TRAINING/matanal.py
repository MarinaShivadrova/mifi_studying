# тренировка операций множества

A = {'ID453', 'ID312', 'ID41', 'ID3', 'ID500', 'ID920', 'ID36', 'ID27'}
B = {'ID41', 'ID36', 'ID27', 'ID124', 'ID7', 'ID501', 'ID91' }
union_AB = A.union(B)
union_AB = A | B
inter_AB = A.intersection(B)
diff_AB = A - B


# тренировка библиотеки SymPy
from sympy import FiniteSet, Union, pprint
l1 = [1, 3, 7, 10] #здесь список
l2 = [9, 7, 1]
s = FiniteSet(*l1) #создание конечного множества 
d = FiniteSet(*l2) #звездочка для распаковки 
print(Union(s, d))

