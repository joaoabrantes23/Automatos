class AFD_NumeroParZeros:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # q0: par, q1: ímpar
        self.estado_inicial = 'q0'  
        self.estado_aceitacao = 'q0'

    def transicao(self, estado, caractere_entrada):
        if caractere_entrada == '0':
            return 'q1' if estado == 'q0' else 'q0'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        return estado_atual == self.estado_aceitacao

# Testando
afd2 = AFD_NumeroParZeros()
print(afd2.aceita("1100"))  # True
print(afd2.aceita("1000001"))    # False
