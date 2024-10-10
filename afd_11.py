class AFD_NumeroImparAs:
    def __init__(self):
        self.estado_inicial = 'q0'  # Estado inicial
        self.estado_aceitacao = 'q1'  # Estado de aceitação
        self.estado_atual = self.estado_inicial

    def transicao(self, estado, caractere_entrada):
        if caractere_entrada == 'a':
            return 'q1' if estado == 'q0' else 'q0'
        return estado  

    def aceita(self, string_entrada):
        self.estado_atual = self.estado_inicial
        
        for char in string_entrada:
            self.estado_atual = self.transicao(self.estado_atual, char)
        
        return self.estado_atual == self.estado_aceitacao

# Testando
afd2 = AFD_NumeroImparAs()
print(afd2.aceita("a"))      # True
print(afd2.aceita("aa"))     # False
print(afd2.aceita("aaab"))    # True
