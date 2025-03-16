'''
My Fancy Terminal
* class Colors
* def fprint
* def print - replaces original print to add the "color" parameter


Usage:
from my_fancy_terminal import print, Colors as Cores
print('Hello World!', color=Cores.RED)

'''
import builtins

# backup a função original de print
builtins.__original_print = print

class Colors:
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
    color = kwargs.get('color', Colors.RESET)
    end = kwargs.get('end', '\n')

    # args
    texto = ' '.join(map(str, args))

    fancy = color + texto + Colors.RESET
    builtins.__original_print(fancy, end=end)

def print(*args, **kwargs):
    fprint(*args, **kwargs)

if __name__ == '__main__':
    print('Hello World!', color=Colors.RED)