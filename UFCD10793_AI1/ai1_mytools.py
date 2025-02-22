

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