class AFN_TerminaEm01:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}  # q0: inicial, q1: após '0', q2: após '01', q3: aceito
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3'}

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':
            if caractere_entrada == '1':
                return {'q1'} 
            elif caractere_entrada == '0':
                return {'q2'}
        elif estado == 'q1':
            if caractere_entrada == '0':
                return {'q2'} 
            elif caractere_entrada == '1':
                return {'q1'}
        elif estado == 'q2':
            if caractere_entrada == '0':
                return {'q2'}  
            elif caractere_entrada == '1':
                return {'q3'}  
        elif estado == 'q3':
            if caractere_entrada == '0':
                return {'q2'}  
            elif caractere_entrada == '1':
                return {'q3'}  
        return {estado}

    def aceita(self, string_entrada):
        estados_atuais = {self.estado_inicial}
        
        for char in string_entrada:
            proximos_estados = set()
            for estado in estados_atuais:
                proximos_estados |= self.transicao(estado, char)
            estados_atuais = proximos_estados
        
        return not estados_atuais.isdisjoint(self.estados_aceitacao)


# Testando o AFN
afn = AFN_TerminaEm01()
print("Testes AFN:")
print(afn.aceita("0101"))    # True, termina com "01"
print(afn.aceita("0010"))    # False, não termina com "01"
print(afn.aceita("10010"))    # True, termina com "01"
print(afn.aceita("0001"))     # False, não termina com "01"
print(afn.aceita("01"))      # True, exatamente "01"
print(afn.aceita("010"))     # False, não termina com "01"
print(afn.aceita("101"))     # False, não termina com "01"
