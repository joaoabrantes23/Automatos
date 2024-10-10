class AFN_AAntesDeB:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # q0: aceita 'a', q1: aceita 'b' (após 'a')
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0', 'q1'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == 'a':
                return 'q0'
            elif caractere_entrada == 'b':
                return 'q1'
        elif estado == 'q1':
            if caractere_entrada == 'a':
                return None  # rejeita se 'a' após 'b'
            elif caractere_entrada == 'b':
                return 'q1'
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
            if estado_atual is None:
                return False
        
        return estado_atual in self.estados_aceitacao

# Testando o AFN
afn25 = AFN_AAntesDeB()
print(afn25.aceita("aaabbb"))  # True
print(afn25.aceita("abab"))    # False
print(afn25.aceita("aaa"))     # True
print(afn25.aceita("bbb"))     # True
