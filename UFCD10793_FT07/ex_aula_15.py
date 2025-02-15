'''
Exercício 15 - Tuplas aninhadas:
'''

nested_tuple = ((20, 40, 60), (10, 30,50),"Python")

# access the first item of the third tuple
print(nested_tuple[2][0]) # P

# iterate a nested tuple
for i in nested_tuple:
    print("tuple", i, "elements")
    for j in i:
        print(j, end=", ")
    print("\n")