class AFD_Sequencia010DuasVezes:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: início, q1: após '0', q2: após '01', q3: aceitação
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3'}
        self.contagem = 0  # Contador de sequências "010"

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '0':
                return 'q1'  
        elif estado == 'q1':
            if caractere_entrada == '1':
                return 'q2' 
        elif estado == 'q2':
            if caractere_entrada == '0':
                self.contagem += 1  
                return 'q1'  
            else :
                return 'q0'
        
        return estado 

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        self.contagem = 0  
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        # Aceita se a contagem de "010" for pelo menos 2
        return self.contagem >= 2

# Testando o AFD
afd24 = AFD_Sequencia010DuasVezes()
print(afd24.aceita("010010"))          # True, contém duas "010"
print(afd24.aceita("00011110001101000"))  # True, contém duas "010"
print(afd24.aceita("00011101000010"))  # True, contém duas "010"
print(afd24.aceita("010"))             # False, apenas uma "010"
print(afd24.aceita("000"))             # False, nenhuma "010"
print(afd24.aceita("0101010"))         # True, contém exatamente duas "010"
print(afd24.aceita("00100100100"))     # False, apenas uma "010"
print(afd24.aceita("010101010"))       # True, contém mais de duas "010"
print(afd24.aceita("01000110"))        # False, apenas uma "010"
print(afd24.aceita("110"))             # False, não contém "010"
print(afd24.aceita("101010010"))       # True, contém duas "010"
print(afd24.aceita("111010"))          # False, apenas uma "010"
print(afd24.aceita("0100110"))    
