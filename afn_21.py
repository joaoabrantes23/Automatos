class AFN_AposCadaBUmA:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: inicial, q1: após 'b', q2: aceito
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0', 'q2'}  # aceita se terminar em q0 ou q2

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == 'a':
                return 'q0'  
            elif caractere_entrada == 'b':
                return 'q1'  
        elif estado == 'q1':
            if caractere_entrada == 'a':
                return 'q0'  
            else:
                return 'q1'  
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFN
afn21 = AFN_AposCadaBUmA()
print(afn21.aceita("ab"))    # True
print(afn21.aceita("abab"))   # False
print(afn21.aceita("baa"))   # False
print(afn21.aceita("aaba"))  # True
