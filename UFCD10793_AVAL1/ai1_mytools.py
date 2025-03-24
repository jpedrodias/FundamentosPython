'''
Avaliação Intermédia 1 - my tools set

* better_input(prompt, error_message="Erro! Introduza um número inteiro superior a zero.", data_type=int, not_allowed={})
    Recebe um prompt, uma mensagem de erro, um tipo de dados, e uma lista de valores não permitidos. 
    Devolve um valor introduzido pelo utilizador que corresponda ao tipo de dados e não esteja na lista de valores não permitidos.

'''

def better_input(prompt, error_message="Erro! Introduza um número inteiro superior a zero.", data_type=int, not_allowed={}):
    done = False
    while not done:
        user_input = input(prompt)
        data = None
        try:
            data = data_type(user_input)
            done = True
        except ValueError:
            print(error_message)
        
        if not_allowed and data in not_allowed:
            print(error_message)
            done = False
    
    return data
