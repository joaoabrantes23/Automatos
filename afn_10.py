class AFN_ZeroSeguidoDeUm:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: inicial, q2: aceito
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q2'

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return 'q1'  
        elif estado == 'q1':
            if caractere_entrada == '1':
                return 'q2'  
            return 'q1'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual == self.estado_aceitacao

# Testando
afn4 = AFN_ZeroSeguidoDeUm()
print(afn4.aceita("01"))    # True
print(afn4.aceita("10"))    # False
print(afn4.aceita("001"))   # True
print(afn4.aceita("00011"))  # True
print(afn4.aceita("111"))    # False
