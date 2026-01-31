'''
main function 
offer 
'''

from LinkList import *
from Frame import *
from scheme_eval import *

def interact(globe_env):
    try:
        inpu = input(">>> ")
        expr = intepret(inpu)
        outpu = str(evaluate(expr, globe_env))
        print(outpu)
    except Exception as e:
        print(f'{inpu} failed')
        print(e)

def intepret(inpu):
    def type_translate(atom):
        try:
            return int(atom)
        except ValueError:
            try:
                return float(atom)
            except ValueError:
                pass
        if atom == '#t':
            return True
        if atom == '#f':
            return False
        if atom == 'nil':
            return nil
        return atom

    def tokenize(source):
        tokens = []
        current = ''
        for ch in source:
            if ch in '()':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append(ch)
            elif ch.isspace():
                if current:
                    tokens.append(current)
                    current = ''
            else:
                current += ch
        if current:
            tokens.append(current)
        return tokens

    def parse_tokens(tokens):
        if not tokens:
            raise Exception('empty input')
        token = tokens.pop(0)
        if token == '(':
            elements = []
            while tokens and tokens[0] != ')':
                elements.append(parse_tokens(tokens))
            if not tokens:
                raise Exception('missing closing parenthesis')
            tokens.pop(0)  # drop ')'
            pair = nil
            for element in reversed(elements):
                pair = LinkList(element, pair)
            return pair
        if token == ')':
            raise Exception('unexpected closing parenthesis')
        return type_translate(token)

    tokens = tokenize(inpu)
    return parse_tokens(tokens)


def interact_mode():
    globe_env = Frame()
    while True:
        interact(globe_env)