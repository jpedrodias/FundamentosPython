'''
Exercício 7 - calcula o consumo por litro + msg

Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro
ex07.py).
'''

distancia = float(input('Introduza a distância percorrida em km: '))
litros = float(input('Introduza a quantidade de litros consumidos: '))
consumo = distancia / litros

msg = f'O consumo é de {consumo:.2f} km/l'
if consumo > 10:
    msg += '''
Consumo muito elevado.
(SUVs grandes, veículos desportivos ou condução agressiva em cidade).'''

elif consumo > 8:
    msg += '''
Consumo elevado.
(SUVs médios ou grandes, veículos com motores mais potentes).'''

elif consumo >= 6:
    msg += '''
Consumo alto.
(A maioria dos veículos ligeiros convencionais a gasolina ou Diesel).
'''

elif consumo >= 4:
    msg += '''
Consumo baixo.
(Veículos compactos, híbridos convencionais ou a Diesel eficiente em rodovia).'''

else:
    msg += '''
Consumo muito baixo.
(Muito raro, geralmente veículos híbridos plug-in ou extremamente eficientes a Diesel)'''

print(msg)