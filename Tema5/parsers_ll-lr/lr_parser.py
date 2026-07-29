import re

class LRParser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        stack = []
        print("--- Trazabilidad del Analizador LR ---")
        
        for token in self.tokens:
            stack.append(token) # Acción SHIFT (Desplazamiento)
            print(f"Shift: {token: <5} | Pila: {stack}")
            
            # Acción REDUCE (Reducción)
            reduced = True
            while reduced:
                reduced = False
                # Regla: num -> E
                if len(stack) >= 1 and stack[-1] == 'num':
                    stack[-1] = 'E'
                    print(f"Reduce: num -> E | Pila: {stack}")
                    reduced = True
                # Regla: E + E -> E
                elif len(stack) >= 3 and stack[-3:] == ['E', '+', 'E']:
                    stack.pop() # Sacar 'E'
                    stack.pop() # Sacar '+'
                    stack[-1] = 'E' # Reemplazar el primer 'E'
                    print(f"Reduce: E+E -> E | Pila: {stack}")
                    reduced = True

        return len(stack) == 1 and stack[0] == 'E'

def tokenize(user_input):
    tokens = []
    raw_tokens = re.findall(r'\d+|[+]', user_input)
    for rt in raw_tokens:
        if rt.isdigit():
            tokens.append('num')
        elif rt == '+':
            tokens.append('+')
    return tokens

if __name__ == '__main__':
    print("=========================================")
    print("        ANALIZADOR LR (Bottom-Up)        ")
    print("=========================================")
    print("Ingrese una expresión (ej. 5 + 3) o 'salir' para terminar.")
    while True:
        try:
            user_input = input(">> ")
        except EOFError:
            break
        if user_input.lower() in ['salir', 'exit', 'quit']:
            break
            
        tokens = tokenize(user_input)
        if not tokens:
            print("No se reconocieron tokens válidos. Intente de nuevo.\n")
            continue
        
        print(f"Tokens a procesar: {tokens}")
        parser = LRParser(tokens)
        if parser.parse():
            print("-> Resultado: ¡Expresión VÁLIDA!\n")
        else:
            print("-> Resultado: Expresión INVÁLIDA\n")
