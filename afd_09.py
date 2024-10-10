class AFD_Contem101:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q3'
        self.estado_atual = self.estado_inicial

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '1':
                return 'q1'
            return 'q0'
        elif estado == 'q1':
            if caractere_entrada == '0':
                return 'q2'
            return 'q1'
        elif estado == 'q2':
            if caractere_entrada == '1':
                return 'q3'
            return 'q0'
        return estado

    def aceita(self, string_entrada):
        self.estado_atual = self.estado_inicial
        
        for char in string_entrada:
            self.estado_atual = self.transicao(self.estado_atual, char)
        
        return self.estado_atual == self.estado_aceitacao

# Testando
afd1 = AFD_Contem101()
print(afd1.aceita("10100"))   # True
print(afd1.aceita("1101"))  # True
print(afd1.aceita("000"))   # False
