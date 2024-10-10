class AFD_MaiorQue:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.estado_inicial = 'q0'
        self.estado_atual = self.estado_inicial
        self.estado_aceitacao = 'q1'  # Aceita se houver mais '1's que '0's
        self.contagem = 0  # Contador para a diferença entre '1's e '0's

    def transicao(self, caractere_entrada):
        if caractere_entrada == '1':
            self.contagem += 1  
        elif caractere_entrada == '0':
            self.contagem -= 1  

        # Atualiza o estado com base na contagem
        if self.contagem > 0:
            self.estado_atual = 'q1'  
        elif self.contagem < 0:
            self.estado_atual = 'q2'  
        else:
            self.estado_atual = 'q0'  

    def aceita(self, string_entrada):
        self.estado_atual = self.estado_inicial
        self.contagem = 0  

        for char in string_entrada:
            self.transicao(char)
        
        # Aceita se no final houver mais '1's que '0's
        return self.estado_atual == self.estado_aceitacao

# Testando o AFD
afd_maior = AFD_MaiorQue()
print(afd_maior.aceita("1101001"))  # True 
print(afd_maior.aceita("101"))    # True 
print(afd_maior.aceita("00"))     # False 
print(afd_maior.aceita("0100"))   # False 
