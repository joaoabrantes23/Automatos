class AFD_ImparZerosEUns:
    def __init__(self):
        self.estados = {'q00', 'q01', 'q10', 'q11'}  # q00: (par, par), q01: (par, ímpar), q10: (ímpar, par), q11: (ímpar, ímpar)
        self.estado_inicial = 'q00'
        self.estados_aceitacao = {'q01', 'q10', 'q11'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q00':
            if caractere_entrada == '0':
                return 'q10' 
            else:
                return 'q01'  
        elif estado == 'q01':
            if caractere_entrada == '0':
                return 'q11'  
            else:
                return 'q00'  
        elif estado == 'q10':
            if caractere_entrada == '0':
                return 'q00'  
            else:
                return 'q11' 
        elif estado == 'q11':
            if caractere_entrada == '0':
                return 'q01'  
            else:
                return 'q10'  
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFD
afd3 = AFD_ImparZerosEUns()
print(afd3.aceita("01"))     # True
print(afd3.aceita("00"))    # False
print(afd3.aceita("110"))     # True
print(afd3.aceita("0101"))   # False
print(afd3.aceita("00111"))   # True
