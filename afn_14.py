class AFN_SemSubstrings:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: inicial e aceito, q1: último '0', q2: último '1'
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0', 'q1', 'q2'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return 'q1'  
            elif caractere_entrada == '1':
                return 'q2'  
        elif estado == 'q1':
            if caractere_entrada == '0':
                return None 
            elif caractere_entrada == '1':
                return 'q2'  
        elif estado == 'q2':
            if caractere_entrada == '1':
                return None  
            elif caractere_entrada == '0':
                return 'q1' 
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            novo_estado = self.transicao(estado_atual, char)
            if novo_estado is None:
                return False  # Se não há transição válida, a string não é aceita
            estado_atual = novo_estado
        
        return estado_atual in self.estados_aceitacao

# Testando o AFN
afn = AFN_SemSubstrings()
print(afn.aceita("01"))        # True (aceito)
print(afn.aceita("10"))        # True (aceito)
print(afn.aceita("00"))        # False (não aceito)
print(afn.aceita("11"))        # False (não aceito)
print(afn.aceita("010"))       # True (aceito)