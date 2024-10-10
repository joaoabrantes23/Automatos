class AFD_TerminaComUm:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # Estados
        self.estado_inicial = 'q0'  # Estado inicial
        self.estado_aceitacao = 'q1'  # Estado de aceitação

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return 'q0'  
            elif caractere_entrada == '1':
                return 'q1' 
        elif estado == 'q1':
            if caractere_entrada == '0':
                return 'q0' 
            elif caractere_entrada == '1':
                return 'q1'  
        return None  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
            if estado_atual is None:
                return False
        return estado_atual == self.estado_aceitacao

# Testando
afd1 = AFD_TerminaComUm()
print(afd1.aceita("11"))  # True
print(afd1.aceita("1011"))  # True
print(afd1.aceita("00"))    # False