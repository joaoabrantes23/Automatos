class AFD_InicioFimMesmo:
    def __init__(self):
        self.estado_inicial = 'q0'  # Estado inicial
        self.estados_aceitacao = {'q3'}  # Aceita strings que começam e terminam com o mesmo caractere
        self.estado_atual = self.estado_inicial
        self.primeiro_caractere = None  # Variável para armazenar o primeiro caractere

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            self.primeiro_caractere = caractere_entrada
            if caractere_entrada == '0':
                return 'q1'
            elif caractere_entrada == '1':
                return 'q2'
        elif estado == 'q1':
            if caractere_entrada == '0':
                return 'q1'
            elif caractere_entrada == '1':
                return 'q2'
        elif estado == 'q2':
            if caractere_entrada == '0':
                return 'q1'
            elif caractere_entrada == '1':
                return 'q2'
        
        return estado

    def aceita(self, string_entrada):
        self.estado_atual = self.estado_inicial
        
        # Processa cada caractere da string de entrada
        for char in string_entrada:
            self.estado_atual = self.transicao(self.estado_atual, char)
        
        # Verifica se o último caractere é igual ao primeiro
        if string_entrada and string_entrada[-1] == self.primeiro_caractere:
            return True
        else:
            return False


# Testes
afd = AFD_InicioFimMesmo()

# Testes no formato desejado
print(afd.aceita("111"))     # True
print(afd.aceita("00"))      # True
print(afd.aceita("01"))      # False 
print(afd.aceita("110010"))  # False 
print(afd.aceita("10001"))   # True
print(afd.aceita("010"))     # True