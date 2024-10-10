class AFN_ComprimentoPar:
    def __init__(self):
        self.estados = {'q0', 'q1'}  # q0: inicial e aceito, q1: ímpar
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            return 'q1'  
        elif estado == 'q1':
            return 'q0'  
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFN
afn1 = AFN_ComprimentoPar()
print(afn1.aceita("ab"))       # True (par)
print(afn1.aceita("a"))        # False (ímpar)
print(afn1.aceita("abab"))     # True (par)
print(afn1.aceita("aabb"))     # True (par)
print(afn1.aceita("aaa"))      # False (ímpar)
