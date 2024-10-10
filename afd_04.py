class AFD_PeloMenosUmZero:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # q0: sem '0', q1: com '0'
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q1'

    def transicao(self, estado, caractere_entrada):
        if caractere_entrada == '0':
            return 'q1'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        return estado_atual == self.estado_aceitacao

# Testando
afd4 = AFD_PeloMenosUmZero()
print(afd4.aceita("111"))   # False
print(afd4.aceita("101"))   # True
