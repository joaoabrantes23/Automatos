class AFN_Contem101ou110:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}  # q3 e q6: aceitação
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3', 'q6'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '1':
                return 'q1'
        elif estado == 'q1':
            if caractere_entrada == '0':
                return 'q2'
            elif caractere_entrada == '1':
                return 'q4'
        elif estado == 'q2':
            if caractere_entrada == '1':
                return 'q3'
        elif estado == 'q4':
            if caractere_entrada == '1':
                return 'q5'
            elif caractere_entrada == '0':
                return 'q6'
        elif estado == 'q5':
            if caractere_entrada == '0':
                return 'q6'
        elif estado == 'q3' or estado == 'q6':
            return estado  # permanece em estado de aceitação
        return 'q0'

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFN
afn23 = AFN_Contem101ou110()
print(afn23.aceita("101"))      # True
print(afn23.aceita("110"))      # True
print(afn23.aceita("011001"))     # True
print(afn23.aceita("011101"))    # True
print(afn23.aceita("000"))      # False
