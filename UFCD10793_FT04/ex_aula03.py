'''
Exercício de aula 3: nested loops
'''
for i in range(1, 11): #outer loop
    #nested loop
    # iterações de 1 to 10
    for j in range(1, 11):
        # print multiplication
        multiplicacao = i * j
        #print("%d x %d = %d" % (i, j, multiplicacao))
        print(f'{i} x {j} = {multiplicacao}')
print('concluido')