class AFD_DiferencaMultiplosDeTres:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: diferença é 0 mod 3, q1: 1 mod 3, q2: 2 mod 3
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0'}  # Aceita se a diferença for múltiplo de 3

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == 'a':
                return 'q1'  
            elif caractere_entrada == 'b':
                return 'q2' 
        elif estado == 'q1':
            if caractere_entrada == 'a':
                return 'q2' 
            elif caractere_entrada == 'b':
                return 'q0'  
        elif estado == 'q2':
            if caractere_entrada == 'a':
                return 'q0' 
            elif caractere_entrada == 'b':
                return 'q1' 
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFD
afd22 = AFD_DiferencaMultiplosDeTres()
print(afd22.aceita("aab"))   # False
print(afd22.aceita("abb"))   # False
print(afd22.aceita("ab"))    # True
print(afd22.aceita("aaaaaabbbab"))  # True
