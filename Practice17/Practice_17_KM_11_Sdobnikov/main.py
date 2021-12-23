import factorial
import exp_root
import logarithm

import os

def get_number(msg, _type, errmsg='Not a number', predicate = lambda a: True):
    while 1:
        inp = input(msg)
        try:
            val = _type(inp)
            if predicate(val): return val
            raise ValueError(errmsg)
        except Exception as e:
            print(f'An error occured: {e}')

def menu():

    funcs_one_arg = [
        [factorial.factorial, int, lambda a: a >= 0],
        [exp_root.root.root2, float, lambda a: True],
        [exp_root.root.root3, float, lambda a: True],
        [exp_root.exponentiation.exp2, float, lambda a: True],
        [exp_root.exponentiation.exp3, float, lambda a: True],
        [logarithm.ln, float, lambda a: a > 0],
        [logarithm.lg, float, lambda a: a > 0]
    ]

    funcs_two_arg = [
            [logarithm.log, float, lambda a: a > 0, lambda a: a > 0 and a != 0]
    ]

    funcs = funcs_one_arg + funcs_two_arg

    print('\nFunctions: \n')

    print(*[f'{funcs_one_arg.index(i)+1}. {i[0].__name__}' for i in funcs_one_arg], sep= '\n')
    print(*[f'{len(funcs_one_arg) + funcs_two_arg.index(i) + 1}. {i[0].__name__}' for i in funcs_two_arg], sep= '\n')

    length = len(funcs_one_arg) + len(funcs_two_arg)

    inp = get_number('Your choice: ', int, errmsg=f'Enter a number between 1 and {length}.', predicate= lambda a: a > 0 and a <= length)
    inp -= 1
    print(f'Function: {funcs[inp][0].__name__}')

    if funcs[inp] in funcs_one_arg:
        arg1 = get_number('Enter argument: ', funcs[inp][1], errmsg='Must be an integer larger than 0', predicate=funcs[inp][2])
        print(f'Result: {funcs[inp][0](arg1)}')

    else:

        arg1 = get_number('Enter argument 1: ', funcs[inp][1], errmsg='Must be a float larger than 0', predicate=funcs[inp][2])
        arg2 = get_number('Enter argument 2: ', funcs[inp][1], errmsg='Must be an float larger than 0 and not equal 1', predicate=funcs[inp][3])

        print(f'Result: {funcs[inp][0](arg1, arg2)}')



clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while 1:
        clear()
        print()
        menu()
        print()
        inp = input('Would you like to continue? Enter `y`: ').replace(' ', '').lower()
        if inp != 'y':
            break
            

if __name__ == '__main__':
    main()