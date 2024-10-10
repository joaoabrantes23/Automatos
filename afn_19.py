class AFN_ContemSubstring010:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: inicial, q1: após '0', q2: após '01', q3: aceito
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q3'

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return 'q1'
            else:
                return 'q0'  
        elif estado == 'q1':
            if caractere_entrada == '0':
                return 'q1'  
            else:
                return 'q2'  
        elif estado == 'q2':
            if caractere_entrada == '0':
                return 'q3'  
            else:
                return 'q0' 
        elif estado == 'q3':
            return 'q3'  
        
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual == self.estado_aceitacao

# Testando o AFN
afn3 = AFN_ContemSubstring010()
print(afn3.aceita("010101"))     # True
print(afn3.aceita("1100"))    # False
print(afn3.aceita("000"))     # False
print(afn3.aceita("010"))     # True
print(afn3.aceita("1110101"))  # True
