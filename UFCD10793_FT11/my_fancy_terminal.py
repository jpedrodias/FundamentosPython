'''
FANCY TERMINAL
* class Cores
* def fprint
'''

class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'

def fprint(*args, **kwargs):
    
    # kargs
    cor = kwargs.get('cor', Cores.RESET)
    end = kwargs.get('end', '\n')

    # args
    texto = ' '.join(map(str, args))

    fancy = cor + texto + Cores.RESET 
    print(fancy, end=end)

    