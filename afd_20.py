class AFD_SequenciaAbUmaVez:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: inicial, q1: após 'a', q2: após 'ab', q3: aceito
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == 'a':
                return 'q1'
            else:
                return 'q0' 
        elif estado == 'q1':
            if caractere_entrada == 'b':
                return 'q2' 
            else:
                return 'q1'  
        elif estado == 'q2':
            if caractere_entrada == 'a':
                return 'q2'  
            elif caractere_entrada == 'b':
                return 'q3' 
        elif estado == 'q3':
            return 'q3'  
        
        return estado

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFD
afd4 = AFD_SequenciaAbUmaVez()
print(afd4.aceita("ab"))        # True
print(afd4.aceita("aab"))       # False
print(afd4.aceita("abab"))      # False
print(afd4.aceita("ba"))        # False
print(afd4.aceita("abc"))       # True
