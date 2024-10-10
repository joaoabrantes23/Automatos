class AFN_Substring110:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: inicial, q3: aceito
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q3'

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '1':
                return 'q1'  
            return 'q0' 
        elif estado == 'q1':
            if caractere_entrada == '1':
                return 'q2'  
            return 'q0'  
        elif estado == 'q2':
            if caractere_entrada == '0':
                return 'q3' 
            return 'q2'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual == self.estado_aceitacao

# Testando o AFN
afn110 = AFN_Substring110()
print(afn110.aceita("001110"))  # True
print(afn110.aceita("0110"))    # True
print(afn110.aceita("111"))      # False
print(afn110.aceita("000"))      # False
print(afn110.aceita("01010110"))  # True
print(afn110.aceita("111001"))    # True
