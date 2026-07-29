import re

class LLParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected_token):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == expected_token:
            self.pos += 1
            return True
        return False

    def parse_E(self):
        # E -> num E'
        if self.match('num'):
            return self.parse_E_prime()
        return False

    def parse_E_prime(self):
        # E' -> + num E'
        if self.match('+'):
            if self.match('num'):
                return self.parse_E_prime()
            return False
        # E' -> epsilon
        return True 

    def parse(self):
        success = self.parse_E()
        if success and self.pos == len(self.tokens):
            return True
        return False

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
    print("          ANALIZADOR LL (Top-Down)       ")
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
        parser = LLParser(tokens)
        if parser.parse():
            print("-> Resultado: ¡Expresión VÁLIDA!\n")
        else:
            print("-> Resultado: Expresión INVÁLIDA\n")
