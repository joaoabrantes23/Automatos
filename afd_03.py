class AFD_ExatamenteDoisUns:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: 0, q1: 1, q2: 2, q3: mais de 2
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q2'

    def transicao(self, estado, caractere_entrada):
        if caractere_entrada == '1':
            if estado == 'q0':
                return 'q1'
            elif estado == 'q1':
                return 'q2'
            elif estado == 'q2':
                return 'q3'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        return estado_atual == self.estado_aceitacao

# Testando
afd3 = AFD_ExatamenteDoisUns()
print(afd3.aceita("110"))   # True
print(afd3.aceita("1011"))   # False
