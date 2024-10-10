class AFN_DivisivelPor3:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: inicial e aceito, q1, q2
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q0'

    def transicao(self, estado, caractere_entrada):
        if caractere_entrada == '0':
            if estado == 'q0':
                return 'q1'
            elif estado == 'q1':
                return 'q2'
            elif estado == 'q2':
                return 'q0'
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        return estado_atual == self.estado_aceitacao

# Testando
afn3 = AFN_DivisivelPor3()
print(afn3.aceita("000"))   # True
print(afn3.aceita("001111000"))    # False
print(afn3.aceita("10100"))  # True
