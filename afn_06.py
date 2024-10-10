class AFN_PeloMenosUmZero:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # q0: inicial, q1: aceito
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q1'

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return {'q1'}  
            return {'q0'}  
        return {estado}  

    def aceita(self, string_entrada):
        estados_atuais = {self.estado_inicial}
        for char in string_entrada:
            proximos_estados = set()
            for estado in estados_atuais:
                proximos_estados |= self.transicao(estado, char)
            estados_atuais = proximos_estados
        return self.estado_aceitacao in estados_atuais

# Testando
afn1 = AFN_PeloMenosUmZero()
print(afn1.aceita("111"))   # False
print(afn1.aceita("101"))   # True
print(afn1.aceita("000"))   # True
